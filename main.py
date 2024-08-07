from fastapi import FastAPI, Request, Form, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from starlette.middleware.sessions import SessionMiddleware
from dotenv import load_dotenv
import os
import requests
import numpy as np

app = FastAPI()

# Load environment variables from .env file
load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")
OLLAMA_API_URL = os.getenv("OLLAMA_API_URL")  # Add the Ollama API URL to your .env file

# Initialize Jinja2 templates
templates = Jinja2Templates(directory="templates")

# Enable session handling
app.add_middleware(SessionMiddleware, secret_key=SECRET_KEY)

# Initial questions
questions = [
    "Can you briefly describe your current academic journey, including any notable achievements?",
    "Are there specific fields of study or professions you are passionate about? Where do you see yourself in five years, academically or professionally?",
    "What extracurricular activities or hobbies do you enjoy that align with your academic interests?",
    "What educational resources or materials do you regularly use?"
]

# Laplace Mechanism for Differential Privacy(DP-OPT)
def laplace_mechanism(value, epsilon):
    scale = 1.0 / epsilon
    noise = np.random.laplace(0, scale)
    return value + noise

def sanitize_response(response, epsilon):
    sanitized_response = []
    for word in response.split():
        try:
            numeric_word = float(word)
            sanitized_response.append(str(laplace_mechanism(numeric_word, epsilon)))
        except ValueError:
            sanitized_response.append(word)
    return " ".join(sanitized_response)

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    request.session.clear()
    request.session['question_index'] = 0
    request.session['user_responses'] = []
    return templates.TemplateResponse("chat.html", {"request": request, "intro_message": "Hi I am Naavi, your personal coach and navigator for higher education...😊"})

@app.post("/process_chat")
async def process_chat(request: Request, user_input: str = Form(...)):
    question_index = request.session.get('question_index', 0)
    user_responses = request.session.get('user_responses', [])

    if question_index > 0:
        sanitized_input = sanitize_response(user_input, epsilon=1.0)  # Sanitize the user input
        user_responses.append(sanitized_input)
        request.session['user_responses'] = user_responses

    if question_index < len(questions):
        next_question = questions[question_index]
        request.session['question_index'] = question_index + 1
        return JSONResponse({'question': next_question})
    else:
        request.session['question_index'] = len(questions)
        return JSONResponse({'response': "Thank you for providing the information. Please click the 'Create a Pathway' button to proceed.", 'show_pathway_button': True})

@app.get("/generate_pathway", response_class=HTMLResponse)
async def generate_pathway(request: Request):
    user_responses = request.session.get('user_responses', [])
    raw_response = await get_ai_response(user_responses)
    pathways = format_response(raw_response)
    return templates.TemplateResponse("pathway.html", {"request": request, "pathway_response": pathways})

async def get_ai_response(user_responses):
    messages = "\n".join([f"user\n{response}\n" for response in user_responses])
    final_prompt = """
Based on the information provided, generate three distinct pathways for achieving the user's educational and career goals. Each pathway should be clearly separated and include step-by-step guidance. The output should be structured as follows:

Pathway 1: [Title]
  Step 1
  Step 2
  Step 3
  Step 4
  Step 5
 
 ...

Pathway 2: [Title]
  Step 1
  Step 2
  Step 3
  Step 4
  Step 5
 
 ...

Pathway 3: [Title]
  Step 1
  Step 2
  Step 3
  Step 4
  Step 5
 ...
"""

    messages += f"assistant\n{final_prompt}\n"

    headers = {
        "Content-Type": "application/json"
    }

    payload = {
        "prompt": messages
    }

    try:
        response = requests.post(OLLAMA_API_URL, headers=headers, json=payload)
        response.raise_for_status()
        ai_response = response.json().get('response', '')
        return ai_response
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating AI response: {e}")

def format_response(raw_response):
    lines = raw_response.split('\n')
    formatted_response = []
    current_pathway = {"title": "", "steps": []}

    for line in lines:
        if line.startswith("Pathway "):
            if current_pathway["steps"]:
                formatted_response.append(current_pathway)
            current_pathway = {"title": line, "steps": []}
        elif line.strip():
            current_pathway["steps"].append(line.strip())

    if current_pathway["steps"]:
        formatted_response.append(current_pathway)
    
    return formatted_response

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

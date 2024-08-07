# Educational Counsellor Chatbot

This repository contains the implementation of an Educational Counsellor Chatbot designed to interact with students, collect their responses, and securely process and analyze the data using differential privacy techniques.

## Architecture

![Architecture Diagram](https://github.com/sivasai3949/OLLAMA-NEW/blob/main2/static/naavi_llm_architecture.png)

## Overview

The Educational Counsellor Chatbot follows the below process flow:

1. **User Interaction**: The chatbot interacts with students, asking questions and collecting their responses.
2. **Data Collection**: The responses from students are collected for further processing.
3. **Secure Data Processing**: The collected data is sent to the backend, where the `dp-opt` component ensures that sensitive data is mixed with the remaining data to maintain privacy.
4. **Prompt Construction**: A secure prompt is created based on the processed data.
5. **Sending to Ollama**: The prompt is sent to the Ollama service, which forwards it to the required selected language model.
6. **Model Response**: The selected language model processes the prompt and sends the response back to the backend.
7. **Displaying the Output**: The backend sends the response to the frontend via FastAPI, and the chatbot displays the output to the user.

## Components

- **Chatbot**: Collects inputs from users and interacts with them.
- **Backend (Flask)**: Handles API requests, processes data using `dp-opt`, and constructs secure prompts.
- **Ollama**: Sends the constructed prompt to the selected language model and receives the response.
- **Language Model (LLM)**: Processes the prompt and generates a response.
- **FastAPI**: Facilitates communication between the backend and the frontend.
- **Frontend**: Displays the output from the language model to the user.

## Installation

To set up the project, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/educational-counsellor-chatbot.git
   cd educational-counsellor-chatbot

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt

3. Run the application:
   ```bash
   python app.py


## Usage

The Educational Counsellor Chatbot can be used as follows:

1. **Start the Chatbot**: Begin by starting the chatbot and interacting with it through the frontend interface.
2. **Questionnaire**: The chatbot will ask a series of questions and collect your responses.
3. **Backend Processing**: The backend will process the data, construct a secure prompt, and send it to the Ollama service.
4. **Model Response**: The selected language model will generate a response based on the prompt.
5. **Display Response**: The response will be sent back to the frontend and displayed to the user.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue if you have any suggestions or improvements.

## License

This project is licensed under the MIT License. See the LICENSE file for details.



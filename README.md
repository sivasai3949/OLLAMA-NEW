# Educational Counsellor Chatbot

This repository contains the implementation of an Educational Counsellor Chatbot designed to interact with students, collect their responses, and securely process and analyze the data using differential privacy techniques.

## Architecture

![Architecture Diagram](https://github.com/sivasai3949/OLLAMA-NEW/blob/main/static/naavi_llm_architecture.jpg)

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

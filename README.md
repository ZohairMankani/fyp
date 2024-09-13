This project integrates Optical Character Recognition (OCR) with a chatbot system. The OCR extracts text from uploaded images, while the chatbot leverages a language model to engage in a conversation. The system is containerized using Docker for easy deployment.

Project Structure

1. app.py
The main entry point for the project. This script coordinates the OCR process and the chatbot interaction. It manages:
Receiving and handling user input (text or images).
Calling ocr_helper.py for processing and extracting text from images.
Handling user sessions and profiles by interacting with user_profile.py.
Integrating with the chatbot (from chatbot.py) to provide responses to user queries.

2. chatbot.py
This file handles the chatbot's functionality. It interacts with a pre-trained language model to:
Analyze user input (text or extracted text from images).
Provide relevant responses based on the input, either through predefined responses or using an external API such as the Groq LLM for dynamic conversations.
Can integrate with additional natural language processing (NLP) models from Hugging Face for improved response generation.

3. Dockerfile
The Docker configuration file for containerizing the project. It defines the environment in which the application will run. This file includes:
The base image (Python 3.x or any suitable OS).
Installation of necessary dependencies as defined in requirements.txt.
Commands to run the application (app.py) when the container starts.
This ensures that the entire system can be run in a consistent environment, making it easier to deploy and scale.

4. ocr_helper.py
This file is responsible for the OCR functionality. It contains:
Functions to process images and extract text using the pytesseract library.
Image pre-processing with OpenCV (cv2) to ensure that text is accurately recognized by the OCR engine.
Cleaning and preparing the extracted text for further use in the chatbot.

5. requirements.txt
This file lists the required Python libraries for the project. It can be used to install dependencies in your local environment or Docker container by running:
pytesseract: For extracting text from images.
PIL and cv2: For image processing.
transformers: Hugging Face library for NLP models.
requests: For API requests, such as interaction with external language models (Groq).

6. user_profile.py
This module manages user profiles and session handling. It is responsible for:
Storing and updating user data, such as preferences and previous interactions.
Tracking the conversation history to provide a more personalized chatbot experience.
Interacting with external data sources (like databases) to retrieve or store user information.

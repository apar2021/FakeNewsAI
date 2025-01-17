Fake News Detection using FastAPI and BERT
This project implements a Fake News Detection System that uses a BERT model fine-tuned on a fake news dataset to classify news articles as either real or fake. The backend is built with FastAPI and the frontend uses Node.js/Express for a simple user interface.

Table of Contents
Project Overview
Technologies Used
Getting Started
Prerequisites
Backend Setup
Frontend Setup
Fine-Tuning the BERT Model
Usage
Running with Docker
Contributing
License
Project Overview
This project consists of two main components:

Backend: A FastAPI service that hosts a BERT-based model for news article classification. It receives input text from the frontend, processes it using the model, and returns a prediction of whether the news is fake or real.

Frontend: A simple Node.js/Express application that provides a user interface for submitting news articles. The frontend sends requests to the FastAPI backend and displays the classification results.

Technologies Used
Backend:

FastAPI
Transformers (Hugging Face)
PyTorch
Uvicorn (ASGI server)
Frontend:

Node.js
Express
Axios (for HTTP requests)
HTML/CSS (for UI)
Model:

BERT (Bidirectional Encoder Representations from Transformers)
Fine-tuned BERT model for fake news classification
Getting Started
Prerequisites
To run this project locally, you need to have the following installed:

Python 3.9 or later
Node.js and npm
Docker (optional, for containerization)

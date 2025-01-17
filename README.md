# Fake News Detection using FastAPI and BERT

This project implements a **Fake News Detection System** that uses a **BERT model** fine-tuned on a fake news dataset to classify news articles as either **real** or **fake**. The backend is built with **FastAPI** and the frontend uses **Node.js/Express** for a simple user interface. 

---

## Table of Contents

- [Project Overview](#project-overview)
- [Technologies Used](#technologies-used)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Backend Setup](#backend-setup)
  - [Frontend Setup](#frontend-setup)
- [Fine-Tuning the BERT Model](#fine-tuning-the-bert-model)
- [Usage](#usage)
- [Running with Docker](#running-with-docker)
- [Contributing](#contributing)
- [License](#license)

---

## PROJECT OVERVIEW

This project consists of two main components:

1. **Backend**: A **FastAPI** service that hosts a **BERT-based model** for news article classification. It receives input text from the frontend, processes it using the model, and returns a prediction of whether the news is **fake** or **real**.

2. **Frontend**: A simple **Node.js/Express** application that provides a user interface for submitting news articles. The frontend sends requests to the FastAPI backend and displays the classification results.

---

## TECHNOLOGIES USED

- **Backend**: 
  - FastAPI
  - Transformers (Hugging Face)
  - PyTorch
  - Uvicorn (ASGI server)

- **Frontend**:
  - Node.js
  - Express
  - Axios (for HTTP requests)
  - HTML/CSS (for UI)

- **Model**:
  - BERT (Bidirectional Encoder Representations from Transformers)
  - Fine-tuned BERT model for fake news classification

---

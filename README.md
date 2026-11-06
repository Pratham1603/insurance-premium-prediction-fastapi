# Insurance Premium Prediction API

A production-ready machine learning web service built with **FastAPI** to predict medical insurance costs based on individual health parameters and demographics.

## Table of Contents
- [Overview](#overview)
- [Key Features](#key-features)
- [Tech Stack](#tech-stack)
- [Project Architecture](#project-architecture)
- [Docker Deployment](#docker-deployment)
- [Local Installation & Setup](#local-installation--setup)
- [API Endpoints](#api-endpoints)
- [Usage Example](#usage-example)
- [Repository & Links](#repository--links)

---

## Overview

Accurate prediction of medical insurance costs helps insurance providers price policies effectively and allows customers to estimate their healthcare expenses. This project provides a containerized, high-performance API endpoint that accepts user demographic and health data to return real-time insurance cost estimates using a trained Machine Learning model.

## Key Features

- **FastAPI Backend**: Asynchronous, high-performance web API framework with automatic OpenAPI documentation.
- **Docker Support**: Pre-built container image available on Docker Hub for rapid cloud deployment.
- **Data Validation**: Strict input data validation and serialization powered by Pydantic schemas.
- **Machine Learning Integration**: Pipeline integration for preprocessing data and generating real-time predictions.
- **RESTful Endpoints**: Clean, well-structured endpoints for health checks and model inference.

## Tech Stack

- **Language**: Python 3.10+
- **API Framework**: FastAPI, Uvicorn
- **Machine Learning**: Scikit-Learn, Pandas, NumPy, Joblib
- **Containerization**: Docker
- **Validation**: Pydantic
- **Version Control**: Git, GitHub

---

## Project Architecture

```
insurance-premium-prediction-fastapi/
│
├── artifacts/              # Trained models and scalers
│   └── model.pkl
├── notebook/               # Data analysis, feature engineering & training notebooks
├── src/                    # Source code directory
│   ├── pipeline/           # Prediction and training pipelines
│   ├── components/         # Data ingestion, transformation, model trainer
│   └── logger.py           # Logging module
│
├── app.py                  # FastAPI application entry point
├── Dockerfile              # Docker container definition
├── requirements.txt        # Python package dependencies
├── setup.py                # Project packaging setup
└── README.md               # Project documentation
```

---

## Docker Deployment

You can pull and run the official pre-built Docker image directly from Docker Hub without needing to set up a Python environment locally.

### Docker Hub Image
- **Image Repository:** [pratham1603/insurance-premium-prediction-fastapi](https://hub.docker.com/r/pratham1603/insurance-premium-prediction-fastapi)

### Quick Run with Docker

1. **Pull the Docker Image:**
   ```bash
   docker pull pratham1603/insurance-premium-prediction-fastapi:latest
   ```

2. **Run the Container:**
   ```bash
   docker run -d -p 8000:8000 --name insurance-api pratham1603/insurance-premium-prediction-fastapi:latest
   ```

3. Access the API locally at `http://127.0.0.1:8000`.

---

## Local Installation & Setup

### Prerequisites

Ensure you have Python 3.9 or higher installed on your system.

### 1. Clone the Repository

```bash
git clone https://github.com/Pratham1603/insurance-premium-prediction-fastapi.git
cd insurance-premium-prediction-fastapi
```

### 2. Create and Activate a Virtual Environment

- **Linux / macOS:**
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

- **Windows:**
  ```cmd
  python -m venv venv
  venv\Scripts\activate
  ```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Application

Start the FastAPI server using Uvicorn:

```bash
uvicorn app:app --reload
```

The server will launch at `http://127.0.0.1:8000`.

---

## API Endpoints

FastAPI automatically generates interactive documentation for testing endpoints:

- **Swagger UI**: `http://127.0.0.1:8000/docs`
- **ReDoc**: `http://127.0.0.1:8000/redoc`

### Primary Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Root endpoint / System Status Check |
| POST | `/predict` | Predicts insurance premium based on input features |

---

## Usage Example

### POST `/predict`

**Request Body:**

```json
{
  "age": 32,
  "sex": "male",
  "bmi": 28.5,
  "children": 2,
  "smoker": "no",
  "region": "southeast"
}
```

**cURL Request:**

```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/predict' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "age": 32,
  "sex": "male",
  "bmi": 28.5,
  "children": 2,
  "smoker": "no",
  "region": "southeast"
}'
```

**Response:**

```json
{
  "predicted_premium": 5420.50
}
```

---

## Repository & Links

- **GitHub Repository:** [Pratham1603/insurance-premium-prediction-fastapi](https://github.com/Pratham1603/insurance-premium-prediction-fastapi)
- **Docker Hub Repository:** [pratham1603/insurance-premium-prediction-fastapi](https://hub.docker.com/r/pratham1603/insurance-premium-prediction-fastapi)

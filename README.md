# grepsr_assessment
This repo is created for job interview in greps

# FastAPI Counter Application

## Overview
This is a simple FastAPI application that counts the number of requests made to the `/count` endpoint. Each time the `/count` endpoint is accessed, the count is incremented and stored in a local SQLite database (`test.db`).

## Prerequisites
Before running the application, make sure you have the following installed on your system:

- **Python 3.9+**
- **pip** (Python package installer)

## Setup and Installation

### Step 1: Clone the Repository
Clone the repository to your local machine:

    git clone <your-repository-url> cd <project-directory>

### Step 2: Create a Virtual Environment (Optional but Recommended)
It is recommended to create a virtual environment to manage dependencies:

1. Create a virtual environment:
    ```
    python -m venv env
    ```

2. Activate the virtual environment:
- On **Windows**:
  ```
  .\env\Scripts\activate
  ```
- On **macOS/Linux**:
  ```
  source env/bin/activate
  ```

### Step 3: Install Dependencies
Install the required dependencies from the `requirements.txt` file:

    pip install -r requirements.txt


### Step 4: Run the Application
Start the FastAPI application with **Uvicorn**:

    uvicorn main:app --reload

- The `--reload` flag ensures the server restarts upon code changes.

### Step 5: Access the Application
Open your browser and go to `http://127.0.0.1:8000` to view the application.

- The root (`/`) endpoint will show a welcome message.
- The `/count` endpoint will show the current request count.

### Example Responses

- **Root (`/`) Route**:
  ```json
  {
    "message": "Welcome to the FastAPI Counter App!"
  }

- **Root (`/count`) Route**:
  ```json
  {
  "count": 1
  }

## Project Structure

    .
    ├── main.py                   # FastAPI application code
    ├── requirements.txt           # Python dependencies (FastAPI, Uvicorn)
    └── README.md                  # Project documentation


## Technologies Used

    FastAPI: Web framework for building APIs with Python.
    Uvicorn: ASGI server for serving FastAPI applications.
    SQLite: Database for storing the request count.


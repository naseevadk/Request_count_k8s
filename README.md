# grepsr_assessment
This repo is created for job interview in Grepsr

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
    ├── .github
    │   ├── workflows
    │       ├── python.yaml      # GitHub Actions file
    ├── app
    │   ├── main.py              # FastAPI application code
    ├── kubernetes
    │   ├── deployment.yaml      # kubernetes deployment file
    │   ├── service.yaml         # kubernetes service file
    ├── requirements.txt         # Python dependencies (FastAPI, Uvicorn)
    ├── Dockerfile               # Dockerfile to containerize and run 
    ├── docker-compose.yaml      # Docker compose file 
    ├── .gitignore               # Git ignore file
    └── README.md                # Project documentation


## Technologies Used

    FastAPI: Web framework for building APIs with Python.
    Uvicorn: ASGI server for serving FastAPI applications.
    SQLite: Database for storing the request count.

## Dockerizing the Application
To run the FastAPI application in a containerized environment using Docker, follow these steps:

###  Step 1: Build the Dockerfile
The project includes a Dockerfile that contains the instructions to build the container image. Run the following command to build the dockerfile:


    docker build -t fastapi-counter . #you can change the tag as you wish

###  Step 2: Run the Dockerfile
After building the image, run the container using the following command:

    docker run -d -p 80:80 fastapi-counter

  The **-d** flag runs the container in detached mode.<br>
  The **-p 80:80** flag maps the local port 80 to the container's port 80.

### Step 3: Access the Application
Open your browser and go to **http://127.0.0.1:80** to view the application running inside the Docker container.

## Docker Compose
Docker Compose allows you to define and run multi-container Docker applications. To simplify the setup, we have included a docker-compose.yml file.

### Step 1: Build and Run with Docker Compose
To build and start the application using Docker Compose, run the following command in the root directory:

    docker-compose build
The **--build** flag ensures that the Docker image is built before starting the containers.

### Step 2: Run in Detached Mode

To run the application in detached mode (in the background), use the following command:

    docker-compose up -d
This will build the images and start the application in the background.

### Step 3: Access the Application
Once the application is up and running, open your browser and go to http://127.0.0.1:80 to view the application running inside the container.


## Running the Application in Kubernetes

### Prerequisites
Ensure you have the following tools installed:

    Minikube (Local Kubernetes cluster)
    Kubectl (Kubernetes CLI)

### Step 1: Start Minikube with Docker Driver
Start Minikube using the Docker driver:

    minikube start --driver=docker
### Step 2: Apply Kubernetes Manifests
Deploy the application to Kubernetes using the provided manifests:

    kubectl apply -f deployment.yaml
    kubectl apply -f service.yaml
The deployment.yaml contains the Deployment resource that defines the application pods.
The service.yaml exposes the application via a NodePort service.
### Step 3: Verify Resources
Verify that the pods and services are running:

    kubectl get pods
    kubectl get services
### Step 4: Access the Application
Option 1: Using Minikube Tunnel
If using Minikube with the Docker driver, expose the service with the tunnel command:

    minikube service fastapi-counter-service
This will open a tunnel and expose the service at a localhost URL (e.g., http://127.0.0.1:30001).
Option 2: Port Forwarding
You can forward the Kubernetes service port to your local machine using:

    kubectl port-forward service/fastapi-counter-service 8080:80
Access the application at http://127.0.0.1:8080.
Option 3: NodePort with Minikube IP
Use the Minikube IP and NodePort to access the application:

Get the Minikube IP:

    minikube ip
Access the application at **http://minikube-ip:30001**.


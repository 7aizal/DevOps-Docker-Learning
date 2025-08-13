<<<<<<< HEAD
# Docker Learning 
Created a simple Flask app (app.py)

=======
# Dockers and Containers


Flask + Docker Example
Ì≥å Overview
This project demonstrates a simple Flask application containerized with Docker.

Ì≥ù Flask App (app.py)
Listens on / and returns "Hello, Flask!".

Runs with debug=True for development.

Ì≥¶ Dockerfile Details
Base Image: python:3.13.5-slim (lightweight)

Working Directory: /app

Copied Source Code: Application files are copied into the container.

Installed Dependencies: Flask installed via pip.

Port Exposure: 5000

Default Command:

python app.py
Ì∫Ä Running the App with Docker

1. Build the Image
docker build -t hello-flask .

2. Run the Container
docker run -d -p 5000:5000 hello-flask
‚úÖ Verification
The container is now live and mapped to:
http://localhost:5000

Check running containers:

docker ps
Shows:

The container up and running

Correct port mapping: 5000 -> 5000

Ì≥¶ Flask + Docker + MySQL + AWS ECR ‚Äî Learning Journey
Overview
This project documents my hands-on learning with Docker, Flask, MySQL, and AWS ECR.
It started with a simple Flask app, then evolved into container networking, dependency debugging, and multi-container orchestration with Docker Compose.

Ì≥ç Step-by-Step Progression
1Ô∏è‚É£ Created a Simple Flask App (app.py)
>>>>>>> 5314682 (updated progression on Dockers learning module, pushed an image on dockerhub,aws ecr, merged two in same network)
Listens on / and returns "Hello, Flask!"

Runs with debug=True for development

<<<<<<< HEAD
Wrote a Dockerfile

Used the lightweight python:3.13.5-slim base image

Set /app as the working directory

Copied your source code in

Installed Flask inside the container

Exposed port 5000

Set the default command to python app.py

Built and ran the container

You learned that you must build the image first with:


docker build -t hello-flask .
before running it with:

docker run -d -p 5000:5000 hello-flask
The container is now live and mapped to localhost:5000

Confirmed it‚Äôs running

docker ps shows the container up with the correct port mapping

<img width="861" height="463" alt="image3" src="https://github.com/user-attachments/assets/83db336f-08a2-44e2-88cd-8a42266fff9d" />
<img width="641" height="338" alt="image2" src="https://github.com/user-attachments/assets/f42950da-fde2-4c40-ab0d-1a8ea07f739e" />
<img width="439" height="304" alt="image" src="https://github.com/user-attachments/assets/021c019a-439f-43cd-a4e8-14b96c3a5a52" />
=======
python
Copy
Edit
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello, Flask!"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
2Ô∏è‚É£ Dockerizing the Flask App
Dockerfile:

dockerfile
Copy
Edit
FROM python:3.13.5-slim
WORKDIR /app
COPY . .
RUN pip install flask
EXPOSE 5000
CMD ["python", "app.py"]
Build & Run:

bash
Copy
Edit
docker build -t hello-flask .
docker run -d -p 5000:5000 hello-flask
‚úÖ Verified running container using:

bash
Copy
Edit
docker ps
3Ô∏è‚É£ Docker Networking + MySQL Integration
Created a custom network for container-to-container communication:

bash
Copy
Edit
docker network create my-custom-network
Ran MySQL container:

bash
Copy
Edit
docker run -d --name mydb --network my-custom-network \
-e MYSQL_ROOT_PASSWORD=my-secret-pw mysql:5.7
Updated Flask app to connect to MySQL using container name as hostname:

python
Copy
Edit
host="mydb", user="root", passwd="my-secret-pw", db="mysql"
4Ô∏è‚É£ Fixing mysqlclient Build Error
Problem: mysqlclient failed due to missing build dependencies in python:slim

Solution: Updated Dockerfile:

dockerfile
Copy
Edit
RUN apt-get update && apt-get install -y \
    gcc python3-dev libmariadb-dev pkg-config
RUN pip install flask mysqlclient
Rebuilt image:

bash
Copy
Edit
docker build -t hello-flask-mysql .
5Ô∏è‚É£ AWS ECR Integration
Installed & configured AWS CLI:

bash
Copy
Edit
aws configure
Logged in to ECR:

bash
Copy
Edit
aws ecr get-login-password --region eu-north-1 \
| docker login --username AWS --password-stdin <account_id>.dkr.ecr.eu-north-1.amazonaws.com
Tagged & pushed:

bash
Copy
Edit
docker tag hello-flask-mysql <account_id>.dkr.ecr.eu-north-1.amazonaws.com/flask-mysql:latest
docker push <account_id>.dkr.ecr.eu-north-1.amazonaws.com/flask-mysql:latest
6Ô∏è‚É£ Multi-Container Setup with Docker Compose
docker-compose.yml

yaml
Copy
Edit
version: '3.8'
services:
  web:
    image: <account_id>.dkr.ecr.eu-north-1.amazonaws.com/flask-mysql:latest
    ports:
      - "5000:5000"
    depends_on:
      - mydb

  mydb:
    image: mysql:5.7
    environment:
      MYSQL_ROOT_PASSWORD: my-secret-pw
Started both services:

bash
Copy
Edit
docker compose up
Ì≥å Current Status
Flask app runs inside Docker

Connects successfully to MySQL container

Image pushed & stored in AWS ECR

Docker Compose orchestrates multi-container setup


>>>>>>> 5314682 (updated progression on Dockers learning module, pushed an image on dockerhub,aws ecr, merged two in same network)

# Docker Learning 
Created a simple Flask app (app.py)

Listens on / and returns "Hello, Flask!"

Runs with debug=True for development

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

Confirmed it’s running

docker ps shows the container up with the correct port mapping

<img width="861" height="463" alt="image3" src="https://github.com/user-attachments/assets/83db336f-08a2-44e2-88cd-8a42266fff9d" />
<img width="641" height="338" alt="image2" src="https://github.com/user-attachments/assets/f42950da-fde2-4c40-ab0d-1a8ea07f739e" />
<img width="439" height="304" alt="image" src="https://github.com/user-attachments/assets/021c019a-439f-43cd-a4e8-14b96c3a5a52" />

# 🐳 Docker Learning Progress

## **Flask App in Docker**
- **Created a simple Flask app** (`app.py`)
  - Listens on `/` and returns `"Hello, Flask!"`
  - Runs with `debug=True` for development
- **Wrote a Dockerfile**
  - Used the lightweight `python:3.13.5-slim` base image
  - Set `/app` as the working directory
  - Copied the source code into the container
  - Installed Flask inside the container
  - Exposed port **5000**
  - Set the default command to run `python app.py`
- **Built and ran the container**
  - Build:  
    ```bash
    docker build -t hello-flask .
    ```
  - Run:  
    ```bash
    docker run -d -p 5000:5000 hello-flask
    ```
- The container is live and mapped to `localhost:5000`
- **Confirmed it’s running**:  
    ```bash
    docker ps
    ```
    Shows the container up with correct port mapping.

---

<img width="861" height="463" alt="image3" src="https://github.com/user-attachments/assets/83db336f-08a2-44e2-88cd-8a42266fff9d" />
<img width="641" height="338" alt="image2" src="https://github.com/user-attachments/assets/f42950da-fde2-4c40-ab0d-1a8ea07f739e" />
<img width="439" height="304" alt="image" src="https://github.com/user-attachments/assets/021c019a-439f-43cd-a4e8-14b96c3a5a52" />
 
 ## **Docker Networking & MySQL Integration – with a Debugging Twist 🚀**

**Goal:** Connect a Flask app to a MySQL database container.

### **Challenges**
- `mysqlclient` install failed inside the Flask container due to missing build dependencies in the slim Python image.

### **The Fix**
- Updated Dockerfile to install required packages:
    ```dockerfile
    RUN apt-get update && apt-get install -y gcc python3-dev libmariadb-dev pkg-config
    ```
- Rebuilt the image:
    ```bash
    docker build -t hello-flask-mysql .
    ```

---<img width="1063" height="275" alt="11" src="https://github.com/user-attachments/assets/ecf16981-b83a-4827-ba93-806c7e1a79a5" />
<img width="763" height="399" alt="10" src="https://github.com/user-attachments/assets/896b6b83-c2b8-4b10-a189-4fc14d5fb3d0" />
<img width="552" height="86" alt="9" src="https://github.com/user-attachments/assets/10d1350e-a51e-4cd9-807c-ad654d6e1b50" />
<img width="388" height="157" alt="8" src="https://github.com/user-attachments/assets/e434307c-8dbd-4a18-b2f5-a3335044eebf" />
<img width="936" height="619" alt="7" src="https://github.com/user-attachments/assets/b269f4da-ad90-48f4-a82a-b877df60de11" />
### **Networking & Container Linking**
1. Created a custom Docker network:
    ```bash
    docker network create my-custom-network
    ```
2. Ran MySQL container:
    ```bash
    docker run -d --name mydb --network my-custom-network -e MYSQL_ROOT_PASSWORD=my-secret-pw mysql:5.7
    ```
3. Ran Flask container on same network:
    ```bash
    docker run -d -p 5000:5000 --network my-custom-network hello-flask-mysql
    ```<img width="987" height="349" alt="15" src="https://github.com/user-attachments/assets/e7247281-ed9e-44c5-97c5-fbf5054f6703" />
<img width="1130" height="169" alt="14" src="https://github.com/user-attachments/assets/b113c562-88b4-48d7-b0f0-5ba9bdaf5a80" />
<img width="546" height="333" alt="13" src="https://github.com/user-attachments/assets/88024a29-4f62-418e-b9a8-b7adacd0cb23" />
<img width="940" height="519" alt="12" src="https://github.com/user-attachments/assets/3e60922f-635b-40ab-aefd-5b95be36c1e6" />


**Used Docker Compose for Multi-Container Setup**
docker-compose.yml
```yaml

version: '3.8'
services:
  web:
    build: .
    ports:
      - "5000:5000"
    depends_on:
      - mydb
  mydb:
    image: mysql:5.7
    environment:
      MYSQL_ROOT_PASSWORD: my-secret-pw

```
```bash
docker compose up -d
```
<img width="478" height="100" alt="17" src="https://github.com/user-attachments/assets/564d5584-d63f-4bb6-b9e3-a595426ec9c0" />
<img width="1149" height="530" alt="16" src="https://github.com/user-attachments/assets/21ebfec3-9aa2-49ef-96f9-8cd4700902f3" />
<img width="987" height="349" alt="15" src="https://github.com/user-attachments/assets/0ed9e006-ad02-4f9b-b95f-d3b94e31c16f" />

**Pushed Image to AWS ECR**
*Authenticate:*

```bash

aws ecr get-login-password --region eu-north-1 \
| docker login --username AWS --password-stdin <account_id>.dkr.ecr.eu-north-1.amazonaws.com
Tag & Push:
```
```bash

docker tag flask-mysql:latest <account_id>.dkr.ecr.eu-north-1.amazonaws.com/flask-mysql:latest
docker push <account_id>.dkr.ecr.eu-north-1.amazonaws.com/flask-mysql:latest
Run with MySQL on the Same Network:
```
```bash

docker run -p 5000:5000 --network my-aws-app \
<account_id>.dkr.ecr.eu-north-1.amazonaws.com/flask-mysql:latest
```





import os
from flask import Flask
import redis

app = Flask(__name__)

# Read environment variables
redis_host = os.getenv('REDIS_HOST', 'localhost')
redis_port = int(os.getenv('REDIS_PORT', 6379))

# Connect to Redis
r = redis.Redis(host=redis_host, port=redis_port, decode_responses=True)

@app.route('/')
def home():
    return "Asalamualaikum Habibi!"

@app.route('/count')
def count():
    visits = r.incr('visits')
    return f"Number of visits: {visits}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

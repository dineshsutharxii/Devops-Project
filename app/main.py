from flask import Flask, jsonify
import redis

app = Flask(__name__)

# Connect to Redis
redis_client = redis.Redis(host='redis', port=6379, decode_responses=True)

@app.route('/')
def home():
    return jsonify({"message": "Flask app is running!"})

@app.route('/health')
def health():
    return jsonify({"status": "healthy"})

@app.route('/counter')
def counter():
    count = redis_client.incr("counter")  # Increment the counter in Redis
    return jsonify({"counter": count})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

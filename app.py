from flask import Flask, jsonify
from prometheus_client import Counter, generate_latest

app = Flask(__name__)

REQUESTS = Counter(
    "student_app_requests_total",
    "Total requests received"
)

@app.route("/")
def home():
    REQUESTS.inc()
    return """
    <h1>Student Management App</h1>
    <p>DevOps pipeline is running!</p>
    """

@app.route("/health")
def health():
    REQUESTS.inc()
    return jsonify(status="ok")

@app.route("/students")
def students():
    REQUESTS.inc()
    return jsonify(students=[
        {"roll_no": 1, "name": "Asha"},
        {"roll_no": 2, "name": "Rahul"}
    ])

@app.route("/metrics")
def metrics():
    return generate_latest(), 200, {
        "Content-Type": "text/plain; version=0.0.4"
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
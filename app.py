from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
    {
        "id": 1,
        "title": "Data Analyst",
        "location": "Accra, Ghana",
        "salary": "GHS 4,000.00"
    },
    {
        "id": 2,
        "title": "Data Scientist",
        "location": "Kumasi, Ghana",
        "salary": "GHS 5,000.00"
    },
    {
        "id": 3,
        "title": "Web Developer",
        "location": "Accra, Ghana",
        
    },
    {
        "id": 4,
        "title": "Backend Enginner",
        "location": "Remote",
        "salary": "USD 70,000.00"
    },
]

@app.route("/")
def hello_world():
    return render_template('home.html', jobs=JOBS, company_name="Evans")

@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)
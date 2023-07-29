from flask import Flask, render_template, jsonify
from database import load_jobs_from_db, load_jobs_from_db
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)

@app.route("/")
def home():
    jobs = load_jobs_from_db()
    return render_template('home.html', jobs=jobs, company_name="Jovian")

@app.route("/api/jobs")
def list_jobs():
    jobs = load_jobs_from_db()
    return jsonify(jobs)

@app.route("/jobs/<id>")
def show_job(id):
    job = load_jobs_from_db(id)
    # if job is not found
    if not job:
        return "Not Found", 404
    
    return render_template('jobpage.html', job=job)

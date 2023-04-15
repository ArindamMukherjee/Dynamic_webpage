from flask import Flask, render_template, jsonify, request
from database import engine
from sqlalchemy import text
from database import load_job_from_db
from database import load_jobs_from_db, application_to_the_db

app = Flask(__name__)

@app.route("/")
def hello_jovian():
    jobs = load_job_from_db()
    return render_template('home.html', jobs=jobs, company_name='Vibe')

@app.route("/api/job/<id>")
def show_job_json(id):
  job = load_jobs_from_db(id)
  if not job:
    return "Not Found", 404
  return render_template("jopage.html",job=job)

@app.route("/jobs/<id>/apply", methods=['POST'])
def apply_to_job(id):
    data = request.form
    job = load_jobs_from_db(id)
    # application_to_the_db(id, data)
    # print(data)
    #here we can store this data into the database 
    # on based on the data we can acknowledge the candidate
    return render_template("application_submit.html",application = data, job = job)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

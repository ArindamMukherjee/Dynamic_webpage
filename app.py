from flask import Flask, render_template, jsonify
from database import engine
from sqlalchemy import text
from database import load_job_from_db
from database import load_jobs_from_db

app = Flask(__name__)

# JOBS = [
#   {
#     'id': 1,
#     'title': 'Data Analyst',
#     'location': 'Bengaluru, India',
#     'salary': 'Rs. 10,00,000'
#   },
#   {
#     'id': 2,
#     'title': 'Data Scientist',
#     'location': 'Delhi, India',
#     'salary': 'Rs. 15,00,000'
#   },
#   {
#     'id': 3,
#     'title': 'Frontend Engineer',
#     'location': 'Remote'
#   },
#   {
#     'id': 4,
#     'title': 'Backend Engineer',
#     'location': 'San Francisco, USA',
#     'salary': '$150,000'
#   },

#   {
#     'id': 5,
#     'title': 'FullStack Engineer',
#     'location': 'San Francisco, USA',
#     'salary': '$180,000'
#   }
# ]




@app.route("/")
def hello_jovian():
    jobs =  load_job_from_db()
    return render_template('home.html', 
                           jobs=jobs, 
                           company_name='Vibe ')

@app.route("/api/job/<id>")
def show_job_json(id):
  job = load_jobs_from_db(id)
  return jsonify(job)



@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)

from flask import Flask, render_template, request, redirect, url_for, session, jsonify

app = Flask(__name__)

JOB = [{
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Bengaluru, India',
    'salary': 'Rs. 10,00,000'
}, {
    'id': 2,
    'title': 'Data Scientist',
    'location': 'Delhi, India',
    'salary': 'Rs. 12,00,000',
}, {
    'id': 3,
    'title': 'Frontend Engineer',
    'location': 'Remote',
    'salary': 'Rs. 15,00,000',
}, {
    'id': 4,
    'title': 'Backend Engineer',
    'location': 'San Francisco, USA',
    'salary': '$120,000',
}]


@app.route("/")
def hello_world():
  return render_template("home.html", jobs=JOB, Company_name='U.R. Cristiano')


@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOB)


if (__name__ == "__main__"):
  app.run(host='0.0.0.0', debug=True)

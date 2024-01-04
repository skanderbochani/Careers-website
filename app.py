from flask import Flask, jsonify, render_template
from app import app as application

app = Flask(__name__)
JOBS = [
    {
        'id': 1,
        'title': 'Data Analyst',
        'location': 'Tunis, Tunisie',
        'salary': '4000 TND'
    },
    {
        'id': 2,
        'title': 'software engineer',
        'location': 'Benzart, Tunisie',
        'salary': '4500 TND'
    },
    {
        'id': 3,
        'title': 'Data Scientist',
        'location': 'Sfax, Tunisie',
        'salary': '4000 TND'
    },
    {
        'id': 4,
        'title': 'Cloud Engineer',
        'location': 'Tunis, Tunisie',
        'salary': '3000 TND'
    },
]


@app.route("/")
def hello_MyCareers():
  return render_template('home.html', jobs=JOBS)


@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  application.run()

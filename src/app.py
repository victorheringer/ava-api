from flask import Flask, jsonify
import requests
from bs4 import BeautifulSoup
from scrapers import timeline, courses, dashboard, common
from dotenv import load_dotenv
import os
from flask_cors import CORS

load_dotenv()
app = Flask(__name__)
CORS(app)

def link(id):
  return 'https://www.colaboraread.com.br/aluno/dashboard/index?matriculaId=' + id

@app.route('/')
def home():
  return "Ava api status: ok - Learn more about it at <a target='_blank' href='https://github.com/victorheringer/ava-api'>my github</a>"

@app.route('/courses')
def fetch():
  data = []

  payload = {
    'username': os.environ.get("LOGIN"),
    'password': os.environ.get("PASSWORD")
  }

  # Use 'with' to ensure the session context is closed after use.
  with requests.Session() as s:
    s.post('https://www.colaboraread.com.br/login/authenticate', data=payload)

    page = s.get('https://www.colaboraread.com.br/index/index')
    coursesData = courses.courses(page)

    for indexCourse, courseData in enumerate(coursesData):
      for indexSemester, courseDataSemester in enumerate(courseData["semesters"]):
        semesterLinks = dashboard.dashboard(s, link(courseDataSemester["$activitiesId"]))

        panels = timeline.panels(s, semesterLinks)
        coursesData[indexCourse]["semesters"][indexSemester]["subjects"] = panels

    return jsonify(coursesData)


@app.route('/courses/lightweight')
def lightweight():
  data = []

  payload = {
    'username': os.environ.get("LOGIN"),
    'password': os.environ.get("PASSWORD")
  }

  # Use 'with' to ensure the session context is closed after use.
  with requests.Session() as s:
    s.post('https://www.colaboraread.com.br/login/authenticate', data=payload)

    page = s.get('https://www.colaboraread.com.br/index/index')
    coursesData = courses.courses(page)
    activitiesList = []

    for indexCourse, courseData in enumerate(coursesData):
      for indexSemester, courseDataSemester in enumerate(courseData["semesters"]):
    
        reportCard = s.get(link(courseDataSemester['$activitiesId']))
        pageReportCard = BeautifulSoup(reportCard.text, 'html.parser')
        reportCardIds = common.getReportCardId(pageReportCard)
        coursesData[indexCourse]["semesters"][indexSemester]["$activitiesTemplate"] = []

        for reportCardId in reportCardIds:
          courseDataSemesterId = courseDataSemester['$activitiesId']
          res = s.get('https://www.colaboraread.com.br/aluno/dashboard/listAtividades?id={id}&boletimId={reportId}'.format(id=courseDataSemesterId,reportId=reportCardId))
          coursesData[indexCourse]["semesters"][indexSemester]["$reportId"] = reportCardId
          coursesData[indexCourse]["semesters"][indexSemester]["$activitiesTemplate"].append(res.text)
              
    return jsonify(coursesData)
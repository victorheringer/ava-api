import os
import requests
from parsers import index, dashboard, timeline
from flask import Flask, jsonify, request
from bs4 import BeautifulSoup
#from scrapers import timeline, courses, dashboard, common
from dotenv import load_dotenv
from flask_cors import CORS

load_dotenv()
app = Flask(__name__)
CORS(app)

'''
def link(id):
  return 'https://www.colaboraread.com.br/aluno/dashboard/index?matriculaId=' + id

@app.route('/courses/all', methods=['POST', 'GET'])
def fetch():

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
'''

def login(username, password):
  with requests.Session() as s:
    s.post('https://www.colaboraread.com.br/login/authenticate', data={'username': username, 'password': password})
    return s

@app.route('/')
def home():
  return "Ava api status: ok - Learn more about it at <a target='_blank' href='https://github.com/victorheringer/ava-api'>my github</a>"

@app.route('/index/courses')
def getCourses():

  session = login(os.environ.get("LOGIN"), os.environ.get("PASSWORD"))
  page = session.get('https://www.colaboraread.com.br/index/index')

  return jsonify(index.courses(page.text))

@app.route('/dashboard/subjects/<matriculation_id>')
def getSemester(matriculation_id=''):
  
  session = login(os.environ.get("LOGIN"), os.environ.get("PASSWORD"))
  page = session.get('https://www.colaboraread.com.br/aluno/dashboard/index?matriculaId='+matriculation_id)
  subjects = dashboard.subjects(page.text)

  result = []
  
  for subject in subjects:
    if(subject["report_card_id"] != ''):
      page = session.get('https://www.colaboraread.com.br/aluno/dashboard/listAtividades?id='+matriculation_id+'&boletimId='+subject["report_card_id"])
      subject['activities'] = dashboard.activities(page.text)
      result.append(subject)
    else:
      result.append(subject)
    
  return jsonify(result)

@app.route('/timeline/activities_panels/<matriculation_id>/<discipline_offer_id>')
def getTimeline(matriculation_id='', discipline_offer_id=''):

  session = login(os.environ.get("LOGIN"), os.environ.get("PASSWORD"))
  page = None
  print(discipline_offer_id)

  if(discipline_offer_id != ''):
    page = session.get('https://www.colaboraread.com.br/aluno/timeline/index/'+matriculation_id+'?ofertaDisciplinaId='+discipline_offer_id)
  else:
    page = session.get('https://www.colaboraread.com.br/aluno/timeline/index/'+matriculation_id)

  return jsonify(timeline.activities_panels(page.text))
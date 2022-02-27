import os
import json
from ..dashboard import subjects, activities

def test_get_subjects_dashboard_page():
  path = os.path.dirname(os.path.realpath(__file__))

  teamplate = open(path + "/mocks/dashboard_page.html", "r")
  result = open(path + "/mocks/subjects.json", "r")

  parsed = subjects(teamplate.read())
  static = json.loads(result.read())

  assert parsed == static

def test_get_activities_dashboard_page():
  path = os.path.dirname(os.path.realpath(__file__))

  teamplate = open(path + "/mocks/activities_list.html", "r")
  result = open(path + "/mocks/activities.json", "r")

  parsed = activities(teamplate.read())
  static = json.loads(result.read())

  assert parsed == static
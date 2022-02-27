import os
import json
from ..index import courses

def test_get_courses_index_page():
  path = os.path.dirname(os.path.realpath(__file__))

  teamplate = open(path + "/mocks/index_page.html", "r")
  result = open(path + "/mocks/courses.json", "r")

  parsed = courses(teamplate.read())
  static = json.loads(result.read())

  assert parsed == static
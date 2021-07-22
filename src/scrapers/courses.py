from bs4 import BeautifulSoup
from . import common

"""
@page https://www.colaboraread.com.br/
"""

def courses(page):
  soup = BeautifulSoup(page.text, 'html.parser')
    
  courseList = []
  courses = soup.findAll("div", {"class": "cursosBox"})
  courses = courses[:-1]
  
  for course in courses: 
    courseName = course.find("h3", {"class": "curso"}).text
    ids = common.getRegistrationIds(course)

    courseList.append({"course": courseName, "semesters": ids})

  return courseList
    
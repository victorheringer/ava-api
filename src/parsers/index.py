from bs4 import BeautifulSoup
from utils import strings

def getMatriculationId(page):
  ids = []
  options = page.find("select", {"id": "matriculaId"}).findAll("option")

  if options != None:
    for option in options: 
      ids.append({ 
        "matriculation_id": option.get("value") , 
        "semester_name": option.text, 
        "semester_number": strings.get_first_number(option.text) 
      })

  return ids

"""
@page https://www.colaboraread.com.br/index/index
"""
def courses(page):
  soup = BeautifulSoup(page, 'html.parser')
    
  courseList = []
  courses = soup.findAll("div", {"class": "cursosBox"})
  courses = courses[:-1]
  
  for course in courses: 
    courseName = course.find("h3", {"class": "curso"}).text
    ids = getMatriculationId(course)

    courseList.append({"name": courseName, "semesters": ids})

  return courseList
    
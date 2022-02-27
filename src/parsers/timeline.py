
import json
from bs4 import BeautifulSoup
from utils import strings

def handlePeriod(data):
  date = strings.clean(data.split(":",1)[1]).split("-")
  return { "init": strings.clean(date[0]), "end": strings.clean(date[1]) }

def handleCodActivity(data):
  return strings.clean(data.split(":",1)[1])

def handleCompletude(data):
  progress = data.find("div", {"class": "progress-bar"})
  return strings.clean(progress.text, {"%": ""})

def handleActivityPoints(data):
  gradeString = data.find("div", {"class": "progress-bar"})
  grades = gradeString.text.strip().split("de")
  return { "current": strings.clean(grades[0]), "total": strings.clean(grades[1]) }

"""
@page https://www.colaboraread.com.br/aluno/timeline/index
"""

def activities_panels(page):
  dummy = []
  result = []
  soup = BeautifulSoup(page, 'html.parser')
  panels = soup.find_all("div", {"class": "timeline-panel"})

  for panel in panels:
    smalls = panel.find_all("small")
    p = {
      "period": None,
      "code": None,
      "completeness": None,
      "grade": None
    }
    
    for small in smalls:
      data = strings.clean(small.text)

      if data.find("Período") != -1:
        p['period'] = handlePeriod(data)
         
      if data.find("Cod. Atividade") != -1:
        p['code'] = handleCodActivity(data)

      if data.find("Completude") != -1:
        p['completeness'] = handleCompletude(small.parent)

      if data.find("Pontuação da atividade:") != -1:
        p['grade'] = handleActivityPoints(small.parent)

    p['name'] = strings.clean(smalls[0].text.rsplit("-", 1)[0])
    dummy.append(p)

    pageHeader = soup.find('header', attrs={'class':'page-header'})
    headerName = strings.clean(pageHeader.find('h2').text, {"%": ""})

  return { 'name': headerName, 'activities_panels': dummy  } 

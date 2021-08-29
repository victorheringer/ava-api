from bs4 import BeautifulSoup
import json

"""
@page https://www.colaboraread.com.br/aluno/timeline/index
"""

def panels(s, links):
    pages = []

    for link in links:
      pages.append(s.get('https://www.colaboraread.com.br' + link).text)

    dummy = []

    for page in pages:
      dummy.append(parsePanel(page))
    
    return dummy

def parsePanel(page):
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
      data = small.text.strip()

      if data.find("Período") != -1:
        date = data.split(":",1)[1].strip().split("-")
        p['period'] = { "init": date[0].strip(), "final": date[1].strip() }

      if data.find("Cod. Atividade") != -1:
        code = data.split(":",1)
        p['code'] = code[1].strip()

      if data.find("Completude") != -1:
        completeness = small.parent
        progress = completeness.find("div", {"class": "progress-bar"})
        p['completeness'] = progress.text.strip().replace("%", "")

      if data.find("Pontuação da atividade:") != -1:
        grade = small.parent
        gradeStrig = grade.find("div", {"class": "progress-bar"})
        grades = gradeStrig.text.strip().split("de")
        p['grade'] = {  "current": grades[0].strip(), "total": grades[1].strip() }

    p['name'] = smalls[0].text.rsplit("-", 1)[0].strip()
    dummy.append(p)

    pageHeader = soup.find('header', attrs={'class':'page-header'})
    headerName = pageHeader.find('h2').text.strip().replace("%", "")

  return { 'name': headerName, 'panels': dummy  } 
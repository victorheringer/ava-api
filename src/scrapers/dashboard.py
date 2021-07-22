from bs4 import BeautifulSoup
from . import common

"""
@page https://www.colaboraread.com.br/aluno/dashboard/index
"""

def getActivities(session, page):
  activities = []
  ids = common.getRegistrationIds(page)
  report = common.getReportCardId(page)

  for item in ids:
    res = s.get('https://www.colaboraread.com.br/aluno/dashboard/listAtividades?id={item}&boletimId={report}')
    activities.append(res.text)

  return activities

def dashboard(session, link):

  page = session.get(link)

  storedlinks = []

  soup = BeautifulSoup(page.text, 'html.parser')

  data = soup.findAll('li', attrs={'class':'atividadesCronograma'})

  for li in data:
    links = li.findAll('a')
    
    for a in links: 
      if(a['href'] != '#'): 
        storedlinks.append(a['href'])
  
  return storedlinks
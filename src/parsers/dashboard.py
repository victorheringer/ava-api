from bs4 import BeautifulSoup
from utils import strings

"""
@page https://www.colaboraread.com.br/aluno/dashboard/index?matriculaId=:id
"""


def subjects(page):

  soup = BeautifulSoup(page, 'html.parser')
  lis = soup.findAll('li', attrs={'class':'atividadesCronograma'})

  subjects = []

  for li in lis:
    link = li.find('a', attrs={'class': 'atividadeNome'})
    btn = li.find('a', attrs={'class': 'btnMaisDetalhes'})

    report_card_id = btn.attrs.get("data-boletim-id", None) if btn != None else ''
    
    discipline_offer_id_link = link['href'].split("?")
    discipline_offer_id = strings.get_first_number(discipline_offer_id_link[1]) if len(discipline_offer_id_link) == 2 else ''

    subjects.append({ 
      "name": strings.clean(link.text),
      "report_card_id": report_card_id,
      "discipline_offer_id": discipline_offer_id,
      "activities": []
    })
  
  return subjects

def activities(page):
  
  soup = BeautifulSoup(page, 'html.parser')
  lis = soup.findAll('li')

  activitie = []

  for li in lis:
    a = li.find('a')
    ps = li.find('span', attrs={'class': 'dadosPeriodo'}).findAll('p')

    date = strings.clean(ps[1].text).split(" ")

    activitie.append({
      "name": strings.clean(a.text.split('-')[0]),
      "date": { "init": date[0], "end": date[3] }
    })

  return activitie
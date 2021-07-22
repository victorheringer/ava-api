def getRegistrationIds(page):
  ids = []
  options = page.find("select", {"id": "matriculaId"}).findAll("option")

  if options != None:
    for option in options: 
      ids.append({ "$activitiesId": option.get("value") , "text": option.text })

  return ids

def getReportCardId(page):
  ids = []
  links = page.findAll("a", {"class": "js-active-atividades"})

  if links != None:
    for link in links: 
      ids.append(link.attrs.get("data-boletim-id", None))

  return ids
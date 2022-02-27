import re

def clean(s, replaceMap = {}):
  cleanString = s.strip().replace("%", "")

  for k, v in replaceMap.items():
    cleanString = cleanString.replace(k, v)
  
  return cleanString

def get_first_number(text):
  try:
    result = re.findall('\d+',text)[0]
  except:
    result = ''

  return result

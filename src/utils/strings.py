def clean(s, replaceMap = {}):
  cleanString = s.strip().replace("%", "")

  for k, v in replaceMap.items():
    cleanString = cleanString.replace(k, v)
  
  return cleanString
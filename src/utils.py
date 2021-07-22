import re

def clean(s):
  return re.sub('\s+',' ',s)
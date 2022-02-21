import re

def parse(data):
  data = data[1:-1]
  html_tag = re.compile('<.*?>')
  result = re.sub(html_tag, '', data)
  return result

import requests
from bs4 import BeautifulSoup

def get_citations_needed_count(url):
  count = 0
  page = requests.get(url)

  soup = BeautifulSoup(page.content, "html.parser")

  a_tags = soup.find_all("a")
  
  for tag in a_tags:
    if "citation needed" in tag.get_text():
      count += 1
  return count


def get_citations_needed_report(url):
  page = requests.get(url)

  soup = BeautifulSoup(page.content, "html.parser")

  p_tags = soup.find_all("p")
  # print(p_tags)

  for tag in p_tags:
    if "citation needed" in tag.get_text():
      print(tag.get_text())
  
  

test = get_citations_needed_count("https://en.wikipedia.org/wiki/Alaska")
print(test)

test2 = get_citations_needed_report("https://en.wikipedia.org/wiki/Alaska")
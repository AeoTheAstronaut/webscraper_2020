from bs4 import BeautifulSoup
import requests

mod_url = 'https://csmoodle.clevelandhighschool.org/'
html_text = requests.get(mod_url).text
soup = BeautifulSoup(html_text, 'html.parser')

result = soup.find(id='docs-internal-guid-87d80929-7fff-0746-c3be-a3d1179550a7')

def main():
  for li in soup.select('span'):
    if li.text.strip() == '':
        continue
    return(li.text)

if __name__ == "__main__":
  main();

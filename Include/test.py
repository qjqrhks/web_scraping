import requests

from bs4 import BeautifulSoup

# Send a GET request to the website
url = 'https://media.naver.com/press/214?sid=100#lnb'
response = requests.get(url)
if response.status_code == 200:
    html_content = response.text
    print('1')
else:
    print('Failed to fetch web page')
    
# Parse the HTML content
soup = BeautifulSoup(html_content, 'html.parser')

# Find the title of the webpage
# title = soup.find('title').text

# Find all links on the webpage
links = soup.find_all('a')

# Find elements with a specific class
elements = soup.find_all('span', class_='press_edit_news_title')

# print(elements)

# for link in links:
#      print(link)

for element in elements:
    print(element.text.strip())
import requests
from bs4 import BeautifulSoup

page = requests.get("https://EnterWebsiteUrl...").text

# Creates a BeautifulSoup object
soup = BeautifulSoup(page, "html.parser")

# pulls all instances of <a> tag
artists = soup.find_all('a')

# clears data of all tags
for artist in artists:
    names = artist.contents[0]
    fullLink = artists.get('href')
    print(names)
    print(fullLink)

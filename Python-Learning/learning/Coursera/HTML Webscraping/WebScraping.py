# Webscraping : a process that can be used to automatically extract info from a website

from bs4 import BeautifulSoup

html = "<!DOCTYPE html><html><head><title>Page Title</title></head><body><h3><b id='boldest'>Lebron James</b></h3><p> Salary: $ 92,000,000 </p><h3> Stephen Curry</h3><p> Salary: $ 85,000, 000 </p><h3> Kevin Durant </h3><p> Salary: $73,200, 000</p></body></html>"
soup = BeautifulSoup(html, 'html5lib')

tag_object = soup.title
print(tag_object)

tag_object = soup.h3
print(tag_object)
# Look at Screenshot

tag_child = tag_object.b
print(tag_child)
parent_tag = tag_child.parent
print(parent_tag)

sibling_1 = tag_object.next_sibling
print(sibling_1)
sibling_2 = sibling_1.next_sibling
print(sibling_2)

print(tag_child.attrs)
print(tag_child.string)

html = "<table><tr><td>Pizza Place</td><td>Orders</td><td>Slices </td></tr><tr><td>Domino'sPizza</td><td>10</td><td>100</td></tr><tr><tr><td>Little Caesars</td><td>12</td><td>144</td></table"
table = BeautifulSoup(html, 'html5lib')

table_rows = table.find_all(name = "tr")
print(table_rows)
first_row = table_rows[0]
print(first_row)
print(first_row.td)

for i, row in enumerate(table_rows):
    print("row", i)
    cells = row.find_all("td")

    for j, cell in enumerate(cells):
        print("column", j, "cell", cell)

import requests
url = "http://www.ibm.com"
data = requests.get(url).text
soup = BeautifulSoup(data,"html.parser")  # create a soup object using the variable 'data'
for link in soup.find_all('a',href=True):  # in html anchor/link is represented by the tag <a>

    print(link.get('href'))

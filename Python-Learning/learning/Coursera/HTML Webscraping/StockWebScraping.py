import pandas as pd
import requests
from bs4 import BeautifulSoup

url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/netflix_data_webpage.html"
data = requests.get(url).text
soup = BeautifulSoup(data, 'html5lib')
amazon_data = pd.DataFrame(columns=["Date", "Open", "High", "Low", "Close", "Volume"])

for row in soup.find("tbody").find_all("tr"):
    col = row.find_all("td")
    date = col[0].text  # ADD_CODE
    Open = col[1].text  # ADD_CODE
    high = col[2].text  # ADD_CODE
    low = col[3].text  # ADD_CODE
    close = col[4].text  # ADD_CODE
    adj_close = col[5].text  # ADD_CODE
    volume = col[6].text  # ADD_CODE

    df_new_row = pd.DataFrame(
        {"Date": [date], "Open": [Open], "High": [high], "Low": [low], "Close": [close], "Adj Close": [adj_close],
         "Volume": [volume]})
    amazon_data = pd.concat([amazon_data, df_new_row])
print(amazon_data)

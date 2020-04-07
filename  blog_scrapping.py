# blog scrapping
from bs4 import BeautifulSoup
import requests
from csv import writer

response = requests.get("https://www.rithmschool.com/blog")
soup = BeautifulSoup(response.text, "html.parser")
article = soup.find_all("article")

with open("blog_data.csv", "w") as csv_file:
    csv_writer = writer(csv_file)
    csv_writer.writerow(["title","link","date"])

    for art in article:
        a_tag = art.find("a")
        title = a_tag.get_text()
        url = a_tag["href"]
        date = art.find("time")["datetime"]
        csv_writer.writerow([title, url, date])
    
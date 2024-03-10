import requests
import unicodedata
import csv
from bs4 import BeautifulSoup

req = requests.get("https://www.epicgardening.com/types-of-flowers/")

soup = BeautifulSoup(req.text, 'html.parser')

flowers = []

h2 = soup.find_all("h2")
figure = soup.find_all("figure")
p = soup.find_all("p")

j = 11
for i in range(0, len(h2) - 5):
    name = unicodedata.normalize("NFKD", h2[i].get_text()).strip()
    img = figure[i].img["src"]
    science = unicodedata.normalize("NFKD", p[j].get_text()).strip().replace("Scientific Name: ", "")
    desc = unicodedata.normalize("NFKD", p[j+1].get_text()).strip().replace("\u2044", "").replace("", "")
    if i == 190:
        desc += unicodedata.normalize("NFKD", p[j+2].get_text()).strip()
        j+=1

    flowers.append({"name": name, "img": img, "scientific name": science, "desc": desc})
    j+=2


fields = ["name", "img", "scientific name", "desc"]
with open('test.csv', 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames = fields)
    writer.writeheader()
    writer.writerows(flowers)

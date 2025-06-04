import requests
from bs4 import BeautifulSoup

USERNAME = "nguyencongquang0209"

url = f"https://oj.vnoi.info/user/{USERNAME}"
res = requests.get(url)
soup = BeautifulSoup(res.text, "html.parser")

rating_tag = soup.find("li", string=lambda s: s and "Rating:" in s)
rating = rating_tag.text.split(":")[-1].strip() if rating_tag else "N/A"

badge_template = f"""
<svg xmlns="http://www.w3.org/2000/svg" width="150" height="20">
  <rect width="150" height="20" fill="#555"/>
  <rect x="60" width="90" height="20" fill="#4c1"/>
  <text x="30" y="14" fill="#fff" font-family="Verdana" font-size="11">VNOJ</text>
  <text x="90" y="14" fill="#fff" font-family="Verdana" font-size="11">{rating}</text>
</svg>
"""

with open("rating.svg", "w") as f:
    f.write(badge_template)

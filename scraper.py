import requests
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

quotes = soup.find_all("span", class_="text")
authors = soup.find_all("small", class_="author")

print("=== QUOTES OF THE DAY ===\n")
for i, (quote, author) in enumerate(zip(quotes, authors), 1):
    print(f"{i}. {quote.text}\n")
    print(f"    - . {author.text}\n")
    
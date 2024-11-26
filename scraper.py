import requests
import pandas as pd
from bs4 import BeautifulSoup

# Define the URL of the page you want to scrape
url = "http://books.toscrape.com/"

# Send a GET request to fetch the HTML content of the page
response = requests.get(url)
if response.status_code == 200:
    print("Successfully accessed the page!")
else:
    print("Failed to retrieve the page:", response.status_code)
    exit()

# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Find all book entries on the page
books = soup.find_all("article", class_="product_pod")
book_data = []
# Loop through each book entry and extract information


for book in books:
    title = book.h3.a["title"]
    price = book.find("p", class_="price_color").text
    rating = book.p["class"][1]  # Rating is stored as a CSS class, like "One", "Two", etc.

    book_data.append({"Tile":title, "Price":price, "Rating":rating})
    
df = pd.DataFrame(book_data)
df.to_csv("./data/books_scraped.csv",index=False)
print("Data saved to books")
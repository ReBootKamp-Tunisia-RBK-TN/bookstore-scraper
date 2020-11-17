import urllib.request
from bs4 import BeautifulSoup

# ADD YOUR IMPORTS BEFORE THIS LINE

# Use this function to write information about ONE book
# to the result file
# It takes a string as input, this string should have the following format
# line = book_name,book_price,book_url

# Feel free to change this method, if needed
def write_line(line):
    with open('./books.csv', 'a') as file:
        file.write(line)
        file.write('\n')

# WRITE YOUR CODE BELOW THIS LINE

url_template = 'http://books.toscrape.com/'

# GET URL
resp = urllib.request.urlopen(url_template)
page_html = resp.read() # Read the HTML response
resp.close() # Closes the connection to the url
page_soup = BeautifulSoup(page_html, "html.parser")

articles = page_soup.find_all("article", {"class":"product_pod"})
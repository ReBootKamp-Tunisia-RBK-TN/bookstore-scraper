import urllib.request
from bs4 import BeautifulSoup

# ADD YOUR IMPORTS BEFORE THIS LINE

# Use this function to write information about ONE book_element
# to the result file
# It takes a string as input, this string should have the following format
# line = book_name,book_price,book_url

# Feel free to change this method, if needed
def write_line(line):
    with open('./books.csv', 'a') as file:
        file.write(line)
        file.write('\n')

# WRITE YOUR CODE BELOW THIS LINE

url_template = 'http://books.toscrape.com/catalogue/page-{}.html'

for pageCount in range(1,51):
    # GET URL
    print('fetching page {}'.format(pageCount))
    resp = urllib.request.urlopen(url_template.format(pageCount))
    page_html = resp.read() # Read the HTML response
    resp.close() # Closes the connection to the url
    page_soup = BeautifulSoup(page_html, "html.parser")

    books = page_soup.find_all("article", {"class":"product_pod"})
    for book_element in books:
        # Locate html element that contains the book title
        title_element = book_element.find("h3").find('a')
        name = title_element['title']
        url = title_element['href']
        price = book_element.find("p",{"class": "price_color"}).text
        write_line("{},{},{}".format(name,price,url))

# ADD YOUR IMPORTS BEFORE THIS LINE
>>> import requests
>>> url = requests.get('http://books.toscrape.com/')
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
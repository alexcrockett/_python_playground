# Import libraries and modules
import requests  # To work with URLs
from bs4 import BeautifulSoup as bs  # To format the HTML

def wiki_content():
	# Fetch Wikipedia Main Page HTML content.
	response = requests.get('https://en.wikipedia.org/wiki/Main_Page')  # Get the URL
	return response.text  # Return HTML text

def todays_article(content):
	# Extract today's featured article section from Wikipedia.
	soup = bs(content, 'html.parser')  # Parse HTML content
	article_section = soup.find('div', class_='MainPageBG mp-box')  # Find the section
	return article_section.text.strip() if article_section else "Article not found"

def main():
	# Main function to fetch and display today's featured article.
	content = wiki_content()  # Fetch HTML content
	article = todays_article(content)  # Extract today's article
	print(article)  # Print the article content

if __name__ == "__main__":
	main()

# For this little program we used the following API
# https://api.spaceflightnewsapi.net/v4/docs/

import requests
import json

space_flight_api = "https://api.spaceflightnewsapi.net/v4/articles/?has_event=true&has_launch=true&is_featured=true&limit=3"
space_flight_news = requests.get(space_flight_api).json()
response_json = space_flight_news
articles = response_json['results']
for article in articles:
	print(f"Title: {article['title']}")
	print(f"Summary: {article['summary']}")
	print("\nMore information below:\n")
	print(f"URL: {article['url']}")
	print(f"Image URL: {article['image_url']}")
	print(f"News Site: {article['news_site']}")
	print(f"Published At: {article['published_at']}")
	print(f"Updated At: {article['updated_at']}")
	print(f"Featured: {article['featured']}")
	print(f"Launches: {', '.join([launch['provider'] for launch in article['launches']])}")
	print(f"Events: {', '.join([event['provider'] for event in article['events']])}")
	print("\n" + "-"*50 + "\n")
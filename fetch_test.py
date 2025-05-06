from newsapi import NewsApiClient

# Initialize API

newsapi = NewsApiClient(api_key='43c852ecdc6a46738ef15bd35db8f063')

# Fetch news for a UPSC topic
articles = newsapi.get_everything(q='India government', language='en', page_size=5)

# Print results
for i, article in enumerate(articles['articles'], 1):
    print(f"{i}. {article['title']}")
    print(f"Source: {article['source']['name']}")
    print(f"Description: {article['description']}")
    print("---")
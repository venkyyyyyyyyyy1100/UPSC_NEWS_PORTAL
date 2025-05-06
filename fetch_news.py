from newsapi import NewsApiClient
import nltk
from nltk.tokenize import sent_tokenize
from datetime import datetime, timedelta
import mysql.connector

# Initialize NewsAPI client
newsapi = NewsApiClient(api_key='43c852ecdc6a46738ef15bd35db8f063')

# Define subjects
subjects = {
    "Polity": "government policy",
    "Economy": "economy",
    "Environment": "climate change",
    "International Relations": "foreign policy"
}

# Ensure punkt is available
nltk.download('punkt', quiet=True)

def summarize_text(text, num_sentences=4):
    if not text or text == "No description available":
        return "No summary available."
    sentences = sent_tokenize(text)
    return ' '.join(sentences[:min(num_sentences, len(sentences))])


def fetch_and_save_news():
    # Connect to the database
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="upsc_user",
            password="upsc1234",
            database="upsc_news"
        )
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS news
                     (date VARCHAR(10), title TEXT, source TEXT, summary TEXT, url TEXT, subject TEXT)''')
    except mysql.connector.Error as e:
        print(f"Database connection failed: {e}")
        return

    today = datetime.now().strftime('%Y-%m-%d')
    print(f"Fetching news for {today}...")

    for subject, query in subjects.items():
        # Check if news for this date and subject already exists
        c.execute("SELECT COUNT(*) FROM news WHERE date = %s AND subject = %s", (today, subject))
        existing_count = c.fetchone()[0]

        if existing_count > 0:
            print(f"News for {subject} on {today} already exists. Skipping.")
            continue

        try:
            to_date = datetime.now()
            from_date = to_date - timedelta(days=7)
            from_date_str = from_date.strftime('%Y-%m-%d')
            to_date_str = to_date.strftime('%Y-%m-%d')
            articles = newsapi.get_everything(
                q=query,
                language='en',
                page_size=5,
                from_param=from_date_str,
                to=to_date_str
            )
            inserted_count = 0
            for article in articles['articles']:
                summary = summarize_text(article['description'] or "No description available", num_sentences=4)
                try:
                    c.execute("INSERT INTO news (date, title, source, summary, url, subject) VALUES (%s, %s, %s, %s, %s, %s)",
                              (today, article['title'], article['source']['name'], summary, article['url'], subject))
                    inserted_count += 1
                except mysql.connector.Error as e:
                    print(f"Insert failed for {article['title']}: {e}")
            conn.commit()
            print(f"Saved {inserted_count} articles for {subject} on {today}.")
        except Exception as e:
            print(f"Error fetching news for {subject}: {e}")

    conn.close()

if __name__ == "__main__":
    fetch_and_save_news()

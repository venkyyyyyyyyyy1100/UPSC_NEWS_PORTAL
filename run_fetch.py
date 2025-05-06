import schedule
import time
import os

def run_fetch():
    print("Running fetch_news.py...")
    os.system("python3 fetch_news.py")  # Changed from "python" to "python3"

# Schedule the fetch to run daily at midnight
schedule.every().day.at("19:10").do(run_fetch)

print("Scheduler started. Waiting for the next scheduled fetch...")
while True:
    schedule.run_pending()
    time.sleep(60)  # Check every minute
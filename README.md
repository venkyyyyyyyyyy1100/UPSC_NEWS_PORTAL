# 📰 UPSC News Summarizer

Welcome to the **UPSC News Summarizer**, a smart and user-friendly web portal for UPSC aspirants. This project automatically fetches and summarizes daily news articles using NLP techniques, helping aspirants quickly stay informed with relevant, categorized news summaries.

🔗 **GitHub Repo**: [UPSC_NEWS_PORTAL](https://github.com/venkyyyyyyyyyy1100/UPSC_NEWS_PORTAL)

---

## ✨ Features

- 📅 **Daily News Updates** — Automatically fetches and summarizes news every day
- 🧠 **NLP-Powered Summarization** — Uses natural language processing to generate concise summaries
- 🔐 **User Login System** — Secure login for accessing personalized features
- 📌 **Bookmarking System** — Save and manage important articles permanently
- 🔍 **Category & Date Filters** — Easily view news by category (Polity, Environment, Science & Tech, etc.) and date

---

## 🛠️ Tech Stack

| Component       | Technology         |
|-----------------|--------------------|
| Frontend        | Streamlit          |
| Backend         | Python             |
| NLP             | Hugging Face Transformers / SpaCy |
| News Source     | News API           |
| Database        | MySQL              |
| Automation      | Cron Jobs (Linux)  |
| Hosting (optional) | Streamlit Sharing / Local server |

---

## 📁 Project Structure

UPSC_NEWS_PORTAL/
├── app.py # 🎯 Main Streamlit app
├── login.py # 🔐 Handles user login and session
├── database.py # 🗃️ MySQL connection and queries
├── summarizer.py # 🧠 NLP summarization logic
├── fetch_news.py # 📡 Fetches and stores news from API
├── bookmarks.py # 📌 Manage saved articles
├── utils.py # 🔧 Helper functions
├── requirements.txt # 📦 Python dependencies
├── cron_job.sh # ⏱️ Script for daily news fetching
└── README.md # 📘 Project documentation (this file)



---

## 🚀 How to Run the Project

1. **Clone the repository**
   ```bash
   git clone https://github.com/venkyyyyyyyyyy1100/UPSC_NEWS_PORTAL.git
   cd UPSC_NEWS_PORTAL


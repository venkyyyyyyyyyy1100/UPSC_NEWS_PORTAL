import streamlit as st
import mysql.connector
from datetime import datetime

# Inject custom CSS for background and styling

video_url = "http://localhost:8000/background.mp4"

st.markdown(
    f"""
    <style>
    .stApp {{
        background: linear-gradient(135deg, #dbeafe, #bfdbfe, #93c5fd);  /* Light blue gradient */
        background-size: cover;
        background-attachment: fixed;
        color: #0f172a;  /* Deep navy text for contrast */
    }}
    /* Override specific Streamlit component colors */
    .css-10trblm, .css-1v3fvcr, .css-qbe2hs {{
        color: #0f172a !important;
    }}
    video {{
        position: fixed;
        right: 0;
        bottom: 0;
        min-width: 100%;
        min-height: 100%;
        z-index: -1;
        opacity: 0.1;  /* Very soft overlay */
        object-fit: cover;
    }}
    </style>
    <video autoplay loop muted>
        <source src="{video_url}" type="video/mp4">
    </video>
    """,
    unsafe_allow_html=True
)


st.title("UPSC NEWS SUMMARIZER")


with st.container():
    st.markdown("""
    ### 🌐 About This Website
    Welcome to **UPSC News Digest** — your personalized hub for daily, categorized news tailored for UPSC aspirants.  
    We bring you the most relevant updates across key areas like **Polity**, **Economy**, **Environment**, and **Science & Tech**, helping you stay informed without the clutter.

    📰 *Stay focused. Stay updated.*
    """)


# Define subjects for the dropdown
subjects = ["All", "Polity", "Economy", "Environment", "International Relations"]
subject = st.selectbox("Select the Type of News", subjects)

# Date picker for viewing news
selected_date = st.date_input("Select a Date to View News", value=datetime.now())

if st.button("View News for Selected Date"):
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="upsc_user",
            password="upsc1234",
            database="upsc_news"
        )
        c = conn.cursor()
        selected_date_str = selected_date.strftime('%Y-%m-%d')

        # Query based on date and subject
        if subject == "All":
            c.execute("SELECT * FROM news WHERE date = %s", (selected_date_str,))
        else:
            c.execute("SELECT * FROM news WHERE date = %s AND subject = %s", (selected_date_str, subject))

        past_news = c.fetchall()
        st.write(f"Found {len(past_news)} articles for {selected_date_str} (Subject: {subject})")
        if past_news:
            st.subheader(f"News for {selected_date_str} - {subject}")
            for article in past_news:
                st.write(f"{article[1]}")
                st.write(f"Source: {article[2]}")
                st.write(f"Summary: {article[3]}")
                st.write(f"[Read Full Article]({article[4]})")
                st.write(f"Subject: {article[5]}")
                st.write("---")
        else:
            st.write("No news available for this date and subject.")
        conn.close()
    except Exception as e:
        st.error(f"Error fetching news: {e}")

# Ensure connection is closed if not already
try:
    conn.close()
except:
    pass
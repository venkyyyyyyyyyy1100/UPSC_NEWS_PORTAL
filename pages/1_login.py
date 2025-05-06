import streamlit as st
import mysql.connector
from streamlit_extras.switch_page_button import switch_page

# Set page config
st.set_page_config(page_title="Login - UPSC News", page_icon="🔐")

st.title("🔐 Welcome to UPSC News Summarizer")

# ---------- LOGIN SECTION ----------
with st.expander("🔓 Sign In", expanded=True):
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    def verify_credentials(user, pwd):
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="upsc_user",
                password="upsc1234",
                database="upsc_news"
            )
            cursor = conn.cursor()
            query = "SELECT * FROM users WHERE username = %s AND password = %s"
            cursor.execute(query, (user, pwd))
            result = cursor.fetchone()
            conn.close()
            return result is not None
        except Exception as e:
            st.error(f"Database error: {e}")
            return False

    if st.button("Login"):
        if not username or not password:
            st.warning("Please fill in both fields.")
        elif verify_credentials(username, password):
            st.success("Login successful! Redirecting...")
            switch_page("Home")  # Ensure 'app.py' is in the `pages/` folder if needed
        else:
            st.error("Invalid username or password.")

# ---------- SIGN-UP SECTION ----------
with st.expander("📝 Create New Account"):
    new_user = st.text_input("New Username")
    new_pass = st.text_input("New Password", type="password")

    if st.button("Sign Up"):
        if not new_user or not new_pass:
            st.warning("Please fill in both fields.")
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost",
                    user="upsc_user",
                    password="upsc1234",
                    database="upsc_news"
                )
                cursor = conn.cursor()

                # Check if username already exists
                cursor.execute("SELECT * FROM users WHERE username = %s", (new_user,))
                if cursor.fetchone():
                    st.warning("Username already exists. Choose a different one.")
                else:
                    cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (new_user, new_pass))
                    conn.commit()
                    st.success("Sign-up successful! Please log in now.")
                conn.close()
            except Exception as e:
                st.error(f"Error during sign-up: {e}")

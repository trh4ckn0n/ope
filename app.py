import streamlit as st
import requests
from bs4 import BeautifulSoup
import feedparser  # Pour lire les flux RSS (alternative)
import time

# CONFIGURATION DE LA PAGE
st.set_page_config(page_title="Anonymous Tracker", layout="wide", page_icon="🕶️")

# CSS HACKER STYLE
st.markdown("""
    <style>
        body {
            background-color: #000;
            color: #0f0;
            font-family: 'Courier New', monospace;
        }
        .stApp {
            background-color: #000;
        }
        .stMarkdown {
            color: #0f0;
        }
        .stSidebar {
            background-color: #111;
            color: #0f0;
            border-right: 2px solid #0f0;
        }
        .stButton>button {
            background-color: #0f0;
            color: #000;
            font-weight: bold;
        }
        .stAlert {
            background-color: #222;
            color: #ff0;
        }
        .title {
            text-align: center;
            font-size: 36px;
            font-weight: bold;
            text-shadow: 0 0 10px #0f0;
        }
        .banner {
            text-align: center;
            font-size: 20px;
            color: #0f0;
            animation: blink 1s infinite;
        }
        @keyframes blink {
            50% { opacity: 0.5; }
        }
    </style>
""", unsafe_allow_html=True)

# TITRE PRINCIPAL AVEC EFFET
st.markdown('<h1 class="title">🕶️ Anonymous Tracker : Luttes et Opérations en Cours</h1>', unsafe_allow_html=True)
st.markdown('<div class="banner">⚡ Live updates | Cyberwarfare & Hacktivism ⚡</div>', unsafe_allow_html=True)


# SIDEBAR
st.sidebar.header("🔎 Navigation")
page = st.sidebar.radio("Choisissez une section", ["Accueil", "Opérations en cours", "Histoire d'Anonymous", "Ressources"])

# 📰 FONCTION : RÉCUPÉRER LES ACTUALITÉS (API RSS GOOGLE NEWS)
def get_anonymous_news():
    rss_url = "https://news.google.com/rss/search?q=Anonymous+Hacktivism&hl=fr&gl=FR&ceid=FR:fr"
    
    try:
        feed = feedparser.parse(rss_url)
        articles = [{"title": entry.title, "link": entry.link} for entry in feed.entries[:5]]

        if not articles:
            return [{"title": "⚠️ Aucune actualité disponible", "link": "#"}]
        return articles
    
    except Exception as e:
        return [{"title": f"🚨 Erreur de connexion : {str(e)}", "link": "#"}]    

# PAGE ACCUEIL
if page == "Accueil":
    st.markdown("## 📢 Dernières actualités sur Anonymous")
    
    with st.spinner("🔍 Chargement des actualités..."):
        time.sleep(1)
        news = get_anonymous_news()
    
    for article in news:
        st.markdown(f"🔹 [{article['title']}]({article['link']})")

# MESSAGE FINAL
st.sidebar.write("💡 **Projet éducatif et informatif uniquement**")

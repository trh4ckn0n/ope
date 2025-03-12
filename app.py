import streamlit as st
import requests
from bs4 import BeautifulSoup
import plotly.express as px
import pandas as pd
import feedparser
import time

# CONFIGURATION DE LA PAGE
st.set_page_config(
    page_title="Anonymous Tracker",
    layout="wide",
    page_icon="🕶️"
)

# CSS PERSONNALISÉ (Thème Hacker)
st.markdown("""
    <style>
        body { background-color: #000; color: #0f0; font-family: 'Courier New', monospace; }
        .stApp { background-color: #000; }
        .stMarkdown { color: #0f0; }
        .stSidebar { background-color: #111; color: #0f0; border-right: 2px solid #0f0; }
        .stButton>button { background-color: #0f0; color: #000; font-weight: bold; }
        .title { text-align: center; font-size: 36px; font-weight: bold; text-shadow: 0 0 10px #0f0; }
        .banner { text-align: center; font-size: 20px; color: #0f0; animation: blink 1s infinite; }
        @keyframes blink { 50% { opacity: 0.5; } }
    </style>
""", unsafe_allow_html=True)

# TITRE PRINCIPAL AVEC EFFET
st.markdown('<h1 class="title">🕶️ Anonymous Tracker : Luttes et Opérations en Cours</h1>', unsafe_allow_html=True)
# Ajout du logo principal
st.markdown("""
    <div style="text-align: center;">
        <img src="https://f.top4top.io/p_3357q35po1.png" width="150">
    </div>
""", unsafe_allow_html=True)
st.markdown('<div class="banner">⚡ Live updates | Cyberwarfare & Hacktivism ⚡</div>', unsafe_allow_html=True)

# SIDEBAR INTERACTIVE
st.sidebar.markdown("""
    <div style="text-align: center;">
        <img src="https://e.top4top.io/p_33570y4z00.png" width="180">
    </div>
""", unsafe_allow_html=True)
st.sidebar.header("🔎 Navigation")
page = st.sidebar.radio("Choisissez une section", ["Accueil", "Opérations en cours", "Histoire d'Anonymous", "Ressources"])

# 📰 RÉCUPÉRATION DES ACTUALITÉS (RSS Google News)
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

# 🌍 PAGE OPÉRATIONS EN COURS (CARTE INTERACTIVE)
elif page == "Opérations en cours":
    st.markdown("## 🌍 Carte des Opérations en Cours")

    # Base de données des opérations Anonymous
    data = pd.DataFrame({
        "Ville": ["Paris", "New York", "Berlin", "Tokyo", "Rome", "Gaza", "Kiev"],
        "Latitude": [48.8566, 40.7128, 52.5200, 35.6895, 41.9028, 31.5, 50.4501],
        "Longitude": [2.3522, -74.0060, 13.4050, 139.6917, 12.4964, 34.47, 30.5234],
        "Opération": ["#OpFrance", "#OpUSA", "#OpGermany", "#OpJapan", "#OpIsrahell", "#OpRussia", "#OpFckPtn"]
    })

    fig = px.scatter_mapbox(
        data, lat="Latitude", lon="Longitude", 
        text="Opération", zoom=1,
        color_discrete_sequence=["#00FF00"],
        mapbox_style="carto-darkmatter"
    )

    st.plotly_chart(fig, use_container_width=True)

# 📜 PAGE HISTOIRE D'ANONYMOUS
elif page == "Histoire d'Anonymous":
    st.markdown("## 📜 Histoire d'Anonymous")
    st.write("""
    Anonymous est un collectif hacktiviste né sur le forum 4chan en 2003.
    Leur devise est : *We Are Anonymous. We Are Legion. We Do Not Forgive. We Do Not Forget. Expect Us.*
    """)

# 📚 PAGE RESSOURCES ET APPRENTISSAGE
elif page == "Ressources":
    st.markdown("## 📚 Ressources et Apprentissage")
    st.write("- [Guide de cybersécurité](https://www.cybersecurity-guide.com)")
    st.write("- [Forum Anonymous (Tor)](http://example.onion)")
    st.write("- [Débuter en OSINT](https://osintframework.com)")

# 📢 FOOTER
st.sidebar.write("💡 **Projet éducatif et informatif uniquement**")

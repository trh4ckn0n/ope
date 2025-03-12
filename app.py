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

# CSS PERSONNALISÉ (Thème Hacker + EFFET GLITCH)
st.markdown("""
    <style>
        body { background-color: #000; color: #0f0; font-family: 'Courier New', monospace; }
        .stApp { background-color: #000; }
        .stMarkdown { color: #0f0; }
        .stSidebar { background-color: #111; color: #0f0; border-right: 2px solid #0f0; }
        .stButton>button { background-color: #0f0; color: #000; font-weight: bold; }
        
        /* Effet glitch sur le titre */
        .glitch {
            font-size: 40px;
            font-weight: bold;
            text-align: center;
            color: #0f0;
            position: relative;
            text-shadow: 0 0 10px #0f0, 0 0 20px #0f0;
            animation: glitch 1.5s infinite;
        }
        
        @keyframes glitch {
            0% { transform: translate(0); }
            20% { transform: translate(-2px, 2px); }
            40% { transform: translate(2px, -2px); }
            60% { transform: translate(-2px, 2px); }
            80% { transform: translate(2px, -2px); }
            100% { transform: translate(0); }
        }

        /* Animation blink */
        .banner {
            text-align: center;
            font-size: 20px;
            color: #0f0;
            animation: blink 1s infinite alternate;
        }
        @keyframes blink {
            50% { opacity: 0.5; }
        }
        
        /* Boutons hacker */
        .stButton>button {
            border: 2px solid #0f0;
            background-color: transparent;
            color: #0f0;
            font-weight: bold;
            text-shadow: 0 0 5px #0f0;
            transition: 0.3s;
        }
        .stButton>button:hover {
            background-color: #0f0;
            color: #000;
            text-shadow: none;
        }
    </style>
""", unsafe_allow_html=True)

# 🔥 TITRE PRINCIPAL AVEC GLITCH
st.markdown('<h1 class="glitch">🕶️ Anonymous Tracker : Luttes et Opérations en Cours</h1>', unsafe_allow_html=True)

# LOGO PRINCIPAL
st.markdown("""
    <div style="text-align: center;">
        <img src="https://raw.githubusercontent.com/trh4ckn0n/ope/refs/heads/main/picsvg_download.svg" width="150">
    </div>
""", unsafe_allow_html=True)

# ANIMATION SOUS-TITRE
st.markdown('<div class="banner">⚡ Live updates | Cyberwarfare & Hacktivism ⚡</div>', unsafe_allow_html=True)

# SIDEBAR INTERACTIVE AVEC LOGO (VERSION FOND NOIR)
st.sidebar.markdown("""
    <div style="text-align: center;">
        <img src="https://e.top4top.io/p_33570y4z00.png" width="180">
    </div>
""", unsafe_allow_html=True)

st.sidebar.header("🔎 Navigation")
st.sidebar.write("[![Star](https://img.shields.io/github/stars/trh4ckn0n/ope.svg?logo=github&style=social)](https://gitHub.com/trh4ckn0n/ope)")

page = st.sidebar.radio("Choisissez une section", ["Accueil", "Opérations en cours", "Histoire d'Anonymous", "Ressources", "À propos"])
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

# Ajout d'une nouvelle option dans la navigation

# 📄 PAGE À PROPOS
if page == "À propos":
    st.markdown("## ℹ️ À propos d'Anonymous Tracker")

    st.write("""
    **Anonymous Tracker** est une plateforme interactive permettant de suivre les actions du collectif Anonymous à travers le monde.
    Son objectif est d'offrir une **visualisation en temps réel** des opérations, une centralisation des informations issues de sources OSINT,
    et un espace éducatif pour sensibiliser à la cybersécurité et au hacktivisme.

    🚀 **Fonctionnalités principales** :
    - 📢 **Fil d'actualités** sur Anonymous et le hacktivisme.
    - 🌍 **Carte interactive** des opérations en cours.
    - 📜 **Histoire du collectif** pour comprendre son impact.
    - 📚 **Ressources** pour apprendre l'OSINT et la cybersécurité.

    Ce projet est **strictement éducatif** et ne vise en aucun cas à inciter à des activités illégales.
    """)

    st.write("[![Star](https://img.shields.io/github/stars/trh4ckn0n/ope.svg?logo=github&style=social)](https://gitHub.com/trh4ckn0n/ope)")
    # Ajout du logo Anonymous en bas
    st.markdown("""
        <div style="text-align: center;">
            <img src="https://raw.githubusercontent.com/trh4ckn0n/ope/refs/heads/main/picsvg_download.svg" width="150">
        </div>
    """, unsafe_allow_html=True)
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
        "Ville": ["Paris", "New York", "Berlin", "Tokyo", "Roma", "Gaza", "Minsk", "Kiev"],
        "Latitude": [48.8566, 40.7128, 52.5200, 35.6895, 41.9028, 31.5, 53.9045398, 50.4801],
        "Longitude": [2.3522, -74.0060, 13.4050, 139.6917, 12.4964, 34.47, 27.5615244, 30.5254],
        "Opération": ["#OpFrance", "#OpUSA", "#OpGermany", "#OpJapan", "#OpItalia", "#OpIsrahell", "#OpRussia", "#OpFckPtn"]
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
    st.write("- [Forum Anonymous (Tor)](http://**.onion/soon)")
    st.write("- [Débuter en OSINT](https://osintframework.com)")

# 📢 FOOTER
st.sidebar.write("💡 **Projet éducatif et informatif uniquement**")

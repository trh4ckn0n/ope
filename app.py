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
    page_icon="馃暥锔�"
)

# CSS PERSONNALIS脡 (Th猫me Hacker + EFFET GLITCH)
st.markdown("""
    <style>
        body { background-color: #000; color: #0f0; font-family: 'Courier New', monospace; }
        .stApp {
            background-color: transparent; /* Rendre le fond de l'application transparent */
        }        
        .stMarkdown { color: #0f0; }
        .stSidebar { background-color: #111; color: #0f0; border-right: 2px solid #0f0; }

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

# 馃敟 TITRE PRINCIPAL AVEC GLITCH
st.markdown('<h1 class="glitch">馃暥锔� Anonymous Tracker : Luttes et Op茅rations en Cours</h1>', unsafe_allow_html=True)

# LOGO PRINCIPAL
st.markdown("""
    <div style="text-align: center;">
        <img src="https://raw.githubusercontent.com/trh4ckn0n/ope/refs/heads/main/uYidUgA01.svg" width="150">
    </div>
""", unsafe_allow_html=True)

# ANIMATION SOUS-TITRE
st.markdown('<div class="banner">鈿� Live updates | Cyberwarfare & Hacktivism 鈿�</div>', unsafe_allow_html=True)

# SIDEBAR INTERACTIVE AVEC LOGO (VERSION FOND NOIR)
st.sidebar.markdown("""
    <div style="text-align: center;">
        <img src="https://e.top4top.io/p_33570y4z00.png" width="180">
    </div>
""", unsafe_allow_html=True)

st.sidebar.header("馃攷 Navigation")
st.sidebar.write("[![Star](https://img.shields.io/github/stars/trh4ckn0n/ope.svg?logo=github&style=social)](https://gitHub.com/trh4ckn0n/ope)")

page = st.sidebar.radio("Choisissez une section", ["Accueil", "Op茅rations en cours", "Histoire d'Anonymous", "Ressources", "脌 propos"])
# 馃摪 R脡CUP脡RATION DES ACTUALIT脡S (RSS Google News)
def get_anonymous_news():
    rss_url = "https://news.google.com/rss/search?q=Anonymous+Hacktivism&hl=fr&gl=FR&ceid=FR:fr"
    
    try:
        feed = feedparser.parse(rss_url)
        articles = [{"title": entry.title, "link": entry.link} for entry in feed.entries[:8]]

        if not articles:
            return [{"title": "鈿狅笍 Aucune actualit茅 disponible", "link": "#"}]
        return articles
    
    except Exception as e:
        return [{"title": f"馃毃 Erreur de connexion : {str(e)}", "link": "#"}]    

# Ajout d'une nouvelle option dans la navigation

# 馃搫 PAGE 脌 PROPOS
if page == "脌 propos":
    st.markdown("## 鈩癸笍 脌 propos d'Anonymous Tracker")

    st.write("""
    **Anonymous Tracker** est une plateforme interactive permettant de suivre les actions du collectif Anonymous 脿 travers le monde.
    Son objectif est d'offrir une **visualisation en temps r茅el** des op茅rations, une centralisation des informations issues de sources OSINT,
    et un espace 茅ducatif pour sensibiliser 脿 la cybers茅curit茅 et au hacktivisme.

    馃殌 **Fonctionnalit茅s principales** :
    - 馃摙 **Fil d'actualit茅s** sur Anonymous et le hacktivisme.
    - 馃實 **Carte interactive** des op茅rations en cours.
    - 馃摐 **Histoire du collectif** pour comprendre son impact.
    - 馃摎 **Ressources** pour apprendre l'OSINT et la cybers茅curit茅.

    Ce projet est **strictement 茅ducatif** et ne vise en aucun cas 脿 inciter 脿 des activit茅s ill茅gales.
    """)

    st.write("[![Star](https://img.shields.io/github/stars/trh4ckn0n/ope.svg?logo=github&style=social)](https://gitHub.com/trh4ckn0n/ope)")
    # Ajout du logo Anonymous en bas
    st.markdown("""
        <div style="text-align: center;">
            <img src="https://raw.githubusercontent.com/trh4ckn0n/ope/refs/heads/main/KXnKNCo01.svg" width="150">
        </div>
    """, unsafe_allow_html=True)
# PAGE ACCUEIL
if page == "Accueil":  
    st.markdown("## 馃摙 Derni猫res actualit茅s sur Anonymous")
    
    with st.spinner("馃攳 Chargement des actualit茅s..."):
        time.sleep(1)
        news = get_anonymous_news()

    for article in news:
        st.markdown(f"馃敼 [{article['title']}]({article['link']})")

# 馃實 PAGE OP脡RATIONS EN COURS (CARTE INTERACTIVE)
elif page == "Op茅rations en cours":
    st.markdown("## 馃實 Carte des Op茅rations en Cours")

    # Base de donn茅es des op茅rations Anonymous
    data = pd.DataFrame({
        "Ville": ["Paris", "New York", "Berlin", "Tokyo", "Roma", "Gaza", "Minsk", "Kiev"],
        "Latitude": [48.8566, 40.7128, 52.5200, 35.6895, 41.9028, 31.5, 53.9045398, 50.4801],
        "Longitude": [2.3522, -74.0060, 13.4050, 139.6917, 12.4964, 34.47, 27.5615244, 30.5254],
        "Op茅ration": ["#OpFrance", "#OpUSA", "#OpGermany", "#OpJapan", "#OpItalia", "#OpIsrahell", "#OpRussia", "#OpFckPtn"]
    })

    fig = px.scatter_mapbox(
        data, lat="Latitude", lon="Longitude", 
        text="Op茅ration", zoom=1,
        color_discrete_sequence=["#00FF00"],
        mapbox_style="carto-darkmatter"
    )

    st.plotly_chart(fig, use_container_width=True)

# 馃摐 PAGE HISTOIRE D'ANONYMOUS
elif page == "Histoire d'Anonymous":
    st.markdown("## 馃摐 Histoire d'Anonymous")
    st.markdown("""
    <div style="text-align: center;">
        <img src="https://raw.githubusercontent.com/trh4ckn0n/ope/refs/heads/main/6c8KI301%20(4).svg" width="150">
    </div>
""", unsafe_allow_html=True)

    st.write("""
    Anonymous est un collectif hacktiviste n茅 sur le forum 4chan en 2003.
    Leur devise est : *We Are Anonymous. We Are Legion. We Do Not Forgive. We Do Not Forget. Expect Us.*
    """)

# 馃摎 PAGE RESSOURCES ET APPRENTISSAGE
elif page == "Ressources":
    st.markdown("## 馃摎 Ressources et Apprentissage")
    st.write("- [Guide de cybers茅curit茅](https://www.cybersecurity-guide.com)")
    st.write("- [Forum Anonymous (Tor)](http://**.onion/soon)")
    st.write("- [D茅buter en OSINT](https://osintframework.com)")

# 馃摙 FOOTER
st.sidebar.write("馃挕 **Projet 茅ducatif et informatif uniquement**")

import streamlit as st
import requests
from bs4 import BeautifulSoup
import plotly.express as px
import pandas as pd
import feedparser
import time
from argon2 import PasswordHasher
import hashlib
import os

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

# 🔥 TITRE PRINCIPAL AVEC GLITCH
st.markdown('<h1 class="glitch">🕶️ Anonymous Tracker : Luttes et Opérations en Cours</h1>', unsafe_allow_html=True)

# LOGO PRINCIPAL
st.markdown("""
    <div style="text-align: center;">
        <img src="https://raw.githubusercontent.com/trh4ckn0n/ope/refs/heads/main/uYidUgA01.svg" width="150">
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

page = st.sidebar.radio("Choisissez une section", ["Accueil", "Opérations en cours", "Histoire d'Anonymous", "Ressources", "À propos", "Se connecter"])

# 🔒 AUTHENTIFICATION AVEC ARGON2
ph = PasswordHasher()

# Exemple de base de données utilisateur fictive (en production, tu utiliserais une base de données réelle)
users_db = {
    "admin": ph.hash("adminpassword"),  # Mot de passe sécurisé
}

# Gestion des sessions
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

# Fonction de connexion
def authenticate(username, password):
    if username in users_db:
        try:
            ph.verify(users_db[username], password)
            return True
        except:
            return False
    return False

# Gérer la page de connexion
if page == "Se connecter":
    st.markdown("## 🔑 Connexion")
    username = st.text_input("Nom d'utilisateur", "")
    password = st.text_input("Mot de passe", type="password")

    if st.button("Se connecter"):
        if authenticate(username, password):
            st.session_state.authenticated = True
            st.success("Bienvenue ! Vous êtes connecté.")
        else:
            st.error("Nom d'utilisateur ou mot de passe incorrect.")

# Pages accessibles seulement si l'utilisateur est authentifié
if st.session_state.authenticated:
    # PAGE À PROPOS
    if page == "À propos":
        st.markdown("## ℹ️ À propos d'Anonymous Tracker")
        st.write("""
        **Anonymous Tracker** est une plateforme interactive permettant de suivre les actions du collectif Anonymous à travers le monde.
        Son objectif est d'offrir une **visualisation en temps réel** des opérations, une centralisation des informations issues de sources OSINT,
        et un espace éducatif pour sensibiliser à la cybersécurité et au hacktivisme.
        """)

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

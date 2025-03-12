import streamlit as st
import requests
from bs4 import BeautifulSoup
import plotly.express as px
import pandas as pd

# Configuration de la page
st.set_page_config(page_title="Anonymous Tracker", layout="wide")

# CSS pour un thème sombre et contrasté
st.markdown(
    """
    <style>
        body {
            background-color: #0d1117;
            color: #ffffff;
        }
        .stApp {
            background-color: #0d1117;
        }
        .sidebar .sidebar-content {
            background-color: #161b22;
        }
        h1, h2, h3, h4, h5, h6 {
            color: #00ffcc;
        }
        .stMarkdown a {
            color: #ff0066;
            font-weight: bold;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Titre principal
st.title("🕶️ Anonymous Tracker : Luttes et Opérations en Cours")

# Sidebar
st.sidebar.header("Navigation")
page = st.sidebar.radio("Choisissez une section", ["Accueil", "Opérations en cours", "Histoire d'Anonymous", "Ressources"])

# Fonction pour récupérer des news
def get_anonymous_news():
    url = "https://www.cybersecurity-insiders.com/category/anonymous/"  # Exemple de source
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    news = soup.find_all('h2', class_='entry-title')

    articles = []
    for n in news[:5]:  # Récupérer les 5 derniers articles
        title = n.text.strip()
        link = n.a['href']
        articles.append({"title": title, "link": link})
    return articles

# Page Accueil
if page == "Accueil":
    st.markdown("## 📢 Dernières actualités sur Anonymous")
    news = get_anonymous_news()
    for article in news:
        st.markdown(f"🔹 [{article['title']}]({article['link']})")

# Page Opérations en cours (exemple avec une carte)
elif page == "Opérations en cours":
    st.markdown("## 🌍 Carte des Opérations en Cours")
    
    # Dataset avec les latitudes et longitudes
    data = pd.DataFrame({
        "Ville": ["Paris", "New York", "Berlin", "Tokyo", "Rome", "Gaza", "Kiev"],
        "Latitude": [48.8566, 40.7128, 52.5200, 35.6895, 41.9028, 31.5, 50.4501],
        "Longitude": [2.3522, -74.0060, 13.4050, 139.6917, 12.4964, 34.47, 30.5234],
        "Opération": ["#OpFrance", "#OpUSA", "#OpGermany", "#OpJapan", "#OpIsrahell", "#OpRussia", "#OpFckPtn"]
    })
    
    # Carte avec un fond sombre et des marqueurs colorés
    fig = px.scatter_mapbox(
        data, 
        lat="Latitude", lon="Longitude", 
        text="Opération", zoom=1,
        mapbox_style="carto-darkmatter",  # Fond sombre
        color_discrete_sequence=["#ff0066"]  # Couleur des marqueurs en fluo
    )
    
    st.plotly_chart(fig)

# Page Histoire
elif page == "Histoire d'Anonymous":
    st.markdown("## 📜 Histoire d'Anonymous")
    st.write("Anonymous est un collectif hacktiviste né sur le forum 4chan en 2003...")

# Page Ressources
elif page == "Ressources":
    st.markdown("## 📚 Ressources et Apprentissage")
    st.write("- [Guide de cybersécurité](https://www.cybersecurity-guide.com)")
    st.write("- [Forum Anonymous (Tor)](http://example.onion)")

# Footer
st.sidebar.write("💡 **Projet éducatif et informatif uniquement**")

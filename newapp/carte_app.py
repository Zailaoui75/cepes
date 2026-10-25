# carte_app.py — affiche sortie_cepes/carte_chenaies_20km.html en plein écran dans Streamlit
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

CARTE = Path(__file__).parent / "sortie_cepes" / "carte_chenaies_20km.html"

st.set_page_config(page_title="Carte cèpes", layout="wide", initial_sidebar_state="collapsed")

# enlève marges, en-tête et pied de page de Streamlit, et étire la carte à 100 % de la fenêtre
st.markdown("""
<style>
  header, footer, [data-testid="stToolbar"], [data-testid="stDecoration"] {display: none !important;}
  .block-container, [data-testid="stMainBlockContainer"] {padding: 0 !important; max-width: 100% !important;}
  [data-testid="stVerticalBlock"] {gap: 0 !important;}
  iframe {width: 100vw !important; height: 100vh !important; border: 0; display: block;}
</style>
""", unsafe_allow_html=True)


@st.cache_data(show_spinner="Chargement de la carte…")
def lire_carte(chemin: str, date_modif: float) -> str:
    return Path(chemin).read_text(encoding="utf-8")


if not CARTE.exists():
    st.error(f"Carte introuvable : {CARTE}")
    st.stop()

html = lire_carte(str(CARTE), CARTE.stat().st_mtime)
if hasattr(st, "iframe"):          # Streamlit récent
    st.iframe(html, height=900)
else:                              # anciennes versions
    components.html(html, height=900, scrolling=False)

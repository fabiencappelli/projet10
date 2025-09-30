import os
import requests
import streamlit as st

API_BASE = os.getenv("RECO_API_URL", "https://recoprojet10.azurewebsites.net")
SECRET = os.getenv("AZ_RECO_SECRET")

st.set_page_config(page_title="Recommandations", page_icon="📰", layout="centered")
st.title("📰 Recommandations d'articles")

with st.form("reco_form"):
    user_id = st.text_input("ID utilisateur", value="12345")
    k = st.number_input("Nombre d'articles", min_value=1, max_value=20, value=5, step=1)
    submitted = st.form_submit_button("Obtenir des recommandations")

if submitted:
    if not SECRET:
        st.error("Clé d'API manquante côté serveur (AZ_RECO_SECRET).")
    else:
        try:
            url = f"{API_BASE}/api/recommend"
            params = {"code": SECRET, "user_id": user_id, "k": k}
            r = requests.get(url, params=params, timeout=15)
            r.raise_for_status()
            data = (
                r.json()
                if r.headers.get("content-type", "").startswith("application/json")
                else r.text
            )
            st.subheader("Résultats")
            st.write(data)
        except Exception as e:
            st.error(f"Erreur d'appel API : {e}")

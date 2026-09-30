import streamlit as st

# Configuration de la page mobile
st.set_page_config(page_title="Bot Pronostic Football", page_icon="⚽", layout="centered")

# Titre principal
st.title("⚽ Bot Pronostic Football")
st.caption("Analyseur de tendances et probabilités de buts")

st.write("---")

# Section Équipe A
st.header("🏠 Équipe à Domicile (Équipe A)")
saisie_A = st.text_input(
    "Derniers scores de l'Équipe A (séparés par des virgules) :",
    value="2,1,3,1",
    help="Exemple : 2,1,3,1"
)

# Section Équipe B
st.header("✈️️ Équipe à l'Extérieur (Équipe B)")
saisie_B = st.text_input(
    "Derniers scores de l'Équipe B (séparés par des virgules) :",
    value="0,2,1,1",
    help="Exemple : 0,2,1,1"
)

st.write("---")

# Bouton de lancement
if st.button("🚀 Lancer l'Analyse", type="primary", use_container_width=True):
    try:
        # Conversion des entrées en listes d'entiers
        scores_A = [int(x.strip()) for x in saisie_A.split(",") if x.strip() != ""]
        scores_B = [int(x.strip()) for x in saisie_B.split(",") if x.strip() != ""]

        if not scores_A or not scores_B:
            st.error("Veuillez saisir au moins un score pour chaque équipe.")
        else:
            # Calculs statistiques
            moy_A = sum(scores_A) / len(scores_A)
            moy_B = sum(scores_B) / len(scores_B)
            total_buts = moy_A + moy_B

            pct_A = (sum(1 for x in scores_A if x > 0) / len(scores_A)) * 100
            pct_B = (sum(1 for x in scores_B if x > 0) / len(scores_B)) * 100

            # Affichage des métriques clés
            st.subheader("📊 Résultats de l'Analyse")
            
            col1, col2 = st.columns(2)
            col1.metric("Moyenne Équipe A", f"{moy_A:.2f}")
            col2.metric("Moyenne Équipe B", f"{moy_B:.2f}")

            st.metric("Prévision Total Buts", f"{total_buts:.2f}")

            # Diagnostic Over/Under 2.5
            if total_buts > 2.5:
                st.success("⚽ **Tendance Buts :** Plus de 2.5 buts (Over 2.5)")
            else:
                st.info("🛡️ **Tendance Buts :** Moins de 2.5 buts (Under 2.5)")

            # Diagnostic BTTS (Les deux équipes marquent)
            if pct_A >= 75 and pct_B >= 75:
                st.success("🔥 **Les deux équipes marquent :** OUI")
            else:
                st.warning("❌ **Les deux équipes marquent :** NON")

    except ValueError:
        st.error("Format invalide. Assure-toi de mettre uniquement des chiffres séparés par des virgules.")


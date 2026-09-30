import streamlit as st
import numpy as np

st.title("🤖 Bot Pronos Football Pro+")
st.markdown("Analyse avancée : Noms, Scores, Tirs, Score exact, 1X2 et BTTS")

# --- 1. SAISIE DES ÉQUIPES, SCORES ET TIRS ---
col1, col2 = st.columns(2)

with col1:
    st.subheader("🏠 Équipe à Domicile")
    nom_a = st.text_input("Nom Équipe A", "Real Madrid")
    scores_a_str = st.text_input(f"Scores récents ({nom_a})", "2,1,3,1")
    tirs_a_str = st.text_input(f"Tirs moyens/match ({nom_a})", "14,12,16,15")

with col2:
    st.subheader("✈️ Équipe à l'Extérieur")
    nom_b = st.text_input("Nom Équipe B", "Barcelone")
    scores_b_str = st.text_input(f"Scores récents ({nom_b})", "0,2,1,1")
    tirs_b_str = st.text_input(f"Tirs moyens/match ({nom_b})", "10,13,11,12")

# --- 2. CALCULS ET ANALYSE ---
if st.button("🚀 Lancer l'Analyse Complète"):
    try:
        # Conversion des données en listes de nombres
        scores_a = [float(x.strip()) for x in scores_a_str.split(",")]
        scores_b = [float(x.strip()) for x in scores_b_str.split(",")]
        tirs_a = [float(x.strip()) for x in tirs_a_str.split(",")]
        tirs_b = [float(x.strip()) for x in tirs_b_str.split(",")]
        
        moy_a = np.mean(scores_a)
        moy_b = np.mean(scores_b)
        moy_tirs_a = np.mean(tirs_a)
        moy_tirs_b = np.mean(tirs_b)
        
        # Estimation du score exact (arrondi au nombre de buts)
        buts_a = round(moy_a)
        buts_b = round(moy_b)
        
        # Calcul des probabilités 1X2 intégrant les tirs et les buts
        force_a = moy_a * 1.5 + (moy_tirs_a / 10)
        force_b = moy_b * 1.5 + (moy_tirs_b / 10) + 0.1 # Léger bonus extérieur compensé
        total_force = force_a + force_b
        
        prob_a = min(max((force_a / total_force) * 100 + 5, 15), 75)
        prob_b = min(max((force_b / total_force) * 100, 15), 75)
        prob_nul = max(100 - (prob_a + prob_b), 10)
        
        total_p = prob_a + prob_nul + prob_b
        p_1 = (prob_a / total_p) * 100
        p_x = (prob_nul / total_p) * 100
        p_2 = (prob_b / total_p) * 100
        
        # Option "Les deux équipes marquent" (BTTS)
        btts = "Oui 🟢" if (moy_a > 0.7 and moy_b > 0.7 and moy_tirs_a > 9 and moy_tirs_b > 9) else "Non 🔴"
        
        # --- 3. AFFICHAGE DES RÉSULTATS ---
        st.success("Analyse complète terminée !")
        
        st.markdown(f"### 📊 Match : {nom_a} vs {nom_b}")
        
        # Affichage du Score Exact en grand
        st.metric(label="⚽ Score Exact Estimé", value=f"{buts_a} - {buts_b}")
        
        # Affichage des Probabilités 1X2 en colonnes
        st.write("#### 📈 Probabilités du Match (1X2)")
        col_res1, col_res2, col_res3 = st.columns(3)
        col_res1.metric(f"Victoire {nom_a}", f"{p_1:.1f}%")
        col_res2.metric("Match Nul", f"{p_x:.1f}%")
        col_res3.metric(f"Victoire {nom_b}", f"{p_2:.1f}%")
        
        # Affichage des statistiques détaillées (Buts + Tirs)
        st.write("#### 🔍 Statistiques Offensives & Tendances")
        st.info(
            f"- **{nom_a}** : {moy_a:.2f} buts/match | {moy_tirs_a:.1f} tirs en moyenne\n"
            f"- **{nom_b}** : {moy_b:.2f} buts/match | {moy_tirs_b:.1f} tirs en moyenne\n"
            f"- Les deux équipes marquent (BTTS) : **{btts}**"
        )
        
    except Exception as e:
        st.error(f"Erreur dans le format des données. Utilise uniquement des chiffres séparés par des virgules (ex: 14,12,16). Détail : {e}")
        
        


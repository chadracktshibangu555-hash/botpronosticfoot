import streamlit as st
import numpy as np

st.title("🤖 Bot Pronos Football Pro+")
st.markdown("Analyse avancée : Scores, Tirs, Tirs cadrés, Corners, 1X2 et BTTS")

# --- 1. SAISIE DES DONNÉES ÉTENDUES ---
col1, col2 = st.columns(2)

with col1:
    st.subheader("🏠 Équipe à Domicile")
    nom_a = st.text_input("Nom Équipe A", "Real Madrid")
    scores_a_str = st.text_input(f"Scores récents ({nom_a})", "2,1,3,1")
    tirs_a_str = st.text_input(f"Tirs totaux moyens ({nom_a})", "14,12,16,15")
    cadrés_a_str = st.text_input(f"Tirs cadrés moyens ({nom_a})", "6,5,7,6")
    corners_a_str = st.text_input(f"Corners moyens ({nom_a})", "5,4,6,5")

with col2:
    st.subheader("✈️ Équipe à l'Extérieur")
    nom_b = st.text_input("Nom Équipe B", "Barcelone")
    scores_b_str = st.text_input(f"Scores récents ({nom_b})", "0,2,1,1")
    tirs_b_str = st.text_input(f"Tirs totaux moyens ({nom_b})", "10,13,11,12")
    cadrés_b_str = st.text_input(f"Tirs cadrés moyens ({nom_b})", "4,6,5,5")
    corners_b_str = st.text_input(f"Corners moyens ({nom_b})", "4,5,4,6")

# --- 2. CALCULS ET ANALYSE ---
if st.button("🚀 Lancer l'Analyse Détaillée"):
    try:
        # Conversion des données en listes de nombres
        scores_a = [float(x.strip()) for x in scores_a_str.split(",")]
        scores_b = [float(x.strip()) for x in scores_b_str.split(",")]
        tirs_a = [float(x.strip()) for x in tirs_a_str.split(",")]
        tirs_b = [float(x.strip()) for x in tirs_b_str.split(",")]
        cadres_a = [float(x.strip()) for x in cadrés_a_str.split(",")]
        cadres_b = [float(x.strip()) for x in cadrés_b_str.split(",")]
        corners_a = [float(x.strip()) for x in corners_a_str.split(",")]
        corners_b = [float(x.strip()) for x in corners_b_str.split(",")]
        
        moy_a = np.mean(scores_a)
        moy_b = np.mean(scores_b)
        moy_tirs_a = np.mean(tirs_a)
        moy_tirs_b = np.mean(tirs_b)
        moy_cadres_a = np.mean(cadres_a)
        moy_cadres_b = np.mean(cadres_b)
        moy_corners_a = np.mean(corners_a)
        moy_corners_b = np.mean(corners_b)
        
        # Estimation du score exact et des corners
        buts_a = round(moy_a)
        buts_b = round(moy_b)
        est_corners_a = round(moy_corners_a)
        est_corners_b = round(moy_corners_b)
        
        # Calcul des probabilités 1X2 intégrant les tirs cadrés
        force_a = moy_a * 1.5 + (moy_cadres_a / 3)
        force_b = moy_b * 1.5 + (moy_cadres_b / 3) + 0.1
        total_force = force_a + force_b
        
        prob_a = min(max((force_a / total_force) * 100 + 5, 15), 75)
        prob_b = min(max((force_b / total_force) * 100, 15), 75)
        prob_nul = max(100 - (prob_a + prob_b), 10)
        
        total_p = prob_a + prob_nul + prob_b
        p_1 = (prob_a / total_p) * 100
        p_x = (prob_nul / total_p) * 100
        p_2 = (prob_b / total_p) * 100
        
        # Option "Les deux équipes marquent" (BTTS)
        btts = "Oui 🟢" if (moy_a > 0.7 and moy_b > 0.7 and moy_cadres_a > 3 and moy_cadres_b > 3) else "Non 🔴"
        
        # --- 3. AFFICHAGE DES RÉSULTATS ---
        st.success("Analyse détaillée terminée !")
        
        st.markdown(f"### 📊 Match : {nom_a} vs {nom_b}")
        
        # Affichage du Score Exact et des Corners estimés
        col_m1, col_m2 = st.columns(2)
        col_m1.metric(label="⚽ Score Exact Estimé", value=f"{buts_a} - {buts_b}")
        col_m2.metric(label="🚩 Corners Estimés", value=f"{est_corners_a} - {est_corners_b}")
        
        # Affichage des Probabilités 1X2 en colonnes
        st.write("#### 📈 Probabilités du Match (1X2)")
        col_res1, col_res2, col_res3 = st.columns(3)
        col_res1.metric(f"Victoire {nom_a}", f"{p_1:.1f}%")
        col_res2.metric("Match Nul", f"{p_x:.1f}%")
        col_res3.metric(f"Victoire {nom_b}", f"{p_2:.1f}%")
        
        # Affichage des statistiques détaillées
        st.write("#### 🔍 Statistiques Offensives & Tendances")
        st.info(
            f"- **{nom_a}** : {moy_a:.2f} buts | {moy_tirs_a:.1f} tirs ({moy_cadres_a:.1f}$ cadrés) | {moy_corners_a:.1f} corners\n"
            f"- **{nom_b}** : {moy_b:.2f} buts | {moy_tirs_b:.1f} tirs ({moy_cadres_b:.1f} cadrés) | {moy_corners_b:.1f} corners\n"
            f"- Les deux équipes marquent (BTTS) : **{btts}**"
        )
        
    except Exception as e:
        st.error(f"Erreur dans le format des données. Utilise uniquement des chiffres séparés par des virgules. Détail : {e}")
        import streamlit as st
import numpy as np

st.title("🤖 Bot Pronos Football Pro+")
st.markdown("Analyse avancée : Scores, Tirs, Cadrés, Corners, 1X2, Double Chance et BTTS")

# --- 1. SAISIE DES DONNÉES ÉTENDUES ---
col1, col2 = st.columns(2)

with col1:
    st.subheader("🏠 Équipe à Domicile")
    nom_a = st.text_input("Nom Équipe A", "Real Madrid")
    scores_a_str = st.text_input(f"Scores récents ({nom_a})", "2,1,3,1")
    tirs_a_str = st.text_input(f"Tirs totaux moyens ({nom_a})", "14,12,16,15")
    cadrés_a_str = st.text_input(f"Tirs cadrés moyens ({nom_a})", "6,5,7,6")
    corners_a_str = st.text_input(f"Corners moyens ({nom_a})", "5,4,6,5")

with col2:
    st.subheader("✈️ Équipe à l'Extérieur")
    nom_b = st.text_input("Nom Équipe B", "Barcelone")
    scores_b_str = st.text_input(f"Scores récents ({nom_b})", "0,2,1,1")
    tirs_b_str = st.text_input(f"Tirs totaux moyens ({nom_b})", "10,13,11,12")
    cadrés_b_str = st.text_input(f"Tirs cadrés moyens ({nom_b})", "4,6,5,5")
    corners_b_str = st.text_input(f"Corners moyens ({nom_b})", "4,5,4,6")

# --- 2. CALCULS ET ANALYSE ---
if st.button("🚀 Lancer l'Analyse Détaillée"):
    try:
        # Conversion des données en listes de nombres
        scores_a = [float(x.strip()) for x in scores_a_str.split(",")]
        scores_b = [float(x.strip()) for x in scores_b_str.split(",")]
        tirs_a = [float(x.strip()) for x in tirs_a_str.split(",")]
        tirs_b = [float(x.strip()) for x in tirs_b_str.split(",")]
        cadres_a = [float(x.strip()) for x in cadrés_a_str.split(",")]
        cadres_b = [float(x.strip()) for x in cadrés_b_str.split(",")]
        corners_a = [float(x.strip()) for x in corners_a_str.split(",")]
        corners_b = [float(x.strip()) for x in corners_b_str.split(",")]
        
        moy_a = np.mean(scores_a)
        moy_b = np.mean(scores_b)
        moy_tirs_a = np.mean(tirs_a)
        moy_tirs_b = np.mean(tirs_b)
        moy_cadres_a = np.mean(cadres_a)
        moy_cadres_b = np.mean(cadres_b)
        moy_corners_a = np.mean(corners_a)
        moy_corners_b = np.mean(corners_b)
        
        # Estimation du score exact et des corners
        buts_a = round(moy_a)
        buts_b = round(moy_b)
        est_corners_a = round(moy_corners_a)
        est_corners_b = round(moy_corners_b)
        
        # Calcul des probabilités 1X2
        force_a = moy_a * 1.5 + (moy_cadres_a / 3)
        force_b = moy_b * 1.5 + (moy_cadres_b / 3) + 0.1
        total_force = force_a + force_b
        
        prob_a = min(max((force_a / total_force) * 100 + 5, 15), 75)
        prob_b = min(max((force_b / total_force) * 100, 15), 75)
        prob_nul = max(100 - (prob_a + prob_b), 10)
        
        total_p = prob_a + prob_nul + prob_b
        p_1 = (prob_a / total_p) * 100
        p_x = (prob_nul / total_p) * 100
        p_2 = (prob_b / total_p) * 100
        
        # --- CALCUL DE LA DOUBLE CHANCE ---
        dc_1x = p_1 + p_x  # Victoire Domicile ou Nul
        dc_12 = p_1 + p_2  # Victoire Domicile ou Victoire Extérieur (Pas de Nul)
        dc_x2 = p_x + p_2  # Nul ou Victoire Extérieur
        
        # Option "Les deux équipes marquent" (BTTS)
        btts = "Oui 🟢" if (moy_a > 0.7 and moy_b > 0.7 and moy_cadres_a > 3 and moy_cadres_b > 3) else "Non 🔴"
        
        # --- 3. AFFICHAGE DES RÉSULTATS ---
        st.success("Analyse détaillée terminée !")
        
        st.markdown(f"### 📊 Match : {nom_a} vs {nom_b}")
        
        # Affichage du Score Exact et des Corners estimés
        col_m1, col_m2 = st.columns(2)
        col_m1.metric(label="⚽ Score Exact Estimé", value=f"{buts_a} - {buts_b}")
        col_m2.metric(label="🚩 Corners Estimés", value=f"{est_corners_a} - {est_corners_b}")
        
        # Affichage des Probabilités 1X2 en colonnes
        st.write("#### 📈 Probabilités du Match (1X2)")
        col_res1, col_res2, col_res3 = st.columns(3)
        col_res1.metric(f"Victoire {nom_a}", f"{p_1:.1f}%")
        col_res2.metric("Match Nul", f"{p_x:.1f}%")
        col_res3.metric(f"Victoire {nom_b}", f"{p_2:.1f}%")
        
        # Affichage de la Double Chance
        st.write("#### 🛡️ Options Double Chance")
        col_dc1, col_dc2, col_dc3 = st.columns(3)
        col_dc1.metric(f"{nom_a} ou Nul (1X)", f"{dc_1x:.1f}%")
        col_dc2.metric(f"Pas de Nul (12)", f"{dc_12:.1f}%")
        col_dc3.metric(f"Nul ou {nom_b} (X2)", f"{dc_x2:.1f}%")
        
        # Affichage des statistiques détaillées
        st.write("#### 🔍 Statistiques Offensives & Tendances")
        st.info(
            f"- **{nom_a}** : {moy_a:.2f} buts | {moy_tirs_a:.1f} tirs ({moy_cadres_a:.1f} cadrés) | {moy_corners_a:.1f} corners\n"
            f"- **{nom_b}** : {moy_b:.2f} buts | {moy_tirs_b:.1f} tirs ({moy_cadres_b:.1f} cadrés) | {moy_corners_b:.1f} corners\n"
            f"- Les deux équipes marquent (BTTS) : **{btts}**"
        )
        
    except Exception as e:
        st.error(f"Erreur dans le format des données. Utilise uniquement des chiffres séparés par des virgules. Détail : {e}")



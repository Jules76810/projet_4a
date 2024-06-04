import pandas as pd
import numpy as np
import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir) 
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import plotly.express as px
from sklearn import preprocessing
import plotly.graph_objects as go
from sklearn.cluster import KMeans

st.set_page_config(page_title="Vision génerale", initial_sidebar_state='auto', layout="wide")
st.title('Projet 4A - Traitement de données alimentaires')

### du code qui vient de notre notebook, ne fait pas partie de l'affichage
data = pd.read_csv('Agribalyse_Synthese (2).csv')
cols = list(data.columns)
data = data.rename(columns={cols[18]: "effets_toxico_non_cancer", cols[19]: "effets_toxico_cancer"})

## ici oui on l'affiche le dataset avec st
st.header("Les données AgriBalyse brutes")
st.write("Nous vous présentons ci-dessous la base de données complète d'Agribalyse. Plus de **2500** produits la composent.")
st.dataframe(data)
st.write(data.shape)
cols_data, lignes_data = st.columns(2)
cols_data.metric("Produits", str(data.shape[0]))
lignes_data.metric("Paramètres", str(data.shape[1]))
st.divider()


st.image("https://autrecuisine.fr/warehouse/cache/large/poster_5f733477321f3.jpg.png")


st.header('Qualité de la donnée - DQR')
st.write("Étude du paramètre de la variable DQR - Data Quality Ratio, elle évalue la fiabilité des données et préconise une utilisation des données les plus fiables.")

titres = ['mean', 'std', 'min', '25%', '50%', '75%', 'max']

desc = data.describe()


fig, ax = plt.subplots(figsize=(12, 6))
ax.bar(titres, desc['DQR'][1:].values)
ax.set_xlabel('Statistiques')
ax.set_ylabel('Valeurs')
ax.set_title('Diagramme en barres des statistiques descriptives de DQR')
st.pyplot(fig)
st.caption("On retrouve une moyenne ainsi qu'une médiane d'une valeure approximative de 2,7. De plus, on peut observer un maximum de 4,87 et un minimum de 1,2 ce qui signifie une grande hétérogénéité entre les produits de la base de données. ")

fig = px.box(data, x="DQR", title="Box Plot de DQR")
st.dataframe(data)
st.plotly_chart(fig)
st.write("Ce box plot montre la distribution des valeurs de la colonne DQR. Les lignes horizontales indiquent les quartiles.")

st.write("Il est conseillé de prendre les valeurs avec un DQR inférieur à 3 afin d'utiliser les valeurs les plus fiables, selon la Commission Européenne.")
st.divider()

st.write("Vous pouvez choisir la valeur de la qualité via le sélecteur ci-dessous.")
dqr_value = st.select_slider('Qualité de la donnée',
    options=[1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5])
st.write('Donnés avec DQR plus petit que:', dqr_value)


df = data[data["DQR"]<dqr_value]
st.dataframe(df)
st.write(df.shape)
lignes_df, cols_df= st.columns(2)
lignes_df.metric("Produits", str(df.shape[0]))
cols_df.metric("Paramètres", str(df.shape[1]))
a = np.round(df.shape[0] / data.shape[0],3)*100
st.write("Pourcentage de produits gardés selon la qualité de la donnée choisie précédemment (par rapport au total) :", a, " %")
st.divider()

variables = ['Changement climatique',
       "Appauvrissement de la couche d'ozone", "Rayonnements ionisants",
       "Formation photochimique d'ozone", "Particules fines",
       'effets_toxico_non_cancer', 'effets_toxico_cancer',
       'Acidification terrestre et eaux douces', 'Eutrophisation eaux douces',
       'Eutrophisation marine', 'Eutrophisation terrestre',
       "Écotoxicité pour écosystèmes aquatiques d'eau douce",
       'Utilisation du sol', 'Épuisement des ressources eau',
       'Épuisement des ressources énergétiques',
       'Épuisement des ressources minéraux']



st.header('Les variables')
variable_select = st.selectbox('Choisisez une variable', (i for i in variables))

confirm = st.checkbox('Afficher détails')

if confirm:
    st.write(variable_select)
    col1, col2, col3 = st.columns(3)
    with col1:
        fig = px.histogram(df[variable_select], x=variable_select, nbins=10)
        st.plotly_chart(fig, use_container_width=True)
    with col2:
        fig2 = px.box(df[variable_select], y=variable_select)
        st.plotly_chart(fig2, use_container_width=True)
    min_variable, max_variable, mean_variable = st.columns(3)
    min_variable.metric("Min", np.round(df[variable_select].min(), 3))
    max_variable.metric("Max", np.round(df[variable_select].max(), 3))
    mean_variable.metric("Moyenne", np.round(df[variable_select].mean(), 3))

st.write("Nous vous laissons poursuivre avec la page 3 sur le Score Unique EF de la base de donnée ou revenir à la page d'accueil avec les liens ci-dessous.")
st.page_link("Homepage.py", label="Page d'accueil", icon="🏠")
st.page_link("pages/3_📈_Score_unique_EF.py", label="Score Unique EF 📈", icon="3️⃣")

st.sidebar.title('À propos')
st.sidebar.info('Cette application a été développée par Margaux BOYER, Marion DE CACQUERAY, Jules LEFORT et Laure WATERHOUSE.')

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

st.set_page_config(page_title="Score unique EF", initial_sidebar_state='auto', layout="wide")
data = pd.read_csv('Agribalyse_Synthese (2).csv')
cols = list(data.columns)
data = data.rename(columns={cols[18]: "effets_toxico_non_cancer", cols[19]: "effets_toxico_cancer"})
st.title('Projet 4A - Traitement de données alimentaires')
st.header("Le score unique EF")
st.write("Le score unique EF est la valeur préconisée par la Commission Européenne. Le Score Unique EF regroupe et représente les différents indicateurs ayant une influence environnementale. On peut notamment voir la pondération des différents facteurs qui forme ce score sur le tableau ci-dessous.")
st.image("https://doc.agribalyse.fr/~gitbook/image?url=https%3A%2F%2F2407839794-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-LpO7Agg1DbhEBNAvmHP%252F-MLmGl1xWNUdFGoOBo9f%252F-MLmGoORnso9M46c0PtM%252Fjrc.png%3Falt%3Dmedia%26token%3D9da03594-5db3-433b-9461-c24e23ee5e1c&width=768&dpr=2&quality=100&sign=4fe1c17ceedc8702a665f9d5c511f618313f5439678e76fc2ef954da1cd9c621")

st.title('Analyse des Données avec Streamlit')
st.subheader('Exploration des données avec un Histogramme')
st.write("Voici un aperçu des données utilisées pour créer l'histogramme :")
st.dataframe(data)
fig = px.histogram(data, x="Score unique EF", title="Histogramme de Score Unique EF")
st.plotly_chart(fig)
st.write("Cet histogramme montre la distribution des valeurs de la colonne Score Unique EF. Les barres représentent la fréquence des différentes valeurs dans l'ensemble des données.")

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
len(variables)
df = data[data["DQR"]<3]
variables_EF = res = [*['Score unique EF'], *variables]
df = df[variables_EF]
st.title("Analyse des données avec la corrélation des indicateurs avec le score unique EF")
corr = df.corr()
mask = np.triu(np.ones_like(corr, dtype=bool))
f, ax = plt.subplots(figsize=(10, 7))
cmap = sns.diverging_palette(230, 20, as_cmap=True)
sns.heatmap(corr, mask=mask, cmap=cmap, annot=True, vmin=-1, vmax=1)
st.pyplot(f)

corr = df.corr()['Score unique EF']
st.write("Variables les plus corrélées décroissantes avec le Score unique EF:")
top_variables = pd.DataFrame(df.corr()['Score unique EF'].sort_values(ascending=False))
top_variables = top_variables.reset_index()
top_variables = top_variables.iloc[1:, :]
st.dataframe(top_variables)
st.write("Choix de travailler avec les 5 variables les plus corrélées avec le score unique EF malgré le fait que ce ne soit pas les variables qui possèdent le plus de pondération dans le calcul de ce dernier.")

df.corr()['Score unique EF'].sort_values(ascending=False)[1:6]
cols_importantes = ["Score unique EF",
                    "Particules fines",
                    "Acidification terrestre et eaux douces",
                    "Changement climatique",
                    "Eutrophisation terrestre",
                    "effets_toxico_cancer"]
top_5_var = ["Particules fines",
                    "Acidification terrestre et eaux douces",
                    "Changement climatique",
                    "Eutrophisation terrestre",
                    "effets_toxico_cancer"]
df_selection = df[cols_importantes]
st.divider()
st.write("Nous vous laissons poursuivre avec la page 4 sur la comparaison de couples de produits issus de la base de donnée ou revenir à la page d'accueil avec les liens ci-dessous.")
st.page_link("Homepage.py", label="Page d'accueil", icon="🏠")
st.page_link("pages/4_🍽️_Comparatif.py", label="Comparatif 🍽️", icon="4️⃣")

st.sidebar.title('À propos')
st.sidebar.info('Cette application a été développée par Margaux BOYER, Marion DE CACQUERAY, Jules LEFORT et Laure WATERHOUSE.')

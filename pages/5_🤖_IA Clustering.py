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

st.set_page_config(page_title="IA Clustering", initial_sidebar_state='auto', layout="wide")
st.title("IA Clustering")
st.write("L'utilisation d'une IA va permettre de définir 3 groupes d'aliments qui possèdent des caractéristiques similaires.")
data = pd.read_csv('Agribalyse_Synthese (2).csv')
cols = list(data.columns)
data = data.rename(columns={cols[18]: "effets_toxico_non_cancer", cols[19]: "effets_toxico_cancer"})
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
corr = df.corr()


ds = df[variables]

k = 3
kmeans = KMeans(n_clusters=k, n_init="auto")
kmeans.fit(ds)

centroids = kmeans.cluster_centers_

df['cluster'] = kmeans.labels_

cluster_counts = pd.DataFrame(df['cluster'].value_counts(), columns=['count']).reset_index()
cluster_counts.columns = ['cluster', 'count']
st.write("Comptes des clusters :")
st.dataframe(cluster_counts)


cluster_counts = pd.DataFrame(df['cluster'].value_counts(), columns=['count']).reset_index()
cluster_counts.columns = ['cluster', 'count']

fig = px.bar(cluster_counts, x='cluster', y='count', color='cluster', title='Distribution des Clusters')

st.plotly_chart(fig)

fig = px.box(df, x="cluster", y="Score unique EF", color="cluster", title="Box Plot par Cluster")
st.plotly_chart(fig)

fig, ax = plt.subplots()
sns.barplot(data=df, x="cluster", y="Changement climatique", hue="cluster", ax=ax)
st.pyplot(fig)

st.divider()
st.write("Nous vous laissons poursuivre avec la page 6 sur la conclusion de notre projet ou revenir à la page d'accueil avec les liens ci-dessous.")
st.page_link("Homepage.py", label="Page d'accueil", icon="🏠")
st.page_link("pages/6_⌛️_Conclusion.py", label="Conclusion ⌛️", icon="6️⃣")

st.sidebar.title('À propos')
st.sidebar.info('Cette application a été développée par Margaux BOYER, Marion DE CACQUERAY, Jules LEFORT et Laure WATERHOUSE.')

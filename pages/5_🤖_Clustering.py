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

st.set_page_config(page_title="Clustering", initial_sidebar_state='auto', layout="wide")
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


st.write("L'utilisation d'une IA va permettre de définir 3 groupes d'aliments qui possèdent des caractéristiques similaires.")


ds = df[variables]
st.write("L'utilisation d'une IA va permettre de définir 3 groupes d'aliments qui possèdent des caractéristiques similaires.")
k = 3
kmeans = KMeans(n_clusters=k, n_init="auto")
kmeans.fit(ds)
st.write("L'utilisation d'une IA va permettre de définir 3 groupes d'aliments qui possèdent des caractéristiques similaires.")
centroids = kmeans.cluster_centers_
kmeans.labels_
df['cluster'] = kmeans.labels_
st.write("L'utilisation d'une IA va permettre de définir 3 groupes d'aliments qui possèdent des caractéristiques similaires.")
cluster_counts = pd.DataFrame(df['cluster'].value_counts(), columns=['count']).reset_index()
cluster_counts.columns = ['cluster', 'count']
st.write("Comptes des clusters :")
st.dataframe(cluster_counts)
st.write("L'utilisation d'une IA va permettre de définir 3 groupes d'aliments qui possèdent des caractéristiques similaires.")

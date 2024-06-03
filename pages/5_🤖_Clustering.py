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


st.title("IA Clustering")
st.write("L'utilisation d'une IA va permettre de définir 3 groupes d'aliments qui possèdent des caractéristiques similaires.")
data = pd.read_csv('https://www.data.gouv.fr/fr/datasets/r/743dfdb2-73c4-4312-8256-0bb2d9bbdd13')
cols = list(data.columns)
data = data.rename(columns={cols[18]: "effets_toxico_non_cancer", cols[19]: "effets_toxico_cancer"})

df = data[data["DQR"]<3]
variables_EF = res = [*['Score unique EF'], *variables]
df = df[variables_EF]
corr = df.corr()

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

ds = df[variables]

k = 3
kmeans = KMeans(n_clusters=k, n_init="auto")
kmeans.fit(ds)

centroids = kmeans.cluster_centers_
kmeans.labels_
df['cluster'] = kmeans.labels_

cluster_counts = pd.DataFrame(df['cluster'].value_counts(), columns=['count']).reset_index()
cluster_counts.columns = ['cluster', 'count']
st.write("Comptes des clusters :")
st.dataframe(cluster_counts)


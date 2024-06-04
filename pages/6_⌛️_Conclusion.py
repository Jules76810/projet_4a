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

st.set_page_config(page_title="Conclusion", initial_sidebar_state='auto', layout="wide")
data = pd.read_csv('Agribalyse_Synthese (2).csv')
cols = list(data.columns)
data = data.rename(columns={cols[18]: "effets_toxico_non_cancer", cols[19]: "effets_toxico_cancer"})
st.title('Projet 4A - Traitement de données alimentaires')
st.header("Conclusion")

st.write("""En conclusion, la base données agribalyse est une base de données complète qui peut servir d’outils dans différents secteurs comme : l’agriculture, les consommateurs, le secteur de la restauration ou encore pour la recherche et l’enseignement par exemple. Durant ce projet, l’impact environnementale de certains produits a été mis en lumière. Dans la plupart des cas, des différences majeures ont pu être observées entre les couples choisis, notamment ceux contenant de la viande ou demandant un processus de production ou de transport énergétiquement coûteux.  

Le fait de se baser sur l’analyse du cycle de vie des produits, permet d’identifier les étapes plus gourmandes, en eau ou encore en énergie. L’identification de ces étapes est primordiale pour pouvoir ensuite diminuer ces utilisations de ressources et ainsi essayer de réduire les impacts environnementaux.  

Il a été constaté au début de notre travail que les 5 indicateurs ayant les plus grands scores EF n’était pas forcément ceux qui étaient les plus corrélés ce qui pose un potentiel problème sur l'exploitation totale des données. """)

st.divider()
st.write ("Nous avons travaillé sur la version 3.1.1 de la base de données Agribalyse sortie en 2023 mais la version 3.2 va sortir à l'été 2024. Elle contiendra une mise à jour des données.")
st.write("Si vous souhaitez faire des retours sur la base de données Agribalyse pour des améliorations quelconques : nous vous invitons à cliquer sur le lien de la page officielle de la documentation de la base de données ci-dessous.")
st.page_link("https://doc.agribalyse.fr/documentation/nous-contactez/contribuer-aux-travaux-agribalyse-r", label="Page de contact", icon="📇")

st.divider()
st.write("**Merci d'avoir suivi notre projet, nous vous invitons désormais à revenir à la page d'accueil avec le lien ci-dessous.**")
st.page_link("Homepage.py", label="Page d'accueil", icon="🏠")


st.sidebar.title('À propos')
st.sidebar.info('Cette application a été développée par Margaux BOYER, Marion DE CACQUERAY, Jules LEFORT et Laure WATERHOUSE.')

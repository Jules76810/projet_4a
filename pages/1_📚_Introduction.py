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

st.set_page_config(page_title="Introduction", initial_sidebar_state='auto', layout="wide")
st.title('Introduction')
st.write("La base de données Agribalyse")

#ajouter une image
st.image('Agribalyse-image1.png')
st.caption("Base de données publique régit par plusieurs organismes nationaux tels que : L'ADEME, l'INRAE ainsi que des instituts techniques agricoles et agroalimentaires...")

st.header('La base de données AgriBalyse')
st.write("Quelques mots sur la base de données :")
texte = """
L’analyse du cycle de vie est une méthode de calcul de l’impact environnemental d’un produit. Elle repose sur la norme ISO 14040 dont la méthode comporte 4 principales étapes : 

- **La définition du projet** : c’est à dire cibler et présenter le produit à analyser.
- **Analyse de l’inventaire du cycle de vie** : c’est donc faire le bilan de matière et d’énergie sur l’ensemble de la chaine de production, du transport... depuis la création du produit jusqu’à la fin de son utilisation et au-delà.
- **Évaluation des impacts** : selon la méthode “midpoint” ou “endpoint”.
- **Interprétation des résultats obtenus**.

Cette analyse du cycle de vie a pour but d’identifier les principaux impacts sur l’environnement d’un produit et de trouver des solutions pour les limiter au maximum.  

L’ACV est dite multicritères et multi-étapes. En effet, plusieurs critères environnementaux sont considérés tandis que toutes les phases du cycle de vie d’un produit sont prises en compte. Des bilans matières, d’énergie et d’émissions de polluants sont réalisés à chaque étape du cycle de vie du produit.
"""
st.markdown(texte)
expander = st.expander("Cliquez ici pour plus d'informations")
expander.write("rtrtrttrtrtrtrtr")
expander.image("https://agribalyse.ademe.fr/static/media/logo.e3e348f6.png")

st.divider() # diviseur

st.write("This text is between the horizontal rules.")
st.divider()  # 👈 Another horizontal rule

st.write("This text is between the horizontal rules.")
st.caption('Mini text pour expliquer quelque chose')
st.divider() 
################

st.header("l'ACV")
st.caption('Mini text pour expliquer quelque chose')
st.divider()

st.sidebar.title('À propos')
st.sidebar.info('Cette application a été développée par Margaux BOYER, Marion DE CACQUERAY, Jules LEFORT et Laure WATERHOUSE.')

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
st.header("Quel est le contexte mondiale du secteur agroalimentaire ?")
st.image('Intro.png')
texte = """
Chaque année le marché mondial de l’alimentation ne cesse de croître. Sans même prendre en compte les boissons, ce marché devrait dépasser les 9 000 milliards d’euros en 2024. L’année précédente le chiffre d’affaires mondiale ne représentait que 8 470 milliards d’euros. On remarque alors une hausse de 7 % en 2024. Par ailleurs, dés 2026 ce marché devrait peser près de 10 000 milliards d’euros, avec une hausse annuelle estimée à 6 %.
Malgré un marché en pleine expansion, les entreprises agroalimentaires font face à des modes de consommations qui évoluent. De nos jours, l’impact environnemental des produits de consommation joue en rôle prépondérant au sein des entreprises du monde entier. On remarque notamment l’importance d’une consommation dite responsable. Toutefois, les consommateurs restent accrochés à la volonté d’adopter des comportements alimentaires en adéquation avec le bien-manger. En effet, ces dernières années, les consommateurs ont tendance à prêter de plus en plus attention aux critères environnementaux liés à leurs produits. Les origines des produits qu’ils consomment ou le cahier des charges gage de qualité sont des facteurs déterminants dans le choix des produits qu’ils achètent.

Il existe désormais beaucoup d’outils considérant les procédés de production et d’acheminement du produit jusqu’au consommateur afin de réaliser des observations précises et détaillées. Par ailleurs, la normalisation de méthode d’évaluation permettant de réaliser des bilans environnementaux s’est largement développée au cours de ces dernières années. La méthode d’évaluation de l’ACV, Analyse du Cycle de Vie, est considérée comme la méthode la plus fiable afin d’estimer au maximum l’influence de chaque produit sur l’environnement de sa conception à sa consommation voire son recyclage. Ces analyses sont standardisées afin de prendre conscience de l'influence sur l’environnement des divers processus de production.
"""
st.markdown(texte)
st.divider()
st.header("Quel est l'objectif de notre projet ?")
st.write("**Notre projet consiste à étudier des données alimentaires tout en étant capable de les exploiter avec efficacité. C’est pourquoi nous allons nous appuyer sur une base de données publique française nommée “Agribalyse” utilisant cette méthode d’évaluation pour tenter d’établir des conclusions sur les produits alimentaires quotidiennement acheté par les consommateurs. Dans ce rapport, nous allons dans un premier temps exprimer le contexte du projet, puis nous présenterons notre problématique, ensuite le plan d’action et les paramétrages seront expliqués et enfin nous exposerons et analyserons les résultats.**")

st.header('La base de données AgriBalyse')
#ajouter une image
st.image('Agribalyse-image1.png')
st.caption("Base de données publique régit par plusieurs organismes nationaux tels que : L'ADEME, l'INRAE ainsi que des instituts techniques agricoles et agroalimentaires...")
st.write("Quelques mots sur la base de données :")

texte = """
Ce projet Agribalyse est initié par l’institut de l’INRAE et l’agence de l’ADEME. En addition, ces deux organisations basent aussi leurs recherches sur le travail commun des instituts techniques agricoles et agroalimentaires. 

La base de données Agribalyse est une base de données française, publique et accessible à tous, fournissant des informations sur les impacts environnementaux des différents produits alimentaires transformés/ non transformés, biologiques et non biologiques. Au total, cette base possède plus de 200 références de produits agricoles français, 2500 produits transformés et des produits importés en France comme le thé, le café ou encore le chocolat. 

Cette base de données est depuis 2013 la référence en termes de représentation des impacts environnementaux des produits agricoles ou alimentaires selon la méthodologie de l’ACV. 

Cette base de données peut servir dans différents domaines : 

**Le secteur agricole** 
**Pour les consommateurs** 
**Le secteur de la restauration collective** 
**La recherche et l’enseignement** 
Finalement, tous les produits sont définis selon 16 indicateurs représentant chacun un impact environnemental. Tous ces indicateurs sont calculés sur la base d’1 kilogramme de produit. """
st.markdown(texte)



expander = st.expander("Cliquez ici pour plus d'informations sur les 16 indicateurs qui oriente notre projet")
expander.write(""" 

Notre base de données est basée sur 16 indicateurs environnementaux qui sont fournis pour chaque produit :  

- **Le changement climatique** 
- **Les particules fines** 
- **L’épuisement des ressources en eau** 
- **L’épuisement des ressources énergétiques** 
- **L’usage des terres** 
- **L’épuisement des ressources en minéraux** 
- **L’appauvrissement de la couche d’ozone** 
- **L’acidification** 
- **L’effet des radiations ionisantes sur la santé** 
- **La formation photochimique d’ozone** 
- **L’eutrophisation terrestre** 
- **L’eutrophisation marine** 
- **L’eutrophisation d’eau douce** 
- **L’écotoxicité d’eau douce** 
 

Ces 16 indicateurs influencent le dérèglement climatique/ changement climatique auquel nous faisons face aujourd’hui.  
""")
expander.image("https://agribalyse.ademe.fr/static/media/logo.e3e348f6.png")

st.divider() # diviseur

st.header("L'ACV")
st.caption('ACV = Analyse du Cycle de Vie')
texte = """
L’analyse du cycle de vie est une méthode de calcul de l’impact environnemental d’un produit. Elle repose sur la norme ISO 14040 dont la méthode comporte 4 étapes majeures : 

- **La définition du projet** : Cibler et présenter le produit à analyser.
- **Analyse de l’inventaire du cycle de vie** : Faire le bilan de matière et d’énergie sur l’ensemble de la chaine de production... depuis la création du produit jusqu’à la fin de son utilisation et au-delà.
- **Évaluation des impacts** : Selon la méthode “midpoint” ou “endpoint”.
- **Interprétation des résultats obtenus**.

Cette analyse du cycle de vie a pour but d’identifier les principaux impacts sur l’environnement d’un produit et de trouver des solutions pour les limiter au maximum.  

L’ACV est dite multicritères et multi-étapes. En effet, plusieurs critères environnementaux sont considérés tandis que toutes les phases du cycle de vie d’un produit sont prises en compte. Des bilans matières, d’énergie et d’émissions de polluants sont réalisés à chaque étape du cycle de vie du produit.
"""
st.markdown(texte)
st.divider()

st.sidebar.title('À propos')
st.sidebar.info('Cette application a été développée par Margaux BOYER, Marion DE CACQUERAY, Jules LEFORT et Laure WATERHOUSE.')

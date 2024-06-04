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

st.set_page_config(page_title="Références Bibligraphiques", initial_sidebar_state='auto', layout="wide")
st.title('Projet 4A - Traitement de données alimentaires')
st.title('Références Bibliographiques')




st.divider()
st.write("**Nous vous laissons revenir à la page d'accueil avec le lien ci-dessous.**")
st.page_link("Homepage.py", label="Page d'accueil", icon="🏠")

st.sidebar.title('À propos')
st.sidebar.info('Cette application a été développée par Margaux BOYER, Marion DE CACQUERAY, Jules LEFORT et Laure WATERHOUSE.')

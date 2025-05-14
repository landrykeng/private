import streamlit as st
import pandas as pd
import geopandas as gpd
import numpy as np
import streamlit as st
import traceback
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px 
from streamlit_plotly_events import plotly_events
import seaborn as sns
import os
import warnings
import datetime
import plotly.graph_objects as go
import plotly.figure_factory as ff
import plotly.graph_objects as go
import plotly.offline as py
import plotly.tools as tls
from scipy.stats import chi2_contingency
from scipy.stats import ttest_ind
from scipy.stats import levene
import plotly
import time
import datetime as dt
import warnings
warnings.filterwarnings('ignore')
from my_fonction import *
from Authentification import *
from PIL import Image
from pathlib import Path
import json
from streamlit_echarts import st_echarts

st.set_page_config(layout="wide")
#import_users_from_excel()

st.markdown("""
            <style>
            /* Quand la sidebar est fermée */
            [data-testid="stSidebar"][aria-expanded="false"] {
                width: 0;
                min-width: 0;
                overflow: hidden;
                transition: width 0.3s ease;
            }
            
            /* Extension complète du contenu principal quand sidebar fermée */
            [data-testid="stSidebar"][aria-expanded="false"] + div [data-testid="stAppViewContainer"] {
                max-width: 100% !important;
                padding: 0 !important;
            }
            
            /* Graphiques en plein écran */
            [data-testid="stSidebar"][aria-expanded="false"] + div .stPlotlyChart {
                width: 100% !important;
                max-width: 100% !important;
            }
            
            /* Conteneurs étendus */
            [data-testid="stSidebar"][aria-expanded="false"] + div [data-testid="stBlock"] {
                width: 100% !important;
                padding: 0 !important;
                margin: 0 !important;
            }
            
            /* Style de la sidebar quand ouverte */
            [data-testid="stSidebar"][aria-expanded="true"] {
                width: 250px !important;
                min-width: 250px !important;
                transition: width 0.3s ease;
            }
            
            /* Ajustements généraux */
            .stPlotlyChart {
                width: 100%;
                max-width: 100%;
            }
            </style>
            """, unsafe_allow_html=True)

        #pour les conteneurs de graphiques

st.markdown("""
                <style>
                /* Styles de base pour tous les thèmes */
                .stContainer {
                    border-radius: 10px;  /* Coins arrondis */
                    border: 2px solid transparent;  /* Bordure transparente par défaut */
                    padding: 20px;  /* Espacement intérieur */
                    margin-bottom: 20px;  /* Espace entre les conteneurs */
                    transition: all 0.3s ease;  /* Animation douce */
                }

                /* Mode Clair (par défaut) */
                body:not(.dark) .stContainer {
                    background-color: rgba(255, 255, 255, 0.9);  /* Fond blanc légèrement transparent */
                    border-color: rgba(224, 224, 224, 0.7);  /* Bordure grise légère */
                    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.08);  /* Ombre douce */
                }

                /* Mode Sombre */
                body.dark .stContainer {
                    background-color: rgba(30, 30, 40, 0.9);  /* Fond sombre légèrement transparent */
                    border-color: rgba(60, 60, 70, 0.7);  /* Bordure sombre légère */
                    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.2);  /* Ombre plus marquée */
                }

                /* Effet de survol - Mode Clair */
                body:not(.dark) .stContainer:hover {
                    box-shadow: 0 8px 12px rgba(0, 0, 0, 0.5);  /* Ombre plus prononcée */
                    transform: translateY(-5px);  /* Léger soulèvement */
                    border-color: rgba(200, 200, 200, 0.9);  /* Bordure plus visible */
                }

                /* Effet de survol - Mode Sombre */
                body.dark .stContainer:hover {
                    box-shadow: 0 8px 12px rgba(255, 255, 255, 0.5);  /* Ombre claire */
                    transform: translateY(-5px);  /* Léger soulèvement */
                    border-color: rgba(100, 100, 110, 0.9);  /* Bordure plus visible */
                }

                /* Style spécifique pour les graphiques - Mode Clair */
                body:not(.dark) .stPlotlyChart {
                    background-color: rgba(250, 250, 250, 0.95);  /* Fond très légèrement gris */
                    border-radius: 8px;  /* Coins légèrement arrondis */
                    padding: 10px;
                    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);  /* Ombre très légère */
                }

                /* Style spécifique pour les graphiques - Mode Sombre */
                body.dark .stPlotlyChart {
                    background-color: rgba(40, 40, 50, 0.95);  /* Fond sombre légèrement transparent */
                    border-radius: 8px;  /* Coins légèrement arrondis */
                    padding: 10px;
                    box-shadow: 0 2px 4px rgba(255, 255, 255, 0.05);  /* Ombre très légère */
                }
                </style>
                """, unsafe_allow_html=True)

useless_style="""
        <style>
        .sidebar-link {
            display: block;
            margin-bottom: 15px;
            padding: 10px 15px;
            text-decoration: none;
            color: #333;
            background-color: #f8f9fa;
            border-radius: 8px;
            transition: all 0.3s ease;
            font-weight: 500;
        }

        .sidebar-link-right {
            display: block;
            margin-bottom: 15px;
            padding: 10px 15px;
            text-decoration: none;
            color: #333;
            background-color: #f8f9fa;
            border-radius: 8px;
            transition: all 0.3s ease;
            font-weight: 500;
            text-align: right;
        }

        .sidebar-link-center {
            display: block;
            margin-bottom: 15px;
            padding: 10px 15px;
            text-decoration: none;
            color: #333;
            background-color: #f8f9fa;
            border-radius: 8px;
            transition: all 0.3s ease;
            font-weight: 500;
            text-align: center;
        }
        </style>
        """

sidebar_css = """
        <style>
        .sidebar-link {
            display: block;
            margin-bottom: 15px;
            padding: 10px 15px;
            text-decoration: none;
            color: #333;
            background-color: #f8f9fa;
            border-radius: 8px;
            transition: all 0.3s ease;
            font-weight: 500;
        }

        .sidebar-link:hover {
            background-color: #e9ecef;
            color: #007bff;
            transform: translateX(5px);
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }

        .sidebar-link-icon {
            margin-right: 10px;
        }
        </style>
        """
        
table_css = """
        <style>
        /* Style général des tableaux */
        .stDataFrame {
            border-collapse: collapse;
            width: 100%;
            margin-bottom: 20px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            border-radius: 10px;
            overflow: hidden;
        }

        /* En-tête du tableau */
        .stDataFrame thead {
            background-color: #4b8bff;
            color: white;
            font-weight: bold;
        }

        /* Lignes du tableau */
        .stDataFrame tbody tr:nth-child(even) {
            background-color: #f8f9fa;
        }

        .stDataFrame tbody tr:nth-child(odd) {
            background-color: #ffffff;
        }

        /* Effet de survol */
        .stDataFrame tbody tr:hover {
            background-color: #e9ecef;
            transition: background-color 0.3s ease;
        }

        /* Cellules */
        .stDataFrame th, .stDataFrame td {
            padding: 12px;
            text-align: left;
            border-bottom: 1px solid #dee2e6;
        }

        /* Style des colonnes */
        .stDataFrame th {
            text-transform: uppercase;
            font-size: 0.9em;
            letter-spacing: 1px;
        }
        </style>
        """

title_css = """
        <style>
        .dashboard-title-container {
            background: linear-gradient(135deg, #ff4b4b 0%, #ff6b6b 100%);
            color: white;
            padding: 30px 20px;
            border-radius: 15px;
            box-shadow: 0 10px 20px rgba(0,0,0,0.1);
            text-align: center;
            margin-bottom: 20px;
            transition: all 0.3s ease;
        }

        .dashboard-title-container:hover {
            transform: scale(1.02);
            box-shadow: 0 15px 30px rgba(0,0,0,0.15);
        }

        .dashboard-main-title {
            font-size: 2.5em;
            font-weight: 800;
            margin-bottom: 10px;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        }

        .dashboard-subtitle {
            font-size: 1.2em;
            font-weight: 300;
            color: rgba(255,255,255,0.9);
            max-width: 800px;
            margin: 0 auto;
            line-height: 1.6;
        }

        .title-icon {
            margin: 0 15px;
            opacity: 0.8;
        }
        </style>
        """

header_css = """
        <style>
        .header-container {
            background: linear-gradient(135deg, #ff4b4b 0%, #ff6b6b 100%);
            border-radius: 15px;
            padding: 20px;
            margin-bottom: 20px;
            box-shadow: 0 10px 20px rgba(0,0,0,0.1);
            text-align: center;
            position: relative;
            overflow: hidden;
        }

        .header-container::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: rgba(255,255,255,0.1);
            transform: skew(-15deg) rotate(-15deg);
            z-index: 1;
        }

        .header-title {
            color: white;
            font-size: 2.5em;
            font-weight: 800;
            margin-bottom: 10px;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
            position: relative;
            z-index: 2;
        }

        .header-subtitle {
            color: rgba(255,255,255,0.9);
            font-size: 1.2em;
            font-weight: 300;
            max-width: 800px;
            margin: 0 auto;
            text-align: center;
            line-height: 1.6;
            position: relative;
            z-index: 2;
        }

        .image-container {
            display: flex;
            justify-content: center;
            gap: 20px;
            margin-bottom: 20px;
        }

        .image-wrapper {
            border-radius: 15px;
            overflow: hidden;
            box-shadow: 0 10px 20px rgba(0,0,0,0.1);
            transition: transform 0.3s ease;
        }

        .image-wrapper:hover {
            transform: scale(1.03);
        }
        </style>
        """

tabs_css="""
<style>
.stTabs [data-baseweb="tab-list"] {
    display: flex;
    justify-content: center;
    align-items: center;
    background-color: 
#f0f2f6;
    border-radius: 15px;
    padding: 10px;
    box-shadow: 0 4px 6px rgba(0,0,0,0.1);
}

.stTabs [data-baseweb="tab"] {
    padding: 10px 15px;
    margin: 0 5px;
    border-radius: 10px;
    transition: all 0.3s ease;
    font-weight: 500;
    color: 
#4a4a4a;
    background-color: transparent;
}

.stTabs [data-baseweb="tab"]:hover {
    background-color: rgba(75, 139, 255, 0.1);
    color: 
#4b8bff;
}

.stTabs [data-baseweb="tab"][aria-selected="true"] {
    background-color: 
#4b8bff;
    color: white;
    box-shadow: 0 4px 6px rgba(75, 139, 255, 0.3);
}

.stTabs [data-baseweb="tab"] svg {
    margin-right: 8px;
}
</style>
"""

global_font_css = """
        <style>
        /* Définit la taille de police par défaut pour toute la page */
        body, .stMarkdown, .stTextInput>div>div>input, .stSelectbox>div>div>select, 
        .stMultiSelect>div>div>div, .stDateInput>div>div>input, 
        .stNumberInput>div>div>input, .stTextArea>div>div>textarea {
            font-size: 19px !important; /* Taille de police de base */
        }

        /* Styles pour différents types de texte */
        h1 { font-size: 2.5em !important; }  /* Titres principaux */
        h2 { font-size: 2em !important; }    /* Sous-titres */
        h3 { font-size: 1.5em !important; }  /* Titres de section */
        p, div, span { font-size: 19px !important; } /* Texte de paragraphe */

        /* Option pour ajuster la taille de police de manière responsive */
        @media (max-width: 600px) {
            body, .stMarkdown {
                font-size: 14px !important;
            }
        }
        </style>
        """

profile_css = """
        <style>
        .profile-container {
            background-color: #1e2736;
            border-radius: 15px;
            padding: 20px;
            color: white;
            display: flex;
            align-items: center;
            box-shadow: 0 10px 20px rgba(0,0,0,0.2);
            max-width: 600px;
            margin: 20px auto;
        }

        .profile-image {
            width: 150px;
            height: 150px;
            object-fit: cover;
            margin-right: 20px;
            border-radius: 10px; /* Légèrement arrondi si souhaité */
        }

        .profile-content {
            flex-grow: 1;
        }

        .profile-name {
            font-size: 1.8em;
            color: #4b8bff;
            margin-bottom: 5px;
        }

        .profile-title {
            font-size: 1em;
            color: #a0a0a0;
            margin-bottom: 10px;
        }
        </style>
        """

button_style = """
            <style>
            div[data-baseweb="segmented-control"] > div {
                background-color: #f0f2f6;  /* Couleur de fond */
                border-radius: 10px;  /* Coins arrondis */
                padding: 5px;
            }
            
            div[data-baseweb="segmented-control"] button {
                color: white !important;  /* Couleur du texte */
                background-color: #4CAF50 !important;  /* Couleur de fond des boutons */
                border-radius: 8px !important;  /* Arrondi des boutons */
                padding: 10px 20px !important;  /* Espacement interne */
                font-weight: bold !important;
            }

            div[data-baseweb="segmented-control"] button:hover {
                background-color: #45a049 !important;  /* Couleur au survol */
            }
            </style>
            """

            # Custom CSS for beautiful effects and styling
custom_effects_css = """
            <style>
            /* Beautiful gradient animations */
            @keyframes gradient {
                0% {background-position: 0% 50%;}
                50% {background-position: 100% 50%;}
                100% {background-position: 0% 50%;}
            }

            /* Cards and containers styling */
            .stCard {
                background: rgba(255, 255, 255, 0.95);
                backdrop-filter: blur(10px);
                border-radius: 20px;
                padding: 1.5rem;
                box-shadow: 0 8px 32px rgba(31, 38, 135, 0.15);
                border: 1px solid rgba(255, 255, 255, 0.18);
                transition: transform 0.3s ease, box-shadow 0.3s ease;
            }

            .stCard:hover {
                transform: translateY(-5px);
                box-shadow: 0 12px 40px rgba(31, 38, 135, 0.25);
            }

            /* Button styling */
            .stButton > button {
                background: linear-gradient(45deg, #4b8bff, #7b5fff);
                border: none;
                border-radius: 10px;
                color: white;
                padding: 0.6em 1.2em;
                font-weight: 600;
                transition: all 0.3s ease;
            }

            .stButton > button:hover {
                background: linear-gradient(45deg, #7b5fff, #4b8bff);
                transform: translateY(-2px);
                box-shadow: 0 5px 15px rgba(123, 95, 255, 0.4);
            }

            /* Selectbox styling */
            .stSelectbox > div > div > select {
                background: rgba(255, 255, 255, 0.9);
                border-radius: 10px;
                border: 1px solid #e0e0e0;
                padding: 0.5em;
                transition: all 0.3s ease;
            }

            .stSelectbox > div > div > select:focus {
                border-color: #4b8bff;
                box-shadow: 0 0 0 2px rgba(75, 139, 255, 0.2);
            }

            /* Metric styling */
            .stMetric {
                background: linear-gradient(135deg, #f6f9fe 0%, #f1f4f9 100%);
                border-radius: 15px;
                padding: 1rem;
                border: 1px solid #e0e6ed;
                transition: all 0.3s ease;
            }

            .stMetric:hover {
                transform: scale(1.02);
                box-shadow: 0 8px 20px rgba(0,0,0,0.1);
            }

            /* Slider styling */
            .stSlider > div > div {
                color: #4b8bff;
            }

            .stSlider > div > div > div > div {
                background-color: #4b8bff;
            }

            /* Custom scrollbar */
            ::-webkit-scrollbar {
                width: 10px;
                height: 10px;
            }

            ::-webkit-scrollbar-track {
                background: #f1f1f1;
                border-radius: 5px;
            }

            ::-webkit-scrollbar-thumb {
                background: #4b8bff;
                border-radius: 5px;
            }

            ::-webkit-scrollbar-thumb:hover {
                background: #7b5fff;
            }

            /* Text highlights */
            ::selection {
                background: rgba(75, 139, 255, 0.3);
            }

            /* Loading animation */
            .stSpinner > div {
                border-color: #4b8bff transparent transparent;
            }

            /* Progress bar */
            .stProgress > div > div > div {
                background-color: #4b8bff;
                background-image: linear-gradient(45deg, 
                    rgba(255,255,255,.15) 25%, 
                    transparent 25%, 
                    transparent 50%, 
                    rgba(255,255,255,.15) 50%, 
                    rgba(255,255,255,.15) 75%, 
                    transparent 75%, 
                    transparent);
                background-size: 1rem 1rem;
                animation: progress-bar-stripes 1s linear infinite;
            }

            @keyframes progress-bar-stripes {
                from {background-position: 1rem 0}
                to {background-position: 0 0}
            }
            </style>
            """

st.markdown(custom_effects_css, unsafe_allow_html=True)
st.markdown(global_font_css, unsafe_allow_html=True)
        #=======================================================================
        #================== Sélecteur de langue ================================


def set_language():
    return st.sidebar.selectbox("🌍 Choisissez la langue / Choose the language", ["", "Français", "English"])


def main():
    #st.write("Autre approche: Au cas ou la première approche ne marche pas, inscrivez vous dans l'onglet connexion ci contre et utiliser vos identifiants pour vous connecter")
    st.markdown(tabs_css, unsafe_allow_html=True)
    is_authenticated = authentication_system("Superviseur")
    if is_authenticated:
        
        st.markdown(sidebar_css, unsafe_allow_html=True)
        st.markdown(useless_style, unsafe_allow_html=True)
        st.markdown(title_css, unsafe_allow_html=True)
        st.markdown(header_css, unsafe_allow_html=True)
        st.markdown(profile_css, unsafe_allow_html=True)
        st.markdown(table_css, unsafe_allow_html=True)
        st.markdown(button_style, unsafe_allow_html=True)
        st.markdown(global_font_css, unsafe_allow_html=True)
        lang = set_language()
        lang1="Français" if lang=="" else lang
        
        data=gpd.read_file("geo_data_survey.shp")
        data_rep=pd.read_excel("Data_Simulation.xlsx")
        
        # Create a dictionary of dictionaries
        role_counts = {
            "Superviseur": data_rep["ID_Superviseur"].value_counts().to_dict(),
            "Contrôleur": data_rep["ID_Contrôleur"].value_counts().to_dict(),
            "Enquêteur": data_rep["ID_Enquêteur"].value_counts().to_dict()
        }

        
        data['Total_enfa'] = np.where(data['Type_Quest'] == 'Enfant', 1, 0)
        data['Total_ense'] = np.where(data['Type_Quest'] == 'Enseignant', 1, 0)

        logo=Image.open("Logo_INS.png")
        logo2=Image.open("Logo_FEICOM.png")
        cl_tb=st.columns([1,7,1])
        with cl_tb[0]:
            st.image(logo,caption="INSTITUT NATIONAL DE LA STATISTIQUE",width=165)
        with cl_tb[1]:
            st.markdown(
            f"""
            <div class="dashboard-title-container" style="background-color: #3717BF;">
                <h1 class="dashboard-main-title"> 
                <img src="https://cdn-icons-png.flaticon.com/512/190/190411.png" alt="Icon" class="title-icon" width="50" height="50">
                {traduire_texte("Tableau de Bord Pour le suivi de la collecte sur l'enquête du FECOM", lang)}
                </h1>
                <p class="dashboard-subtitle"> 
                {"FECOM - INS "}
                </p>
            </div>
            """,
            unsafe_allow_html=True)
        with cl_tb[2]:
            st.image(logo2,width=165)
        
        la_date=st.sidebar.date_input(traduire_texte("Sélectionner la date de collecte",lang),dt.datetime(2025, 5, 20).date(),min_value=dt.datetime(2023, 1, 1).date(),max_value=dt.datetime(2025, 12, 31).date())
        data["Date"]=data["Date_Colle"].dt.strftime("%Y-%m-%d")
        
        user=st.session_state['username']
        data_rep=data_rep[data_rep["ID_Superviseur"]==user]
        
        data_to_plot=data[(data["Date_Colle"]<=la_date.strftime("%Y-%m-%d")) & (data["ID_Supervi"]==user)]
        tabs = st.tabs([
            f"📈 {traduire_texte('ANALYSE GENERALE', lang)}", 
            f"📊 {traduire_texte('PERFORMANCE ET QUALITE DES DONNEES', lang)}"
            ])
        
        with tabs[0]:
            ca=st.columns(4)
            df_date1=data_to_plot[data_to_plot["Date"]<=la_date.strftime("%Y-%m-%d")]
            df_date2=data_to_plot[data_to_plot["Date"]<=(la_date- dt.timedelta(days=1)).strftime("%Y-%m-%d")]
            ab=df_date1["Type_Quest"].value_counts()
            ab2=df_date2["Type_Quest"].value_counts()
            ab=pd.DataFrame(ab)
            ab.columns=["today"]
            ab["yesterday"]=ab2
            total_today = ab['today']["Enfant"] + ab['today']["Enseignant"]
            total_yesterday = ab['yesterday']["Enfant"] + ab['yesterday']["Enseignant"]
            
            progress_enf=data_to_plot['Total_enfa'].sum()/(18*data_rep.shape[0])
            progress_ens=data_to_plot['Total_ense'].sum()/(3*data_rep.shape[0])
            
            with ca[0]:
                display_single_metric_advanced("Qestionnaire Enfant", ab['today']["Enfant"], delta=round(100*progress_enf,2), color_scheme="blue")
            with ca[1]:
                display_single_metric_advanced("Questionnaire Enseignant", ab['today']["Enseignant"], delta=round(100*progress_ens,2), color_scheme="green")
            with ca[2]:
                display_single_metric_advanced("Questionnaire Total", total_today, delta=round(100*(total_today - total_yesterday) / total_yesterday, 2), color_scheme="purple")
            with ca[3]:
                display_single_metric_advanced("Questionnaire Total", total_today, delta=round(100*(total_today - total_yesterday) / total_yesterday, 2), color_scheme="yellow")
            st.write('')  
            col=st.columns([5.3,4.7])
            with col[1]:
                subcol=st.columns([1,1])    
                with subcol[0]:
                    opacity=st.slider(traduire_texte("Opacité de la carte",lang), 0.0, 1.0, value=0.5)  
                    data_tx=data_to_plot.groupby(['Région']).agg({'Total_enfa':'sum','Total_ense':'sum', 'Reg_ens':'first','Reg_enf':'first'}).reset_index()
                    data_tx['progression'] = (data_tx['Total_enfa'] + data_tx['Total_ense'])/(data_tx['Reg_ens'] + data_tx['Reg_enf'])
                    progress_enf=data_tx['Total_enfa'].sum()/data_tx['Reg_enf'].sum()
                    progress_ens=data_tx['Total_ense'].sum()/data_tx['Reg_ens'].sum()
                    global_progress=(data_tx['Total_enfa'].sum() + data_tx['Total_ense'].sum())/(data_tx['Reg_ens'].sum() + data_tx['Reg_enf'].sum())
                    make_progress_char(global_progress,couleur="",titre=traduire_texte("Progression de la collecte",lang))
                    
                with subcol[1]:
                    style_carte=st.selectbox(traduire_texte("Style de la carte",lang), ["carto-positron", "carto-darkmatter", "open-street-map", "CartoDB positron", "CartoDB dark_matter"])  
                    fond_color=st.selectbox(traduire_texte("Couleur de fond",lang), sequence_couleur)
                    make_dbl_progress_char(["Enfants","Enseignants"],[progress_enf,progress_ens],colors=["#4b8bff","#ff4b4b"],titre=traduire_texte("Progression par type de questionnaire ",lang),height=323)
                make_multi_progress_bar(data_tx['Région'],data_tx['progression'],colors=palette[0:11],titre=traduire_texte("Progression par région",lang),height=700)
            with col[0] :
                type_questionnaire=st.multiselect("Type de Questionnaire", options=data_to_plot["Type_Quest"].unique(),default=data_to_plot["Type_Quest"].unique()[0])
                if type_questionnaire=="Enseignant":
                    fond_color= "greens" 
                elif type_questionnaire=="Enfant":
                    fond_color= "blues"
                elif type_questionnaire=="Mairie":
                    fond_color= "reds"
                elif type_questionnaire=="Chefferie":
                    fond_color= "orange"
                else:
                    fond_color= "blues"
                data_to_plot_cart=data_to_plot[data_to_plot["Type_Quest"].isin(type_questionnaire)]
                make_school_map2(data_to_plot_cart,opacity=opacity,style_carte=style_carte,palet_color=fond_color,width=780, height=1000)
                make_cross_hist_b(data,var1="Type_Quest",palette=palette[6:],var2="Région",titre=traduire_texte("Répartition par région de la charge de travail",lang))
            
        with tabs[1]:

            #st.dataframe(data.style.set_table_attributes('class="stDataFrame"').set_properties(**{'text-align': 'left'}),use_container_width=True)
            col1=st.columns([1,1])
            with col1[0]:
                make_cross_hist_b(data_to_plot,var2="ID_Supervi",palette=palette[3:],var1="Type_Quest",titre=traduire_texte("Charge de travail accomplie par superviseur",lang))
                
            with col1[1]:
                sbcl=st.columns([1,1])
                with sbcl[0]:
                    superviseur=st.selectbox(traduire_texte("Sélectionner le controleur",lang),data_to_plot["ID_Supervi"].unique())
                with sbcl[1]:
                    data_superviz=data_to_plot[data_to_plot["ID_Supervi"]==superviseur]   
                    controleur=st.multiselect(traduire_texte("Sélectionner le controleur",lang),data_superviz["ID_Contrô"].unique(),default=data_superviz["ID_Contrô"].unique())
                    data_controleur = data_superviz[data_superviz["ID_Contrô"].isin(controleur)]
                data_tx_sup=data_superviz.groupby(['Région']).agg({'Total_enfa':'sum','Total_ense':'sum', 'Reg_ens':'first','Reg_enf':'first'}).reset_index()
                data_tx_sup['progression'] = (data_tx_sup['Total_enfa'] + data_tx_sup['Total_ense'])/(data_tx_sup['Reg_ens'] + data_tx_sup['Reg_enf'])
                progress_enf_sup=data_tx_sup['Total_enfa'].sum()/data_tx_sup['Reg_enf'].sum()
                progress_ens_sup=data_tx_sup['Total_ense'].sum()/data_tx_sup['Reg_ens'].sum()
                global_progress_sup=(data_tx_sup['Total_enfa'].sum() + data_tx_sup['Total_ense'].sum())/(data_tx_sup['Reg_ens'].sum() + data_tx_sup['Reg_enf'].sum())
                subcol1=st.columns([1,1])
                with subcol1[0]:
                    make_progress_char(global_progress_sup,couleur="",titre=traduire_texte("Progression de la collecte",lang))
                with subcol1[1]:
                    make_dbl_progress_char(["Enfants","Enseignants"],[progress_enf_sup,progress_ens_sup],colors=["#4b8bff","#ff4b4b"],titre=traduire_texte("Progression par type de questionnaire ",lang),height=300)
                make_cross_hist_b(data_superviz,var1="ID_Contrô",palette=palette[6:],var2="Type_Quest",titre=traduire_texte("Charge de travail accomplie par controleur",lang),sens="h",height=200)
                data_control=data_superviz.groupby(['ID_Contrô']).agg({'Total_enfa':'sum','Total_ense':'sum'})
                # Calculate the progression for each controller
                data_control['progression'] = (
                    (data_control['Total_enfa'] + data_control['Total_ense']) /
                    (data_control.index.map(role_counts["Contrôleur"]) * (18 + 3))
                )
                make_multi_progress_bar(data_control.index,data_control['progression'],colors=palette[2:5], titre=traduire_texte("Progression des contrôleurs",lang),height=200)
            with col1[0]:
                #make_cross_hist_b(data_to_plot,var2="ID_Supervi",var1="Type_Quest",titre=traduire_texte("Charge de travail accomplie par superviseur",lang))
                make_cross_hist_b(data_controleur,var2="ID_Enquêt",palette=palette[6:],var1="Type_Quest",titre=traduire_texte("Charge de travail accomplie par enquêteur",lang),typ_bar=2)
            cross_enq=pd.crosstab(data["ID_Enquêt"],data["Date"])
            make_st_heatmap_echat2(cross_enq,title=traduire_texte("Charge de travail accomplie par enquêteur",lang))
            
        
if __name__ == "__main__":
    main()     
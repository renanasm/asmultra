from pydoc import classname
from dash import html, dcc
from dash.dependencies import Input, Output, State
from datetime import date, datetime, timedelta
import dash_bootstrap_components as dbc
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import calendar

from app import app

card_icon = {
    "color": "white",
    "textAlign": "center",
    "fontSize": 30,
    "margin": "auto",
}



# =========  Layout  =========== #
layout = dbc.Col([
               dbc.Row([
                dbc.Col([
                    dbc.CardGroup([
                        dbc.Card([
                            html.Legend('Saldo'),
                            html.H5('R$ 6600', id='p-saldo-dashboards', style={})
                        ], style={'padding-left': '20px', 'padding-top': '10px'}),
                        dbc.Card(
                            html.Div(className='fa fa-university', style=card_icon),
                            color='warning',
                            style={'maxWidth': 75, 'height': 100, 'margin-left': '-10px'}
                        )
                    ])
                ], width=4),
                dbc.Col([
                    dbc.CardGroup([
                        dbc.Card([
                            html.Legend('Receita'),
                            html.H5('R$ 12000', id='p-Receita-dashboards', style={})
                        ], style={'padding-left': '20px', 'padding-top': '10px'}),
                        dbc.Card(
                            html.Div(className='fa fa-smile-o', style=card_icon),
                            color='success',
                            style={'maxWidth': 75, 'height': 100, 'margin-left': '-10px'}
                        )
                    ])
               ], width=4),
               dbc.Col([
                    dbc.CardGroup([
                        dbc.Card([
                            html.Legend('Despesa'),
                            html.H5('R$ 5400', id='p-despesa-dashboards', style={})
                        ], style={'padding-left': '20px', 'padding-top': '10px'}),
                        dbc.Card(
                            html.Div(className='fa fa-meh-o', style=card_icon),
                            color='danger',
                            style={'maxWidth': 75, 'height': 100, 'margin-left': '-10px'}
                        )
                    ])
        ], width=4),
    ], style={'margin': '10px'}),
    dbc.Row([
        dbc.Col([
            dbc.Card([
                html.Legend("Filtrar lançamentos", className="card-title"),
                html.Label("Categoria das receitas"),
                html.Div(
                dcc.Dropdown(
                    id="dropdown-receita",
                    clearable=False,
                    style={"width": "100%"},
                    persistence=True,
                    persistence_type="session",
                    multi=True)
                ),
                html.Label("Categoria das despesas", style={"margin-top": "10px"}),
                dcc.Dropdown(
                    id="dropdown-despesa",
                    clearable=False,
                    style={"width": "100%"},
                    persistence=True,
                    persistence_type="session",
                    multi=True
                ),
                html.Legend("Período de Análise (MM/DD/YYYY)", style={"margin-top": "10px"}),
                dcc.DatePickerRange(
                    month_format='Do MM, YY',
                    end_date_placeholder_text='Data...',
                    start_date=datetime(2022,4,1).date(),
                    end_date=datetime.today() + timedelta(days=31),
                    updatemode='singledate',
                    id='date-picker-config',
                    style={'z-index': '100'})
                    ], style={'height': "100%", 'padding': '25px'})
        ],width=4),
        dbc.Col(
            dbc.Card(dcc.Graph(id='graph1'), style={'height': '100%', 'pandding': '10px'}), width=8
        )
    ], style={'margin': '10px'}),
    dbc.Row([
       
            dbc.Col(dbc.Card(dcc.Graph(id='graph2'), style={'height': '100%', 'pandding': '10px'}), width=6),
            dbc.Col(dbc.Card(dcc.Graph(id='graph3'), style={'height': '100%', 'pandding': '10px'}), width=3),
            dbc.Col(dbc.Card(dcc.Graph(id='graph4'), style={'height': '100%', 'pandding': '10px'}), width=3),
        
    ])
])




# =========  Callbacks  =========== #

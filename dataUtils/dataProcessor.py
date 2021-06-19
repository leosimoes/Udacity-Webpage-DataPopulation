import numpy as np
import pandas as pd
import json
import requests
import plotly
import plotly.graph_objs as go

COUNTRY_CODE = 'BR'
INDICATORS_CODE = {'Rural_Population_Percentage':'SP.RUR.TOTL.ZS',
                   'Urban_Population_Percentage':'SP.URB.TOTL.IN.ZS'}
ENDPOINT_PATTERN = 'http://api.worldbank.org/v2/country/{country}/indicators/{indicator}?date=2000:2019&format=json'

def dataframeLoader(endpoint):
    r = requests.get(endpoint)
    data = r.json()[1]
    df = pd.DataFrame(data)
    # df.name = 'Name'
    return df[['date', 'value']].dropna()

def generateScatterPlot(df):
    return go.Scatter(
        x=df['date'].values,
        y=df['value'].values,
        mode='lines',
    )

def generateBarPlot(df):
    return go.Bar(
        x=df['date'].values,
        y=df['value'].values,
    )

def generateGraphOne():
    indicator_description = 'Rural_Population_Percentage'
    endpoint1 = ENDPOINT_PATTERN.format(country=COUNTRY_CODE, indicator=INDICATORS_CODE[indicator_description])
    df = dataframeLoader(endpoint1)

    graph_one = []
    graph_one.append(generateScatterPlot(df))

    layout_one = dict(title='Rural population (% of total population) X Year',
                      xaxis=dict(title='Years'),
                      yaxis=dict(title='% of total population'),
                      )

    return dict(data=graph_one, layout=layout_one)


def generateGraphTwo():
    indicator_description = 'Rural_Population_Percentage'
    endpoint2 = ENDPOINT_PATTERN.format(country=COUNTRY_CODE, indicator=INDICATORS_CODE[indicator_description])
    df = dataframeLoader(endpoint2)

    graph_two = []
    graph_two.append(generateBarPlot(df))

    layout_two = dict(title='Rural population (% of total population) X Year',
                      xaxis=dict(title='Years'),
                      yaxis=dict(title='% of total population'),
                      )

    return dict(data=graph_two, layout=layout_two)


def generateGraphThree():
    indicator_description = 'Urban_Population_Percentage'
    endpoint3 = ENDPOINT_PATTERN.format(country=COUNTRY_CODE, indicator=INDICATORS_CODE[indicator_description])
    df = dataframeLoader(endpoint3)

    graph_three = []
    graph_three.append(generateScatterPlot(df))

    layout_three = dict(title='Urban population (% of total population) X Year',
                        xaxis=dict(title='Years'),
                        yaxis=dict(title='% of total population'),
                        )

    return dict(data=graph_three, layout=layout_three)


def generateGraphFour():
    indicator_description = 'Urban_Population_Percentage'
    endpoint4 = ENDPOINT_PATTERN.format(country=COUNTRY_CODE, indicator=INDICATORS_CODE[indicator_description])
    df = dataframeLoader(endpoint4)

    graph_four = []
    graph_four.append(generateBarPlot(df))

    layout_four = dict(title='Urban population (% of total population) X Year',
                       xaxis=dict(title='Years'),
                       yaxis=dict(title='% of total population'),
                       )

    return dict(data=graph_four, layout=layout_four)


def generateGraphs():
    figures = []
    figures.append(generateGraphOne())
    figures.append(generateGraphTwo())
    figures.append(generateGraphThree())
    figures.append(generateGraphFour())

    return figures
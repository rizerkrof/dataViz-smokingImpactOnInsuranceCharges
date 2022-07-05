#!/usr/bin/env python3

import pandas as pd
import plotly.express as px

# import data
df = pd.read_csv('../data/expenses.csv')

# define plot type
fig = px.scatter(df, x='bmi', y='charges', facet_col="smoker")

# make grid lines darker
fig.update_xaxes(
    showgrid=True, gridwidth=1, gridcolor='#31353F',
    showline=True, linewidth=2, linecolor='#31353F'
)
fig.update_yaxes(
    showgrid=True, gridwidth=1, gridcolor='#31353F',
    showline=True, linewidth=2, linecolor='#31353F'
)

# define markers colors
fig.update_traces(
    marker=dict(
        color='#E22A26',
        size=20,
        line=dict(
            width=2,
            color='#31353F'
        )
    ),
    selector=dict(mode='markers')
)

# define graphic dimensions and background
fig.update_layout(
    autosize=False,
    width=1500,
    height=1000,
    plot_bgcolor = 'rgba(0,0,0,0)',
    paper_bgcolor = 'rgba(0,0,0,0)'

)

fig.show()
# the blur effect on the final viz is created by selecting the markers (box selection) directly on the plotly view.

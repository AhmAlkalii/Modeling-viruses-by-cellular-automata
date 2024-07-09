import pandas as pd
import plotly.graph_objs as go
from plotly.offline import plot

def create_choromap():
    # Load the data
    covid = pd.read_csv('USA Data.csv')
    print(covid.head(1))

    # Create the choropleth map
    data_choropleth = dict(
        type='choropleth',
        colorscale='Viridis',
        reversescale=True,
        locations=covid['State Abv'],
        locationmode="USA-states",
        z=covid['Recovered per 1M'],
        text=covid['USA State'],
        colorbar={'title': 'Recovered per 1M'},
    )

    layout_choropleth = dict(
        title='USA Covid Data: Total Recovered per 1M Population',
        geo=dict(scope='usa', showlakes=True, lakecolor='rgb(85,173,240)')
    )

    choromap = go.Figure(data=[data_choropleth], layout=layout_choropleth)
    # plot(choromap, validate=False)

if __name__ == "__main__":
    create_choromap()

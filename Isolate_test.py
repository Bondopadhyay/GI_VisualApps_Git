from dash import Dash, dcc, Output, Input
import dash_bootstrap_components as dbc   
import plotly.express as plex
import pandas as pd                     

# incorporate data into app
# Source - https://www.cdc.gov/nchs/pressroom/stats_of_the_states.htm
ds = pd.read_csv("https://github.com/anirbanGIS/GI_VisualApps_Git/blob/main/Socio_Health_US.csv")
print(ds.head())

# Build your components
app = Dash(__name__, external_stylesheets=[dbc.themes.QUARTZ])

# to render and porting via Git
server = app.server

mytitle = dcc.Markdown(children='')
mygraph = dcc.Graph(figure={})
dropdown = dcc.Dropdown(options=ds.columns.values[1:],
                        value='STATE',  # initial value displayed when page first loads
                        clearable=False)

# Customize your own Layout
app.layout = dbc.Container([
    dbc.Row([
        dbc.Col([mytitle], width=6)
    ], justify='center'),
    dbc.Row([
        dbc.Col([dropdown], width=6)
    ], justify='center'),    
    dbc.Row([
        dbc.Col([mygraph], width=10)
    ])

], fluid=True)

# Callback allows components to interact
@app.callback(
    Output(mygraph, 'figure'),
    Output(mytitle, 'children'),
    Input(dropdown, 'value')
)
def update_graph(column_name):  # function arguments come from the component property of the Input

    print(column_name)
    print(type(column_name))
    # print(type('Click to isolate'))
    # https://plotly.com/python/choropleth-maps/
    # Check the py docs for it's reference----
    fig = plex.choropleth(data_frame=ds,
                        locations='STATE',
                        locationmode="USA-states",
                        scope="usa",
                        height=600,
                        color=column_name)
                        # animation_frame='YEAR')

    return fig, '# '+column_name  # returned objects are assigned to the component property of the Output


# Run app
if __name__=='__main__':
    app.run_server(debug=True, port=5056)


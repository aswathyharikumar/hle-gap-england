
import dash
from dash import dcc, html, Input, Output
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

# Load the data
df = pd.read_csv("outputs/final_analysis_with_projections.csv")

# Initialize the Dash app
app = dash.Dash(__name__)
server = app.server  # Required for deployment

# Get list of areas for dropdown
area_list = sorted(df["Area name"].unique())

# Define colors for status
status_colors = {
    "On Track (Improving)": "#2ecc71",
    "Borderline (Slow Decline)": "#f39c12", 
    "Off Track (Rapid Decline)": "#e74c3c"
}

# App layout
app.layout = html.Div([
    html.H1("England Healthy Life Expectancy Gap Dashboard", 
            style={"textAlign": "center", "color": "#2c3e50", "padding": "20px"}),

    html.Div([
        html.H3("Measuring Years Lived in Poor Health: 2011-2024 Trends & 2035 Projections", 
                style={"textAlign": "center", "color": "#7f8c8d"})
    ]),

    # Summary statistics
    html.Div([
        html.Div([
            html.H4("128", style={"color": "#2c3e50", "margin": "0"}),
            html.P("Areas Analyzed", style={"color": "#7f8c8d"})
        ], style={"textAlign": "center", "padding": "20px", "flex": "1"}),

        html.Div([
            html.H4("18", style={"color": "#2ecc71", "margin": "0"}),
            html.P("Improving (14%)", style={"color": "#7f8c8d"})
        ], style={"textAlign": "center", "padding": "20px", "flex": "1"}),

        html.Div([
            html.H4("110", style={"color": "#e74c3c", "margin": "0"}),
            html.P("Worsening (86%)", style={"color": "#7f8c8d"})
        ], style={"textAlign": "center", "padding": "20px", "flex": "1"}),

        html.Div([
            html.H4("+2.6", style={"color": "#e74c3c", "margin": "0"}),
            html.P("Average Change (years)", style={"color": "#7f8c8d"})
        ], style={"textAlign": "center", "padding": "20px", "flex": "1"}),
    ], style={"display": "flex", "justifyContent": "space-around", "backgroundColor": "#ecf0f1", 
              "borderRadius": "10px", "margin": "20px"}),

    # Status distribution chart
    html.Div([
        dcc.Graph(id="status-chart")
    ], style={"padding": "20px"}),

    # Area comparison tool
    html.Div([
        html.H3("Compare Local Authorities", style={"color": "#2c3e50"}),
        html.Div([
            html.Div([
                html.Label("Select Area 1:"),
                dcc.Dropdown(
                    id="area1-dropdown",
                    options=[{"label": area, "value": area} for area in area_list],
                    value="Birmingham"
                )
            ], style={"width": "45%", "display": "inline-block"}),

            html.Div([
                html.Label("Select Area 2:"),
                dcc.Dropdown(
                    id="area2-dropdown",
                    options=[{"label": area, "value": area} for area in area_list],
                    value="Richmond upon Thames"
                )
            ], style={"width": "45%", "display": "inline-block", "marginLeft": "5%"}),
        ]),

        dcc.Graph(id="comparison-chart")
    ], style={"padding": "20px", "backgroundColor": "#f8f9fa", "borderRadius": "10px", "margin": "20px"}),

    # Footer
    html.Div([
        html.P("Data: ONS Health State Life Expectancy 2011-2024 | Analysis: Python (pandas, plotly)",
               style={"textAlign": "center", "color": "#95a5a6", "fontSize": "12px"})
    ], style={"padding": "20px"})
])

# Callback for status chart
@app.callback(
    Output("status-chart", "figure"),
    Input("status-chart", "id")
)
def update_status_chart(_):
    status_counts = df["status_2035"].value_counts()

    fig = go.Figure(data=[
        go.Bar(
            x=["On Track<br>(Improving)", "Borderline<br>(Slow Decline)", "Off Track<br>(Rapid Decline)"],
            y=[
                status_counts.get("On Track (Improving)", 0),
                status_counts.get("Borderline (Slow Decline)", 0),
                status_counts.get("Off Track (Rapid Decline)", 0)
            ],
            marker_color=["#2ecc71", "#f39c12", "#e74c3c"],
            text=[
                status_counts.get("On Track (Improving)", 0),
                status_counts.get("Borderline (Slow Decline)", 0),
                status_counts.get("Off Track (Rapid Decline)", 0)
            ],
            textposition="outside",
            textfont=dict(size=14, color="black")
        )
    ])

    fig.update_layout(
        title="2035 Outlook: Only 14% of Areas Are Improving",
        yaxis_title="Number of Local Authorities",
        height=400,
        showlegend=False
    )

    return fig

# Callback for comparison chart
@app.callback(
    Output("comparison-chart", "figure"),
    [Input("area1-dropdown", "value"),
     Input("area2-dropdown", "value")]
)
def update_comparison(area1, area2):
    # Get data for both areas
    data1 = df[df["Area name"] == area1].iloc[0]
    data2 = df[df["Area name"] == area2].iloc[0]

    fig = go.Figure()

    # Area 1
    fig.add_trace(go.Bar(
        name=area1,
        x=["2011-2013", "2022-2024", "2035 Projected"],
        y=[data1["gap_2011_2013"], data1["gap_2022_2024"], data1["gap_2035_projected"]],
        marker_color="#3498db"
    ))

    # Area 2
    fig.add_trace(go.Bar(
        name=area2,
        x=["2011-2013", "2022-2024", "2035 Projected"],
        y=[data2["gap_2011_2013"], data2["gap_2022_2024"], data2["gap_2035_projected"]],
        marker_color="#e67e22"
    ))

    fig.update_layout(
        title=f"HLE Gap Comparison: {area1} vs {area2}",
        yaxis_title="HLE Gap (years in poor health)",
        barmode="group",
        height=400
    )

    return fig

# Run the app
if __name__ == "__main__":
    print("\n" + "="*60)
    print("DASHBOARD STARTING...")
    print("="*60)
    print("\nOpen your browser and go to: http://127.0.0.1:8050")
    print("\nPress CTRL+C to stop the dashboard\n")
    app.run(debug=True)

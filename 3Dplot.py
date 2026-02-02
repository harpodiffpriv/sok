import pandas as pd
import plotly.express as px

df = pd.read_excel("scores.xlsx")

fig = px.scatter_3d(
    df,
    x="Privacy",
    y="Utility",
    z="Safety",
    text="Paper",
    color="Safety",
    range_x=[0,1],
    range_y=[0,1],
    range_z=[0,1])

fig.update_traces(
    marker=dict(size=10, opacity=0.9),
    hoverlabel=dict(
        font_size=50,
        font_family="Nimbus Roman No9 L",
        bgcolor="rgba(200,200,220,0.35)",
        bordercolor="black"
    ),
    textfont=dict(
        size=21,       
        color="black"
    ),
    textposition="top center"
)
fig.update_layout(
    scene=dict(
        xaxis_title="Privacy",
        yaxis_title="Utility",
        zaxis_title="Safety",
        xaxis=dict(backgroundcolor="white", gridcolor="lightgray"),
        yaxis=dict(backgroundcolor="white", gridcolor="lightgray"),
        zaxis=dict(backgroundcolor="white", gridcolor="lightgray"),
    ),
    margin=dict(l=0, r=0, b=0, t=40)
)

fig.show()

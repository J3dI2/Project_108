import pandas as pd
import csv
import plotly.figure_factory as ff

df = pd.read_csv("data.csv")
fig = ff.create_distplot([df["Avg_Rating"].tolist()], ["Rating"], show_hist=False)
fig.show()

fig = ff.create_distplot([df["Mobile_Brand"].tolist()], ["Brand"], show_hist=False)
fig.show()
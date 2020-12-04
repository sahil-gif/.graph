import pandas
import plotly.express as px

df = pd.read_csv("data.csv")
fig = px.bar(df , x='Country',y='CovidPatient')

fig.show()

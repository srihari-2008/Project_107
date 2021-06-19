import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

df=pd.read_csv("data_project.csv")
mean=df.groupby(["student_id","level"],as_index=False)["attempt"].mean()
figure=px.scatter(mean,x="student_id",y="level",size="attempt",color="attempt")
figure.show()
   
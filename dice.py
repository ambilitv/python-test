import random
import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff
import csv

df=pd.read_csv("HeightWeight.csv")
count=[]
dice_result=[]
for i in range(1,100):
    dice1= random.randint(1,6)
    dice2 =random.randint(1,6)
    sum= dice1+dice2
    dice_result.append(sum)
    count.append(i)
print(dice_result)

fig = px.bar(x= dice_result,y=count)
#fig.show()

fig2=ff.create_distplot([dice_result],["result"])
#fig2.show();

fig3=ff.create_distplot([df["Height(Inches)"].tolist()],["Height"],show_hist=False)
fig3.show()
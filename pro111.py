import csv
from collections import Counter
import pandas as pd
import math
import statistics
import plotly.graph_objects as go
import plotly.figure_factory as ff
import random 



df=pd.read_csv("pro111.csv")
data=df["claps"].to_list()

mean= statistics.mean(data)
stdev=statistics.stdev(data)

dataSet=[]
for i in range(0,100) :
    index=random.randint(0,len(data))
    value=data[index]
    dataSet.append(value)
mean2= statistics.mean(dataSet)
stdev2=statistics.stdev(dataSet)


fig=ff.create_distplot([data],['claps'],show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean], y=[0, 0.1], mode="lines", name="mean"))
fig.show()


print("mean",mean,"stdev",stdev)


def random_mean(counter) :
    dataSet=[]
    for i in range(0,counter) :
        index=random.randint(0,len(data)-1)
        value=data[index]
        dataSet.append(value)
    mean2= statistics.mean(dataSet)
    stdev2=statistics.stdev(dataSet)
    return(mean2)


def graph(meanList):
    df=meanList
    fig=ff.create_distplot([df],['claps'],show_hist=False)
    fig.add_trace(go.Scatter(x=[mean,mean], y=[0, 0.1], mode="lines", name="mean"))
    fig.show()



def setUp():
    meanSet=[]
    for i in range(0,1000):
        setMeans=random_mean(100)
        meanSet.append(setMeans)

    meanCount= statistics.mean(meanSet)
    stdevCount=statistics.stdev(meanSet)

    print("meanOfSampleDis",meanCount,"stdevOfSampleDis",stdevCount)
    graph(meanSet)

setUp()
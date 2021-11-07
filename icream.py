import plotly.express as px
import csv 
import numpy as np
def plotfig(data_path):
  with open (data_path)as csv_file:

    df= csv.DictReader(csv_file)
    fig= px.scatter(df,x='Roll No',y='Marks In Percentage')
    fig.show()

def getDataSource(data_path) :
    icecream=[]
    temp=[]
    with open (data_path)as csv_file:
      reader=csv.DictReader(csv_file)

      for row in reader:
        icecream.append(float(row["Marks In Percentage"]))
        temp.append(float(row["Roll No"]))
    return{"x":icecream,"y":temp}
def fcorrelation(DataSource):
  correlation= np.corrcoef(DataSource["x"],DataSource["y"])
  print("corelation brtwween Roll No  and icecream",correlation[0,1])
def setup():
  data_path = "/Users/manassingi/Desktop/python/PRO-106/stu.csv"
  DataSource= getDataSource(data_path)
  fcorrelation(DataSource)
  plotfig(data_path)
  
setup()
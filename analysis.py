#PANDS Project: An Analysis of the Iris-Fisher data set
#Author: Chris Foley

#Start by importing modules used in the analysis
import pandas as pd #for manipulating data-set
import matplotlib.pyplot as plt #for graphing data
import seaborn as sns #for graphing data


sns.set_style('dark') #sets background style of seaborn graphs 

df = pd.read_csv('IRIS.csv') #reading in data set

df.info() #pandas method, outputs number of columns, empty variables and type of object in the data-set 
print(df.describe(include='all')) #pandas method, outputs summary statistics e.g means, standard deviations, and counts catagorical variables.



# Histograms of the three plants for each variable
#sns.histplot(data = df, x = 'sepal_length', hue = "species") # plt.legend removes labels
#sns.histplot(data = df, x = 'petal_length', hue = "species")
#sns.histplot(data = df, x = 'sepal_width', hue = "species")
#sns.histplot(data = df, x = 'sepal_width', hue = "species")

# Plots line map of 3 species in line
plot = sns.FacetGrid(df, col="species") #***
#plot.map(plt.plot, "sepal_width") 
#plot.map(plt.plot, "petal_width")
#plot.map(plt.plot, "sepal_length")
#plot.map(plt.plot, "petal_length")


sns.pairplot(df, hue='species', height=2) # compares each pair of variables by species


#plt.legend()
plt.show()

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
fig1 = sns.histplot(data = df, x = 'sepal_length', hue = "species", multiple="dodge").set(title='Histogram of Iris Sepal Length')

plt.savefig("fig1") 

fig2 = sns.histplot(data = df, x = 'petal_length', hue = "species", multiple="dodge").set(title='Histogram of Iris Petal Length')

plt.savefig("fig2")

fig3 = sns.histplot(data = df, x = 'sepal_width', hue = "species", multiple="dodge").set(title='Histogram of Iris Sepal Width')

plt.savefig("fig3")

fig4 = sns.histplot(data = df, x = 'petal_width', hue = "species", multiple="dodge").set(title='Histogram of Iris Petal Width')
plt.savefig("fig4")


# Plots line map of 3 species side by side on named variable
plot = sns.FacetGrid(df, col="species") #takes data and column as input.
plot.map(plt.plot, "sepal_length")
plot.map(plt.plot, "petal_length")
plot.map(plt.plot, "sepal_width") 
plot.map(plt.plot, "petal_width")

print(df.corr()) #prints correlation table for data-set
dataplot = sns.heatmap(df.corr(), cmap="Spectral", annot=True) #prints heatmap of correlations

sns.pairplot(df, hue='species', height=2) # compares each pair of variables by species

plt.show()

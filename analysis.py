#PANDS Project: An Analysis of the Iris-Fisher data set
#Author: Chris Foley
#We start by importing modules used in the analysis
import pandas as pd #Used for manipulating the data-set
import matplotlib.pyplot as plt #Used for graphing data
import seaborn as sns #Addition to matplot.lib for more aesthetic graphing of data
sns.set_style('dark') #sets background style of seaborn graphs
from sklearn.cluster import KMeans #Used for setting number of clusters and iterations in kmeans testing
df = pd.read_csv('IRIS.csv')#reading in our data set from the current directory
df.info() #A pandas method which outputs number of columns, empty variables and type of object in the data-set 
print(df.describe(include='all')) #A pandas method which outputs some descriptive statistics, e.g means, 
#standard deviations and counts catagorical variables.

#Next we plot Histograms of the three plants for each variable
#"x" provides the variable we're looking at the frequency of while "Hue" tells Seaborn to divide the scores 
#according to out categorical variable column "species". "dodge" tells Seaborn to present the graphs side by side
#and not overlapping or on top of one another. Finally we use ".set(title" to title our Histograms. The legend is 
#automatically input by Seaborn's "hue" function.  
fig1 = sns.histplot(data = df, x = 'sepal_length', hue = "species", multiple="dodge").set(title='Histogram of Iris Sepal Length')
plt.savefig("fig1") 
fig2 = sns.histplot(data = df, x = 'petal_length', hue = "species", multiple="dodge").set(title='Histogram of Iris Petal Length')
plt.savefig("fig2")
fig3 = sns.histplot(data = df, x = 'sepal_width', hue = "species", multiple="dodge").set(title='Histogram of Iris Sepal Width')
plt.savefig("fig3")
fig4 = sns.histplot(data = df, x = 'petal_width', hue = "species", multiple="dodge").set(title='Histogram of Iris Petal Width')
plt.savefig("fig4")

# Plots line map of 3 species side by side on named variable
plot = sns.FacetGrid(df, col="species", hue="species") #Takes data and column as input.
#Each of the below tells Seaborn what variable to plot.
plot.map(plt.plot, "sepal_length")
plot.map(plt.plot, "petal_length")
plot.map(plt.plot, "sepal_width") 
plot.map(plt.plot, "petal_width")

#Correlational analysis
#prints correlation table for data-set
print(df.corr()) 

#prints heatmap of correlations, "cmap" chooses color scheme. Setting "annot" to "True" tells Seaborn to display the 
#numerical values of each relation in each cell making for better readability 
dataplot = sns.heatmap(df.corr(), cmap="Spectral", annot=True).set(title='Correlation Heatmap for Iris Plant Scores')  

# compares each pair of variables by species
sns.pairplot(df, hue='species', height=2) 

#Sets number of clusters and number of times algorithim will run with different centroid seeds.
km=KMeans(n_clusters=2, n_init=2)

#fit_predict calculates cluster centres and predicts cluster index for each sample.
y_predicted =km.fit_predict(df[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']])
#y_predicted

#Finds the centroid of the clusters. This will be consistent with labels unless the algorithim stops before fully converging  
km.cluster_centers_
#assigns samples in data to indexes in cluster
df['clusters'] = km.labels_
#plots pairplot
sns.pairplot(df, hue = 'clusters')
plt.show()


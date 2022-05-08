# pands-project
READ ME
Chris Foley PANDS Project

Analysis of the Iris-Fisher data set
This document runs through and explains my programmatic analysis of the Iris-Fisher data-set. The Iris data-set is comprised of 150 observations of 5 variables, 
sepal length and width, petal length and width and species. There are three species included, Iris Setosa, Iris Versicolor and Iris Virginica, with 50 measurements 
of sepal and petal length and width for each. The Iris set is widely used for training aspiring data scientists and machines alike. 
A note on using this code: The code contains many plots, when ran all at once some of these will overlap each other. I recommend commenting out any lines containing plots not presently in use to get the intended graph.

We start by importing the python modules we'll be using for our analysis. Primarily, these are: Pandas, Matplotlib and Seaborn.
Next we use a Pandas function 
	
	1. df = (pd.read_csv)  
	
to read our data set in from our machine. "df" is the shorthand name for our data-set hereafter. 
The Iris set can also be read in our programme with Seaborn by using the below
	
	2. iris = sns.load_dataset('iris') 

With the data set in hand we're ready to analyse. I start by using two useful Pandas methods "df.info()" and "df.describe()".
	
	3. df.info() 

The "info" method tells us how many columns are in the data-set, the type and quantity of data contained in the set and also if there 
are any empty variables or null values. Here we have four floats, one categorical object and no null values. If we had any null values now would be a good time to remove or
replace them with dummy variables so as not to interfere with our analysis. Pandas' "info" method also tells us how much memory the programme uses, which would be more
important if we were dealing with a vary large data-set.  

	4. df.describe() 
	
The "describe" method outputs a variety of useful statistics from our data-set, more so for numerical data but by adding 
"(include='all') we can include any categorical data. In this case "species", telling us there are three distinct types with a frequency 
of 50 variables each totalling 150. 

The describe method also outputs, for each numerical variable, the mean, standard deviation, min and max values as well as the 25th, 50th 
and 75th percentile. The mean serves as a useful measure of the central tendency of each variable and taken with the standard deviation 
we get some preliminary insights into our data. For instance, we can see the highest value is for sepal length at 7.9cm. 
The next closest is petal length at 6.9cm. Sepal length is also the highest minimum value at 4.3cm. 
Petal width is the smallest value as measured by mean, min and max, and has a similar standard deviation to sepal length (.82 and .76). 
Sepal width and petal length then represent the middle range of our set's scores at 3 and 3.7 respectively. However, 
in spite of the closeness of their means, we can't necessarily expect these scores to be clustered closely together, 
as between them they have the smallest and largest standard deviations, at 0.4 for sepal width and 1.7 for petal length.
Note we could also use the median and mode (with methods "df.median()" and "df.mode()") to give us  as measures of central tendency, but since mode is more applicable
to categorical data and median gives paints a similar picture to the one given above by means and standard deviations I've omitted them from the analysis.   

Histograms
Our next step is to graphically represent our data using Seaborn. First we plot histograms for the three species, showing the frequency of each plants scores 
in sepal/petal length/width. To do this we use the seaborn method of plotting histograms, starting with sepal length.

	5.1 sns.histplot(data = df, x = 'sepal_length', hue = "species", multiple="dodge") 

Seaborn lets us choose the axis we want to display our data along by naming our variable, e.g. "sepal length" either "x" or "y". Setting "hue" to "species" then 
tells it to divide the scores (by colour) according to our categorical variable type, species. Finally by using "multiple="dodge"" we can tell seaborn to place the bars
side by side, rather than overlapping, or stacking. 

The resulting histogram shows that the Setosa plant has the shortest 
sepal length, with most of it's scores clustered between 4.5 and 5.5cm. Iris-Virginica has the largest sepal length with most of it's scores clustered between 6 and 8cm. 
Iris-Versicolor occupies the middle range between the two. This implies if we're looking at sepal length alone, an Iris plant with a very long sepal is likely a Virginica. 
Conversely if the sepal is very short it's likely a Setosa. 

Our next histogram, created with the below code shows a similar pattern but for petal length.

	5.2 sns.histplot(data = df, x = 'petal_length', hue = "species", multiple="dodge")  

Iris-Setosa is distinctly shorter than it's peers, with all of it's scores in a range of 1-2cm. Meanwhile Iris-Virginica is again the longest with most of it's scores between 
5.5 and 6 and it's highest coming in at 7. Iris-Versicolor is again the middle value but this time with less overlap than in sepal length. Meaning when it comes to petal 
petal length we can be reasonably assured a length of 1-2cm indicates a Setosa, a length of 3-5cm a Versicolor and a length of 5-7 a Virginica. Briefly summarised, 
our findings on length are that Iris-Setosa is the shortest, Virginica is the longest. Now we move on to width.

	5.3 sns.histplot(data = df, x = 'sepal_width', hue = "species", multiple="dodge") 

Looking at sepal width, we can see a much denser distribution around 2.5 and 3.5cm for each species. On the wider end of the spectrum sit's the Setosa while the narrowest 
plant is the Versicolor. Iris-Virginica occupies the middle when it comes to width. Overall though these scores are much closer together and therefore less likely 
to be reliable predictors of species type by themselves. Though taken with our previous insights, if an Iris is very short and very wide it's probably a Setosa.

Finally, to petal width.

	5.4 sns.histplot(data = df, x = 'petal_width', hue = "species", multiple="dodge") 

And we can see this looks a lot like the graph for petal length, which may lead us to suppose there will be a strong positive correlation between petal length and width, 
a supposition we will test shortly. Unlike it's sepal, the Setosa's petal is quite small, with all of it's scores coming between 0.1 and 0.5cm. Iris-Versicolor comprises
the middle range from 1-1.6cm with an outlier nearing 2cm. The widest petal belongs to Iris-Virginica at 2.5 and indeed, the majority of it's scores are in the range 2-2.5cm.
There is a Virginica outlier too around 1.4cm. 

From these histograms we've learned to distinguish Iris-Setosa from it's fellows by it's short length, narrow petal and wide sepal. Iris-Virginica too can be distinguished 
by it's long petal and sepal and wide petal. Iris-Versicolor is most often the middle between the Setosa and Virginica's extremes, except in Sepal width, where it's most
likely the narrowest. Though with Versicolor's tendency towards the middle the probability of correctly guessing it's species based on this data alone should be lower than for 
Virginica and less again than for Setosa. 

Line Plots
We can see the same result via a series of line plots for each numerical variable given below.

	6. plot = sns.FacetGrid(df, col="species")  

	plot.map(plt.plot, "sepal_length")

	plot.map(plt.plot, "petal_length")

	plot.map(plt.plot, "sepal_width") 

	plot.map(plt.plot, "petal_width") 


Again this code uses Seaborn’s methods to conveniently present data. By setting the column to Species we get 3 graphs (one for each species) for each measurement. 


Correlations
Earlier we noted a striking similarity in the histograms for petal length and petal width and using python we can confirm this, and also tell if there are any other interesting correlations we may have missed. 
We do this with the following code

	7. print(df.corr()) 

We can also make this look nicer with a correlation heatmap courtesy of Seaborn via the following code

	8. dataplot = sns.heatmap(df.corr(), cmap="YlGnBu", annot=True) 

Here "cmap" chooses the colour scheme while "annot=True" tells python to display the numerical value of each correlation on the heatmap. We can see a very strong positive correlation 
at 0.96 for petal length and petal width, as suspected. Petal length and sepal length also share a strong positive correlation of 0.87, as do sepal length and petal width at 0.82. In addition there are weak 
negative correlations for sepal width and petal length (-0.42), and for sepal width and petal width (-0.36). Finally there is an almost no relation whatsoever between sepal length and sepal width (-0.11). 
Looking back at our line plots we can also see these relationships. But there is another way to visualise them all at once again using Seaborn. The method

	9. sns.pairplot(df, hue='species', height=2) 

lets us see the relationships between each pair of variables for each species all at once. It gives us the same picture as the heatmap but is comprised of the individual data points in the set. 

Looking at the data in this way we can see Iris-Setosa can be easily distinguished by being typically smaller than its compatriots in all areas but Sepal width. While Iris-Virginica and Versicolor are closer 
together in most areas, Virginica’s slight size edge over versicolor in all but sepal width mean it is also fairly reliably distinguishable from it’s cohorts on these grounds. 

References
1. Reading data-set with Pandas: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html
2. Loading data-sets in Seaborn: https://seaborn.pydata.org/generated/seaborn.load_dataset.html
3. Pandas Info method: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.info.html
4. Pandas Describe method: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.describe.html
5. Ploting Histplots in Seaborn: https://seaborn.pydata.org/generated/seaborn.histplot.html
6. Plotting FacetGrid in Seaborn: https://seaborn.pydata.org/generated/seaborn.FacetGrid.html
7. Pandas correlation method: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.corr.html
8. Heatmaping correlations in Seaborn: https://seaborn.pydata.org/generated/seaborn.heatmap.html
9. Pairplotting in Seaborn: https://seaborn.pydata.org/generated/seaborn.pairplot.html

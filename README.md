# pands-project

READ ME

Chris Foley PANDS Project

Analysis of the Iris-Fisher data set

This document runs through and explains my programmatic analysis of the Iris-Fisher data-set.


We start by importing the python modules we'll be using for our analysis. Primarily, these are: Pandas, Matplotlib and Seaborn.

Next we use a Pandas function 

	df = (pd.read_csv)  
	
to read our data set in from our machine. "df" is the shorthand name for our data-set hereafter. 
The Iris set can also be read in our programme with Seaborn by using the below method. 
	
	iris = sns.load_dataset('iris')
	
With the data set in hand we're ready to analyse. I start by using two useful Pandas methods "df.info()" and "df.describe()".
The "info" method tells us how many columns are in the data-set, the type and quantity of data contained in the set and also if there 
are any empty variables or null values. Here we have four floats, one categorical object and no null values. It also tells us how
much memory the programme uses. 

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

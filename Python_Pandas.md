# Python Cheat Sheet

**__init__ is the constructor for a class. The self parameter refers to the instance of the object.**

## Describing the data
``` py
* df.shape  #returns number of instances (rows) and attributes (columns)
* df.head() #returns the first 10 rows of the dataset
* df.describe() #statistical summary (count, mean, min, max values)

#Class distribution
* pd.groupby('series').size() #Look at the number of instances that belong to each attribute.
* df['serie'].value_counts() #The most common instances of an attribute in decending order
```

## Visualizing the data
``` py
#Univariate Plots
* df.hist() #Create a histogram to get an idea of the distribution
* df.plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False) #Boxplot (numeric input)

#Multivariate Plots
* scatter_matrix(df) #Pairplots to spot structured relationsships between input variables

```

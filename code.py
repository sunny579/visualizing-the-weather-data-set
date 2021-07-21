# --------------
# Import the required Libraries
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import calendar
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")


# Generate a line chart that visualizes the readings in the months

def line_chart(df,period,col):
    plt.plot(df[period] ,df[col] )
    plt.xticks(rotation = 90)
    plt.show()
    """ A line chart that visualizes the readings in the months
    
    This function accepts the dataframe df ,period(day/month/year) and col(feature), which plots the aggregated value of the feature based on the periods. Ensure the period labels are properly named.
    
    Keyword arguments:
    df - Pandas dataframe which has the data.
    period - Period of time over which you want to aggregate the data
    col - Feature of the dataframe
    
    """
    
    







# Function to perform univariate analysis of categorical columns
def plot_categorical_columns(df):
    plt.figure(figsize = (12,8))
    df["Weather"].value_counts().plot(kind= "bar")
    plt.show()
    """ Univariate analysis of categorical columns
    
    This function accepts the dataframe df which analyzes all the variable in the data and performs the univariate analysis using bar plot.
    
    Keyword arguments:
    df - Pandas dataframe which has the data.
    
    """
    








# Function to plot continous plots
def plot_cont(df,plt_typ):
    if plt_typ == "distplot":
        sns.distplot(df["Temp (C)"])
        plt.show()
        sns.distplot(df['Dew Point Temp (C)'])
        plt.show()
        sns.distplot(df["Rel Hum (%)"])
        plt.show()
        sns.distplot(df["Wind Spd (km/h)"])
        plt.show()
        sns.distplot(df["Visibility (km)"])
        plt.show()
        sns.distplot(df["Stn Press (kPa)"])
        plt.show()
    elif plt_typ == "boxplot":
        sns.boxplot(df["Temp (C)"])
        plt.show()
        sns.boxplot(df["Dew Point Temp (C)"])
        plt.show()
        sns.boxplot(df["Rel Hum (%)"])
        sns.boxplot(df["Wind Spd (km/h)"])
        plt.show()
        sns.boxplot(df["Visibility (km)"])
        plt.show()
        sns.boxplot(df["Stn Press (kPa)"])
        plt.show()
    

    """ Univariate analysis of Numerical columns
    
    This function accepts the dataframe df, plt_type(boxplot/distplot) which analyzes all the variable in the data and performs the univariate analysis using boxplot or distplot plot.
    
    Keyword arguments:
    df - Pandas dataframe which has the data.
    plt_type - type of plot through which you want to visualize the data
    
    """
    
    







# Function to plot grouped values based on the feature
def group_values(df,col1,agg1,col2):
    df = df.groupby(col1).agg({col2 : agg1})
    plt.bar(df.index,df[col2])
    plt.xticks(rotation= 90)
    plt.show()
    """ Agrregate values by grouping
    
    This function accepts a dataframe, 2 column(feature) and aggregated function(agg1) which groupby the dataframe based on the column and plots the bar plot.
   
    Keyword arguments:
    df - Pandas dataframe which has the data.
    col1 - Feature of the dataframe on which values will be aggregated.
    agg1 - Dictionary of aggregate functions with feature as the key and func as the value
    col2 - Feature of the dataframe to be plot against grouped data.
    
    Returns:
    grouping - Dataframe with all columns on which it is grouped on.
    """
    
    




# Read the Data and pass the parameter as parse_dates=True, index_col='Date/Time'

weather_df = pd.read_csv(path,parse_dates = True,index_col = "Date/Time")
print(weather_df.select_dtypes(include = "object").columns)
print(weather_df.select_dtypes(include = "number").columns)
weather_df.reset_index(inplace = True)
# Lets try to generate a line chart that visualizes the temperature readings in the months.
# Call the function line_chart() with the appropriate parameters.
weather_df["Month"] = pd.to_datetime(weather_df["Date/Time"]).dt.month

df = weather_df.groupby("Month")[["Temp (C)"]].mean()
df.reset_index(inplace = True)
df["Month"] = df["Month"].map({1:"January",2:"February",3:"March",4:"April",5:"May",6:"June",7:"July",8:"August",9:"September",10:"October",11:"November",12:"December"} )

line_chart(df , "Month", "Temp (C)")
weather_df.set_index(["Date/Time"],inplace = True)
weather_df.drop(["Month"],inplace = True,axis =1)

# Now let's perform the univariate analysis of categorical features.
# Call the "function plot_categorical_columns()" with appropriate parameters.

plot_categorical_columns(weather_df)

# Let's plot the Univariate analysis of Numerical columns.
# Call the function "plot_cont()" with the appropriate parameters to plot distplot

plot_cont(weather_df,"distplot")

# Call the function "plot_cont()" with the appropriate parameters to plot boxplot
plot_cont(weather_df,"boxplot")

# Groupby the data by Weather and plot the graph of the mean visibility during different weathers. Call the function group_values to plot the graph.
group_values(weather_df,"Weather",np.mean,"Visibility (km)")
# Feel free to try on diffrent features and aggregated functions like max, min.





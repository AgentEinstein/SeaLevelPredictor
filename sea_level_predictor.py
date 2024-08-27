import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    df = pd.read_csv('epa-sea-level.csv')
    
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue', label='Original Data')
    
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years_extended = pd.Series(range(1880, 2051))
    sea_levels_predicted = intercept + slope * years_extended
    plt.plot(years_extended, sea_levels_predicted, 'r', label='Best Fit Line (1880-2050)')
    
    df_recent = df[df['Year'] >= 2000]
    slope_recent, intercept_recent, r_value_recent, p_value_recent, std_err_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    years_recent_extended = pd.Series(range(2000, 2051))
    sea_levels_recent_predicted = intercept_recent + slope_recent * years_recent_extended
    plt.plot(years_recent_extended, sea_levels_recent_predicted, 'green', label='Best Fit Line (2000-2050)')
    
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()
    
    plt.savefig('sea_level_plot.png')
    return plt.gca()

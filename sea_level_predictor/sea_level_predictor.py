import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # Read the data from the CSV file
    df = pd.read_csv('epa-sea-level.csv')

    # Create a scatter plot of the Year vs Sea Level
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'],
                c='blue', s=8)

    # Calculate and plot the first line of best fit (using all data)
    slope, intercept, *_ = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x_predict_2050 = range(1880, 2051)
    plt.plot(x_predict_2050, intercept + slope * x_predict_2050,
             'r', label='First Line of Best Fit')

    # Calculate and plot the second line of best fit (using data from 2000 onwards)
    df_recent = df[df['Year'] >= 2000]
    slope_recent, intercept_recent, *_ = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    x_predict_2000_2050 = range(2000, 2051)
    plt.plot(x_predict_2000_2050, intercept_recent + slope_recent * x_predict_2000_2050,
             'g', label='Second Line of Best Fit')

    # Add labels and title to the plot
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')

    # Add a legend with custom labels
    first_line_handle, = plt.plot(x_predict_2050, intercept + slope * x_predict_2050, 'r',
                                  label='First Line of Best Fit')
    second_line_handle, = plt.plot(x_predict_2000_2050, intercept_recent + slope_recent * x_predict_2000_2050, 'g',
                                   label='Second Line of Best Fit')
    plt.legend([first_line_handle, second_line_handle], ['First Line of Best Fit', 'Second Line of Best Fit'])

    # Save the plot as an image file
    plt.savefig('sea_level_plot.png')

    return plt.gca()


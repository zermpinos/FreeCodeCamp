# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data from a CSV file and parse dates
df = pd.read_csv('fcc-forum-pageviews.csv', index_col='date', parse_dates=True)

# Remove outliers from the data
df = df[(df['value'] >= df['value'].quantile(0.025)) & (df['value'] <= df['value'].quantile(0.975))]


# Create a line plot
def draw_line_plot():
    # Create a figure with a specific size
    fig, ax = plt.subplots(figsize=(15, 5))

    # Plot the data as a line chart
    ax.plot(df.index, df['value'], color='red')

    # Set the x and y-axis labels and the chart title
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')

    # Adjust the layout of the chart
    plt.tight_layout()

    # Save the chart as an image and return the figure
    fig.savefig('line_plot.png')
    return fig


# Create a bar chart
def draw_bar_plot():
    # Group the data by year and month and calculate the average page views for each group
    df_bar = df.groupby([df.index.year, df.index.month]).mean()

    # Create a bar chart with a specific size and a legend
    ax = df_bar.unstack().plot(kind='bar', figsize=(10, 8))
    ax.legend(title='Months', labels=[
        'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November',
        'December'
    ])

    # Set the x and y-axis labels
    ax.set(xlabel='Years', ylabel='Average Page Views')

    # Save the chart as an image and return the figure
    fig = ax.get_figure()
    fig.savefig('bar_plot.png', bbox_inches='tight')
    return fig


# Create box plots
def draw_box_plot():
    # Add 'year' and 'month' columns to the data
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Create two box plots side by side
    fig, axes = plt.subplots(1, 2, figsize=(20, 8))

    # Draw the first box plot for the year-wise trend
    sns.boxplot(x='year', y='value', data=df_box, ax=axes[0])
    axes[0].set_title('Year-wise Box Plot (Trend)')
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Page Views')

    # Draw the second box plot for the month-wise seasonality
    sns.boxplot(x='month', y='value', data=df_box, ax=axes[1], order=[
        'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
    ])
    axes[1].set_title('Month-wise Box Plot (Seasonality)')
    axes[1].set_xlabel('Month')
    axes[1].set_ylabel('Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig

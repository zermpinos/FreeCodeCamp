import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Read the dataset and create a new column called 'overweight':
df = pd.read_csv('medical_examination.csv')
df['overweight'] = (df['weight'] / ((df['height'] / 100) ** 2)).apply(lambda x: 1 if x > 25 else 0)

# Normalize 'cholesterol' and 'gluc' columns
# If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df['cholesterol'] = df['cholesterol'].apply(lambda x: 0 if x == 1 else 1)
df['gluc'] = df['gluc'].apply(lambda x: 0 if x == 1 else 1)


# Draw Categorical Plot
def draw_cat_plot():
    # Melt the DataFrame to create a new DataFrame with 'cardio', 'variable', and 'value' columns
    df_cat = pd.melt(df, id_vars=['cardio'],
                     value_vars=['active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke'], var_name='variable')

    # Group the new DataFrame by 'cardio', 'variable', and 'value', count the occurrences,
    # and rename the 'value' column to 'total':
    df_cat = pd.DataFrame(df_cat.groupby(['cardio', 'variable', 'value'])
                          ['value'].count()).rename(columns={'value': 'total'}).reset_index()

    # Create a Seaborn categorical plot using the grouped DataFrame
    # Draw the catplot with 'sns.catplot()'
    g = sns.catplot(data=df_cat, x='variable', y='total', hue='value', col='cardio', kind='bar')

    # Get the figure for the output
    fig = g.fig

    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat = df[(df['ap_lo'] <= df['ap_hi'])
                 & (df['height'] >= df['height'].quantile(0.025))
                 & (df['height'] <= df['height'].quantile(0.975))
                 & (df['weight'] >= df['weight'].quantile(0.025))
                 & (df['weight'] <= df['weight'].quantile(0.975))]

    # Calculate the correlation matrix
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    mask = np.zeros_like(corr)
    mask[np.triu_indices_from(mask)] = True

    # Set up the Matplotlib figure and plot the Seaborn heatmap
    fig, ax = plt.subplots(figsize=(12, 12))
    sns.heatmap(corr, mask=mask, annot=True, fmt='.1f', vmax=.3, center=0, square=True, linewidths=.5,
                cbar_kws={'shrink': .5})

    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig

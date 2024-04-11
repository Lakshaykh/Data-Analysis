#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df=pd.read_csv("medical_examination.csv")
df['overweight'] = (df['weight'] / ((df['height'] / 100) ** 2) > 25).apply(lambda x: 1 if x>25 else 0)
df['Cholesterol']=df['Cholesterol'].apply(lambda x :0 if x ==1 else 1)
df['Glucose']=df['Glucose'].apply(lambda x : 0 if x==1 else 1)

def draw_catplot():
    df_cat=pd.melt(df,id_vars=['cardio'],value_vars=['cholesterol','gluc','smoke','alco','active','overweight'])
    df_cat['total'] = 1
    df_cat = df_cat.groupby(['cardio', 'variable', 'value'], as_index=False).count()

    # Rename one of the columns for the catplot to work correctly
    df_cat.rename(columns={'total': 'total'}, inplace=True)

    # Convert the data into long format and create a chart using seaborn's catplot
    g = sns.catplot(data=df_cat, x='variable', hue='value', kind='bar', col='cardio', y='total', ci=None)
    fig = g.fig

    # Do not modify the next two lines
    plt.close(fig)
    return fig
df_heat = df[
    (df['ap_lo'] <= df['ap_hi']) &
    (df['height'] >= df['height'].quantile(0.025)) &
    (df['height'] <= df['height'].quantile(0.975)) &
    (df['weight'] >= df['weight'].quantile(0.025)) &
    (df['weight'] <= df['weight'].quantile(0.975))
]

# Calculate the correlation matrix
corr = df_heat.corr()

# Generate a mask for the upper triangle
mask = ((corr.where(np.triu(np.ones(corr.shape), k=1).astype(bool))).abs() > 0.0)

# Set up the matplotlib figure
fig, ax = plt.subplots(figsize=(11, 9))

# Plot the correlation matrix using seaborn's heatmap
sns.heatmap(corr, annot=True, fmt='.1f', mask=mask, vmax=.3, center=0, square=True, linewidths=.5, cbar_kws={"shrink": .5})

# Do not modify the next two lines
plt.show()


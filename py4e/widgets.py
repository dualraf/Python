import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from ipywidgets import interact
import ipywidgets as widgets


x1 = np.random.normal(-2.5, 1, 1000)
x2 = np.random.gamma(2, 1.5, 1000)
x3 = np.random.exponential(2, 1000)+7
x4 = np.random.uniform(14,20, 1000)

df=pd.DataFrame()
df['Normal']=x1
df['Gamma']=x2
df['Exponential']=x3
df['Uniform']=x4
col=df.columns
@interact(col_names=widgets.SelectMultiple(
    options=col,
    value=(col[0],),
    description='Columns'))
def plot_data(col_names):
    plt.figure(figsize=[9,3])
    plt.gcf().suptitle(col_names)
    plt.hist(df[list(col_names)], density=True, bins=20, alpha=0.5)
    plt.axis([-7,21,0,0.6])
    plt.show()
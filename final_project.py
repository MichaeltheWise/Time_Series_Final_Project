#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 12 14:12:53 2018

@author: MichaelLin
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf
import statsmodels.api as sm
from statsmodels.tsa import seasonal
import seaborn as sns
from datetime import datetime

## Detrend with time
data = pd.read_excel("inflation.xlsx")
data.columns = ['Inflation_Data']
data['Time_t'] = data.index
data = data.sort_values('Time_t')
data['Time'] = pd.factorize(data['Time_t'])[0] + 1
mapping = dict(zip(data['Time'], data['Time_t'].dt.date))
fig = plt.figure(figsize = (10,5))
sns.regplot(x = 'Time',y = 'Inflation_Data',data = data)
ax = plt.gca()
labels = pd.Series(ax.get_xticks()).map(mapping).fillna('')
ax.set_xticklabels(labels)

fig1 = plt.figure(figsize = (10,5))
sns.residplot(x = 'Time', y = 'Inflation_Data', data = data, lowess = True)

## Detrend using previous year data
data['Inflation_PY_Data'] = data['Inflation_Data'].shift(1)
data.dropna()
fig2 = plt.figure(figsize = (10,5))
model1 = smf.ols('Inflation_Data ~ Inflation_PY_Data', data = data).fit()
sns.regplot(x = 'Inflation_PY_Data',y = 'Inflation_Data', data = data)

fig3 = plt.figure(figsize = (10,5))
sns.residplot(x = 'Inflation_PY_Data', y = 'Inflation_Data', data = data, lowess = True)



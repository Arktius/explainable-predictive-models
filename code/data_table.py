# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 06:56:46 2020

@author: Admin
"""

import pandas as pd
import numpy as np

n = 1000
dpath = './data/1kplus_data_and_labels_outcome_pred_with_nans.pkl'

df = pd.DataFrame()
df['AD_NIH'] = pd.Categorical(np.random.randint(0,3,n))
df['AT_LY'] = np.random.choice([False,True],n)
df['DG_SEX'] = np.random.choice([False,True],n)
df['RF_DM'] = np.random.choice([False,True],n)
df['RF_HC'] = np.random.choice([False,True],n)
df['DG_AG'] = np.round(np.random.normal(72,7.5,n),2)
df['CH'] = pd.Categorical(np.random.randint(0,10,n))

df['label'] = pd.Categorical((np.random.normal(0.5,1,n)>0.8)+0)

df.to_pickle(dpath)

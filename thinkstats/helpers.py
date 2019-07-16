import numpy as np
import pandas as pd

def clean_fem_preg(df):
    df.agepreg /=100.
    
    na_vals = [97,98,99]
    df.birthwgt_lb.replace(na_vals,np.nan,inplace=True)
    df.birthwgt_oz.replace(na_vals,np.nan,inplace=True)
    df['totalwgt_lb'] = df.birthwgt_lb + df.birthwgt_oz / 16.0
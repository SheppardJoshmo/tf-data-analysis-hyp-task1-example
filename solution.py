import pandas as pd
import numpy as np


chat_id = 696934164 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    from statsmodels.stats.proportion import proportions_ztest


    alpha = 0.08
    counts = np.array([x_success, y_success])
    nobs = np.array([x_cnt, y_cnt])
    zstat, p_value = proportions_ztest(counts, nobs, alternative = 'smaller')
    answer = p_value < alpha 
    return answer

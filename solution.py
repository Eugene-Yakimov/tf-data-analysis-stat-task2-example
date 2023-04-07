import pandas as pd
import numpy as np

from scipy.stats import erlang

chat_id = 1412519104

def solution(p: float, x: np.array) -> tuple:
    alpha = 1 - p
    return 2*(x.mean() - erlang.ppf(alpha / 2, len(x), loc = 0, scale = 1 / len(x))) / 2209, \
           2*(x.mean() - erlang.ppf(1 - alpha / 2, len(x), loc = 0, scale = 1 / len(x))) / 2209

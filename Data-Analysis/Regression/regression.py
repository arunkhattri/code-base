import numpy as np
import statsmodels.formula.api as sfm

def backward_elimination(x, y, sl):
    '''
    :param x: array, independent variables
    :param y: target variable
    :param sl: significant level
    :return: array of optimised feature variables
    '''
    num_vars = len(x[0])
    for i in range(0, num_vars):
        result = sfm.OLS(y, x).fit()
        max_var = max(result.pvalues).astype(float)
        if max_var > sl:
            x = np.delete(x, np.argmax(result.pvalues), 1)
    result.summary()
    return x

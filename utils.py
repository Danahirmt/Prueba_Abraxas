import pandas as pd
import unidecode
import matplotlib.pyplot as plt
from collections import defaultdict
import numpy as np
import pandas as pd
import math
from sklearn.model_selection import train_test_split
from ml_metrics import rmsle
from subprocess import check_output
from sklearn.metrics import make_scorer, mean_squared_error
from sklearn.preprocessing import normalize
import xgboost as xgb

def remove_accents(a):
    '''
    Remover acentos
    
    return: string sin acentos
    '''
    return unidecode.unidecode(a.encode().decode('utf-8'))

def normalize(s):
    '''
    Limpieza de df clientes
    
    return: string limpio
    
    '''
    replacements = (
        ("   ", " "),
        ("  ", " ")

 
        
    )
    for a, b in replacements:
        s = s.replace(a, b)
    return s


def rmsle_func(truths, preds):
    '''
    Función de perdida personalizada, utilizando logaritmo
    
    return: perdida
    '''
    truths = np.asarray(truths)
    preds = np.asarray(preds)
    
    n = len(truths)
    diff = (np.log(preds+1) - np.log(truths+1))**2
    print(diff, n, np.sum(diff))
    return np.sqrt(np.sum(diff)/n)
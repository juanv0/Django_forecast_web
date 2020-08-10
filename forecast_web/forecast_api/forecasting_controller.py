from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np
import warnings
import itertools
import pandas as pd
from statsmodels.tsa.arima_model import ARIMA

from contextlib import contextmanager
import sys, os

def get_datos(ventas):
    Y = []
    X = []
    for i in range(2, len(ventas)):
        Y.append(float(ventas[i]['ganancia']))
        ganacia_anterior = float(ventas[i-1]['ganancia'])
        ganacia_anterior_2 = float(ventas[i-2]['ganancia'])
        diff =  float(ventas[i]['ganancia']) - ganacia_anterior
        diff2 = float(ventas[i-1]['ganancia']) - ganacia_anterior_2
        X.append([ganacia_anterior, diff, diff2])
    return X,Y

def get_forecast_xgboost(ventas):
    # Y = np.array([float(x['ganancia']) for x in ventas])
    # X = np.array([int(x['fecha']) for x in ventas])
    X,Y = get_datos(ventas)
    X = np.array(X)
    Y = np.array(Y)
    print(X)
    print(Y)
    seed=7
    test_size=0.20
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y,
        test_size=test_size, random_state=seed)
    model = XGBClassifier()
    print("x_traihn", X_train)
    print("y_traihn", Y_train)
    print("x_test", X_test)
    print("y_est", Y_test)
    model.fit(X_train, Y_train)
    Y_pred = model.predict(X_test)
    predictions = [value for value in Y_pred]
    print(predictions)
    accurancy = accuracy_score(Y_test, predictions)
    print("Accurancy: %.2f%%" %(accurancy*100.0))
    Y_I = Y[::-1]
    X_final = np.array([[Y_I[0],Y_I[0]-Y_I[1],Y_I[1]-Y_I[2]]])
    return (model.predict(X_final))

@contextmanager
def suppress_stdout():
    with open(os.devnull, "w") as devnull:

        old_stderr = sys.stderr
        sys.stderr = devnull

        try:
            yield
        finally:
            sys.stderr = old_stderr

def get_forecast_arima(ventas):
    # Count the arguments
    with suppress_stdout():
        X,Y = get_datos(ventas)
        X = np.array(X)
        Y = np.array(Y)

        table = {"valor": Y, "fecha": Y}
        data = pd.DataFrame(table)
        data.set_index("fecha", inplace=True)

        order = (3, 1, 0)
        model = ARIMA(data, order)
        model = model.fit()
        n = len(Y)
        result = model.predict(1, n)

    return(result[::-1][0])

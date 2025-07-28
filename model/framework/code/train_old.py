import os
import pandas as pd
import numpy as np
import lazyqsar as lq

import sys

folder = sys.argv[1]
dataset = sys.argv[2]


DATAPATH = "../data"
MODELPATH =  "../../checkpoints"

def fit_clf(X, y):
    model = lq.MorganBinaryClassifier(time_budget_sec = 1200, reduced= False, estimator_list = ["rf", "lgbm", "xgboost"]) 
    model.fit(X, y)
    return model


if __name__ == '__main__':
    train = pd.read_csv(os.path.join(DATAPATH, folder, "{}.csv".format(dataset)))
    mdl = fit_clf(train["st_smiles"], train["bin"])
    mdl.save(os.path.join(MODELPATH, folder, "{}_morgan.joblib".format(dataset)))
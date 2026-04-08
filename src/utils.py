import os
import pickle
import sys
import pandas as pd
import numpy as np
import dill
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV
from src.exception import CustomException
from src.logger import logging


def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, 'wb') as file_obj:
            dill.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)
    
def evaluate_models(X_train, y_train, X_test, y_test, models, params):
    try:
        report = {}

        for model_name, model in models.items():

            para = params.get(model_name, {})  # 🔥 SAFE

            from sklearn.model_selection import GridSearchCV

            if para:
                gs = GridSearchCV(model, para, cv=3)
                gs.fit(X_train, y_train)

                model.set_params(**gs.best_params_)

            model.fit(X_train, y_train)

            y_test_pred = model.predict(X_test)

            from sklearn.metrics import r2_score

            test_model_score = r2_score(y_test, y_test_pred)

            report[model_name] = test_model_score

        return report

    except Exception as e:
        raise CustomException(e, sys)
def load_object(file_path):
    try:
        print(f"Loading file: {file_path}")

        with open(file_path, "rb") as file_obj:
            obj = pickle.load(file_obj)

        print(f"Loaded successfully: {file_path}")

        return obj

    except Exception as e:
        print("ERROR WHILE LOADING:", e)
        raise CustomException(e, sys)
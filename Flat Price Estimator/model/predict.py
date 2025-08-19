import pickle
import pandas as pd

# loading the ml model
with open('model/flats_xgb.pkl', 'rb') as f:
    model = pickle.load(f)

def predict_output(user_input:dict):
    df = pd.DataFrame([user_input])

    # get the prediction
    prediction = model.predict(df)[0]

    return prediction
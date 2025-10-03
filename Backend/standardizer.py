import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OneHotEncoder
import joblib

# Load your model

def Standardizer(data):

    stdscaler = joblib.load("model/scaler.pkl")
    ohe = joblib.load("model/encoder.pkl")



    num_columns = data.select_dtypes(include=['int64', 'float64']).columns
    # Transform numeric columns using the already fitted scaler
    data[num_columns] = stdscaler.transform(data[num_columns])


   # Select categorical columns from data
    cat_columns = data.select_dtypes(include=['object']).columns

    # Transform using the already-fitted encoder
    x_encoded_array = ohe.transform(data[cat_columns])
    x_encoded_cols = ohe.get_feature_names_out(cat_columns)

    # Create a DataFrame for the encoded columns
    x_encoded_df = pd.DataFrame(x_encoded_array, columns=x_encoded_cols, index=data.index)

    # Combine numeric columns with the encoded categorical columns
    data_final = pd.concat([data.drop(cat_columns, axis=1), x_encoded_df], axis=1)

    res = data_final.values
    return res

'''# 1. Scale numeric columns
stdscaler = StandardScaler()
num_columns = data.select_dtypes(include=['int64', 'float64']).columns
data[num_columns] = stdscaler.fit_transform(data[num_columns])

# 2. Encode categorical columns
cat_columns = data.select_dtypes(include=['object']).columns
ohe = OneHotEncoder(sparse_output=False)
ohe_encoded_array = ohe.fit_transform(data[cat_columns])
ohe_encoded_cols = ohe.get_feature_names_out(cat_columns)
ohe_encoded_data = pd.DataFrame(ohe_encoded_array, columns=ohe_encoded_cols, index=data.index)

# 3. Combine back into one DataFrame
processed_data = pd.concat([data[num_columns], ohe_encoded_data], axis=1)
'''


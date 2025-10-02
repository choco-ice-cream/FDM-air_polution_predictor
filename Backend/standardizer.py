import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OneHotEncoder



def Standardizer(incomming):

    data = pd.DataFrame([incomming])

    stdscaler = StandardScaler()

   # 1. Scale numeric columns
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
    res = []
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


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures

df = pd.read_csv('../data/RFID_DATA_SET_v1.csv')
# print(df.head(15))
# print(df.dtypes)

df.fillna(0)

df2 = df
X = df2.drop('RSSI_DEC', axis=1)
X = X.iloc[0::].values
y = df2['RSSI_DEC'].values

# print(X)
# print(y)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=66)
poly = PolynomialFeatures(degree=2)
x_poly = poly.fit_transform(X_train)
poly.fit(X_train, y_train)

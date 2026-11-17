import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
data = pd.read_csv("/home/avcoe/Housing.csv")
print("Dataset loaded successfully")
print("\nDataset Shape:")
print(data.shape)
print("\nFirst 5 Rows:")
print(data.head())
print("\nMissing Values:")
print(data.isnull().sum())
# 2. Define Target Column
TARGET_COLUMN = "price"
X = data.drop(columns=[TARGET_COLUMN])
y = data[TARGET_COLUMN]
# 3. Identify Columns
numeric = X.select_dtypes(include=["number"]).columns
categorical = X.select_dtypes(include=["object", "category"]).columns
# 4. Handle Missing Values
X[numeric] = X[numeric].fillna(X[numeric].median())
for col in categorical:
    X[col] = X[col].fillna(X[col].mode()[0])
# 5. Convert Categorical Data
X = pd.get_dummies(X, columns=categorical, dtype=int)
print("\nFeatures After Encoding:")
print(X.shape)
# 6. Split Dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42
)
print("\nTraining Samples:", len(X_train))
print("Testing Samples:", len(X_test))
# 7. Linear Regression
model = LinearRegression()
model.fit(X_train, y_train)
# 8. Prediction
predictions = model.predict(X_test)
# 9. Evaluation
mse = mean_squared_error(y_test, predictions)
mae = mean_absolute_error(y_test, predictions)
r2 = r2_score(y_test, predictions)
print("\nLINEAR REGRESSION RESULTS")
print("MSE:", round(mse, 4))
print("MAE:", round(mae, 4))
print("R2 Score:", round(r2, 4))
# 10. Sample Predictions
results = pd.DataFrame({
    "Actual Price": y_test.values[:10],
    "Predicted Price": predictions[:10]
})
print("\nSAMPLE PREDICTIONS")
print(results.to_string(index=False))

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
data = pd.read_csv("/home/avcoe/Housing.csv")
print("Dataset loaded successfully")
print("\nDataset Shape:")
print(data.shape)
print("\nFirst 5 Rows:")
print(data.head())
print("\nColumn Names:")
print(data.columns.tolist())
print("\nData Types:")
print(data.dtypes)
print("\nMissing Values:")
print(data.isnull().sum())
TARGET_COLUMN = "price"
X = data.drop(columns=[TARGET_COLUMN])
y = data[TARGET_COLUMN]
print("\nInput Shape:", X.shape)
print("Target Shape:", y.shape)
numeric_columns = X.select_dtypes(include=["number"]).columns
categorical_columns = X.select_dtypes(include=["object", "category"]).columns
print("\nNumerical Columns:")
print(numeric_columns.tolist())
print("\nCategorical Columns:")
print(categorical_columns.tolist())
X[numeric_columns] = X[numeric_columns].fillna(X[numeric_columns].median())
for column in categorical_columns:
    X[column] = X[column].fillna(X[column].mode()[0])
X = pd.get_dummies(X, columns=categorical_columns, dtype=int)
print("\nColumns After Encoding:")
print(X.columns.tolist())
print("\nMissing Values After Preprocessing:")
print(X.isnull().sum().sum())
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42
)
print("\nTraining Samples:", len(X_train))
print("Testing Samples:", len(X_test))
print("Number of Features:", X.shape[1])
linear_model = LinearRegression()
linear_model.fit(X_train, y_train)
linear_predictions = linear_model.predict(X_test)
linear_mse = mean_squared_error(y_test, linear_predictions)
linear_mae = mean_absolute_error(y_test, linear_predictions)
linear_r2 = r2_score(y_test, linear_predictions)
print("\nLINEAR REGRESSION")
print("MSE:", round(linear_mse, 4))
print("MAE:", round(linear_mae, 4))
print("R2 Score:", round(linear_r2, 4))
polynomial_model = Pipeline([
    ("polynomial", PolynomialFeatures(degree=2, include_bias=False)),
    ("scaler", StandardScaler()),
    ("linear", LinearRegression())
])
polynomial_model.fit(X_train, y_train)
polynomial_predictions = polynomial_model.predict(X_test)
polynomial_mse = mean_squared_error(y_test, polynomial_predictions)
polynomial_mae = mean_absolute_error(y_test, polynomial_predictions)
polynomial_r2 = r2_score(y_test, polynomial_predictions)
print("\nPOLYNOMIAL REGRESSION")
print("MSE:", round(polynomial_mse, 4))
print("MAE:", round(polynomial_mae, 4))
print("R2 Score:", round(polynomial_r2, 4))
results = pd.DataFrame({
    "Actual Price": y_test.values[:10],
    "Linear Prediction": linear_predictions[:10],
    "Polynomial Prediction": polynomial_predictions[:10]
})
print("\nSAMPLE PREDICTIONS")
print(results.to_string(index=False))
comparison = pd.DataFrame({
    "Model": ["Linear Regression", "Polynomial Regression"],
    "MSE": [linear_mse, polynomial_mse],
    "MAE": [linear_mae, polynomial_mae],
    "R2": [linear_r2, polynomial_r2]
})
print("\nMODEL COMPARISON")
print(comparison.to_string(index=False))

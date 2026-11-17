import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
df = pd.read_csv("Admission_Predict.csv")
print(df.head())
print(df.info())
print(df.describe())
print("\nMissing Values:")
print(df.isnull().sum())
corr = df.corr(numeric_only=True)
plt.figure(figsize=(10, 8))
sns.heatmap(corr, annot=True, cmap="YlGnBu", fmt=".2f")
plt.title("Correlation Heatmap")
plt.show()
X = df.drop("target", axis=1)
y = df["target"]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
knn_clf = KNeighborsClassifier(n_neighbors=5)
knn_clf.fit(X_train, y_train)
train_pred = knn_clf.predict(X_train)
print("\nKNN - TRAIN RESULT")
print("Accuracy:",
      accuracy_score(y_train, train_pred) * 100)
print("Classification Report:")
print(classification_report(y_train, train_pred))
print("Confusion Matrix:")
print(confusion_matrix(y_train, train_pred))
test_pred = knn_clf.predict(X_test)
print("\nKNN - TEST RESULT")
print("Accuracy:",
      accuracy_score(y_test, test_pred) * 100)
print("Classification Report:")
print(classification_report(y_test, test_pred))
print("Confusion Matrix:")
print(confusion_matrix(y_test, test_pred))
train_score = accuracy_score(y_train, train_pred) * 100
test_score = accuracy_score(y_test, test_pred) * 100
results_df = pd.DataFrame(
    [["K-Nearest Neighbors", train_score, test_score]],
    columns=['Model', 'Training Accuracy %', 'Testing Accuracy %']
)
print("\nFINAL RESULT")
print(results_df)

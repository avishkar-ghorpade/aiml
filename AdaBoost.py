import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import AdaBoostClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
data = pd.read_csv("wdbc.csv")
X = data.drop(columns=["target"])
y = data["target"]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)
model = AdaBoostClassifier(random_state=42)
model.fit(X_train, y_train)
pred_before = model.predict(X_test)
print("Accuracy Before Tuning:",
      accuracy_score(y_test, pred_before) * 100)
params = {
    "n_estimators": [50, 100],
    "learning_rate": [0.5, 1.0]
}
grid = GridSearchCV(model, params, cv=5, scoring="accuracy")
grid.fit(X_train, y_train)
best_model = grid.best_estimator_
pred = best_model.predict(X_test)
print("\nADABOOST RESULTS")
print("Best Parameters:", grid.best_params_)
print("Accuracy:", accuracy_score(y_test, pred) * 100)
print("Precision:", precision_score(y_test, pred, average="weighted"))
print("Recall:", recall_score(y_test, pred, average="weighted"))
print("F1 Score:", f1_score(y_test, pred, average="weighted"))

# Project
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import LinearRegression
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score

# ============================================================================
# Split the data into training and test set in the ratio of 70:30 respectively
# ============================================================================
bank_data = pd.read_csv("Bank_Personal_Loan_Modelling-1.csv")
bank_head = bank_data.head()
print(bank_head)
loan_data = list(bank_data["Personal Loan"])
train = bank_data.drop(["ID", "Personal Loan"], axis=1)
test = bank_data['Personal Loan']
X_train, X_test, y_train, y_test = train_test_split(train, test, test_size=0.3, random_state=1)
print("\nX_train:\n")
print(X_train.head())
print(X_train.shape)

print("\nX_test:\n")
print(X_test.head())
print(X_test.shape)

# =================================================================
# Use different classification models (Logistic, Linear) to predict
# the likelihood of a liability customer buying personal loans
# =================================================================

print("\nNull Columns\n")
null_data = bank_data.isnull().sum()
print(null_data)

print("\nLINEAR REGRESSION MODEL:")
print("========================\n")

linear_model = LinearRegression()
# Fit the model to our X and y training sets
linear_model.fit(X_train, y_train)
linear_prediction = linear_model.predict(X_test)
linear_score = linear_model.score(X_test, y_test)
print("Linear Prediction :\n")
print(linear_prediction)
print("Linear Accuracy Score")
print("=====================")
print(linear_score)



print("\n\nLOGISTIC REGRESSION MODEL:")
print("==========================\n")

log_model = LogisticRegression(max_iter=5000)
# Fit the model to our X and y training sets
log_model.fit(X_train, y_train)
logistic_prediction = log_model.predict(X_test)
logistic_score = log_model.score(X_test, y_test)
print("Logistic Prediction :\n")
print(logistic_prediction)
print("\nLogistic Score :\n")
print(logistic_score)

report = classification_report(y_test, logistic_prediction)
print("Logistic Classification Report")
print("==============================")
print(report)


accuracy_score = accuracy_score(y_test, logistic_prediction)
print("Logistic Accuracy Score")
print("======================")
print(accuracy_score)


confusion_matrix = confusion_matrix(y_test, logistic_prediction)
print("Logistic Confusion Matrix")
print("=========================\n")
print(confusion_matrix)


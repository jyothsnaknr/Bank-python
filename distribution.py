# Project - Visualisation

import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

# ======================================================================
# Read the column description
# ======================================================================
bank_data = pd.read_csv("Bank_Personal_Loan_Modelling-1.csv")
print("Table Columns")
print("=============")
columns = bank_data.columns
print(columns)
print("Column Shape")
print("============")
shape = bank_data.shape
print(shape)
print("Column Description")
print("==================")
description = bank_data.describe()
print(description)

# ======================================================================
# Study the data distribution in each attribute, share your findings
# ======================================================================
bank_head = bank_data.head()
# Get first 5 table data
print(bank_head)
age_list = list(bank_data["Age"])
exp_list = list(bank_data["Experience"])
inc_list = list(bank_data["Income"])
zip_list = list(bank_data["ZIP Code"])
fam_list = list(bank_data["Family"])
avg_list = list(bank_data["CCAvg"])
edu_list = list(bank_data["Education"])
mor_list = list(bank_data["Mortgage"])
per_list = list(bank_data["Personal Loan"])
sec_list = list(bank_data["Securities Account"])
cd_list = list(bank_data["CD Account"])
net_list = list(bank_data["Online"])
card_list = list(bank_data["CreditCard"])


# 1. Age - Histogram
plt.hist(age_list, bins=20)
plt.grid(True)
plt.xlabel("Age")
plt.show()
# sns.countplot(x="Personal Loan", y="Age", data=bank_data)

# 2. Experience - Histogram
plt.hist(exp_list, bins=20)
plt.grid(True)
plt.xlabel("Experience")
plt.show()

# 3. Income - Histogram
plt.hist(inc_list, bins=20)
plt.grid(True)
plt.xlabel("Income")
plt.show()
# income vs personal loan
sns.boxplot(x="Personal Loan", y="Income", data=bank_data)
plt.show()

# 4. ZIP Code - Histogram
plt.hist(zip_list, bins=20)
plt.grid(True)
plt.xlabel("Zip Code")
plt.show()

# 5. Family - Histogram
plt.hist(fam_list, bins=20)
plt.grid(True)
plt.xlabel("Family")
plt.show()
# income vs personal loan
sns.boxplot(x="Personal Loan", y="Family", data=bank_data)
plt.show()

# 6. CCAvg - Histogram
plt.hist(avg_list, bins=20)
plt.grid(True)
plt.xlabel("CCAvg")
plt.show()

# 7. Education - Histogram
plt.hist(edu_list, bins=20)
plt.grid(True)
plt.xlabel("Education")
plt.show()
sns.countplot(x="Personal Loan", hue="Education", data=bank_data)

# 8. Mortgage - Histogram
plt.hist(mor_list, bins=20)
plt.grid(True)
plt.xlabel("Mortgage")
plt.show()

# 9. Personal Loan - Histogram
plt.hist(per_list, bins=20)
plt.grid(True)
plt.xlabel("Personal Loan")
plt.show()

# 10. Securities Account - Histogram
plt.hist(sec_list, bins=20)
plt.grid(True)
plt.xlabel("Securities Account")
plt.show()

# 11. CD Account - Histogram
plt.hist(cd_list, bins=20)
plt.grid(True)
plt.xlabel("CD Account")
plt.show()

# 12. Online - Histogram
plt.hist(net_list, bins=20)
plt.grid(True)
plt.xlabel("Online")
plt.show()
# online vs personal loan
sns.boxplot(x="Personal Loan", y="Family", data=bank_data)
plt.show()

# 13. CreditCard - Histogram
plt.hist(card_list, bins=20)
plt.grid(True)
plt.xlabel("CreditCard")
plt.show()

import pandas as pd
import numpy as np

# -----  Veri Hazırlama ve yükleme -------#
TRAINPATH = "database/mitbih_train.csv"
TESTPATH = "database/mitbih_test.csv"
Train = pd.read_csv(TRAINPATH, header=None)
Test = pd.read_csv(TESTPATH, header=None)
X_train = np.array(Train)[:, :187]
y_train = np.array(Train)[:, 187]

X_test = np.array(Test)[:, :187]

y_test = np.array(Test)[:, 187]

# -----  Model Hazırlama -------#

from sklearn.naive_bayes import CategoricalNB

nb = CategoricalNB()
nb.fit(X_train, y_train)  # öğrenmesi
y_pred = nb.predict(X_test)  # test eder

print(y_pred)
print(y_test)


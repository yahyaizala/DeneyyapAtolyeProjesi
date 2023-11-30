import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn import metrics
from sklearn.metrics import confusion_matrix
from sklearn.naive_bayes import CategoricalNB
import seaborn as sb

# -----  Veri Hazırlama ve yükleme -------#
TRAINPATH = "database/mitbih_train.csv"
TESTPATH = "database/mitbih_test.csv"
Train = pd.read_csv(TRAINPATH)
Test = pd.read_csv(TESTPATH)
# kaç adet kolon ve sütun var buradan görülebilir
print(Train.head())
X_train = np.array(Train)[:, :187]
y_train = np.array(Train)[:, 187]
X_test = np.array(Test)[:, :187]
y_test = np.array(Test)[:, 187]

# -----  Model Hazırlama -------#
nb = CategoricalNB()
nb.fit(X_train, y_train)  # öğrenmesi
y_pred = nb.predict(X_test)  # test eder

# ---- Modeli Görselleştirme --- #
conf = confusion_matrix(y_test, y_pred)
index_columns = ["No", "S", "V", "F", "Q"]
cm_df = pd.DataFrame(conf, index_columns, index_columns)
plt.figure(figsize=(10, 6))

sb.heatmap(cm_df, annot=True, fmt="d", cmap="YlGnBu")
plt.show()

accuracy = metrics.accuracy_score(y_test, y_pred)
print(f"EKG başarı değeri {accuracy}")

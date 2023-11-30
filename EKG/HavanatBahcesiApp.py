import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from sklearn import metrics
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import CategoricalNB
import seaborn as sb

PATH = "database/hayvanatbahcesi.csv"

doc = pd.read_csv(PATH, encoding="unicode_escape")
# print(doc)
X_data = np.array(doc.drop(["sinifi", "hayvan adi"], axis=1))
# print(X_data[0].shape)
Y_data = np.array(doc["sinifi"])
# print(Y_data.shape)

# --- train test split ----- #
X_train, X_test, y_train, y_test = train_test_split(X_data, Y_data, test_size=0.3, random_state=42)

nb = CategoricalNB()
nb.fit(X_train, y_train)

y_pred = nb.predict(X_test)

conf = confusion_matrix(y_test, y_pred)

index_columns = ["A", "B", "C", "D", "E", "F", "G"]
cm_df = pd.DataFrame(conf, index_columns, index_columns)
plt.figure(figsize=(10, 6))

sb.heatmap(cm_df, annot=True, fmt="d", cmap="YlGnBu")
plt.show()

accuracy = metrics.accuracy_score(y_test, y_pred)
print(f"EKG başarı değeri {accuracy}")

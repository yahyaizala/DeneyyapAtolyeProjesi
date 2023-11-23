from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

iris = load_iris()
# print(iris.feature_names)
# print(iris.target_names)
# print(iris.data)
# print(f"total element size is {len(iris.data)}")
# print(iris.target)
'''
X1=3
X2=4
x3=5
x4=6

y=f(x1,x2,x3,x4) 
--- x lere bilinmeyen 
--- sayılara   katsayı
x1*a1+x2*a2+x3*a3+x4*a4 = y1 0 (0) (%100)
         = y2  0.3 (1) %30
         = y3 10 (2)  %0
------- 100 ----
eğitim ---> 80 -- 70 -- 60
test   ---> 20 -- 30 -- 40

'''
X = iris.data
Y = iris.target
# 150 * 0.30 = 45 (test) 105 (train)
X_train, X_test, y_train, y_test = train_test_split(X,
                                                    Y,
                                                    test_size=.3,
                                                    random_state=42)
# decision tree - karar ağaçlar
model = DecisionTreeClassifier()

model.fit(X_train, y_train)
y_predict = model.predict(X_test)
print(f"predicted {y_predict}")
print(f"gerçek cevaplar {y_test}")
conf = confusion_matrix(y_test, y_predict)
print(conf)
index = ["setosa", "versicolor", "virginica"]
hata_goster = pd.DataFrame(conf, index, index)
print(hata_goster)
plt.figure(figsize=(10, 6))
sns.heatmap(hata_goster,annot=True)
plt.show()

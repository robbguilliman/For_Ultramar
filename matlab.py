from sklearn.datasets import load_iris
import pandas as pd

from sklearn.model_selection import train_test_split

from sklearn.tree import DecisionTreeClassifier

from sklearn.metrics import accuracy_score


# Förbered data

X = iris.drop('species', axis=1)  # Egenskaper

y = iris['species']  # Målvariabel


# Dela upp datan i tränings- och testuppsättningar

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# Skapa och träna beslutsträdmodellen

model = DecisionTreeClassifier()

model.fit(X_train, y_train)


# Gör prediktioner på testdata

predictions = model.predict(X_test)


# Utvärdera modellen

accuracy = accuracy_score(y_test, predictions)

print(f'Accuracy: {accuracy:.2f}')
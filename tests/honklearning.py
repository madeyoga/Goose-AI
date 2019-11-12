import numpy as np
import pandas as pd
import random
from sklearn.tree import DecisionTreeClassifier

behavior_df = pd.read_csv('dataset.csv')
# print(behavior_df.head())

X_train = behavior_df.iloc[:, :-1]
y_train = behavior_df.iloc[:, -1:]
# print(X_train, y_train)

model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# Perfect stat
hp = 100
stamina = 100
hot = 0
hunger = 100
hunter = 0

for i in range(20):
    test = [[hp, stamina, hot, hunger, hunter]]
    predicted = model.predict(test)
    print(hp, stamina, hot, hunger, hunter, predicted)

    stamina -= random.randint(1, 10)
    hot += random.randint(1, 10)
    hunger -= random.randint(1, 10)

while True:
    break
    

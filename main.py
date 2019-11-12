import pandas as pd
import random

from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn.externals.six import StringIO
import pydot

from game.goose import Goose
import pygame

# Load dataset
behavior_df = pd.read_csv('dataset.csv')

# Split to attributes & class
X_train = behavior_df.iloc[:, :-1]
y_train = behavior_df.iloc[:, -1:]

# Train decision tree model behavior
model = DecisionTreeClassifier(criterion='gini')
model.fit(X_train, y_train)

# Graphs Decision Tree Model
def save_dtree(model, feats, targs):
    dot_data = StringIO()
    export_graphviz(model,
                    out_file=dot_data,
                    feature_names=feats,
                    class_names=targs)
    graph = pydot.graph_from_dot_data(dot_data.getvalue())
    graph[0].write_pdf("Goose.pdf")
save_dtree(model, X_train.columns, model.classes_)

# Perfect stat
hp = 100
stamina = 100
hot = 0
hunger = 100
hunter = 1
chara = {
    'position': [500, 360],
    'maximum_speed': 5,
    'velocity': [0, 0],
    'orientation': [0, 0],
    'rotation': 0,
    'max_accel': 2.5
}

# Initial Goose
goose = Goose(chara, {}, hp=hp, stamina=stamina, hot=hot, hunger=hunger, hunter=hunter)
goose.set_model(model)

# To do Map
def rest():
    print('back to nest & rest. zzZZ...')
    return

def eat():
    print('Eat <3')
    return

def hide():
    print('RUN!!')
    return

def swim():
    print('swim-swim')
    return

def wander():
    print('wandering...')
    return

def honk():
    print('HONK! HONK! MDFKER!')
    return

def dead():
    print('What magic is tis...?')
    return

todo_map = {
    'rest': rest,
    'eat': eat,
    'hide': hide,
    'swim': swim,
    'wander': wander,
    'dead': dead,
    'honk': honk}

# Game Main Loop
while True:
    decision = goose.get_decision()[0]
    print(decision)
    todo_map[decision]()
    break

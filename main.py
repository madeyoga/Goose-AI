import pandas as pd
import random

from scipy.spatial import distance
from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn.externals.six import StringIO
import pydot

from game.goose import Goose
from game.obstacle import Obstacle, Pond
from pygai.core.utils import angle_from_vector, counter_clockwise, getvectorlen, degrees_as_vector
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
hunter = 0
chara = {
    'position': [500, 360],
    'maximum_speed': 10,
    'velocity': [1, 0],
    'orientation': [0, 0],
    'rotation': 0,
    'max_accel': 2.5
}

# Initial Goose
goose = Goose(chara, {}, hp=hp, stamina=stamina, hot=hot, hunger=hunger, hunter=hunter)
goose.set_model(model)
goose.set_image("assets/goose2.1.png", size=(100,100))

# Nests obstacle
nests = [
    Obstacle(post=pygame.Vector2(64, 720), image_path='assets/nest.png', size=(180, 100), walkable=True),
    Obstacle(post=pygame.Vector2(64, 640), image_path='assets/nest.png', size=(180, 100), walkable=True),
    Obstacle(post=pygame.Vector2(196, 680), image_path='assets/nest.png', size=(180, 100), walkable=True),
]

water = Pond(post=pygame.Vector2(1100, 0), image_path='assets/water1.jpg', size=(300, 768))

# Font 
pygame.font.init()
comic_sans_font = pygame.font.SysFont('Comic Sans MS', 30)

todo_text = "Wander"
todo_text_surface = comic_sans_font.render(todo_text, False, (0, 0, 0))

hp_surf = comic_sans_font.render("Hp {}".format(goose.hp), False, (0, 0, 0))
stamina_surf = comic_sans_font.render("Stamina {}".format(goose.stamina), False, (0, 0, 0))
hunger_surf = comic_sans_font.render("Hunger {}".format(goose.hunger), False, (0, 0, 0))
hot_surf = comic_sans_font.render("Hot {}".format(goose.hot), False, (0, 0, 0))
hunter_surf = comic_sans_font.render("Hunter {}".format(goose.hunter), False, (0, 0, 0))

# To do Map
def rest(win):

    goose.hot += 0.2

    goose.target['position'] = [128, 640]
    goose.arrive_totarget()
    goose.face_target()

    check_water()
    check_food()
    check_nest()
    
    global todo_text_surface
    todo_text_surface = comic_sans_font.render("Rest...", False, (0, 0, 0))
    print('back to nest & rest. zzZZ...')
    return

def eat(win):

    goose.hot += 1

    global todo_text_surface
    todo_text_surface = comic_sans_font.render("Eat..", False, (0, 0, 0))
    goose.target['position'] = pygame.Vector2(720, 360)
    goose.arrive_totarget()
    goose.face_target()

    check_water()
    check_food()
    check_nest()

    return

def hide(win):
    
    goose.stamina -= 1
    goose.hunger -= 1

    global todo_text_surface
    todo_text_surface = comic_sans_font.render("Hide!", False, (0, 0, 0))
    print('RUN!!')
    return

def swim(win):
    
    goose.stamina -= 1
    goose.hunger -= 1
    goose.hot += 0.2

    check_water()

    global todo_text_surface
    todo_text_surface = comic_sans_font.render("Swim.", False, (0, 0, 0))

    post = (goose.ai['position'][0] + goose.ai['velocity'][0], goose.ai['position'][1] + goose.ai['velocity'][1])
    honk_surf = comic_sans_font.render("HOT!", False, (0, 0, 0))
    win.blit(honk_surf, post)
    
    goose.target['position'] = (1250, 360)
    goose.arrive_totarget()
    goose.face_target()


    return

def wander(win):
    
    goose.stamina -= 0.5
    goose.hot += 0.5
    goose.hunger -= 0.5

    global todo_text_surface
    todo_text_surface = comic_sans_font.render("Wander~", False, (0, 0, 0))
    print('wandering...')
    
    goose.wander_around()
    goose.face_target()

    check_water()
    return

def honk(win):
    
    goose.stamina -= 0.5
    goose.hot += 1
    goose.hunger -= 1

    global todo_text_surface
    todo_text_surface = comic_sans_font.render("Honk!", False, (0, 0, 0))
    
    if not pygame.mixer.music.get_busy():
        pygame.mixer.music.load('sound/honk-sound-2.mp3')
        pygame.mixer.music.play()

    goose.wander_around()
    goose.face_target()

    check_water()

    return

def dead(win):
    global todo_text_surface
    todo_text_surface = comic_sans_font.render("Dead.", False, (0, 0, 0))
    print('What magic is tis...?')
    return

def check_water():
    if goose.ai['position'][0] > 1150:
        goose.hot -= 5
        return

def check_food():
    if distance.euclidean([720, 360], goose.ai['position']) < 30:
        goose.stamina += 3
        goose.hunger += 25
        goose.hp += 10

def check_nest():
    if distance.euclidean([128, 640], goose.ai['position']) < 60:
        goose.stamina += 25
        goose.hp += 10

def draw_environ():
        # Draw Current stat Text
    win.blit(todo_text_surface, (0, 0))

    # Draw obstacles
    for nest in nests:
        nest.draw(win)

    water.draw(win)

    # Draw status
    hp_surf = comic_sans_font.render("Hp {}".format(goose.hp), False, (0, 0, 0))
    win.blit(hp_surf, (0, 64))

    stamina_surf = comic_sans_font.render("Stamina {}".format(goose.stamina), False, (0, 0, 0))
    win.blit(stamina_surf, (0, 128))
    
    hunger_surf = comic_sans_font.render("Hunger {}".format(goose.hunger), False, (0, 0, 0))
    win.blit(hunger_surf, (0, 196))

    hot_surf = comic_sans_font.render("Hot {}".format(goose.hot), False, (0, 0, 0))
    win.blit(hot_surf, (0, 260))

    hunter_surf = comic_sans_font.render("Hunter {}".format(goose.hunter), False, (0, 0, 0))
    win.blit(hunter_surf, (0, 324))

todo_map = {
    'rest': rest,
    'eat': eat,
    'hide': hide,
    'swim': swim,
    'wander': wander,
    'dead': dead,
    'honk': honk}

# GAME
pygame.init()
win = pygame.display.set_mode((1366, 768))
pygame.display.set_caption("Goose")

# Game Main Loop
running = True
while running:
    pygame.time.delay(100)

    decision = goose.get_decision()[0]
    print(decision)

    # Event loop
    for event in pygame.event.get():
        # Quit input
        if event.type == pygame.QUIT:
            running = False

    todo_map[decision](win)

    # Increment/Decrement stat
    if goose.hunger < 15 or goose.hot >= 85 or goose.stamina <= 0:
        goose.hp -= 1

    # Clear
    win.fill((255, 255, 255))

    ##########
    ## DRAW ## 
    ##########
    draw_environ()

    if decision == 'honk':
        honk_surf = comic_sans_font.render("HOONK!", False, (0, 0, 0))
        post = (goose.ai['position'][0] + goose.ai['velocity'][0], goose.ai['position'][1] + goose.ai['velocity'][1])
        win.blit(honk_surf, post)
    elif decision == 'swim':
        post = (goose.ai['position'][0] + goose.ai['velocity'][0], goose.ai['position'][1] + goose.ai['velocity'][1])
        hot_surf = comic_sans_font.render("HOT!", False, (0, 0, 0))
        win.blit(hot_surf, post)

    goose.draw(win)

    # Update
    pygame.display.update()

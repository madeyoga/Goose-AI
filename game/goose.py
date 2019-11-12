from pygai.movement import Face, Wander, Arrive, ObstacleAvoidance
from pygai.core.utils import angle_from_vector, counter_clockwise, getvectorlen, degrees_as_vector
from pygai.core.utils import line_coefs, lines_intersect, lines_intersection, find_intersection
import math
import pygame

class Character:
    def __init__(self, character, target, obstacles=None, image='triangle.png'):
        self.surface = pygame.transform.scale(pygame.image.load(image), (20, 20))
        self.surface_to_draw = self.surface
        self.rect = self.surface_to_draw.get_rect()

        self.face = Face(character=character, target=target)
        self.wander = Wander(character, target)
        self.arrive = Arrive(character, target, stop_radius=15, slow_radius=30)
        
        self.ai = character
        self.target = target
        self.obstacles = obstacles

        self.avoidance = ObstacleAvoidance(character, obstacles, avoid_distance=20, lookahead=120)
        self.avoid_target = pygame.Vector2(0, 0)
    
    def set_image(self, filename, size=(20,20)):
        self.surface = pygame.transform.scale(pygame.image.load(filename), size)
        self.surface_to_draw = self.surface
        self.rect = self.surface_to_draw.get_rect()

    def set_obstacles(self, obstacles):
        self.obstacles = obstacles
        self.avoidance.obstacles = obstacles

    def rotate_image(self):
        angle = angle_from_vector(counter_clockwise(self.ai['orientation']))

        center = self.surface_to_draw.get_rect().center
        self.surface_to_draw = pygame.transform.rotate(self.surface, int(angle))
        self.rect.center = center

    def face_target(self):
        steering_dict, steering_obj = self.face.get_steering()
        self.steer(steering_obj)

        self.rotate_image()

    def arrive_totarget(self):
        steer_obj = self.arrive.get_steering()
        self.steer(steer_obj)

    def wander_around(self):
        steer_obj = self.wander.get_steering()
        self.steer(steer_obj)

        self.rotate_image()

    # def avoid_obstacles(self, win):
    #     steer_obj, intersection_point, new_target_position = self.avoidance.get_steering()
    #     if intersection_point is not None:
    #         print("new target", self.avoidance.seek.target['position'])
    #         pygame.draw.circle(win, (255, 0, 0), [int(self.avoidance.seek.target['position'][0]), int(self.avoidance.seek.target['position'][1])], int(5))
    #         self.target['position'] = new_target_position
            
    #         ## Update current arrive target position
    #         self.arrive.target['position'] = new_target_position
    #         self.avoid_target = new_target_position

    #         self.steer(steer_obj)
    #     return intersection_point

    def draw(self, win):
        post = (self.ai['position'][0], self.ai['position'][1])
        self.rect = self.rect.move((post[0], post[1]))
        self.rect.center = (post[0], post[1])
        
        win.blit(self.surface_to_draw, self.rect)

    def steer(self, steering, time=1):
        """Dynamic Steering, Update AI Function"""

        speed = [self.ai['velocity'][index] * time for index in range(len(self.ai['velocity'])) ]

        self.ai['position'] = [ self.ai['position'][index] + speed[index] for index in range(len(self.ai['position'])) ]

        rotation = self.ai['rotation'] * time
        # orientation in degrees
        orientation = angle_from_vector(self.ai['orientation'])
        orientation += rotation
        self.ai['orientation'] = degrees_as_vector(orientation)

        self.ai['velocity'] = [self.ai['velocity'][index] + steering.linear[index] * time for index in range(len(self.ai['velocity']))]

        self.ai['rotation'] += steering.angular * time

        vector_len = getvectorlen(self.ai['velocity'])
        if vector_len > self.ai['maximum_speed']:
            value = sum([self.ai['velocity'][index] ** 2 for index in range(len(self.ai['velocity']))])
            abs_v = math.sqrt(abs(value))
            self.ai['velocity'] = [(self.ai['velocity'][index] / abs_v) * self.ai['maximum_speed'] for index in range(len(self.ai['velocity']))]
        return

class Goose(Character):
    """
    Object Represents goose
    """
    
    def __init__(self, character, target, hp=100, stamina=100, hot=0, hunger=100, hunter=0, model=None):
        super().__init__(character=character, target=target)
        self.hp = hp
        self.stamina = stamina
        self.hot = hot
        self.hunger = hunger
        self.hunter = hunter
        self.model = model
        self.face = Face(character=self.ai, target=self.target)
        self.arrive = Arrive(character=self.ai, target=self.target)

    def set_target(self, target):
        self.target = target

    def set_model(self, model):
        self.model = model
    
    def train(self, X_train, y_train):
        self.model.fit(X_train, y_train)
        return self.model

    def get_decision(self):
        return self.model.predict([[self.hp, self.stamina, self.hot, self.hunger, self.hunter]])

    

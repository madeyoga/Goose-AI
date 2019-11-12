import time
import random

hp = 50
stamina = 100
hot = 0
hunger = 100
rand = 0

while(True):
    print("honk machine is wandering..")
    hunger = hunger - 10
    hot = hot + 10
    stamina = stamina - 10
    time.sleep(2)
    rand = random.randint(0,5)
    if rand == 0:
        print("honk honk")
        print("hp = "+str(hp))
        print("stamina = "+str(stamina))
        print("hunger = "+str(hunger))
        print("hot = "+str(hot))
        time.sleep(2)
        continue
    elif rand == 1:
        print("found another honk machine")
        time.sleep(2)
        rand = random.randint(0,1)
        if rand == 0:
            print("happily honking")
            time.sleep(2)
            continue
        else:
            print("honk rejected")
            time.sleep(2)
            continue
    elif rand == 3:
        print("searching for food..")
        print("hp = "+str(hp))
        print("stamina = "+str(stamina))
        print("hunger = "+str(hunger))
        print("hot = "+str(hot))
        time.sleep(2)
        while(True):
            rand = random.randint(0,1)
            if rand == 0:
               hunger = hunger - 10
               hot = hot + 10
               stamina = stamina - 10
               print("still searching for food..")
               print("hp = "+str(hp))
               print("stamina = "+str(stamina))
               print("hunger = "+str(hunger))
               print("hot = "+str(hot))
               time.sleep(2)
               continue
            elif rand == 1:
                print("found food!")
                hunger = hunger + 10
                hp = hp + 10
                print("hp = "+str(hp))
                print("stamina = "+str(stamina))
                print("hunger = "+str(hunger))
                print("hot = "+str(hot))
                time.sleep(2)
                if hunger < 30:
                    continue
                else:
                    break
                if hot > 50:
                    print("searching for pond..")
                    print("hp = "+str(hp))
                    print("stamina = "+str(stamina))
                    print("hunger = "+str(hunger))
                    print("hot = "+str(hot))
                    time.sleep(2)
                    while(True):
                        rand = random.randint(0,1)
                        if rand == 0:
                            hunger = hunger - 10
                            hot = hot + 10
                            stamina = stamina - 10
                            print("still searching for pond..")
                            print("hp = "+str(hp))
                            print("stamina = "+str(stamina))
                            print("hunger = "+str(hunger))
                            print("hot = "+str(hot))
                            time.sleep(2)
                            continue
                        elif rand == 1:
                            print("found pond!")
                            while(True):
                                hot = hot - 10
                                if hot > 50:
                                    continue
                                else:
                                    rand = random.randint(0,1)
                                    if rand == 0:
                                        continue
                                    elif rand == 1:
                                        break
                if stamina < 30:
                    print("honk machine is resting..")
                    stamina = stamina + 20
                    hp = hp + 10
                    print("hp = "+str(hp))
                    print("stamina = "+str(stamina))
                    print("hunger = "+str(hunger))
                    print("hot = "+str(hot))
                    time.sleep(2)
                continue
    elif rand == 4:
        print("searching for pond..")
        print("hp = "+str(hp))
        print("stamina = "+str(stamina))
        print("hunger = "+str(hunger))
        print("hot = "+str(hot))
        time.sleep(2)
        while(True):
            rand = random.randint(0,1)
            if rand == 0:
                hunger = hunger - 10
                hot = hot + 10
                stamina = stamina - 10
                print("still searching for pond..")
                print("hp = "+str(hp))
                print("stamina = "+str(stamina))
                print("hunger = "+str(hunger))
                print("hot = "+str(hot))
                time.sleep(2)
                continue
            elif rand == 1:
                print("found pond!")
                while(True):
                    hot = hot + 1
                    if hot > 50:
                        continue
                    else:
                        rand = random.randint(0,1)
                        if rand == 0:
                            time.sleep(2)
                            continue
                        elif rand == 1:
                            time.sleep(2)
                            if hunger < 30:
                                print("searching for food..")
                                print("hp = "+str(hp))
                                print("stamina = "+str(stamina))
                                print("hunger = "+str(hunger))
                                print("hot = "+str(hot))
                                time.sleep(2)
                                while(True):
                                    rand = random.randint(0,1)
                                    if rand == 0:
                                       hunger = hunger - 10
                                       hot = hot + 10
                                       stamina = stamina - 10
                                       print("still searching for food..")
                                       print("hp = "+str(hp))
                                       print("stamina = "+str(stamina))
                                       print("hunger = "+str(hunger))
                                       print("hot = "+str(hot))
                                       time.sleep(2)
                                       continue
                                    elif rand == 1:
                                        print("found food!")
                                        hunger = hunger + 10
                                        hp = hp + 10
                                        print("hp = "+str(hp))
                                        print("stamina = "+str(stamina))
                                        print("hunger = "+str(hunger))
                                        print("hot = "+str(hot))
                                        time.sleep(2)
                                        if hunger < 30:
                                            continue
                                        else:
                                            break
                            if stamina < 30:
                                print("honk machine is resting..")
                                stamina = stamina + 20
                                hp = hp + 10
                                print("hp = "+str(hp))
                                print("stamina = "+str(stamina))
                                print("hunger = "+str(hunger))
                                print("hot = "+str(hot))
                                time.sleep(2)
                            break
    elif rand == 5:
        print("hunter spotted!!,honk machine is fleeing")
        while(True):
            rand = random.randint(0,1)
            if rand == 0:
                print("honk machine got shot!")
                hp = hp - 25
                print("hp = "+str(hp))
                print("stamina = "+str(stamina))
                print("hunger = "+str(hunger))
                print("hot = "+str(hot))
                if hp <= 0:
                    print("honk machine died, but alas another one respawned")
                    break
                time.sleep(2)
                rand = random.randint(0,1)
                if rand == 0:
                    print("hunter gave up!")
                    time.sleep(2)
                    break
                elif rand == 1:
                    print("hunter haven't gave up!")
                    time.sleep(2)
                    continue
    elif hunger < 30:
        print("searching for food..")
        print("hp = "+str(hp))
        print("stamina = "+str(stamina))
        print("hunger = "+str(hunger))
        print("hot = "+str(hot))
        time.sleep(2)
        while(True):
            rand = random.randint(0,1)
            if rand == 0:
               hunger = hunger - 10
               hot = hot + 10
               stamina = stamina - 10
               print("still searching for food..")
               print("hp = "+str(hp))
               print("stamina = "+str(stamina))
               print("hunger = "+str(hunger))
               print("hot = "+str(hot))
               time.sleep(2)
               continue
            elif rand == 1:
                print("found food!")
                hunger = hunger + 10
                hp = hp + 10
                print("hp = "+str(hp))
                print("stamina = "+str(stamina))
                print("hunger = "+str(hunger))
                print("hot = "+str(hot))
                time.sleep(2)
                if hunger < 30:
                    continue
                else:
                    break
    elif hot > 50:
        print("searching for pond..")
        print("hp = "+str(hp))
        print("stamina = "+str(stamina))
        print("hunger = "+str(hunger))
        print("hot = "+str(hot))
        time.sleep(2)
        while(True):
            rand = random.randint(0,1)
            if rand == 0:
                hunger = hunger - 10
                hot = hot + 10
                stamina = stamina - 10
                print("still searching for pond..")
                print("hp = "+str(hp))
                print("stamina = "+str(stamina))
                print("hunger = "+str(hunger))
                print("hot = "+str(hot))
                time.sleep(2)
                continue
            elif rand == 1:
                print("found pond!")
                while(True):
                    hot = hot - 10
                    if hot > 50:
                        continue
                    else:
                        rand = random.randint(0,1)
                        if rand == 0:
                            continue
                        elif rand == 1:
                            break
    elif stamina < 30:
        print("honk machine is resting..")
        stamina = stamina + 20
        hp = hp + 10
        print("hp = "+str(hp))
        print("stamina = "+str(stamina))
        print("hunger = "+str(hunger))
        print("hot = "+str(hot))
        time.sleep(2)
        continue
        
               

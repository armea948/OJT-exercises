import datetime
import time

mainStr = "Now is the time for all good men to come to the aid of their country."
user_input = ""
username = ""
users = []
rate = 0.0

def promptgame(answr):
    x = 0
    start_game = False
    answr = answr.lower()
    while (x == 0):
        if (answr == 'y'):
            start_game = True
            x = 1
        elif(answr == 'n'):
            start_game = False
            x = 1
        else:
            answr = raw_input('Play? [Y/N]: ').lower()
            x = 0
    return start_game

def keyrate(total_sec):
    l = float(len(user_input))
    #print ("l", l)
    ts = float(total_sec)
    #print ("ts", ts)
    time_rate = l / ts
    #print ("RATE: ", time_rate)
    return time_rate

def accuracy():
    global user_input
    no_of_letters = len(mainStr)
    len_user = len(user_input)
    len_use = 0
    if(no_of_letters >= len_user):
        mistakes = no_of_letters - len_user
        len_use = len_user
    else:
        mistakes = len_user - no_of_letters
        len_use = no_of_letters


    for i in range (len_use-1):
        if(mainStr[i] == user_input[i]):
            continue
        else:
            mistakes = mistakes + 1

    if(mistakes == 0):
        accuracyRate = 100
    else:
        mis = float(mistakes)
        nol = float(no_of_letters)
        accyRate = mis / nol
        #print (accyRate)
        accyRate = accyRate * 100
        #print (accyRate)
        accuracyRate = 100 - accyRate
        #print(accuracyRate)

    return accuracyRate


def total_seconds(total_time):
    global users
    global rate
    lists = total_time.split(':')
    seconds = int(lists[2])
    minutes = (int(lists[1])) * 60
    #hours = (int(list[0])) *3600

    total_sec = seconds + minutes #+ hours
    rate = keyrate(total_sec)
    accRate = accuracy()
    users.append({'Field Name':username, 'Percentage':accRate, 'Rate':rate})


def gameproper():
    global user_input
    print mainStr + '\n'
    start_time = time.time()
    user_input = raw_input("Retype: ")
    end_time = time.time()
    total_time = end_time - start_time
    total_time = str(datetime.timedelta(seconds=int(total_time)))
    total_seconds(total_time)
    starthere()

def topTen(option):
    if(len(users) != 0):
        top = []
        all_list = []
        name_list = []
        for i in range(len(users)):
            all_list.append(users[i].get(option))

        all_list.sort()
        all_list.reverse()

        if(len(users) < 10):
            r = len(users)
        else:
            r = 10

        for x in range (r):
            top.append(all_list[x])

        var = option.upper()
        var_str = "=====TOP 10 USERS WITH HIGHEST " + var +"===="
        print(var_str)
        for a in range(r):
            tp = top[a]
            for b in range(len(users)):
                p = users[b].get(option)
                if (tp == p):
                    name = users[b].get('Field Name')
                    if name in name_list:
                        continue
                    name_list.append(name)

        for c in range(r):
            v = c +1
            s = "#%d     " %v
            s = s + str(top[c]) + "                " + str(name_list[c])
            print (s)
    else:
        print("=====TOP 10 USERS WITH HIGHEST PERCENTAGE====")
        print("=================NO USERS YET=================")

    which()

def which():
    print("Which Top 10 would you like to view?")
    print("[1] Percentage")
    print("[2] Rate")
    print("[other] Exit")
    choice = raw_input("Answer: ")
    if (choice == '1'):
        topTen('Percentage')
    elif(choice == '2'):
        topTen('Rate')

def starthere():
    global username
    game = ""
    username = raw_input('Enter user: ')
    if username:
        game = raw_input("Play? (Y/N): ")
        yesorno = promptgame(game)
        if(yesorno):
            for x in range(len(users)):
                name = users[x].get('Field Name')
                if(name == username):
                    users.pop(x)
                    break
            gameproper()

    else:
        which()


starthere()






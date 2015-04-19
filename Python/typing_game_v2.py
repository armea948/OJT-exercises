import datetime
import time
import random
import ast

mainStr = ""
user_input = ""
username = ""
rate = 0.0

def promptgame(answr):
    '''This checks whether or not the user wants to start the game'''
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
    '''This calculates the number of key per minute'''
    l = float(len(user_input))
    ts = float(total_sec)
    time_rate = (l / ts)
    return time_rate

def accuracy():
    '''This calculates the user accuracy or percentage'''
    global user_input
    mistakes = 0
    no_of_letters = (len(mainStr)) -1
    len_user = len(user_input)
    len_use = 0
    if(no_of_letters >= len_user):
        mistakes = no_of_letters - len_user
        len_use = len_user
    else:
        mistakes = len_user - no_of_letters
        len_use = no_of_letters


    for i in range (len_use):
        if(mainStr[i] == user_input[i]):
            continue
        else:
            mistakes = mistakes + 1

    print "mistakes: %d" %mistakes
    if(mistakes == 0):
        accuracyRate = 100
    else:
        mis = float(mistakes)
        nol = float(no_of_letters)
        accyRate = mis / nol
        accyRate = accyRate * 100
        accuracyRate = 100 - accyRate

    return accuracyRate

def userRecord(username, percentage, rate, final_score):
    '''Records user and game details in score.txt'''
    f = open('score.txt', 'a')
    f.write("{'Field Name':'%s'" % username)
    f.write(", 'Percentage':%.2f" % percentage)
    f.write(", 'Rate':%.2f" % rate)
    f.write(", 'Final Score':%.2f" % final_score)
    f.write("}\n")
    f.close()

def total_seconds(total_time):
    '''This calculates the time the user spent in typing'''
    global rate
    lists = total_time.split(':')
    seconds = float(lists[2])
    minutes = (int(lists[1])) * 60

    total_sec = seconds + minutes #+ hours
    rate = keyrate(total_sec)
    accRate = accuracy()
    final_score = accRate *rate
    fn = "Field Name: %s ;" %username
    per = " Percentage: %.2f ; " %accRate
    r = "Rate: %.2f ;" %rate
    final = "Final Score: %.2f" %final_score
    s = fn + per + r + final
    print s

    userRecord(username, accRate, rate, final_score)

def getWord():
    '''This returns the random word in words.txt'''
    f = open('words.txt', 'r')
    lists = f.readlines()
    no_of_lines = len(lists)
    index = random.randrange(0,no_of_lines)
    f.close()
    return lists[index]

def gameproper():
    '''This starts the game'''
    global user_input
    global mainStr
    mainStr = getWord()
    print mainStr + '\n'
    start_time = time.time()
    user_input = raw_input("Retype: ")
    end_time = time.time()
    total_time = end_time - start_time
    total_time = str(datetime.timedelta(seconds=total_time))
    total_seconds(total_time)
    starthere()

def topTen():
    '''This shows the top 10 list'''
    users_data = []

    f = open('score.txt', 'r')
    users = f.readlines()
    f.close()

    if(len(users) != 0):
        for j in range (len(users)):
            x = ast.literal_eval(users[j])
            users_data.append(x)

        top = []            #lists of the top 10 final scores only
        all_list = []       #lists of all Final scores only
        name_list = []      #lists of users in the top 10
        for i in range(len(users_data)):
            all_list.append(users_data[i].get('Final Score'))

        all_list.sort()
        all_list.reverse()

        if(len(users_data) < 10):
            r = len(users_data)
        else:
            r = 10

        for x in range (r):
            top.append(all_list[x])

        print "=====TOP 10 USERS WITH HIGHEST SCORES OF ALL TIME===="
        for a in range(r):
            tp = top[a]
            for b in range(len(users_data)):
                p = users_data[b].get('Final Score')
                if (tp == p):
                    name = users_data[b].get('Field Name')
                    if name in name_list:
                        continue
                    name_list.append(name)

        for c in range(r):
            v = c +1
            s = "#\t\t%d\t\t\t" %v
            s = s + str(top[c]) + "\t\t\t" + str(name_list[c])
            print (s)
    else:
        print("=====TOP 10 USERS WITH HIGHEST SCORES OF ALL TIME====")
        print("=================NO USERS YET=================")

    raw_input("Press 'enter' to continue...")


def removeData(users):
    '''This rewrites the entire score.txt without the user with the same username'''
    f = open('score.txt', 'w')
    for i in range(len(users)):
        f.write(str(users[i]) + '\n')
    f.close()


def starthere():
    '''This is where the user is asked for their name.'''

    global username
    users = []
    f = open('score.txt', 'r')
    tmp_list = f.readlines()
    f.seek(0)

    for j in range (len(tmp_list)):
        a = f.readline()
        users.append(ast.literal_eval(a))
    f.close()
    game = ""
    username = raw_input('Enter user: ')
    if username:
        game = raw_input("Play? (Y/N): ")
        yesorno = promptgame(game)
        if(yesorno):
            for x in range(len(users)):
                name = users[x].get('Field Name')
                tmpname = name.lower()
                tmp_user = username.lower()
                if(tmpname == tmp_user):
                    users.pop(x)
                    removeData(users)
                    username = name
                    break
            gameproper()

    else:
        topTen()

starthere()

# KOH JING WEN, VERLYN   MA8

import random
import time
import turtle

'''
turtle code
'''
x = turtle.Turtle(visible=False)
c = turtle.getcanvas() 
window = turtle.Screen()
window.bgcolor('black')
window.tracer(False)
window.setup(width = 1.0, height = 1.0)
x.penup()
center = turtle.position()
turtle.hideturtle()

numsector = 24
radius = 250
angle = 360 / numsector
rad = 220
angle0 = 0
wheelindex = 0

wheelcolour = ['#FFD1DC','#BAED91','#B2CEFE','#FEA3AA','#FFD1DC','#FAF884','#F2A2E8','#F8B88B',
               '#B2CEFE','#FEA3AA','#FAF884','#BAED91','#EEECF1','#DCDCDC','#F8B88B','#BAED91',
               '#FFD1DC','#F2A2E8','#FEA3AA','#F8F8FF','#B2CEFE','#AFEEEE','#FFD1DC','#DCDCDC'] 
txt = ['$900', '$500', '$350', '$600', '$500', '$400', '$550', '$800', '$300',
       '$700', '$900', '$500', '$5000', 'BANKRUPT', '$300', '$500', '$450',
       '$500', '$800', 'Lose A Turn', '$700', 'Free Play', '$650', 'BANKRUPT']
txt4 = []
for i in txt:
    if len(i) == 4:
        txt4.append(i)
    else:
        txt4.append('    ')

colourdict = {'red':'#FEA3AA', 'orange':'#F8B88B', 'yellow':'#FAF884','green':'#BAED91',
              'blue':'#B2CEFE', 'purple':'#F2A2E8', 'pink':'#FFD1DC', 'white':'#F8F8FF',
              'grey':'lightgrey'}
              
        

#player properties defined
player1name = input('Enter name of Player 1: ')
player2name = input('Enter name of Player 2: ')
player3name = input('Enter name of Player 3: ')
bank1 = 0
bank2 = 0
bank3 = 0
colour1 = ''
colour2 = ''
colour3 = ''
#defining players as a class with properties
class players:
   def __init__(playern, name, bank, colour):
       playern.name = name
       playern.bank = bank
       playern.colour = colour
player1 = players(player1name, bank1, colour1)
player2 = players(player2name, bank2, colour2)
player3 = players(player3name, bank3, colour3)

def choosecolour(player):
    while True:
        clstr = ' choose your colour from RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE, PINK, WHITE & GREY:  '
        cl = input(player.name + clstr).lower()
        if cl in colourdict:
            player.colour = colourdict[cl]
            break
        else:
            print('Please enter a valid option')
choosecolour(player1)
choosecolour(player2)
choosecolour(player3)

def drawcircle():
    for i in range(0,24):
        x.color(wheelcolour[i])
        x.pendown()
        x.begin_fill()
        x.circle(radius, extent=angle)
        position = x.position()
        x.goto(center)
        x.end_fill()
        x.penup()
        x.goto(position)

def typewriter(text, fontsize):
    a = x.xcor()
    b = x.ycor()
    item_id = c.create_text(a, -b, text=text, angle= angle0 ,
                            font=("Arial", fontsize, "normal"), fill = 'grey')
no = 1
def digit4(a,b,c,d):
    global no
    global angle0
    angle0=((angle/2)*no)+180
    x.circle(rad, extent=angle/2)
    position = x.position()
    x.position()
    x.left(90)
    typewriter(a, 45)
    x.fd(60)
    typewriter(b, 35)
    x.fd(50)
    typewriter(c, 25)
    x.fd(40)
    typewriter(d, 15)
    x.goto(position)
    x.right(90)
    x.circle(rad, extent=angle/2)
    no += 2

def digit4txt():
    x.sety(-rad)
    for i in txt4:
        q = i[0]
        w = i[1]
        e = i[2]
        r = i[3]
        digit4(q,w,e,r)

def bankrupttxt():
    global angle0
    global rad
    rad = rad + 10
    for c in [13.5, 23.5]:
        x.setx(0)
        x.sety(-rad)
        x.circle(rad, extent=angle*c)
        x.left(90)
        indexb = 0
        angle0 = angle*(c-12)
        for i in 'BANKRUPT':
            if 'BANKRUPT'.index(i) < 5:
                typewriter(i, 38-indexb-3)
                x.fd(38 - indexb - ('BANKRUPT'.index(i))-2)
            elif 'BANKRUPT'.index(i) > 4:
                typewriter(i, 38-indexb-2)
                x.fd(38 - indexb - ('BANKRUPT'.index(i))+2)
            indexb += 4            
        x.home()
              
def digit5():
    global angle0
    angle0 = angle/2
    x.goto(0,(rad-10))
    x.left(180)
    x.circle((rad-10), extent=angle/2)
    x.left(90)
    typewriter('$', 45)
    x.fd(55)
    typewriter('5', 35)
    x.fd(40)
    typewriter('0', 25)
    x.fd(30)
    typewriter('0', 20)
    x.fd(22)
    typewriter('0', 15)
    x.home()
    
def letter4(sect, phrase):
    global angle0
    x.sety(-rad)
    position = x.position()
    z = 7/8
    for i in phrase:  
        x.goto(position)
        x.circle(rad, extent=angle*(sect+(z)))
        angle0=angle*(sect-12+(z))
        typewriter(i,16)
        x.home()
        z = z - 2/8

def freeplaytxt():
    global rad
    rad = rad+5
    letter4(21, 'FREE')
    rad = rad-17
    letter4(21, 'PLAY')
           
def loseaturntxt():
    global rad
    global angle0
    rad = rad+17
    letter4(19, 'LOSE')
    x.sety(-rad)
    x.circle(rad, extent=angle*19.5)
    x.left(90)
    x.fd(35)
    angle0 = angle*7.5
    typewriter('A', 20)
    x.fd(50)
    typewriter('T', 30)
    x.fd(33)
    typewriter('U', 25)
    x.fd(28)
    typewriter('R', 20)
    x.fd(20)
    typewriter('N', 15)
    x.home()
    
def wheeltxt():
    digit4txt()
    bankrupttxt()      
    digit5()
    freeplaytxt()
    loseaturntxt()
    
def arrow(cl):      
    x.pendown()
    x.pencolor(cl)
    x.fillcolor(cl)
    x.begin_fill()
    x.right(60)
    x.fd(20)
    x.right(120)
    x.fd(20)
    x.right(120)
    x.fd(20)
    x.end_fill()
    x.penup()

pos = (0,rad+50)
tilt = 0
def arrowspin():
    global pos
    global tilt
    x.home()
    x.goto(pos)
    x.setheading(tilt)
    x.pendown()
    x.right(60)
    arrow('black')
    def arrowblue():
        x.circle(rad+20, extent=angle/2)
        arrow('#5499e8')
        x.right(60)
    def arrowbg():
        arrow('black')
        x.right(60)
    x.goto(0, rad + 20)
    x.setheading(180)
    for i in range(0, wheelindex):
        arrowbg()
        arrowblue()
        window.update()
        window.ontimer(arrowbg(), 10)
    arrow('#5499e8')
    pos = x.position()
    tilt = x.heading()
def arrowspinner():
#   x.pendown()
#   x.right(60)
#   arrow('black')
   arrowspin()

#creating boxes in turtle
def box():
    x.pendown()
    x.color('grey')
    for i in range (0,2):
        x.fillcolor('grey')
        x.begin_fill()
        x.fd(23)
        x.right(90)
        x.fd(35)
        x.right(90)
        x.end_fill()
    x.penup()
    x.fd(27)
def nextline():
    x.setx(275)
    x.right(90)
    x.fd(45)
    x.left(90)
boxdict = {}
boxnum = 0
def drawbox():
    global boxdict
    global boxnum
    for word in phrase.split():   
        ltrnum = len(word)
        for i in range (0, ltrnum):
            pos = x.position()
            boxdict[boxnum] = pos
            box()
            boxnum += 1 
        nextline()
        boxnum += 1

def playericon():
    def icon(cl):
        x.left(180)
        x.color(cl)
        x.pendown()
        x.begin_fill()
        x.circle(20)
        x.end_fill()
        x.penup()
        x.right(180)
        x.fd(28)
        x.right(90)
        x.fd(57)
        x.left(180)
        x.pendown()
        x.begin_fill()
        x.circle(28, extent=180)
        x.end_fill()
        x.penup()
        x.fd(100)
        x.left(90)
        x.fd(30)
    x.goto(-550, 200)
    icon(player1.colour)
    icon(player2.colour)
    icon(player3.colour)
    x.home()

def playername():
    x.goto(-500, 170)
    def name(player):
        x.pencolor(player.colour)
        x.write(player.name.upper(), move=False, align="left", font=("Arial", 20, "bold"))
        x.setheading(270)
        x.fd(155)
    name(player1)
    name(player2)
    name(player3)
    x.home()
    
def bankr(player):
    x.pencolor(player.colour)
    x.write('$'+str(player.bank), move=False, align="left", font=("Arial", 20, "bold"))
    x.setheading(270)
    x.fd(155)
def playerbank():
    x.goto(-500, 140)
    bankr(player1)
    bankr(player2)
    bankr(player3)
    x.home()
def playerbankchange(player):
    o = 0
    if player == player1:
        o = 0
    elif player == player2:
        o = 1
    elif player == player3:
        o = 2
    def clear():
        x.color('black')
        x.right(180)
        x.pendown()
        x.begin_fill()
        for i in range (0,2):
            x.fd(30)
            x.right(90)
            x.fd (100)
            x.right(90)
        x.end_fill()
        x.penup()
    x.home()
    x.goto(-500, 140-(o*155))
    x.right(90)
    clear()
    bankr(player)
    
def spintext(text,colour):
    def clear():
        x.home()
        x.color('black')
        x.goto(-700,275)
        x.pendown()
        x.begin_fill()
        for i in range (0,2):
            x.fd(1400)
            x.left(90)
            x.fd (60)
            x.left(90)
        x.end_fill()
        x.penup()
    clear()
    x.goto(0,275)
    x.color(colour)
    x.write(text, move=False, align="center", font=("Arial", 35, "bold"))
    x.home()    

def drawwheel():
    x.sety(-radius)
    drawcircle()
    wheeltxt()
    x.home()
    x.goto(275,200)
    drawbox()
    x.home()
    playericon()
    playername()
    playerbank()
    x.goto(0,rad+20)
    x.left(180)
    arrow('#5499e8')
    x.right(60)

'''
game code
'''

txt0 = [900, 500, 350, 600, 500, 400, 550, 800, 300,
       700, 900, 500, 5000, 'BANKRUPT', 300, 500, 450,
       500, 800, 'Lose A Turn', 700, 'Free Play', 650, 'BANKRUPT']
#choosing phrase
phraselist = open("WofFPhrases.txt")
countp = 0
pnum = random.randint(0,74)
for e in phraselist:
    countp += 1
    if countp == pnum:        
        phrase = e
        break
p = phrase

vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
guesslist = []


#replace letters with blanks
for i in phrase:
   if i.isalpha():
       p = p.replace(i, '☐')
      
#list of letters. removes correctly guessed letters 
remainder = ' '.join(list(phrase)).split()
def remove(letter, list):
   str(letter)
   while letter in list:
       list.remove(letter)

def letterprint(text,a,b):
    item_id = c.create_text(a, -b, text=text, angle= 0 ,font=("Arial", 18, "bold"), fill = 'white')
       
#replace blank with guessed letter
def fillbox(letr):
   global p
   liszt = []
   index = 0
   while index < len(phrase):
       index = phrase.find(letr, index)
       if index == -1:
           break
       liszt.append(index)
       index += 1
   for i in liszt:
       global p
       p = list(p)
       p[i] = letr
       p = "".join(p)
       xpos,ypos = boxdict[i]
       a = xpos + 12.5
       b = ypos - 17.5
       letterprint(letr,a,b)
   window.update()
def fill(letr):
    fillbox(letr)
    print(p)
   
def consonant(spinvalue, player):
    while True:
       a = time.perf_counter()
       cons = input(player.name + ' to call a consonant in 10 seconds: ').upper()
       b = time.perf_counter()
       if b - a > 10:
           print ('Sorry, times up!')
           break
       elif b - a <= 10:
           if cons.isalpha():
               if cons in vowels:
                   print('Not a consonant. Try again.')
               elif len(cons) != 1:
                   print('Type one letter. Try again')
               else:
                   global remainder
                   global guesslist
                   if cons in guesslist:
                       print('Sorry, consonant already guessed! \n',
                             "Turn lost! Next player \n",
                             player.name, "'s turn finished with $", player.bank,' in bank!')
                       break
                   elif cons in phrase:
                       remove(cons, remainder)
                       fill(cons)
                       guesslist.append(cons)
                       conscount = phrase.count(cons)
                       player.bank += conscount*int(spinvalue)
                       playerbankchange(player)
                       print("Congratulations! There's", conscount, cons, '(s) in the phrase! \n',
                             player.name, ' has $', player.bank, ' in bank')
                       choice(player)
                       break
                   else:
                       print('Sorry, consonant not in phrase \n',
                             "Turn lost! Next player! \n",
                             player.name, "'s turn finished with $", player.bank, ' in bank!')
                       guesslist.append(cons)
                       break
           else:
               print('Not a letter. Try again.')

def vowel(player):
   if player.bank < 250:
       print('Insufficient value. Spin again')
       input('Press enter to spin wheel:')
       spinstarter(player)
   else:
       while True:
           a = time.perf_counter()
           vow = input('Call a vowel in 10 seconds: ').upper()
           b = time.perf_counter()
           if b - a > 20:
              print('Sorry, times up!')
              break
           elif b - a <= 20: 
               if vow.isalpha():
                   global guesslist
                   if len(vow) != 1:
                       print('Type one letter. Try again')
                   elif vow in vowels:
                       player.bank -= 250
                       playerbankchange(player)
                       print('$250 subtracted from ' + player.name + 's bank!')
                       if vow in guesslist:
                           print('Sorry, vowel already guessed! \n',
                                 "Turn lost! Next player \n",
                                 player.name, "'s turn finished with $", player.bank, ' in bank!')
                           break
                       else:
                           global remainider
                           if vow in phrase:
                               remove(vow, remainder)
                               fill(vow)
                               vowcount = phrase.count(vow)
                               print("Congratulations! There's", vowcount, vow, '(s) in the phrase! \n',
                                     player.name, ' has $', player.bank, ' in bank')
                               guesslist.append(vow)
                               choice(player)
                               break
                           else:
                               print('Sorry, vowel not in phrase \n',
                                     "Turn lost! Next player \n",
                                     player.name, "'s turn finished with $", player.bank, ' in bank!')
                               break
                   else:
                       print("Not a vowel. Try again.")
               else:
                   print('Not a letter. Try again.')

def bankrupt(player):
   player.bank = 0
   playerbankchange(player)
   print(player.name, 'has gone bankrupt!', player.name, "'s bank balance is reset to $0!")
   time.sleep(2)

def loseaturn(player):
   print(player.name, ' has spun Lose A Turn!', player.name, 'ends turn with bank balance $', player.bank)
   time.sleep(2)

def freeplay(player):
   print(player.name, ' has spun Free Play!')
   while True:
       global remainder 
       global guesslist
       a = time.perf_counter()
       ltr = input('Call any letter in 10 seconds: ').upper()
       b = time.perf_counter()
       if b - a > 10:
          print('Sorry, times up!')
          break
       elif b - a <= 10:
           if ltr.isalpha():
               if ltr in guesslist:
                   print('Sorry, consonant already guessed!')
                   choice(player)
                   break          
               elif ltr in phrase:
                   remove(ltr, remainder)
                   fill(ltr)
                   ltrcount = phrase.count(ltr)
                   print("Congratulations! There's", ltrcount, ltr, '(s) in the phrase! \n',
                          player.name, ' has $', player.bank, ' in bank')           
                   guesslist.append(ltr)
                   choice(player)
                   break
               else:
                   print('Sorry. Letter not in phrase')
                   choice(player)
                   break
           else:
               print('Not a letter. Try again.')

solvestatus = False
def solve(player):
   print(player.name, 'has 20 seconds to guess the phrase!')
   a = time.perf_counter()
   print(p)
   slv = str(input('Your guess: ')).upper()
   b = time.perf_counter()
   global solvestatus
   if b - a > 20:
       print('Sorry, times up!')
   elif b - a <= 20:
       if slv == phrase:
           print('Congratulations!', player.name, "'s guess is correct!", player.name, "wins $", player.bank,"!")
           solvestatus = True
       else:
           print('Sorry, your guess is incorrect! Turn lost!')
           solvestatus = False

#spins the wheel
def spinstarter(player):
   global wheelindex 
   print('spinning...')
   wheelindex = random.randrange(49, 48*2 +1 , 2)
   textindex = (((wheelindex % 48) // 2) + 12)% 24
   spinvalue = str(txt0[textindex])
   arrowspinner()
   if spinvalue.isnumeric():
       print(player.name + " has spun $", spinvalue, "!")
       spintext('$'+spinvalue, wheelcolour[textindex])
       consonant(spinvalue, player)
   elif spinvalue == 'BANKRUPT':
       spintext('BANKRUPT','#FEA3AA')
       bankrupt(player)
   elif spinvalue == 'Lose A Turn':
       spintext('Lose A Turn', '#FAF884')
       loseaturn(player)       
   elif spinvalue == 'Free Play':
       spintext('Free Play', '#AFEEEE')
       freeplay(player)

def choice(player):
   while True:
       print(p)
       choice = input('Spin the wheel(enter c), buy a vowel(enter v) or solve(enter s)?: ').lower()
       if choice == 'c':
           if conscheck():
               spinstarter(player)
               break
           else:
               print('All consonants have been guessed, cannot spin wheel! Choose another option. ')
       elif choice == 'v':
           if vowcheck():
               vowel(player)
               break
           else:
               print('All vowels have been guessed! Choose another option. ')
       elif choice == 's':
           solve(player)
           break
       else:
           print('Please enter a valid option')


#checks for vowels left
def vowcheck():
   modifiedlist = list(remainder)
   for ltr in vowels:
       remove(ltr, modifiedlist)
   if remainder == modifiedlist:
       return False
   else: 
       return True


#checks for consonant left
def conscheck():
   modifiedlist = list(remainder)
   for ltr in vowels:
       remove(ltr, modifiedlist)
   if modifiedlist:  
       return True
   else:  
       return False

def fillremainder():
    for i in remainder:
        fillbox(i)

def allguessed(player):
    if remainder == []:
        print ('All letters revealed.')
        solve(player)

def playerwin(playerA,playerB):
    playerA.bank = 0
    playerbankchange(playerA)
    playerB.bank = 0
    playerbankchange(playerB)
    fillremainder()

'''
game starts here
'''

    
print("Welcome to Wheel of Fortune!\n", p)
drawwheel()

#gameloop execution              
firstturn = True
while True:
    if firstturn:
        spintext(player1.name.upper() + ' SPIN THE WHEEL TO BEGIN!', player1.colour)
        input(player1.name + ' spin the wheel to begin! \n'
                        'Press enter to spin wheel:')
        spinstarter(player1)
        firstturn = False
        if solvestatus:
            playerwin(player2,player3)
            break
        else:
            spintext(player2.name.upper() + "'S TURN!", player2.colour)
            print(player2.name + "'s turn!")                               
            allguessed(player2)
            if solvestatus:
                playerwin(player1,player3)
                break
            else:
               choice(player2)
               if solvestatus:
                   playerwin(player1,player3)
                   break
               else:
                   spintext(player3.name.upper() + "'S TURN!", player3.colour)
                   print(player3.name + "'s turn!")                               
                   allguessed(player3)
                   if solvestatus:
                        playerwin(player1,player2)
                        break
                   else:
                       choice(player3)
                       if solvestatus:
                           playerwin(player1,player2)
                           break
                       else:
                           print('At the end of this turn,\n',
                                 player1.name, ' has $', player1.bank, '!\n',
                                 player2.name, ' has $', player2.bank, '!\n',
                                 player3.name, ' has $', player3.bank, '!\n')      
    else:
        spintext(player1.name.upper() + "'S TURN!", player1.colour)
        print(player1.name + "'s turn!")                               
        allguessed(player1)
        if solvestatus:
            playerwin(player2,player3)
            break
        else:
            choice(player1)
            if solvestatus:
                playerwin(player2,player3)
                break
            else:
                spintext(player2.name.upper() + "'S TURN!", player2.colour)
                print(player2.name + "'s turn!")                               
                allguessed(player2)
                if solvestatus:
                    playerwin(player1,player3)
                    break
                else:
                   choice(player2)
                   if solvestatus:
                       playerwin(player1,player3)
                       break
                   else:
                       spintext(player3.name.upper() + "'S TURN!", player3.colour)
                       print(player3.name + "'s turn!")                               
                       allguessed(player3)
                       if solvestatus:
                            playerwin(player1,player2)
                            break
                       else:
                           choice(player3)
                           if solvestatus:
                               playerwin(player1,player2)
                               break
                           else:
                               print('At the end of this turn,\n',
                                     player1.name, ' has $', player1.bank, '!\n',
                                     player2.name, ' has $', player2.bank, '!\n',
                                     player3.name, ' has $', player3.bank, '!\n')

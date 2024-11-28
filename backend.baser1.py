import random 

deck1 = ['s01','s02','s03','s04','s05','s06','s07','s08','s09','s10','s11','s12','s13','h01','h02','h03','h04','h05','h06','h07','h08','h09','h10','h11','h12','h13','c01','c02','c03','c04','c05','c06','c07','c08','c09','c10','c11','c12','c13','d01','d02','d03','d04','d05','d06','d07','d08','d09','d10','d11','d12','d13']
deck = deck1.copy()

def shuffle(x):
   random.shuffle(x)
   random.shuffle(x)
   return x

def orderdeck():
  global deck
  deck = deck1.copy()

#~~~~~~~~~~~ G A M E    S E T T I N G ~~~~~~~~~#
# 0 = off
# 1 = snap 
# 2 = whist
global gtype
gtype =  0


class Player:
 def __init__(self,priority,bet,miniscore,hand,gamescore):
   self.priority  = priority 
   self.bet = bet
   self.miniscore = miniscore 
   self.hand = hand
   self.gamescore = gamescore


player1 = Player(0,0,0,[],0)
player2 = Player(0,0,0,[],0)
player3 = Player(0,0,0,[],0)
player4 = Player(0,0,0,[],0)

players = [player1,player2,player3,player4]

global player_index
player_index = 0
##miscelaneous##
def display_smlscores():
  print('player1s score is ',str(player1.miniscore))
  print('player2s score is ',str(player2.miniscore))
  print('player3s score is ',str(player3.miniscore))
  print('player4s score is ',str(player4.miniscore))

def display_bigscores():
  print('player1s score is ',str(player1.gamescore))
  print('player2s score is ',str(player2.gamescore))
  print('player3s score is ',str(player3.gamescore))
  print('player4s score is ',str(player4.gamescore))

def display_hands():
 print(player1.hand,'player1', len(player1.hand))
 print(player2.hand,'player2', len(player2.hand))
 print(player3.hand,'player3', len(player3.hand))
 print(player4.hand,'player4', len(player4.hand))

def reset():
      player1.hand = []
      player2.hand = []
      player3.hand = []
      player4.hand = []
      global deck
      deck = deck1.copy()
      display_hands()
      orderdeck()


'''------------------------------------------'''
####################'''TRUMPS'''##################

def mtrump():
  t = input('player - x - which suit would you like to be trumps ?')
  if t[0] == 's':
   trump = 's'
  if t[0] == 'd':
   trump = 'd'
  if t[0] == 'h':
   trump = 'h'
  if t[0] == 'c':
   trump = 'c' 
  print(trump)
  return trump  

def strump():
  subtrump = ''
  st = roundpile [0]
  if st[0] == 's':
   subtrump = 's'
  if st[0] == 'd':
   subtrump = 'd'
  if st[0] == 'h':
   subtrump = 'h'
  if st[0] == 'c':
   subtrump = 'c'
  return subtrump 


###   dealing    ###

shuffle(deck)


######  IRISH SNAP  ########## :
''' this code below is finished - look above 4 the shuffle functions and if you finish try out the whistdeal function'''
global snap
snap = False
downpile = []
srefpile = downpile.copy()
turncount = 0

def snapdeal():
      player_index = 0
      while len(deck) > 1 : 
        x = (random.randint(0,len(deck)-1)) 
        card = deck.pop(x) 
        players[player_index].hand.append(card) 
        player_index = (player_index + 1) % 4 
      if deck:
        last_card = deck.pop()  
        players[player_index].hand.append(last_card)
      display_hands()
      print(len(deck))

def checksnap():
  if len(downpile) > 1:
   x = downpile[-1]
   y = downpile[-2]
   x1 = int(x[1:])
   y1 = int(y[1:])
   if x1 == y1 :
    print('SNAP !!')
    global snap
    snap = True 
  if len(downpile) > 0:
   tc = str(turncount+1).zfill(2)
   tc = int(tc)%13
   print(tc)
   x = downpile[-1]
   x1 = int(x[1:])
   if tc == x1 : 
    print('snap22')
    snap = True

def askplace():
  global player_index
  place = input('player '+str(player_index + 1)+ ' do you want to play')
  if place == 'yes':
    playerturn()
  else:
    askplace()

def playerturn():
 x = player_index 
 i = (len(players[x].hand)-1)
 card = players[x].hand.pop(i)
 downpile.append(card)
 print(downpile,'\n')
 
def wholeturn():
 # while snap == False:
    askplace()
    checksnap()
    display_hands()

def snaprounds():
  while snap == False:
   global player_index
   x = player_index 
   wholeturn()
   player_index = (x + 1) % 4 
   print(player_index)
   global turncount
   turncount = turncount + 1

def setsnap():
 global snap
 global turncount
 global downpile
 global srefpile
 snap = False
 turncount = 0
 downpile = srefpile
 

#def wipesnap():
##snap main below runs the entirety of snap and can be called whenevr 

def snapmain():
 global gtype
 gtype = 1
 reset()
 snapdeal()
 snaprounds()
 checksnap()
 setsnap()


'''##end of irish snap###'''

## - - - - - - - - W ~ H ~ I ~ S ~ T - - - - - - - ##

roundpile = []
setpile = roundpile.copy()
def whistdeal(round):
      player_index = 0
      while len(player4.hand) < 8-round : 
          x = (random.randint(0,len(deck)-1)) 
          card = deck.pop(x) 
          players[player_index].hand.append(card) 
          player_index = (player_index + 1) % 4 
      display_hands()
      print(len(deck))

def orderplayer():
  players =[player3,player1,player4,player1]

def betting():
 realtr = mtrump()
 a = realtr
 tophand = len(player1.hand) 
 totalbet = 0 
 for i in range (0,len(players)):
    if totalbet < 8 and i == 3:
      nobet = 7 - totalbet 
      x23 = int(input('player '+ str(i+1) + '  enter an number that is not ' + str(nobet)+ ' for your bet:'))
      totalbet = totalbet + int(x23)
      if int(x23) == nobet:
        x23 = int(input('player '+ str(i+1) + '  enter an number that is not ' + str(nobet)+ ' for your bet:'))
    else:
     x23 = int(input('player '+ str(i+1) + '  enter an number between 0 and ' + str(tophand)+ ' for your bet:'))
     players[i].bet = int(x23)
     totalbet = totalbet + int(x23)
    print(players[i].bet)
 return realtr

def findcard(target,x):
  for i in range(len(players[x].hand)):
   if players[x].hand[i] == target:
      return i  
  return -1 

def whisturn():
  x = player_index 
  print(players[x].hand)
  target = input('player '  + str(x+1) + ' which card would you like to play')
  cplace = findcard(target,x)
  card = players[x].hand.pop(cplace)
  roundpile.append(card)
  print(roundpile,'\n')
  display_hands()
 
def whistplay():
  global player_index
  for i in range(0,4):
    player_index = i
    whisturn() 

def orderpile(a):
 #strump()
 for i in range(len(roundpile)-1):
  for j in range(i + 1, len(roundpile)):
    x = roundpile[i]
    y = roundpile[j]
    x1 = int(x[1:])
    y1 = int(y[1:])
    if x1 > y1 :
     roundpile[i], roundpile[j] = roundpile[j], roundpile[i]
  print(roundpile)
 for i in range(len(roundpile)-1):
  for j in range(i + 1, len(roundpile)):
    x = roundpile[i]
    y = roundpile[j]
    x1 = str(x[0])
    y1 = str(y[0])
    if x1 == a:
     roundpile[i], roundpile[j] = roundpile[j], roundpile[i]
    
 print(roundpile)

def roundw ():
  refpile = roundpile.copy()
  if len(roundpile) == 4:
    global realtr
    orderpile(realtr)
    targetx = roundpile[-1]
    for i in range(len(refpile)):
      if refpile[i] == targetx:
       print (i) 
       global hwin
       hwin = i 
  print('player '+ str(hwin+1) + ' has won')
  players[hwin].miniscore = players[hwin].miniscore + 1
  display_smlscores()

def whisthands():
  whistplay()
  roundw()

def whistround(hs):
  global gtype 
  gtype = 2
  handsize = 1
  reset()
  shuffle(deck)
  whistdeal(handsize)
  global realtr
  realtr = betting()
  for i in range(hs): 
    wipe_roundpile()
    whisthands()
    
def wipe_roundpile():
    global roundpile
    roundpile.clear()
    print("Roundpile has been wiped!",roundpile)

## def bigwhist
# whistdeal(x)
# betting 
# whistmain


#########################
'''whole game '''


def totalscores():
  for i in range(0,4):
    if players[i].bet == players[i].miniscore :
      players[i].gamescore =  players[i].gamescore + players[i].miniscore + 9
  display_bigscores()
      

def gamemain():
 for i in range(0,7):
  x = 7 - i 
  print('\n'+str(x)+'\n')
  snapmain() 
  whistround(x)
  totalscores()
  

for i in range(0,3):
 snapmain()



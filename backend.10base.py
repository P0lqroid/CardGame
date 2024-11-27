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

#y = shuffle(deck)
#print(y)

class Player:
 def __init__(self,priority,bet,score,hand):
   self.priority  = priority 
   self.bet = bet
   self.score = score 
   self.hand = hand


player1 = Player(0,0,0,[])
player2 = Player(0,0,0,[])
player3 = Player(0,0,0,[])
player4 = Player(0,0,0,[])

players = [player1,player2,player3,player4]

global player_index
player_index = 0
##miscelaneous##


def display_hands():
 print(player1.hand,'player1', len(player1.hand))
 print(player2.hand,'player2', len(player2.hand))
 print(player3.hand,'player3', len(player3.hand))
 print(player4.hand,'player4', len(player4.hand))

def snp2whist():
      player1.hand = []
      player2.hand = []
      player3.hand = []
      player4.hand = []
      global deck
      deck = deck1.copy()
      display_hands()
      orderdeck()



###   dealing    ###

shuffle(deck)


######  IRISH SNAP  ##########
global snap
snap = False
downpile = []
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
   print(tc)
   tc = int(tc)
   x = downpile[-1]
   x1 = int(x[1:])
   if tc == x1 : 
    print('snap22')
    snap = True

def askplace():
  place = input('do you want to play')
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

def snapmain():
 while snap == False:
   x = player_index 
   wholeturn()
   player_index = (x + 1) % 4 
   print(player_index)
   turncount = turncount + 1


'''##end of irish snap###'''

###############whist##############

roundpile = []
def whistdeal(round):
      player_index = 0
      while len(player4.hand) < 8-round : 
          x = (random.randint(0,len(deck)-1)) 
          card = deck.pop(x) 
          players[player_index].hand.append(card) 
          player_index = (player_index + 1) % 4 
      display_hands()
      print(len(deck))

def betting ():
 nobet = len(player1.hand)
 player_index = 0
 for i in range (1,5):
  x23 = int(input('enter a number between 1 and',+nobet))
  players[i].bet = int(x23)
  print(players[i].bet)

def orderplayer():
  players =[player3,player1,player4,player1]

def betting():
 tophand = len(player1.hand) 
 player_index = 0
 totalbet = 0 
 for i in range (1,len(players)+1):
    if totalbet < 8 and i == 4:
      nobet = 7 - totalbet 
      x23 = int(input('player '+ str(i) + '  enter an number that is not ' + str(nobet)+ ' for your bet:'))
      totalbet = totalbet + int(x23)
      if int(x23) == nobet:
        x23 = int(input('player '+ str(i) + '  enter an number that is not ' + str(nobet)+ ' for your bet:'))
    else:
     x23 = int(input('player '+ str(i) + '  enter an number between 0 and ' + str(tophand)+ ' for your bet:'))
     players[i].bet = int(x23)
     totalbet = totalbet + int(x23)
    print(players[i].bet)

def findcard(target,x):
  for i in range(len(players[x].hand)):
    if players[x].hand[i] == target:
      cplace = int(i)
      return cplace 


def whisturn():
  x = player_index 
  print(players[x].hand)
  place = input('which card would you like to play')
  target = place 
  findcard(target,x)
  card = players[x].hand.pop[cplace]
  roundpile.append(card)
  print(roundpile,'\n')
 

whistdeal(1)
betting()
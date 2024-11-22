import random 

ogdeck = ['s01','s02','s03','s04','s05','s06','s07','s08','s09','s10','s11','s12','s13','h01','h02','h03','h04','h05','h06','h07','h08','h09','h10','h11','h12','h13','c01','c02','c03','c04','c05','c06','c07','c08','c09','c10','c11','c12','c13','d01','d02','d03','d04','d05','d06','d07','d08','d09','d10','d11','d12','d13']
deck = ogdeck.copy

def shuffle(x):
   random.shuffle(x)
   random.shuffle(x)
   return x

def orderdeck():
  global deck
  deck = ogdeck.copy

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

def display_hands():
 print(player1.hand, len(player1.hand))
 print(player2.hand, len(player2.hand))
 print(player3.hand, len(player3.hand))
 print(player4.hand, len(player4.hand))

def snp2whist():
      player1.hand = []
      player2.hand = []
      player3.hand = []
      player4.hand = []
      global deck
      deck = ogdeck.copy

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

def whistdeal(round):
      player_index = 0
      while len(player4.hand) < 8-round : 
          x = (random.randint(0,len(deck)-1)) 
          card = deck.pop(x) 
          players[player_index].hand.append(card) 
          player_index = (player_index + 1) % 4 
      display_hands()
      print(len(deck))


orderdeck()
shuffle(deck)
snapdeal()
#snp2whist()
orderdeck()
#whistdeal(1)

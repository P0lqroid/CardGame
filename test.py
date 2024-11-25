import arcade
import random

def startup():
    ogdeck = ['s01','s02','s03','s04','s05','s06','s07','s08','s09','s10','s11','s12','s13','h01','h02','h03','h04','h05','h06','h07','h08','h09','h10','h11','h12','h13','c01','c02','c03','c04','c05','c06','c07','c08','c09','c10','c11','c12','c13','d01','d02','d03','d04','d05','d06','d07','d08','d09','d10','d11','d12','d13']
    deck = ogdeck.copy

    def shuffle(x):
        random.shuffle(x)
        random.shuffle(x)
        return x

    def orderdeck():
        global deck
        deck = ogdeck.copy



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
    global players
    players = [player1,player2,player3,player4]

def card_update():
    global players
    for player_index in range(0,3):

        for i in range(len(players[player_index].hand)):
            cardimage=str(players[player_index].hand[i]+".png")
            print (cardimage)
            card = arcade.Sprite(cardimage,CARD_SCALING)
            xPos = int(100+(int(i)*20))
            card.position = (xPos, 50)
            #self.card_list.append(card)

startup()
card_update()
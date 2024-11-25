import arcade
import os
import random

SCREEN_TITLE = "Whistle Hit"

PLAYER_SCALING = 0.05
CARD_SCALING = 0.15

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 700


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

def snapdeal():
      global players
      player_index = 0
      while len(deck) > 1 : 
        x = (random.randint(0,len(deck)-1)) 
        card = deck.pop(x) 
        players[player_index].hand.append(card) 
        player_index = (player_index + 1) % 4 
      if deck:
        last_card = deck.pop()
        players[player_index].hand.append(last_card)

class snapGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self, width, height, title):
        """ Initializer """

        # Call the parent class initializer
        super().__init__(width, height, title)

        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        # Background image will be stored in this variable
        self.background = None

        # Variables that will hold sprite lists
        self.player_list = None
        self.card_list = None

        # Set up the player info
        self.player_sprite = None
        self.score = 0
        self.score_text = None

        # Show the mouse cursor
        self.set_mouse_visible(False)

    def card_update(self):
        global players
        for player_index in range(0,3):

            for i in range(len(players[player_index].hand)):
                cardimage=str(players[player_index].hand[i]+".png")
                print (cardimage)
                card = arcade.Sprite(cardimage,CARD_SCALING)
                xPos = int(100+(int(i)*20))
                card.position = (xPos, 50)
                self.card_list.append(card)
                    
        

    

    def setup(self):
        """ Set up the snap game and initialize the variables. """

        # Load the background image. Do this in the setup so we don't keep reloading it all the time.
        self.background = arcade.load_texture("Cards\Table.png")

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.card_list = arcade.SpriteList()

        # Set up the player
        self.score = 0
        self.player_sprite = arcade.Sprite("cursor.png",
                                           PLAYER_SCALING)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

        self.card_update()

        for i in range(5):

            # Create the coin instance
            card = arcade.Sprite("Cards\c13.png", CARD_SCALING)

            # Position the coin
            card.center_x = random.randrange(SCREEN_WIDTH)
            card.center_y = random.randrange(SCREEN_HEIGHT)

            # Add the coin to the lists
            #self.card_list.append(card)

    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        self.clear()

        # Draw the background texture
        arcade.draw_lrwh_rectangle_textured(0, 0,
                                            SCREEN_WIDTH, SCREEN_HEIGHT,
                                            self.background)

        # Draw all the sprites.
        self.card_list.draw()
        self.player_list.draw()

        # Render the text
        arcade.draw_text(f"Score: {self.score}", 10, 20, arcade.color.WHITE, 14)

    def on_mouse_motion(self, x, y, dx, dy):
        """
        Called whenever the mouse moves.
        """
        self.player_sprite.center_x = x
        self.player_sprite.center_y = y

    def on_update(self, delta_time):
        """ Movement and game logic """

        # Call update on the coin sprites (The sprites don't do much in this
        # example though.)
        self.card_list.update()

        # Generate a list of all sprites that collided with the player.
        hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.card_list)

        # Loop through each colliding sprite, remove it, and add to the score.
        for card in hit_list:
            card.remove_from_sprite_lists()
            self.score += 1


def main():
    """ Main function """
    startup()
    snapdeal()
    window = snapGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
import arcade,arcade.gui
import os
import random
import math
from arcade.gui import (
    UIFlatButton,
    UIOnChangeEvent,
    UITextureButton,
)



SCREEN_TITLE = "Whistle Hit"

PLAYER_SCALING = 0.075
CARD_SCALING = 0.15

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000

deck1 = ['s01','s02','s03','s04','s05','s06','s07','s08','s09','s10','s11','s12','s13','h01','h02','h03','h04','h05','h06','h07','h08','h09','h10','h11','h12','h13','c01','c02','c03','c04','c05','c06','c07','c08','c09','c10','c11','c12','c13','d01','d02','d03','d04','d05','d06','d07','d08','d09','d10','d11','d12','d13']
deck = deck1.copy()

global snap
snap = False
downpile = []
turncount = 0
global player_index
player_index = 0
global count
count=0


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


def startup():
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

class RotatedUITextureButton(arcade.gui.UITextureButton):
    def __init__(self, *args, angle=0, **kwargs):
        super().__init__(*args, **kwargs)
        self.angle = angle

    def draw(self):
        # Apply rotation before drawing the button
        arcade.start_render()
        with arcade.push_matrix():
            arcade.translate(self.center_x, self.center_y)
            arcade.rotate(self.angle)
            arcade.translate(-self.center_x, -self.center_y)
            super().draw()

class Player:
    def __init__(self,priority,bet,score,hand):
        self.priority  = priority 
        self.bet = bet
        self.score = score 
        self.hand = hand

global player1,player2,player3,player4
player1 = Player(0,0,0,[])
player2 = Player(0,0,0,[])
player3 = Player(0,0,0,[])
player4 = Player(0,0,0,[])
global players
players = [player1,player2,player3,player4]
global pwayers
pwayers =[]

def checksnap():
  if len(downpile) > 1:
   x = downpile[-1]
   y = downpile[-2]
   x1 = int(x[1:])
   y1 = int(y[1:])
   global snap
   if x1 == y1 :
    print('SNAP !!')
    snap = True 
  if len(downpile) > 0:
   tc = str(turncount+1).zfill(2)
   tc = int(tc)%13
   x = downpile[-1]
   x1 = int(x[1:])
   if tc == x1 : 
    print('snap22')
    snap = True


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
        global player_index
        # Background image will be stored in this variable
        self.background = None

        self.manager = arcade.gui.UIManager()
        self.manager.enable()
        self.show_snap_button=False

        button = arcade.gui.UITextureButton(
            x=60,  # Set the desired x-coordinate
            y=80,  # Set the desired y-coordinate
            texture=arcade.load_texture('blankbutton.png'),
            texture_hovered=arcade.load_texture('buttonhover.png'),
            texture_pressed=arcade.load_texture('buttonpress.png'),
            scale=0.6,
            
            text="Player Turn",
            style={
            "font_color": arcade.color.BLACK,  # Set the text color to black
            "font_size":16,
            "text_align":"center"
            }
        )
        button.on_click = self.on_click_turn
        self.manager.add(button)

        button = arcade.gui.UITextureButton(
            x=SCREEN_WIDTH-60-144,  # Set the desired x-coordinate
            y=80,  # Set the desired y-coordinate
            texture=arcade.load_texture('blankbutton.png'),
            texture_hovered=arcade.load_texture('buttonhover.png'),
            texture_pressed=arcade.load_texture('buttonpress.png'),
            scale=0.6,
            
            text="EXIT GAME",
            style={
            "font_color": arcade.color.BLACK,  # Set the text color to black
            "font_size":16,
            "text_align":"center"
            }
        )
        button.on_click = self.on_click_exit
        self.manager.add(button)
        #240 * 160
        #144 * 96
        #72 * 48
        # Create buttons for each player but don't add them yet
        self.player_buttons = []  # List to store player buttons
        # Create buttons for player 1
        button = arcade.gui.UITextureButton(
            
            x=SCREEN_WIDTH//2-72,
            y=215,
            texture=arcade.load_texture('blankbutton.png'),
            texture_hovered=arcade.load_texture('buttonhover.png'),
            texture_pressed=arcade.load_texture('buttonpress.png'),
            scale=0.6,
        )
        button.on_click = lambda event, button=button: self.player1_snap(event, button)
        self.player_buttons.append(button)  # Store the button in the list

        # Create buttons for player 2
        button = arcade.gui.UITextureButton(
            x=SCREEN_WIDTH-215-96,
            y=SCREEN_HEIGHT//2-72,
            texture=arcade.load_texture('blankbuttonrotate.png'),
            texture_hovered=arcade.load_texture('buttonhoverrotate.png'),
            texture_pressed=arcade.load_texture('buttonpressrotate.png'),
            scale=0.6,
        )
        button.on_click = lambda event, button=button: self.player2_snap(event, button)
        self.player_buttons.append(button)  # Store the button in the list
        #Create button for player 3
        button = arcade.gui.UITextureButton(
            x=SCREEN_WIDTH//2-72,
            y=SCREEN_HEIGHT-215-96,
            texture=arcade.load_texture('blankbutton.png'),
            texture_hovered=arcade.load_texture('buttonhover.png'),
            texture_pressed=arcade.load_texture('buttonpress.png'),
            scale=0.6,
        )
        button.on_click = lambda event, button=button: self.player3_snap(event, button)
        self.player_buttons.append(button)  # Store the button in the list

        # Create buttons for player 4
        button = arcade.gui.UITextureButton(
            x=215,
            y=SCREEN_HEIGHT//2-72,
            texture=arcade.load_texture('blankbuttonrotate.png'),
            texture_hovered=arcade.load_texture('buttonhoverrotate.png'),
            texture_pressed=arcade.load_texture('buttonpressrotate.png'),
            scale=0.6,
        )
        button.on_click = lambda event, button=button: self.player4_snap(event, button)
        self.player_buttons.append(button)  # Store the button in the list


        self.show_snap_buttons = False  # Flag to track if snap buttons are shown



        # Variables that will hold sprite lists
        self.player_list = None
        self.card_list = None
        self.button_list = None

        # Set up the player info
        self.player_sprite = None
        self.score = 0
        self.score_text = None

        # Show the mouse cursor
        self.set_mouse_visible(False)

        
        snapdeal()
    #1050 Screen width and height
    def place_cards(self,player,x,y,orientation,angle):
        for i in range(len(players[player].hand)):
            
            #cardimage=str("Cards/"+players[player].hand[i]+".png")
            cardimage="Cards/backcard1.png"
            card = arcade.Sprite(cardimage,CARD_SCALING)
            card.player=player
            card.value=players[player].hand[i]
            card.remove_flag=False
            if orientation=="v":
                card.angle += angle
                newx=int(x+int(i)*40)
                card.position=(newx,y)
                card.original_position = card.position

                card.owner=player
                self.card_list.append(card)
                
            else:
                card.angle += angle
                newy=int(y+int(i)*40)
                card.position=(x,newy)
                card.original_position = card.position
                card.owner=player
                self.card_list.append(card)


    def select_card(self):
        mouse_x, mouse_y = self.player_sprite.center_x, self.player_sprite.center_y

        selected_card = None  # Keep track of the selected card

        for card in reversed(self.card_list):
            if card.collides_with_point((mouse_x, mouse_y)):
                selected_card = card  # Store the selected card
                break  # Exit the loop once a card is selected

        # If a card is selected, move it
        if selected_card:
            if selected_card.player == 0:
                if selected_card.center_y < selected_card.original_position[1] + 20:  
                    selected_card.center_y += 5
            elif selected_card.player == 1:
                if selected_card.center_x > selected_card.original_position[0] - 20:  
                    selected_card.center_x -= 5
            elif selected_card.player == 2:
                if selected_card.center_y > selected_card.original_position[1] - 20:  
                    selected_card.center_y -= 5
            elif selected_card.player == 3:
                if selected_card.center_x < selected_card.original_position[0] + 20:  
                    selected_card.center_x += 5

        # Reset other cards (if any were previously selected)
        for card in self.card_list:
            if card != selected_card and (card.center_x != card.original_position[0] or \
            card.center_y != card.original_position[1]):
                card.center_x = card.original_position[0]
                card.center_y = card.original_position[1]

    def card_update(self):
        #Place cards
        startx=(SCREEN_WIDTH//15)*4-4
        starty=(SCREEN_HEIGHT//15)*2
        self.place_cards(0,startx,starty,"v",0)
        self.place_cards(1,SCREEN_WIDTH-starty,startx,"h",90)
        self.place_cards(2,startx,SCREEN_HEIGHT-starty,"v",180)
        self.place_cards(3,starty,startx,"h",270)


    def setup(self):
        """ Set up the snap game and initialize the variables. """
        self.frame = 0
        # Load the background image. Do this in the setup so we don't keep reloading it all the time.
        self.background = arcade.load_texture("Cards/Table.png")
        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.card_list = arcade.SpriteList()
        self.button_list = arcade.SpriteList()

        # Set up the player
        self.score = 0
        self.player_sprite = arcade.Sprite("cursor.png", PLAYER_SCALING)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

        self.card_update()

    def playerturn(self):   
        global player_index
        global count
        x = player_index%4
        i = (len(players[x].hand)-1)
        card = players[x].hand.pop(i)
        downpile.append(card)
        print(downpile,'\n')


        #Add downpile cards
        for sprite in self.card_list:
            if sprite.value == card:
                sprite_to_remove = sprite
                break
        
        sprite_to_remove.remove_flag = True
        

        cardimage=str("Cards/"+card+".png")
        CARD_SCALING1=0.3
        card1 = arcade.Sprite(cardimage,CARD_SCALING1)
        card1.player=5
        card1.remove_flag=False
        card1.angle -= 45 *count
        card1.original_position=(SCREEN_WIDTH//2,SCREEN_HEIGHT//2)
        self.card_list.append(card1)
        count+=1

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
        self.manager.draw()
        self.player_list.draw()

        #Draw buttons:
        


        # Render the text
        arcade.draw_text(f"Frame: {self.frame}", 10, 20, arcade.color.WHITE, 14)
        if snap==False:
            arcade.draw_text(f"{((player_index%4)+1)}", 125, 100, arcade.color.BLACK, 18)
        
        arcade.draw_text(f"{count%13}", SCREEN_WIDTH//2, 320, arcade.color.BLACK, 18)
        x = SCREEN_WIDTH // 2
        y = SCREEN_HEIGHT // 2
        arcade.draw_text("Player 1", x, 40, arcade.color.WHITE, 15, anchor_x="center",rotation=0)
        arcade.draw_text("Player 2", SCREEN_WIDTH-40, y, arcade.color.WHITE, 15, anchor_x="center",rotation=90)
        arcade.draw_text("Player 3", x, SCREEN_HEIGHT-40, arcade.color.WHITE, 15, anchor_x="center",rotation=180)
        arcade.draw_text("Player 4", 40, y, arcade.color.WHITE, 15, anchor_x="center",rotation=270)
        """
        if snap==True:
            arcade.draw_text("SNAP", x, 250, arcade.color.RED, 30, anchor_x="center",rotation=0)
            arcade.draw_text("SNAP", SCREEN_WIDTH-250, y, arcade.color.RED, 30, anchor_x="center",rotation=90)
            arcade.draw_text("SNAP", x, SCREEN_HEIGHT-250, arcade.color.RED, 30, anchor_x="center",rotation=180)
            arcade.draw_text("SNAP", 250, y, arcade.color.RED, 30, anchor_x="center",rotation=270)
        """
    def on_mouse_motion(self, x, y, dx, dy):
        """
        Called whenever the mouse moves.
        """
        self.player_sprite.center_x = x
        self.player_sprite.center_y = y
        #self.card_update()
        
    def on_update(self, delta_time):
        """ Movement and game logic """
        global snap

        card_list_copy = arcade.SpriteList(self.card_list)  
        card_list_copy.update()
        self.card_list.update()
        if (snap == False):
        # Call update on the coin sprites (The sprites don't do much in this
        # example though.)
            
        # Generate a list of all sprites that collided with the player.
            self.select_card()
            if len(pwayers)!=4:

                checksnap()

        # Loop through each colliding sprite, remove it, and add to the score.
            for sprite in self.card_list:
                if sprite.remove_flag:
                    self.card_list.remove(sprite)

        #Snap

        

        if snap == True and not self.show_snap_buttons:
        # Add buttons when snap is True
            for button in self.player_buttons:
                self.manager.add(button)
            self.show_snap_buttons = True

        elif snap == False and self.show_snap_buttons:
        # Remove buttons when snap is False
            for button in self.player_buttons:
                self.manager.remove(button)
            self.show_snap_buttons = False




        self.frame+=1
    def on_click_turn(self,event):
        print('Button clicked!')
        if snap==False:
            self.playerturn()
            global player_index
            player_index+= 1

    def on_click_exit(self,event):
        print("Exit!")
        arcade.exit()

    def player1_snap(self,event,button):
    # Code to execute when player 1's button is pressed
        print("Player 1 button pressed!")
        pwayers.append('player1')
        print(pwayers)
        self.manager.remove(button)
        
    def player2_snap(self,event,button):
    # Code to execute when player 2's button is pressed
        print("Player 2 button pressed!")
        pwayers.append('player2')
        print(pwayers)
        self.manager.remove(button)
    def player3_snap(self,event,button):
    # Code to execute when player 3's button is pressed
        print("Player 3 button pressed!")
        pwayers.append('player3')
        print(pwayers)
        self.manager.remove(button)
    def player4_snap(self,event,button):
    # Code to execute when player 4's button is pressed
        print("Player 4 button pressed!")
        pwayers.append('player4')
        print(pwayers)
        self.manager.remove(button)

class whistGame(arcade.Window):
    print("Placeholder")

def main():
    """ Main function """
    startup()
    window = snapGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
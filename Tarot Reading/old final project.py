import random
import sys
from tkinter import*
import tkinter as tk
from PIL import Image




# 22 cards total-create 22 cards
# shuffle 22 cards and randomly choose first three from the deck
# each one represent past, present and future 
# each card can be uprighted or inverted
# three cards located at a certain position on the screen, and I will create a position list. 
# name of the card --- direction---meaning

card_list = [('blank','Error','Error'),
    ('The Fool','Free-spirit Purity Beginning','Foolish Careless Naive'),
    ('The Magician', 'Inventive Manifestation True-potential','Trickery Manipulation Untapped-potential'),
    ("The High Priestess", "Intuition Serenity Divine Goddess", "Reconnect Neglect Secrets"),
	("The Emperor", "Authority Ambition Power", "Tyranny Domination Headstrong"),
	("The Hierophant", "Conventional Institution Tradition", "Rebel Maverick Confinement"),
	("The Lovers", "Love Alighment Choices", "Imbalance Misalignment Differences" ),
	("The Chariot", "Victory Willpower Inner-drive", "Directionless Off-course Roaming"),
	("Strength",  "Fierce Endurance Courage","Apprehensive Doubtful Anxious" ),
	("The Hermit","Soul-searching Reflection Truth", "Loneliness Confinement Withdrawal"),
	("Wheel of Fortune","Change Fate Karma","Injustic Unfair Delinquency"),
	("Justice","Law Objective Fair","Injustic Unfair Delinquency"),
	("The Hanged Man","Sacrifice Patience Suspension", "Avoidance Sacrifice Delay"),
	("Death", "Change Ending Rebirth", "Imbalance Discord Frustration"),
	("Temperance", "Balance Patience Synergy", "Imbalance Discord Frustration"),
	("The Devil", "Addiction Enslavement Fears", "Awareness Breaking-free Enpowerment"), 
	("The Tower", "Destruction Abrupt-change Lightning","Warning Fear-of-change Avoidance"), 
    ("The Star", "Healing Inspiration Serenity", "Uninspired Dark Adrift"),
    ("The Moon","Surreal Subconcious Shadow", "Confusion Mixed-signals Hazy"), 
    ("The Sun", "Positive-vibes Warmth Radiance","Lack-luster Cloudy Unrealistic"), 
    ("Judgment", "Absolution Evaluation Reflection","Doubts Self-judgment Over-critical"), 
    ("The world","Completion Achievement Unity", "Final-stretch Impediment Hindrance")]
	

#Bright meaning & Dark meaning intercept should be clear

class Interface:
    def __init__(self, screen_size, card_list):
        self.root = tk.Tk()
        self.root.title("Tarot Game") 
        self.screen_size = screen_size # store the variable into the class as screen_size
    
        self.last_click_position = None 
        self.last_key_press = None
        self.card_list = card_list
        
        #self.card = Card(self.card_list[i], self.orientation)

        self.create_main_frame() 

        self.create_button_frame() 
     

    def create_button_frame(self):

        self.button_frame = tk.Frame(self.root)
        self.start_button = tk.Button(self.button_frame, text="Start", fg="black",bg = "green", command=self.start)# fg: color of the text, command will define later, as a new function, a method in the class. 
        self.reset_button = tk.Button(self.button_frame, text="Reset", fg="black", bg = "yellow",command=self.reset)
        self.quit_button = tk.Button(self.button_frame, text="Quit", fg="black", bg = "red", command=self.quit)
        # self.button_frame.pack()
        # self.start_button.pack(side=tk.LEFT)
        # self.reset_button.pack(side=tk.LEFT)
        # self.quit_button.pack(side=tk.LEFT)
        self.button_frame.grid()
        self.start_button.grid(row = 2, column = 2)
        self.reset_button.grid(row = 3, column = 2)
        self.quit_button.grid(row = 4, column = 2)

        self.agent_photo = PhotoImage(file = 'agent.jpg')
        self.agent = Label(image = self.agent_photo)
        self.welcome_txt = Label(self, text = '')

    def create_main_frame(self):
        self.main_frame = tk.Frame(self.root, width = self.screen_size[0], height = self.screen_size[1])
        #self.main_frame.pack()
        self.main_frame.grid()
        self.main_canvas = tk.Canvas(self.main_frame, width = self.screen_size[0], height = self.screen_size[1], background = 'black')
        #self.main_canvas.pack()
        self.main_canvas.grid()
        self.main_canvas.focus_set()
        #self.main_canvas.bind("<Button-1>", self.main_canvas_click)
        #self.main_canvas.bind("key", self.key_press)# def key_press(self, key)
        #self.card_show = tk.Button(self.main_frame, image = self.card.image, command = self.show_me_the_card)
        
        self.card_orientation()
        self.get_card_list()
        self.redraw()
        self.blank_card = Card(self.cards, 'up')
        self.get_active_cards()
        self.active_card_list = [self.blank_card, self.blank_card, self.blank_card]
        self.build_position_list()
       
        #self.print_out_lines()

    def card_orientation(self):
    	orientation_list = ['up', 'down']
    	self.orientation = random.choice(orientation_list)

    def redraw(self):
    	self.active_card_list = [self.blan_card, self.blank_card, self.blank_card]
    	self.blank_card = Card(self.cards[0], 'up')


    def get_card_list(self):
        # cards is the list of instance, and card is each instance. 
        self.cards = []
        i = 1
        for i in range(0, len(self.card_list)):
        	#name Card is not defined
        	self.card = Card(self.card_list[i], self.orientation)
        	self.cards.append(self.card)
        return self.cards
        print(self.cards)
      
        
        

    def get_active_cards(self):
        
        # shuffle the list and draw three out
       
        random.shuffle(self.cards)
        print("Three chosen cards are:")
      
        self.chosen_card = self.cards[0:2]
        print(self.chosen_card)
        self.active_card_list[0] = self.chosen_card[0]
        self.active_card_list[1] = self.chosen_card[1]
        self.active_card_list[2] = self.chosen_card[2]

    
    	
    def build_position_list(self):

        self.past_pos = (240, 240)
        self.present_pos = (120, 120)
        self.future_pos = (360, 120)
        self.pos_list = [self.past_pos, self.present_pos, self.future_pos]

    def show_cards(self):
        self.active_name = []

        for card_in in self.chosen_card:
            self.active_name =card_in.name  
            load = Image.open(self.active_name + '.png')
            render = ImageTK.PhotoImage(load)

            img = Label(self.image == render)
            img.image = render
            for pos in self.pos_list:
    	        img.place(pos)

class Card:
    def __init__(self, card, orientation):
       
       
        self.name = card[0]
        
        self.orientation = orientation 
        self.image = tk.PhotoImage(file=self.name+".png")
        self.meaning = None 
        if self.orientation == 'down':
            self.show = self.image.transpose(Image.FLIP_TOP_BOTTOM)
            self.meaning = card[2]
        else:
            self.show = self.image
            self.meaning = card[1]
        
#         im = Image.open(self.name + ".png")
#         if self.orientation == "up":
#         	im.show()
#         	self.meaning = card[1]
#         else:
#         	im.rotate(180).show
#         	self.meaing = card[2]
    
# def main():

    screen_size = (900, 800)
    my_game = Interface(screen_size, card_list)
    my_game.root.mainloop()
	

main()

	
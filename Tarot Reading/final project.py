from tkinter import*
import tkinter as tk
from PIL import Image
import random
import sys
import itertools

###Card tuple###

blank_card = ('blank', 'error', 'error')

card_list = [
    ('The Fool','Free-spirit Purity Beginning','Foolishness Carelessness Naivete'),
    ('The Magician', 'Inventiveness Manifestation True-potential','Trickery Manipulation Untapped-potential'),
    ("The High Priestess", "Intuition Serenity Divine Goddess", "Reconnect Neglect Secrets"),
    ("The Emperor", "Authority Ambition Power", "Tyranny Domination Headstrong"),
    ("The Hierophant", "Conventionality Institution Tradition", "Rebel Maverick Confinement"),
    ("The Lovers", "Love Alighment Choices", "Imbalance Misalignment Differences" ),
    ("The Chariot", "Victory Will-power Inner-drive", "Directionlessness Off-course-ideas Roaming"),
    ("Strength",  "Fierce Endurance Courage","Apprehensiveness Uncertainty Anxiety" ),
    ("The Hermit","Soul-searching Reflection Truth", "Loneliness Limitation Withdrawal"),
    ("Wheel of Fortune","Change Fate Karma","Unfortunate-events Resisting-change Letting-go"),
    ("Justice","Law Objectification Fair","Injustice Unfairness Delinquency"),
    ("The Hanged Man","Sacrifice Patience Suspension", "Avoidance Sacrifice Delay"),
    ("Death", "Change Ending Rebirth", "Imbalance Discord Frustration"),
    ("Temperance", "Balance Patience Synergy", "Imbalance Discord Frustration"),
    ("The Devil", "Addiction Enslavement Fears", "Awareness Breaking-free Enpowerment"), 
    ("The Tower", "Destruction Abrupt-change Lightning","Warning Fear-of-change Avoidance"), 
    ("The Star", "Healing Inspiration Serenity", "Uninspiring-events Dark Adrift"),
    ("The Moon","Surreality Subconciousness Shadow", "Confusion Mixed-signals Hazy"), 
    ("The Sun", "Positive-vibes Warmth Radiance","Lackluster Cloudy Unrealisticity"), 
    ("Judgment", "Absolution Evaluation Reflection","Doubts Self-judgment Over-critical"), 
    ("The world","Completion Achievement Unity", "Final-stretch Impediment Hindrance")]


###create the main window and interaction system###

class Interface:
    def __init__(self, screen_size, card_list):

        self.root = tk.Tk()
        self.root.title("Tarot Game")
        self.root.configure(background = 'deep sky blue')

        self.screen_size = screen_size
        # the list of tuples of cards(code)
        self.card_list = card_list
        # the list of instances
        self.cards = []
      
        # define the location of cards
        # define the activate cards(3)
        # 
        self.create_main_frame()#self.card_orientation/self.get_card_list/self.get_active_cards/self.build_position_;ist()
        self.create_button_frame()

    def create_button_frame(self):

        self.button_frame = tk.Frame(self.root, bg = 'deep sky blue')
        self.start_button = tk.Button(self.button_frame, text = 'Start', fg= 'black', bg = 'lightgreen', command = self.start)
        self.reset_button = tk.Button(self.button_frame, text = 'Explain', fg = 'black', bg = 'lightblue', command = self.explanation)
        self.quit_button = tk.Button(self.button_frame, text = 'Quit', fg = 'black', bg = 'pink', command = self.quit)
        
        self.button_frame.grid()

        self.start_button.grid(row = 2, column = 1, columnspan = 2)
        self.reset_button.grid(row = 3, column = 1,columnspan = 2)
        self.quit_button.grid(row = 4, column = 1, columnspan = 2)
        #introducer

        self.agent_photo = PhotoImage(file = 'agent.png')

        self.agent = Label(image = self.agent_photo)

        self.welcome_txt = Label(self.root, text = """
            Welcome to the Tarot game! This is a \n
            intuition tool for spiritual guidance.\n
            You will have three cards representing \n
            past, present, and future(left to right).\n 
            Three key words will be given for each card.\n 
            In the end, there will be a mad_lib paragraph \n
            as an overall explanation.""" )
        
        self.agent.grid(row = 2, column = 1,columnspan = 1, padx = 2, pady= 2)

        self.welcome_txt.grid(row = 2, column =2, columnspan = 2, padx = 2, pady = 5)


    
    def create_main_frame(self):

        self.main_frame = tk.Frame(self.root, width = self.screen_size[0], height = self.screen_size[1])
        self.main_frame.grid()
        self.main_canvas = tk.Canvas(self.main_frame, width = self.screen_size[0], height = self.screen_size[1], background = 'SteelBlue1')
        self.main_canvas.grid(row = 0, column = 0 , columnspan = 20, rowspan = 20, sticky = W+E+N+S, padx = 5, pady = 5)
        self.main_canvas.focus_set()

    
        # get card list of all cards, get the original three blank cards, and get three random cards to change three original cards in a specific position arrangement. 
        #self.get_card_list()
        
        
        self.blank_cards()

        self.create_card_deck()

        #self.draw_cards()
        
        

    def create_card_deck(self):

        for i in range(0, len(self.card_list)):

            self.card_orientation()

            self.card = Card(self.card_list[i], self.orientation)

            self.cards.append(self.card)#cards 变成real cards

            i += 1

        return self.cards


    def draw_cards(self):
        
        self.current_card_list = []
        
        for card in self.cards: 

            if card == self.blank_card:

        	    self.cards.remove(self.blank_card)
  
        for i in range(3):
            #current_card in self or not
            self.current_card = self.cards[i]

            self.current_card_list.append(self.current_card)

            Label(self.root, image = self.current_card.image).grid(row = 0, column = i , columnspan = 1, rowspan = 2, padx = 2, pady = 2)
    
    def card_orientation(self):

        orientation_list = ['up', 'down']

        self.orientation = random.choice(orientation_list)

        return self.orientation

    def blank_cards(self):
        
        self.blank_card = Card(blank_card, 'up')

        self.cards = [self.blank_card, self.blank_card, self.blank_card]
        # self.blank_cards = [self.blank_card, self.blank_card, self.blank_card]
        for i in range(3):

            current_card = self.cards[i]

            Label(self.root, image = current_card.image).grid(row = 0, column = i ,  columnspan = 1, rowspan = 2, padx = 2, pady = 2)


    def start(self):

        
        random.shuffle(self.cards)

        self.draw_cards() 
    
    # to generate the explanation report

    def explanation(self):

        self.good_input = []

        self.bad_input = []
        
        self.chosen_card_list = []

        
        # for card in self.card_list:
        # 	if str(card[0]) == str(self.current_card.name):
        # 		self.chosen_card_list.append(card)

        for self.card in self.current_card_list:

            for i in range(0, len(self.card_list)):
            
                if self.card_list[i][0] == self.card.name:
         	        self.chosen_card_list.append(self.card_list[i])
         	        i += 1
        
        for i in self.chosen_card_list:
        	print(i)


        
        for item in self.chosen_card_list:
        #for item in self.card_list:
            good_meaning = str(item[1])

            good_meaning = good_meaning.lower()
            good_words = good_meaning.split(' ')
            for word in good_words:
                self.good_input.append(word)

            #print(self.good_input)
            bad_meaning = str(item[2])

            bad_meaning = bad_meaning.lower()
            bad_words = bad_meaning.split(' ')
            for word in bad_words:
                self.bad_input.append(word)
            
        # the over report should be a combination of three cards 
        random.shuffle(self.good_input)
        random.shuffle(self.bad_input)


        
        self.lines_past = """
        You might have trouble managing {3} in the past, but you were good at playing with the game of {0}. \n
        There was a certain {4} with how you were living your day-to-day. Seeking {1} tended to be a solo journey. \n
        You might find your {2} inside. You were seeking your deep inner truth to beat the {5}.
        """.format(self.good_input[0], self.good_input[1],self.good_input[2],self.bad_input[0], self.bad_input[1], self.bad_input[2])

        self.lines_present = """
        Now it can indicate {0} and lack of {3}. \n
        You may feel that you have so much {1} to give, but that your talents are not being seen. \n
        The {4} is blocking you. {5} is hindering you and keeping you in a box. Infinite {2} is available as you continue to flow.
        """.format(self.good_input[3], self.good_input[4],self.good_input[5],self.bad_input[3], self.bad_input[4], self.bad_input[5])

        self. lines_future = """
        In the future, remember that this period of {0} is a choice, and you can free yourself from {3}, {4}, and {5}.\n
        Know that you are not alone and that whenever you decide to reach out, a helping hand of {1} and {2}, will be there to support you.
        """.format(self.good_input[6], self.good_input[7],self.good_input[8],self.bad_input[6], self.bad_input[7], self.bad_input[8])

        
        self.explanation_lines =  self.lines_past + self.lines_present + self.lines_future

        self.explain_txt = Label(self.root, text = self.explanation_lines)

        self.explain_txt.grid(row = 3, column = 0, rowspan = 2, columnspan = 2,  padx = 5, pady = 5)
 
        return self.explain_txt


    def quit(self):
        sys.exit()




class Card:

    def __init__(self, card, orientation):
        # for card in card_list, which is the tuple(name, good, bad)
        self.name = card[0]
        self.good_side = card[1]
        self.bad_side = card[2]
        self.orientation = orientation
        # self.x = 100
        # self.y = 100
        
        if self.orientation == 'up':
            self.image = tk.PhotoImage(file = self.name + '.png')
        else:
            self.image = tk.PhotoImage(file = 'inverted/' + self.name +'_iv.png')

       

def main():
    screen_size = (100, 100)
    my_game = Interface(screen_size, card_list)
    my_game.root.mainloop()

main()
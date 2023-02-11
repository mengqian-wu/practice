# import the random module
# use "winnings = random.randint(2, 10)" to generate a random int from 2 - 10 and store in a variable "winnings"
import random



def start_shopping():
    

    welcome = """
    Welcome to the supermarket!  Here's what we have in stock:
    - Lottery tickets cost $2 each
    - Apples cost $0.99 each
    - Cans of beans cost $1.58 each
    - Sodas cost $1.23 each
"""
    print(welcome)

def warning_message():

    if ans not in ['y', 'Y', 'n', 'N']:
        raise Exception("Sorry, please type y or n.")

def lott_game(money):

    lottery_note = """
    You have $5 available. 
    First, do you want to buy a $2 lottery ticket for a chance at wining $2 - $10? (y/n)
"""
    ans = input(lottery_note)

    if ans not in ['y', 'Y', 'n', 'N']:
        raise Exception("Sorry, please type y or n.")

    else:
        if ans in ["Y", "y"]:
            lottery = 1
            money = money - 2
            select_lst = ['A', 'B', 'C']
            win = random.choice(select_lst)

            if win == 'A':
                winnings = random.randint(2, 10)
                money += winnings
                print("Congrats! You won {}".format(winnings))
            else:
                winnings = 0
                print("Sorry! You did not win the lottery.")

        else:
            lottery = 0
            winnings = 0
            print("Thanks! You will not buy a lottery. Now you still have ${}".format(money))

    return money, lottery, winnings
    

def apple_shopping(money, money_spent,apple_amount):

    #  Questions
    apple_note = """
    You have ${} available. 
    Do you want to buy apple(s)? (y/n)""".format(money)

    much_apple = """
    How many apple(s) do you want to buy?"""

    # Purchase Apples
    apple_buy = input(apple_note)

    if apple_buy not in ['y', 'Y', 'n', 'N']:
        
        raise Exception("Sorry, please type y or n.")

    else:

        if apple_buy in ['y', 'Y']:
            apple_num= input(much_apple)
            limit = money/0.99
            
            if apple_num.isnumeric() == True and int(apple_num) <= limit:
                apple_num = int(apple_num)
                apple_amount = apple_num
                apple_cost = apple_num * 0.99

                money_spent += apple_cost 
                money -= apple_cost 

                print("""
                    The user wants to buy {} apple(s). This will cost ${}. 
                    The user has enough money. {} apple(s) purchased.""".format(apple_num, apple_cost, apple_num))

            else:
                apple_amount = 0
                print("Something went wrong. Pick a numeric number or buy less soda please.")

        else:
            apple_amount= 0
            print('No apple purchased!')

    return money, money_spent, apple_amount


def bean_shopping(money, money_spent, canned_beans_amount):

    # Questions
    bean_note = """
    You have ${} available. 
    Do you want to buy can(s) of beans? (y/n)""".format(money)

    much_bean = """
    How many can(s) of bean do you want to buy?"""

    # Purchase Bean
    bean_buy = input(bean_note)

    if bean_buy not in ['y', 'Y', 'n', 'N']:
        
        raise Exception("Sorry, please type y or n.")

    else:

        if bean_buy in ['y', 'Y']:
            bean_num= input(much_bean)
            limit = money/1.58
            

            if bean_num.isnumeric() == True and int(bean_num) <= limit:
                bean_num = int(bean_num)
                canned_beans_amount = bean_num
                bean_cost = bean_num * 1.58

                money_spent += bean_cost 
                money -= bean_cost 

                print("""
                    The user wants to buy {} can(s) of bean. This will cost ${}. 
                    The user has enough money. {} can(s) of bean purchased.""".format(bean_num, bean_cost, bean_num))

            else:
                canned_beans_amount = 0
                print("Something went wrong. Pick a numeric number or buy less please..")

        else:
            print('No cans of bean purchased!')
    
    return money, money_spent, canned_beans_amount



def soda_shopping(money, money_spent, soda_amount):

    #  Questions

    soda_note = """
    You have ${} available. 
    Do you want to buy soda(s)? (y/n)""".format(money)

    much_soda = """ 
    How many soda(s) do you want to buy?"""


    # Purchase Apples
    soda_buy = input(soda_note)

    if soda_buy not in ['y', 'Y', 'n', 'N']:
        
        raise Exception("Sorry, please type y or n.")

    else:

        if soda_buy in ['y', 'Y']:
            soda_num= input(much_soda)
            limit = money/1.23

            if soda_num.isnumeric() == True and int(soda_num) <= limit:
                soda_num = int(soda_num)
                soda_amount = soda_num
                soda_cost = soda_num * 1.23

                money_spent += soda_cost 
                money -= soda_cost 

                print("""
                    The user wants to buy {} apple(s). This will cost ${}. 
                    The user has enough money. {} apple(s) purchased.""".format(soda_num, soda_cost, soda_num))

            else:
                soda_amount = 0
                print("Something went wrong. Pick a numeric number or buy less soda please.")

        else:
            soda_amount = 0
            print('No soda purchased!')

    return money, money_spent, soda_amount

        

def main():
    # unit price of a lottery ticket
    constant_lottery_unit_price = 2

    # unit price of an apple
    constant_apple_unit_price = .99

    # unit price of a can of beans
    constant_canned_beans_unit_price = 1.58

    # unit price of a soda
    constant_soda_unit_price = 1.23

    # the user has initial $5 for shopping
    money = 5

    # the user has spent $0 initially
    money_spent = 0

    # the amounts of lottery tickets, apples, cans of beans, and sodas the user has purchased
    lottery_amount, apple_amount, canned_beans_amount, soda_amount = 0, 0, 0, 0

    start_shopping()
    money, lottery,winnings = lott_game(money)
    money, money_spent, apple_amount = apple_shopping(money, money_spent, apple_amount)
    money, money_spent, bean_amount = bean_shopping(money, money_spent, canned_beans_amount)
    money, money_spent, soda_amount = soda_shopping(money, money_spent, soda_amount)
    
    print("""
    
    Money left: ${}
    Lottery ticket(s) pruchased: {}
    Lottery winnings: {}
    Apple purchased:{}
    cans of bean purchased:{}
    soda purchased:{}

    Good bye!

        """.format(money, lottery, winnings, apple_amount, bean_amount, soda_amount))









main()
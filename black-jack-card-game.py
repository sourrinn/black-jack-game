#Dt.20.02.2021
#Dev.: Sourin Biswas
#Topic: [Card Game] Simplied BlackJack

import random
import pdb

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

def ace_value():
    n=True
    while n:
        r=input("Enter Ace Value: ")
        if r=='11' or r=='1':
            n=False
        elif r!='1' or r!='11':
            print('Enter a value 1 or 11!')
#    values['Ace']=int(r)
    if 'Ace' in values.keys():
    # do something with value
        values['Ace'] = int(r)
    print('Value of ace is {}!'.format(values['Ace']))

class Card:
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
        
    def __str__(self):
        return self.rank + ' of ' + self.suit

class Deck:
    
    def __init__(self):
        # Note this only happens once upon creation of a new Deck
        self.all_cards = [] 
        for suit in suits:
            for rank in ranks:
                # This assumes the Card class has already been defined!
                self.all_cards.append(Card(suit,rank))
                
    def shuffle(self):
        # Note this doesn't return anything
        random.shuffle(self.all_cards)
        
    def deal_one(self):
        # Note we remove one card from the list of all_cards
        return self.all_cards.pop()

class Player:
    
    def __init__(self,name):
        self.name = name
        # A new player has no cards
        self.all_cards = [] 
        
    def remove_one(self):
        # Note we remove one card from the list of all_cards
        # We state 0 to remove from the "top" of the deck
        # We'll imagine index -1 as the bottom of the deck
        return self.all_cards.pop(0)
    
    def add_cards(self,new_cards):
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)

    def ask_balance(self):
    	bal_game=True
    	while bal_game:
	    	balance_update=input('Enter your bank balance: $')
	    	if balance_update.isdigit():
	    		if int(balance_update)>=200 and int(balance_update)<=10000:
	    			bal_game=False
	    		else:
	    			print('Enter a valid amount greater than $200 but less than $10000!')
	    	else:
	    		print('Enter a valid amount greater than $200 but less than $10000!')
    	self.balance=int(balance_update)
    
    def ask_bet(self):
    	bet_game=True
    	while bet_game:
    		bet_update=input('Enter your bet amount: $')
    		if bet_update.isdigit():
    			if int(bet_update)>=2 and int(bet_update)<501 and int(bet_update)<=self.balance:
    				bet_game=False
    			else:
    				print('Enter a valid amount greater than $2 but less than $501!')
    		else:
    			print('Enter a valid amount greater than $2 but less than $501!')
    	self.bet=int(bet_update)
    	print(f'You have ${self.bet} on your bet amount!' )

    def value_reset(self):
    	self.sum=0

    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards.'

#Game Logic
your_name=input('Enter you in-game name: ')
player_one = Player(your_name)
dealer = Player("Dealer")

#New Game
new_deck = Deck()
new_deck.shuffle()
		
player_one.ask_balance()
dealer.balance=player_one.balance

player_one.value_reset()
dealer.value_reset()

game_on = True
round_num = 0
while game_on:
	#Round Begins!
	round_num += 1
	print(f"Round {round_num}")

	#Betting Begins
	print(f'You have ${player_one.balance} in your wallet!' )
	player_one.ask_bet()
	player_one.balance-=player_one.bet
	#Card Storage Declaration
	player_one_cards=[]
	dealer_cards=[]

	#Card Deals
	player_one_cards.append(new_deck.deal_one())
	print(f'Player\'s Card: {player_one_cards[-1]}')
	if 'Ace' in player_one_cards[-1].rank:
		print('I found an Ace. Bravo!')
	if player_one_cards[-1].rank==11:
		ace_value()
		player_one_cards[-1].value=values['Ace']
	dealer_cards.append(new_deck.deal_one())
	print(f'Dealer\'s Card: {dealer_cards[-1]}')
	#Card Deals
	player_one_cards.append(new_deck.deal_one())
	print(f'Player\'s Card: {player_one_cards[-1]}')
	if 'Ace' in player_one_cards[-1].rank:
		print('I found an Ace. Bravo!')
	if player_one_cards[-1].value==11:
		ace_value()
		player_one_cards[-1].value=values['Ace']
	dealer_cards.append(new_deck.deal_one()) #Dealer's second card is not to be shown!

	#THE PLAY
	player_one.sum = player_one_cards[-1].value + player_one_cards[-2].value
	print(f'The sum of Cards for Player {player_one.name} is {player_one.sum}!')

	if player_one.sum==21:
		dealer.balance-=1.5*player_one.bet
		player_one.balance+=2.5*player_one.bet
		print(f'You won the Round and got ${1.5*player_one.bet}! \nAvailable Wallet Balance: ${player_one.balance}')

	if player_one.sum<21:
		act=True
		while act:
			action=input("Choose to \'Hit\' or \'Stay\':")
			if action=='Hit' or action=='hit':
				player_one_cards.append(new_deck.deal_one())
				print(f'Player\'s Card: {player_one_cards[-1]}')
				if 'Ace' in player_one_cards[-1].rank:
					print('I found an Ace. Bravo!')
				if player_one_cards[-1].value==11:
					ace_value()
					player_one_cards[-1].value=values['Ace']
				player_one.sum+=player_one_cards[-1].value
				print(f'The sum of Cards for Player {player_one.name} is {player_one.sum}!')
				hit_go=True
				while hit_go:
					hit_again=input('Do you want to hit again? Yes/No: ')
					if hit_again=='Yes' or hit_again=='yes':
						hit_go=False
					elif hit_again=='No' or hit_again=='no':
						hit_go=False
						act=False
					else:
						print('Please enter a valid option!')
			elif action=='Stay' or action=='stay':
				act=False
			else:
				print("Enter a valid value between \'Hit\' or \'Stand\'!")
	
	if player_one.sum>21:
		print(f'Player {player_one.name} has been bust! The bet amount is Lost.')
		dealer.balance+=player_one.bet

	#THE DEALER'S PLAY
	print(f'The dealer\'s face down card is now revealed to be {dealer_cards[-1]}!')
	temp_sum = dealer_cards[-2].value
	temp_sum2 = temp_sum + dealer_cards[-1].value
	temp_sum=temp_sum2
	auto=False
	auto_check=True
	while auto_check:
		if temp_sum2<17:
			pass
		elif temp_sum2>=17 and temp_sum2<=21:
			auto_check=False
			auto=False
			dealer.sum=temp_sum2
			break
		elif temp_sum2>21:
			if dealer_cards[-1].value==11:
				if dealer_cards[-1].value==11:
					dealer_cards[-1].value=1
				auto_check=False
				auto=True
				break
			elif dealer_cards[-2].value==11:
				if dealer_cards[-2].value==11:
					dealer_cards[-2].value=1
				auto_check=False
				auto=True
				break
			elif dealer_cards[-1]!=11:
				auto_check=False
				dealer.sum=temp_sum2
				if dealer_cards[0].value==11:
					if dealer_cards[0].value==11:
						dealer_cards[0].value = 1
					auto=True
				break
		dealer_cards.append(new_deck.deal_one())
		print(f'A {dealer_cards[-1]} has been added to Dealer\'s collection!')
		temp_sum2 = temp_sum + dealer_cards[-1].value
		temp_sum=temp_sum2

	if auto:
		temp_sum=0
		while len(dealer_cards)!=0:
			temp_sum+=dealer_cards[-1].value
			dealer_cards.pop()
		dealer.sum=temp_sum #with Ace Value = 1q
		print(f'Till Now, Dealer\'s sum is calculated to be ${dealer.sum} with \'Ace Value: 1\'')
		last_check=True
		while last_check:
			if dealer.sum<17:
				pass
			elif dealer.sum>=17 and dealer.sum<=21:
				last_check=False
				break
			elif dealer.sum>21: #busted
				print(f'Dealer has been bust! Twice the bet amount is rewarded to Player {player_one.name}')
				dealer.balance-=player_one.bet
				player_one.balance+=2*player_one.bet
				last_check=False
				break
			dealer_cards.append(new_deck.deal_one())
			if dealer_cards[-1].value==11:
				dealer_cards[-1].value=1
			print(f'A {dealer_cards[-1]} has been added to Dealer\'s collection again!')
			dealer.sum+=dealer_cards[-1].value
			print(f'Till Now, Dealer\'s sum is calculated to be ${dealer.sum} with \'Ace Value: 1\'')

	#Settlements
	print(f'Dealer\'s sum: {dealer.sum}')
	if dealer.sum>=17 and dealer.sum<=21:
		if player_one.sum<=21:
			if dealer.sum>player_one.sum:
				dealer.balance+=player_one.bet
				print(f'Oops! Player {player_one.name} lost the bet amount!')
			elif dealer.sum<player_one.sum:
				dealer.balance-=player_one.bet
				player_one.balance+=player_one.bet
				print(f'Congrats! Player {player_one.name} won double the bet amount!')
			else:
				print('Both the sums are equal. Cheers to No Loss, No Gain!')

	#Force Exit Condition for Player
	continue_game=True
	while continue_game:
		proceed=input('Do you want to continue? Yes/No: ')
		if proceed=='Yes' or proceed=='yes':
			continue_game=False
		elif proceed=='No' or proceed=='no':
			continue_game=False
		else:
			print('Please Choose \'Yes\' or \'No\'')
	if proceed=='No' or proceed=='no':
		print(f"Player {player_one.name} decides to quit!")
		game_on=False

	#Out of Funds Condition for Player
	if player_one.balance<2:
		print(f'Player {player_one.name}\'s Wallet Balance is ${player_one.balance} which is not sufficient to continue!')
		print(f'Game Over! Player {player_one.name} is out of game.')
		game_on=False

	#Out of Cards Condition
	if len(new_deck.all_cards)<10:
		print('Deck is out of sufficient Cards to continue BlackJack Game! \nCasino requests you to restart the game. Hope you had a great time.')
		game_on=False
		break
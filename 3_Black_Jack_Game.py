# Hello this is my 3rd Milestone Project !!!


import random 
print('Welcome To Black Jack Game !!!')
print('\n'*100)

suits = ['Diamonds', 'Hearts', 'Spades', 'Clubs']
ranks = ['Ace', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'Jack', 'Queen', 'King']
values = {'two' : 2, 'three' : 3, 'four' : 4, 'five': 5, 'six' : 6, 'seven' : 7, 'eight' : 8, 'nine' : 9, 'ten' : 10, 'Jack' : 10, 'Queen' : 10, 'King' : 10, 'Ace' : 11}

#-------------------------------------------------------------------------------------------------------------------------------------------

class Card():
    
    def __init__(self, suit, rank):

        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):

        return self.rank + ' of ' + self.suit
    
#-------------------------------------------------------------------------------------------------------------------------------------------

class Deck():
    
    def __init__(self):

        self.all_cards = []
        self.cards_distributed_player = []
        self.cards_distributed_dealer = []

        for suit in suits:
            for rank in ranks:
                new_card = Card(suit, rank)

                self.all_cards.append(new_card)

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_two_player(self):
           
        for cards in range(2):
            self.cards_distributed_player.append(self.all_cards.pop(0))
 
        return self.cards_distributed_player
    
    def deal_two_dealer(self):
           
        for cards in range(2):
            self.cards_distributed_dealer.append(self.all_cards.pop(0))
 
        return self.cards_distributed_dealer
    
    def deal_one(self):
        
        card = []
        card.append(self.all_cards.pop(0))
        return card

    def __str__(self):
        return f'Total remaining cards : {len(self.all_cards)} and cards distributed till now : {len(self.cards_distributed_player) + len(self.cards_distributed_dealer)}'

#-------------------------------------------------------------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------------------------------------------------------------

class PlayerDealer():
    
    def __init__(self, balance):
        
        self.balance = balance
        self.bid = 0

    def bid_player(self):
        
        bid = int(input('How much do you want to bid ? : '))
        return bid
    
    def ask_stand_hit(self):
        
        val = ['h', 's']
        s_h = 'oaga'
        while s_h not in val : 
            s_h = input("Do you want to stand or hit (s/h) ? : ")
        return s_h
    
    def __str__(self):
        
        return f'remaining balance : {self.balance}'
    
#-------------------------------------------------------------------------------------------------------------------------------------------

class Hand():
    
    def __init__(self, deck_instance):
        
        self.in_hands_player = []
        self.in_hands_dealer = []
        self.deck_instance = deck_instance

    def get_cards_player(self):
        
        for i in range(2):
            self.in_hands_player.append(self.deck_instance.all_cards.pop(0))

        return self.in_hands_player
    
    def get_cards_dealer(self):
        
        showing = []
        for i in range(2):
            self.in_hands_dealer.append(self.deck_instance.all_cards.pop(0))

        showing.append(self.in_hands_dealer.pop(0))
        return showing
    
    def get_hit_player(self):

        new_card = self.deck_instance.deal_one()
        self.in_hands_player.extend(new_card)
        return self.in_hands_player
    
    def get_hit_dealer(self):

        new_card = self.deck_instance.deal_one()
        self.in_hands_dealer.extend(new_card)
        return self.in_hands_dealer
    
    def show_cards_dealer(self, showing):
        
        showing.append(self.in_hands_dealer.pop(0))
        return showing
    
#-------------------------------------------------------------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------------------------------------------------------

# Game Logic :

new_deck = Deck()
new_deck.shuffle()
player = PlayerDealer(500)
bal = player.balance

player_in_hand = Hand(new_deck)
dealer_in_hand = Hand(new_deck)

game_on = True
want_to_play = True

while want_to_play:
    
    while game_on:

        print(f'Current balance = {bal}')
        print('\n')
        bid = player.bid_player()
        print('\n')
        if bal == 0:
            game_on = False
        
        while bid > bal:
            
            if bid > bal:
                print("Sorry, You don't have enough balance to bid...")
                bid = player.bid_player()

            else:
                print("Sorry, You don't have enough balance to bid...")
                break
        
        hand_player = player_in_hand.get_cards_player()
        hand_dealer = dealer_in_hand.get_cards_dealer()

        print('Cards with Players : ')
        print('\n')
        print(f'{hand_player[0]}  {hand_player[0].value}')
        print(f'{hand_player[1]}  {hand_player[1].value}')
        print('\n'*2)

        print('Cards with dealer : ')
        print('\n')
        print(f'{hand_dealer[0]}  {hand_dealer[0].value}')
        print('\n'*2)

        hand_dealer = dealer_in_hand.show_cards_dealer(hand_dealer)

        if hand_player[0].value + hand_player[1].value > 21:
            print('Player has busted the limit and lost the bet !!!')
            print('Computer dealer has won the bid !!!')
            print('\n')
            print(hand_player[0].value + hand_player[1].value)
            print('\n')
            print('Current cards with dealer : ')
            print('\n')
            print(f'{hand_dealer[0]}  {hand_dealer[0].value}')
            print(f'{hand_dealer[1]}  {hand_dealer[1].value}')

            bal = bal - bid
            print(f'New balance = {bal}')
            game_on = False
            break
        
        elif hand_player[0].value + hand_player[1].value == 21:
            print('Player has won the bid !!!')
            print('\n')
            print(hand_player[0].value + hand_player[1].value)
            print('\n')
            print('Current cards with dealer : ')
            print('\n')
            print(f'{hand_dealer[0]}  {hand_dealer[0].value}')
            print(f'{hand_dealer[1]}  {hand_dealer[1].value}')
            bal = bal + bid*2
            print(f'New balance = {bal}')
            game_on = False
            break
        
        elif hand_dealer[0].value + hand_dealer[1].value == 21:
            print('computer dealer has won the match !!!')
            print('\n')
            print(hand_dealer[0].value + hand_dealer[1].value)
            print('\n')
            print('Current cards with dealer : ')
            print('\n')
            print(f'{hand_dealer[0]}  {hand_dealer[0].value}')
            print(f'{hand_dealer[1]}  {hand_dealer[1].value}')

            bal = bal - bid
            print(f'New balance = {bal}')
            game_on = False
            break
        
        run = True
        while run:

            hit_stand = player.ask_stand_hit()
            print('\n')

            print('Current cards with dealer : ')
            print('\n')
            print(f'{hand_dealer[0]}  {hand_dealer[0].value}')
            print(f'{hand_dealer[1]}  {hand_dealer[1].value}')
            print('\n')
            
            while hit_stand == 'h':
                
                hand_player = player_in_hand.get_hit_player()
                print('\n')
                
                print('Cards with player after hitting : ')
                print('\n')
                for card in hand_player:
                    print(f'{card.value}  {card.rank} of {card.suit}') 
                print('\n')
                
                sum = 0
                for i in hand_player:
                    sum = sum + i.value                  
                
                aces = 0
                for card in hand_player:
                    if card.rank == 'Ace' :
                        aces += 1
                
                if sum == 21:
                    print('Player has won the bid !')
                    print(f'The sum of player is : {sum}')
                    bal = bal + bid*2
                    print('\n')
                    print(f'New balance = {bal}')
                    game_on = False
                    run = False
                    break
                
                if sum > 21:
                    
                    if aces :
                        sum -= 10

                    else:
                        print('Busted !!')
                        print('Dealer has won the match !')
                        print('\n')
                        print(f'The sum of player is : {sum}')
                        print('\n')
                        bal = bal - bid
                        print(f'New balance = {bal}')
                        game_on = False
                        run = False
                        break
                
                if sum < 21:
                    print(f'The sum of player is : {sum}')
                    hit_stand = player.ask_stand_hit()
                    print('\n')
        
            if hit_stand == 's':
                
                run1 = True
                while run1:
                    
                    hit = []
                    hit = dealer_in_hand.get_hit_dealer()
                    hand_dealer.extend(hit)
                
                    sum1 = 0
                    for i in hand_dealer:
                        sum1 = sum1 + i.value

                    aces1 = 0
                    for card in hand_dealer:
                        if card.rank == 'Ace' :
                            aces1 += 1
                   
                    if sum1 == 21:
                        print('Cards with dealer after hitting : ')
                        print('\n')
                        for card in hand_dealer:
                            print(f'{card.value}  {card.rank} of {card.suit}') 
                        print('\n')
                        print(f'The sum of dealer is : {sum1}')
                        print('\n')
                        
                        print('Sorry, The computer dealer has won the bid')
                        bal = bal - bid
                        print(f'New balance = {bal}')
                        game_on = False
                        run = False
                        break

                    elif sum1 > 21:
                        
                        if aces1 :
                            sum1 -= 10
                                
                        else:
                            print('Cards with dealer after hitting : ')
                            for card in hand_dealer:
                                print(f'{card.value}  {card.rank} of {card.suit}') 
                            print('\n')
                            print(f'The sum of dealer is : {sum1}')
                            print('\n')
                            
                            print('The dealer is busted !!')
                            print('Congratulations !! The player has won the bid...')
                            bal = bal + bid*2
                            print(f'New balance = {bal}')
                            game_on = False
                            run = False
                            break

                    if sum1 < 21:
                        run1 = True

    
    print('\n')
    play_again = input('Want to bid again ? y/n : ')
    print('\n')

    if play_again == 'y':
        game_on = True

    elif play_again == 'n':
        want_to_play = False       
        break
    else:
        break

# Change the dealer winning logic a bit in a new file
# dealer wins if it has high value than player near 21
                



    







    

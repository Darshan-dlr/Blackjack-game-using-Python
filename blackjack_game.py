import random
suits=("hearts","diamonds","spades","clubs")
ranks=("two","three","four","five","six","seven","eight","nine","ten","jack","queen","king","ace")
values={"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9,"ten":10,"jack":10,"queen":10,"king":10,"ace":11}
playing =True

# class for Cards
class Card:
    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank
        
    def __str__(self):
        return self.rank + " of " +self.suit

 #Class for Deck
class Deck:
    def __init__(self):
        self.deck=[]
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))
     
    def __str__(self):
        deck_comp=''
        for card in self.deck:
            deck_comp+= '\n' +card.__str__()
        return "the deck has:"+deck_comp
    
    def shuffle(self):
        random.shuffle(self.deck)
        
      
    def deal(self):
        single_card=self.deck.pop()
        return single_card

#class for Hand
class Hand:
    def __init__(self):
        self.cards=[]
        self.value=0
        self.aces=0
        
       
    def add_cards(self,card):
        self.cards.append(card)
        self.value +=values[card.rank]
        
        if card.rank=='ace':
            self.aces+=1
            
       
    def adjust_for_ace(self):
            while self.value>21 and self.aces>0:
                self.value -=10
                self.aces-=1
                
#class for Chips for consedring bet
class Chips:
    def __init__(self,total=100):
        self.total=total
        self.bet=0
        
       
    def win_bet(self):
        self.total+=self.bet
        
       
    def lose_bet (self):
        self.total -=self.bet
#function that take input to place the bet & check wheter it is valid or not interms of integer and chips user has
def take_bet(chips):
    while True:
        try:
            chips.bet=int(input("how many chips do you like to bet"))
           
        except:
            print("sorry please provide an integer")
           
        else:
            if chips.bet>chips.total:
                print("sorry you dont have enough chips,you have: {}",format(chips.total))
            else:
                break
                
#class deck
def hit(deck,hand):
    single_card=deck.deal()
    hand.add_cards(single_card)
    hand.adjust_for_ace()
#function for hit or stand    
def hit_or_stand(deck,hand):
    global playing
    while True:
        x=input("hit or stand?enter h or s")
        
        if x[0].lower()=='h':
            hit(deck,hand)
            
        elif x[0].lower()=='s':
            print('player stands dealers turn')
            playing =False
            
        else:
            print('sorry ,i did no understand that,pelase enter h or s only!')
            continue
           
        break
        
#function to diplay the card of player and dealer
def show_some(player,dealer):
    print("\nDealer hand:")
    print("<card hidden>")
    print('',dealer.cards[1])
    print('\n players hand:',*player.cards,sep='\n')
def show_all(player,dealer):
    print('\n dealers hand:',*dealer.cards,sep='\n')
    print('\n dealers hand:',dealer.value)
    print('\n players hand:',*player.cards,sep='\n')
    print('\n players hand:',player.value)

    
def player_busts(player,dealer,chips):
    print("bust player")
    chips.lose_bet()
    
def player_wins(player,dealer,chips):
    print("player win")
    chips.win_bet()
    
def dealer_busts(player,dealer,chips):
    print("player wins dealer busted")
    chips.win_bet()

def dealer_wins(player,dealer,chips):   
    print("dealer wins")
    chips.lose_bet()
    
def push(player,dealer):
    print("dealer and player tie!push")

#Game logic

while True:
    print('welcome to blacjack')
    deck=Deck()
    deck.shuffle()
    
    player_hand=Hand()
    player_hand.add_cards(deck.deal())
    player_hand.add_cards(deck.deal())
    
    dealer_hand=Hand()
    dealer_hand.add_cards(deck.deal())
    dealer_hand.add_cards(deck.deal())
    
    player_chips=Chips()
    
    take_bet(player_chips)
    
    show_some(player_hand,dealer_hand)
    
    while playing:
        hit_or_stand(deck,player_hand)
        
        show_some(player_hand,dealer_hand)
        
        if player_hand.value>21:
            player_busts(player_hand,dealer_hand,player_chips)
            break
        
    if player_hand.value<=21:
        while dealer_hand.value<player_hand.value:
            hit(deck,dealer_hand)
                
        show_all(player_hand,dealer_hand)
            
        if dealer_hand.value >21:
            dealer_busts(player_hand,dealer_hand,player_chips)
        elif dealer_hand.value>player_hand.value:
            dealer_wins(player_hand,dealer_hand,player_chips)
        elif dealer_hand.value<player_hand.value:
            player_wis(player_hand,dealer_hand,player_chips)
        else:
            push(player_hand,dealer_hand)
                
                
    print('\n Player total chips are at: {}',format(player_chips.total))
        
        
    new_game=input("would yo like to play another game?y/n")
        
    if new_game[0].lower=='y':
        playing=True
        continue
    else:
        print('thank you for playing')
        break

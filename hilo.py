from card import Card
from player import Player
import random


class Hilo:
    cards = []
    player = Player()

    def stack_cards(self):
        for card_number in range(13):
            card = Card()
            card.number = card_number + 1
            self.cards.append(card)

    def shuffle_cards(self):
        random.shuffle(self.cards)

    def show_cards(self):
        card_stack = ''
        for card in self.cards:
            card_stack += '|#' + str(card.number)+'|,'
        print()
        print('Card stack: ' + card_stack)

    def show_top_card(self):
        print('\nShuffling cards...')
        self.shuffle_cards()
        print('The card is: |#' + str(self.cards[0].number)+'|')

    def get_guess(self):
        # show top card
        self.show_top_card()
        guess = input('Higher or Lower ? [h/l] ')
        if guess == 'h' or guess == 'l':
            if guess == 'h' and self.cards[1].number > self.cards[0].number:
                print('Bingo, next cards was : '+str(self.cards[1].number))
                self.player.score += 100
                self.player.show_score()
                self.play_again()
            elif guess == 'l' and self.cards[1].number < self.cards[0].number:
                print('Bingo, next cards was : '+str(self.cards[1].number))
                self.player.score += 100
                self.player.show_score()
                self.play_again()
            else:
                print('Oooops, next cards was : ' + str(self.cards[1].number))
                print('Wrong guess '+self.player.name+' , -75 points.')
                self.player.score -= 75
                self.player.show_score()
                if self.player.score <= 0:
                    print('Game Over!')
                else:
                    self.play_again()
        else:
            print('Invalid choice try again ')
            self.get_guess()

    def play_again(self):
        choice = input('Play again? [y/n] ')
        if choice == 'y':
            self.get_guess()
        elif choice == 'n':
            self.player.show_score()
            print('Thank you for playing ' + self.player.name + ', see you next time.')
        else:
            print('invalid choice')
            self.play_again()

    def start_game(self):
        # welcome message.
        print('Welcome to HILO game...')

        # get player name
        player_name = input('\nPlease enter your name/nick name to get started: ')
        self.player.name = player_name

        # stack cards.
        self.stack_cards()

        # Show cards.
        self.show_cards()

        print("\n" + self.player.name + ", good luck!")

        # get user guess
        self.get_guess()

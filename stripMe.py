from Assets.util import *

def strip_me():
	players = prepPlayers()
	discardPlie = makeStack()

	def play(currentPlayer):
		counter = 0
		if currentPlayer == 0:
			hand = players[0]
		elif currentPlayer == 1:
			hand = players[1]

		played = playCard(currentPlayer, hand, discardPlie)
		print('\n'+str(played[0]))

		try:
			#IF card played is a "Pretty"
			if isPayCard(top(discardPlie)):
				#pay = number of cards to pay with
				pay = getCardRate(top(discardPlie))

				#Pay with 'pay' number of cards
				for _ in range(pay):
					if currentPlayer == 1:
						play(0)
					elif currentPlayer == 0:
						play(1)
					
					#if card played is a pretty
					if isPayCard(top(discardPlie)):
						#stop paying
						break
					else:
						#make a note of how much cards already paid
						counter += 1
					
				#if number of cards paid matches the amount to be paid
				if counter == pay:
					#player0 takes all the cards in the discardPile
					takePayment(hand, discardPlie)
					print("\n"+"The full payment was made. Player {} claimed the discard pile".format(currentPlayer))
		except:
			pass

	print(showGreeting)
	while True:
		option = input("play(Enter); quit(q,then enter) ")

		if option is 'q':
			print("You quit the game before it ended, so there's no result. Bye!")
			break
			
		try:
			play(1)
		except:
			print("Player 0 WON!")
			break

		try:
			play(0)
		except:
			print("Player 1 WON!")
			break

		print('\n')

if __name__ == '__main__':
	strip_me()

from random import choice
from word_list import get_words


class Hangman:
	"""
	This class is used to play a game of Hangman.

	The game consists of the user guessing letters until they run out of lives, or they guess the word chosen by the
	computer. If the user guesses all the letters correctly, they win the game.

	Attributes:
		word (str):
			The word chosen at random by the program that the user must guess.

		lives (int):
			The number of incorrect attempts the user is allowed before they lose the game (default = 5)

		word_guessed (list):
			A list representing the location of the previously correct guesses in the word and the locations of the letters
			that have not been guessed yet.

		letters_remaining (int):
			The number of unique letters that remain in the chosen word.

		previous_guesses (list):
			The list of letters that the user has already guessed.
	"""

	def __init__(self, lives, min_length, max_length):
		"""
		Constructor method.

		Parameters:
			lives (int): The number of incorrect attempts the user is allowed before they lose the game (default = 5)
		"""
		self.word: str = choice(get_words(min_length, max_length))
		self.lives: int = lives
		self.max_lives: int = lives
		self.word_guessed: list = ["_"] * len(self.word)
		self.letters_remaining: int = len(set(self.word))
		self.previous_guesses: list = []
	
	def __str__(self):
		"""
		String method.

		Returns:
			Information on letters that appear in the word, lives remaining, and previous guessed letters.
		"""
		return f"\nWord: {''.join(self.word_guessed)} | {'❤ '*self.lives}{'✴ '*(self.max_lives - self.lives)}\nPrevious Guesses: {''.join(sorted(self.previous_guesses))}"

	def check_guess(self, guess):
		"""
		Checks `guess` against the letters in `self.word`.

		Parameters:
			guess (str): The letter the user has guessed.

		Returns:
			Boolean
		"""
		if guess in self.word:
			for char in enumerate(self.word):
				if char[1] == guess:
					self.word_guessed[char[0]] = guess.upper()
			self.letters_remaining -= 1
			return True
		else:
			self.lives -= 1
			return False

	def get_input(self):
		"""
		Gets user input and validates it before sending it anywhere else.

		Returns:
			A valid guessed letter.
		"""
		while True:
			guess = input("Enter letter:")
			if guess.upper() in self.previous_guesses:
				print(f"Already guessed '{guess.upper()}'. Try again.")
			elif not guess.isalpha() or not len(guess) == 1:
				print("Invalid input! Try again.")
			else:
				guess = guess.lower()
				self.check_guess(guess)
				self.previous_guesses.append(guess.upper())
				break


def game_loop(**kwargs):
	"""
	Main loop of the game.

	Parameters:
		kwargs (dict): Parameters to be passed to the game's constructor method.
	"""
	lives = 5
	min_length = 5
	max_length = 8

	# Here I'm adding a little customisation to the game:
	if "lives" in kwargs.keys():
		lives = kwargs["lives"]
	if "min_length" in kwargs.keys():
		min_length = kwargs["min_length"]
	if "max_length" in kwargs.keys():
		max_length = kwargs["max_length"]

	# Initialises the game, and starts the main game loop.
	game = Hangman(lives, min_length, max_length)
	while True:
		print(game)
		game.get_input()
		if game.lives <= 0:
			print("\n=== You lose... ===")
			break
		elif game.letters_remaining <= 0:
			print(f"\n=== YOU WIN! ===")
			break
	print(f"The word was: {game.word.upper()}")


if __name__ == "__main__":
	game_loop()
	while True:
		again = input("\nPlay again? (Y/N): ")
		if again.upper() in ["N", "NO"]:
			break
		elif again.upper() in ["Y", "YES"]:
			game_loop()
		else:
			print("Invalid input! Try again.")
		

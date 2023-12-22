import random
import string #generate random words + strings 
#imported ascii art https://gist.github.com/chrishorton/8510732aa9a80a03c829b09f12e20d9c
hangman = [''' 
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

def draw_hangman(mistakes): #takes n of mistakes made as arg & return hangman drawing
	return "\n".join(hangman[mistake] for mistake in range(mistakes))

def load_word_from_file(file_path): #file path arg = read + return chosen word (randomly)
	try:
		with open(file_path, 'r') as file:
			file_content = file.read()
			words = file_content.split()

			if words:
				return random.choice(words)
			else:
				print(f"The file '{file_path}' is empty.")
				return None

	except FileNotFoundError:
		print(f"The file '{file_path}' does not exist.")
		return None

def is_word_completed(secret_word, guessed_letters): # all letters in word guessed ? 
	return all(letter in guessed_letters for letter in secret_word)

def display_guessed_word(secret_word, guessed_letters): # display guessed char _ for unrevealed char
	return ' '.join(letter if letter in guessed_letters else '_ ' for letter in secret_word)

def available_letters(guessed_letters): # returns remaining available char for guessing
	return ''.join(letter for letter in string.ascii_lowercase if letter not in guessed_letters)

def draw_hangman(mistakes):
	return "\n".join(hangman[mistake] for mistake in range(mistakes))

def play_hangman(secret_word): # main f(x) secret word (arg) --> player to spiel 
	print("welcome to xen's hangman!")
	print("guess the word that is", len(secret_word), "letters long.")

	mistakes = 0
	guessed_letters = []

	while 7 - mistakes > 0:
		if is_word_completed(secret_word, guessed_letters):
			print("-------------")
			print("congrats, you guessed right! the word was:", secret_word)
			break
		else:
			print("-----------------------------------------------")
			print("you have", 7 - mistakes, "guesses remaining.")
			print(draw_hangman(mistakes))
			print("word to guess:", display_guessed_word(secret_word, guessed_letters))
			print("remaining letters:", available_letters(guessed_letters))
			guess = input("please, be my guest, guess a letter: ").lower()

			if guess in guessed_letters:
				print("u've already guessed this letter. try again!")
			elif guess in secret_word and guess not in guessed_letters:
				guessed_letters.append(guess)
				print("nice guess champ!")
			else:
				guessed_letters.append(guess)
				mistakes += 1
				print("nope! sorry, this letter isn't in the word.")

		if 7 - mistakes == 0:
			print("-------------")
			print("sorry, you ran out of guesses, you're hanged! the word was:", secret_word)
			break

if __name__ == "__main__":
	available_files = ['words.txt'] #add files for levels (?) + ask input for difficulty 
    
	selected_file = random.choice(available_files)
	secret_word = load_word_from_file(selected_file)
    
	if secret_word:
		play_hangman(secret_word)

# improvements; implement input to add levels 
# add key to the hangman ascii drawing (to show the last stage) --> in test.txt 
# add files (for levels)
# more interactive output ? 
# Hangman
A simple word-based game were the user guesses a word letter-by-letter that the computer chooses at random.


## Installation
1. Download the code as a zip.
2. Extract the files into a folder.
3. Execute the program by running the folder or the `__main__.py` file using this command: 
```sh
$ python "path/to/directory"
```

## Usage
The program will choose a word at random from the word list provided (default parameters being between 5 and 8 characters in length).

You will have 5 lives to guess the word letter-by-letter. If the letter you choose doesn't appear in the word, you lose a life.

The game ends either when you correctly guess all the letters in the chosen word, or you lose all your lives.

*Thanks to [first20hours](https://github.com/first20hours/google-10000-english) for creating the list of 10000 most common English words.*
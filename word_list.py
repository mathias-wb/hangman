from os import path


def get_words(min_length, max_length):
	words = []
	dir_path = path.dirname(path.realpath(__file__))  # This is so that the program gets the correct location of the file it needs to access.
	file_path = path.join(dir_path, "google-10000-english-no-swears.txt")
	
	with open(file_path, "r") as file:  # I chose the file that didn't include swear words.
		row_count = 0
		for word in file:
			if row_count == 5000:  # I chose to limit to the top 5000 entries, so that way the words weren't so obscure.
				break
			cleaned = word.replace("\n", "")  # Get rid of the newline indicator from each row.
			if min_length <= len(cleaned) <= max_length:
				words.append(cleaned.lower())
			row_count += 1
	return words


if __name__ == "__main__":
	print(get_words(5,8))

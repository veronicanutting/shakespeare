import requests
from bs4 import BeautifulSoup


## Read in play codes from file
def getPlays(filename):

	# Store the codes and names of all plays
	plays = {}
	with open(filename) as f:
	    lines = f.readlines()

	    # If file contains codes, remove first line (not a code)
	    if len(lines)>1:
	    	lines = lines[1:]
	    	for l in lines:
	    		play = l.rstrip('\n').split(': ')

	    		# Add play code and name to dict
		    	if len(play)>1:
		    		plays[play[0].upper()]=play[1]
	return plays


## Iterate over each play code and retrieve data from API
def getCharacters(codes):

	# Store characters by name and lines in each play
	# Organized as dict of dicts because character names are not 
	# unique to each play
	characters = {}
	total_characters = 0
	total_lines = 0

	for c in codes:
		url = 'https://www.folgerdigitaltexts.org/' + str(c) + '/charText/'
		response = requests.get(url)
		
		if response.status_code == 200:
			soup = BeautifulSoup(response.text, "html.parser")
			raw_text = soup.find_all("div")
			text = [c.text for c in raw_text]

	    	# If output contains characters, remove first 2 lines (not a linecount and charater)
			if len(text) > 2:
				text = text[2:]

				# Each item in text is either linecount or character's name
				# Need to iterate in pairs of elements in the list
				num_chars = len(text)//2
				total_characters += num_chars
				for i in range(num_chars):
					linecount = int(text[2*i])
					total_lines += linecount
					name = text[2*i+1].replace('.','_').lower()
					if name in characters.keys():
						characters[name][c] = linecount
					else:
						characters[name] = {c: linecount}
	
	return characters,total_characters,total_lines


## Given character, nicely print their info
def printCharacter(name,plays,characters):
	name = name.lower()
	if name in characters.keys():
		play_info = characters[name]
		print(name.capitalize())
		print('Play count',len(play_info))
		print('Total lines',sum([i for i in play_info.values()]))
		for p in play_info:
			print('Lines in',plays[p],play_info[p])
		print() # newline for readability
	else:
		print('Invalid character')
		return 1


## Given play code, nicely print play's info
def printPlay(code,plays,characters):
	code = code.upper()
	if code in plays.keys():
		name = plays[code]
		print(name)

		# Select characters in given play
		play_chars = {}
		for c in characters:
			if code in characters[c].keys():
				play_chars[c] = characters[c][code]

		play_lines = sum([i for i in play_chars.values()])
		
		print('Lines by character')
		for c in play_chars:
			print(c,play_chars[c])
		print() # newline for readability
		return play_chars,play_lines
	
	else:
		print('Invalid play')
		return 1



## Write aggregated character data to file for easy reading
def exportCharacters(filename,characters):
	with open(filename, 'w') as f:
		for c in characters:
			f.write(c + ' ' + str(characters[c])+'\n')

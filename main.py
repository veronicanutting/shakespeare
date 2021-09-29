import requests
from bs4 import BeautifulSoup

plays = {}

# Get play codes from text file
with open('codes.txt') as f:
    lines = f.readlines()
    if len(lines)>1:
    	lines = lines[1:]
    for l in lines:
    	play = l.rstrip('\n').split(': ')
    	if len(play)>1:
    		plays[play[0].upper()]=play[1]
codes = plays.keys()

#codes = ['AWW']

characters = {}

# Using Folger Shakespeare API: https://www.folgerdigitaltexts.org/api
for c in codes:
	url = 'https://www.folgerdigitaltexts.org/' + str(c) + '/charText/'
	response = requests.get(url)
	
	if response.status_code == 200:
		soup = BeautifulSoup(response.text, "html.parser")
		chars = soup.find_all("div")
		char_text = [c.text for c in chars]
		if len(char_text) > 2:
			char_text = char_text[2:]

			num_chars = len(char_text)//2
			for i in range(num_chars):
				char_name = char_text[2*i+1].replace('.','_').lower()
				if char_name in characters.keys():
					characters[char_name][c] = int(char_text[2*i])
				else:
					characters[char_name] = {c: int(char_text[2*i])}

with open('output.txt', 'w') as f:
	for c in characters:
		f.write(c + ' ' + str(characters[c])+'\n')
#print(characters)
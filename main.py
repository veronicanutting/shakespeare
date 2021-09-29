from helpers import *

## Using Folger's Shakespeare API: https://www.folgerdigitaltexts.org/api
## This script scrapes the HTML pages retrieved from the API and 
## analyzes character metrics.

plays = getPlays('data/codes.txt')

# Seperately store play codes for API
codes = plays.keys()
print('Number of plays for analysis: ',len(codes))

# According to API docs, charText query returns a list of characters arranged 
# according to amount of lines spoken, with a link to each character's entire spoken text

# Get characters and print test
characters,total_characters,total_lines = getCharacters(codes)
print('Number of characters for analysis: ',total_characters)
print('Number of lines for analysis: ',total_lines,'\n')
printCharacter('Portia',plays,characters)

# Print test play
mv_chars,mv_lines = printPlay('mv',plays,characters)
print('Number of characters in MV',len(mv_chars))
print('Number of lines in MV',mv_lines)
#print(mv_chars,'\n')

# Can do other things here!
# For instance: What percent of lines in The Merchant of Venice are Portia's?
proportion_mv = str(round(mv_chars['portia']/mv_lines*100))+'%'
print("Proportion of Portia's lines in the Merchant of Venice:",proportion_mv)

# Across all plays?
proportion_all = str(round(mv_chars['portia']/total_lines*100,2))+'%'
print("Proportion of Portia's lines in all of Shakespeare:",proportion_all)


# Write data to file
#exportCharacters('characters.txt',characters)


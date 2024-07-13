# shakespeare
Mini project involving Folger's Shakespeare API and Beautiful Soup!

A couple of years ago, I wrote a [paper](https://blogs.harvard.edu/veronicanutting/women-in-shakespeare) on Portia, a female character in Shakespeare's play _[The Merchant of Venice](http://shakespeare.mit.edu/merchant/full.html)._ I reread this essay a few days ago and started wondering about the relationship of gender and lines spoken in Shakespeare's plays.

How many of Shakespeare's characters are female? [This](https://en.wikipedia.org/wiki/Category:Female_Shakespearean_characters) Wikipedia page lists 48 characters. But when you include smaller parts, like those of attendants, mistresses, and other less well-know characters, the number may be much larger. 

I found [this](https://www.folgerdigitaltexts.org/api) very cool API created and maintained by Folger. It was the best one I could find for the questions I had. The responses were not in JSON format (sigh), so I used a bit of Beautiful Soup to make the HTML parsing easier. From then, I wrote a few simple functions to aggregate character data across all of Shakespeare's plays, such that I might learn from this data subset.

My original question was harder to answer than I realized because gendering character names is tricky. At first I considered writing my own gender classifier, but there was so much variety (and so few rules!) in the character names that I had to rethink my approach. Next I considered using another API to help me identify which character names might be female. Still, for the aforementioned reason, this was not quite going to work either. 

Finally, I settled a cleaner approach which can answer some of the following questions:
1. What proportion of lines in a play belong to each character?
2. What character names appear in which plays, and how frequently do they talk?
3. Which names are most common in Shakespeare's works, and which are the least?
4. etc..

So, back to my original questions about Portia in _The Merchant of Venice_. Here's what I learned:
- 38 Shakespeare plays
- 773 characters total
- 445,443 lines total

Wow, that's a lot of writing, Shakespeare!

A character named "Portia" appears in 2 plays: _The Merchant of Venice_ and _Julius Caesar._ Shakespeare's Portias have 5,323 lines total, 724 in _Julius Caesar_ and 4,599 in _The Merchant of Venice._

Portia is one of 24 characters in _The Merchant of Venice,_ a play of 20,927 lines. 
- **22% of the lines in _The Merchant of Venice_ are Portia's.**
- **1.03% of the lines in all of Shakespeares lines are Portia's.**

Check out my code to see more! I've been redirecting the print statements in this script to a file like this:
`python3 main.py > out.txt`, so you can directly read `out.txt` here in this repo to see my script's output.

import re

f = open('5-1-input.txt', ''r'')

for string in f.readlines():
  newString = re.sub(something!)
  
# the pattern for re.sub is:
# result = re.sub(pattern, repl, string, count=0, flags=0);

polymer = re.sub('(?i:(.)\\1)(?<=[a-z][A-Z]|[A-Z][a-z])', '', polymer)  #stolen, gotta work out how it works!

# The first 'argument' of the re.sub (before the first comma) is the pattern to find.

# It has [a-z][A-Z]|[A-Z][a-z], which is:
# (any lower case letter then any upper case letter OR any lower case letter then any upper case letter).
# That's there because the pairs we are trying to find for Day 5 Part 1 can be as 'aA' or 'Aa'.
# I know that the | represents 'OR',
# and that the [ ] are used to show sets of characters; I have already used those in AoC Day 4.

# The ?<= before that needs figuring out!

# ? causes the resulting regex to match 0 or 1 repetitions of the preceding regex. ab? will match either ‘a’ or ‘ab’.
# It tells the engine to attempt to match the *preceding* token zero times or once, in effect making it optional.
# In this case the preceding token is the part in ( ) before it.
# You can express that you want the token to be repeated {min,max} times; so writing {0,1} is the same as writing ?
# Question mark and { } repetitions are greedy! So are the + and *
# I have already used {n} in my AoC Day 4 (which is incomplete at the time of writing) to pick up n number of characters.

# BUT (?<= [some stuff]) - and not necessarily with a set inside - matches if the current position in the string
# is preceded by a match for [some stuff] that ends at the current position.
# I.e., if there was a match for [some stuff] just before the position the regex has got to in the string; it 'looks behind'. 
# This thing is called a 'positive lookbehind assertion'.

# In contrast, (?![some stuff]) # matches if [some stuff] doesn’t match next. This is a 'negative lookahead assertion'.
# For example, Isaac (?!Asimov) will match 'Isaac ' only if it’s not followed by 'Asimov'.

# SO: Now we know that the (?<=[a-z][A-Z]|A-Z][a-z]) part means:
# "go back a little bit and check: does the match you just found also match the following pattern?"
# Where "the following pattern" is "[a lowercase letter]then[an uppercase letter] OR [an uppercase letter]then[a lowercase letter]"

# Now got to figure out what the preceding part of the pattern does - the (?i:(.)\\1) part!
# The contents of each ( ) is called a group. (?... [with the dots indicating more stuff in the brackets] indicates an 'extension'.
# (?aiLmsux) : These letters set different flags;
# re.A (ASCII-only matching), re.I (ignore case), re.L (locale dependent), re.M (multi-line), re.S (dot matches all), re.U (Unicode matching), and re.X (verbose).
# We set the flags as the first thing in the extension string.
# So we are using (?i... , setting the re.I flag to ignore case.
# The (.) means "any character except linebreaks".
# The \\1 means "repeat the match once more" (I suspect this would work without the first "\", which is escaping the second.


#references:
# https://github.com/geeksareforlife/advent-of-code/blob/master/2018/05/puzzle1-regex.py
# https://docs.python.org/3.7/library/re.html
# https://www.regular-expressions.info/
# https://docs.python.org/3.7/howto/regex.html



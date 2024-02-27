double_quotes_str = "Look! Double quotes!"
single_quotes_str = 'Look! Single quotes!'
print(double_quotes_str)
print(single_quotes_str)
# You can use either double or single quotes because...

# bad_str = 'I said 'Wow!''

escape_str = 'I said \'Wow!\''
print(escape_str)
double_quotes_in_single_quotes_str = 'I said "Wow!"'
print(double_quotes_in_single_quotes_str)
single_quotes_in_double_quotes_str = "I said 'Wow!'"
print(single_quotes_in_double_quotes_str)

# Ramon likes combo of quotes because readability and placement of escape characters can get tricky.

# Remove whitespace - Strip
extra_spaces_str = "  Bob          "
print(len(extra_spaces_str))
print(extra_spaces_str.strip())
print(len(extra_spaces_str.strip()))

# Counting the number of times the sub-string appears
example_str = "Here's some text with lot's of text"
print(example_str)
print(example_str.count("text"))

# Change all text to lower case
print(example_str.lower())

# Change all text to upper case
print(example_str.upper())

# Capitalise first letter
print(example_str.capitalize())

# Replace something in string
print(example_str.replace(" with", ","))

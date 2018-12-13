print('spam eggs')  # single quotes

print('doesn\'t')  # use \' to escape the single quote...

print("doesn't")  # ...or use double quotes instead

print('"Yes," they said.')

print("\"Yes,\" they said.")

print('"Isn\'t," they said.')

str1 = 'First line.\nSecond line.'  # \n means newline

print(str1) 

str2 = r'First line.\nSecond line.' # use raw strings by adding an r

print(str2)

print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""") # String literals can span multiple lines.

print(3 * 'un' + 'ium') # Strings can be concatenated

text = ('Put several strings within parentheses '
        'to have them joined together.')
print(text)

word = 'Python'
print(word[0])
print(word[-1])
print(word[0:3])

'''
 +---+---+---+---+---+---+
 | P | y | t | h | o | n |
 +---+---+---+---+---+---+
 0   1   2   3   4   5   6
-6  -5  -4  -3  -2  -1
'''

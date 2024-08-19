import re

# Sample text
text = """abc123
456xyz
a_b c!
789abcxyz
abc xyz
no_digits_here"""

# 1. Digits and Non-Digits
digits = re.findall(r'\d', text)
non_digits = re.findall(r'\D', text)
print("Digits:", digits)
print("Non-Digits:", non_digits)

# 2. Word and Non-Word Characters
word_chars = re.findall(r'\w', text)
non_word_chars = re.findall(r'\W', text)
print("Word Characters:", word_chars)
print("Non-Word Characters:", non_word_chars)

# 3. Whitespace and Non-Whitespace Characters
whitespace_chars = re.findall(r'\s', text)
non_whitespace_chars = re.findall(r'\S', text)
print("Whitespace Characters:", whitespace_chars)
print("Non-Whitespace Characters:", non_whitespace_chars)

# 4. String Start and End
start_abc = re.findall(r'^abc', text, re.MULTILINE)
end_xyz = re.findall(r'xyz$', text, re.MULTILINE)
print("Lines starting with 'abc':", start_abc)
print("Lines ending with 'xyz':", end_xyz)

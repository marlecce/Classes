import string 

def buildCoder(shift):
    """
    Returns a dict that can apply a Caesar cipher to a letter.
    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation, numbers, and spaces.

    shift: 0 <= int < 26
    returns: dict
    """
    s1 = string.ascii_lowercase
    s2 = string.ascii_uppercase
    cipher_key = {s2[i]: (s2[shift:] + s2[:shift])[i] for i in range(26)}
    cipher_key.update({s1[i]: (s1[shift:] + s1[:shift])[i] for i in range(26)})
    return cipher_key
      

def applyCoder(text, coder):
    """
    Applies the coder to the text. Returns the encoded text.

    text: string
    coder: dict with mappings of characters to shifted characters
    returns: text after mapping coder chars to original text
    """
    cipher_text = ""
    L = string.ascii_lowercase
    U = string.ascii_uppercase
    for plain_char in text:
        if (plain_char not in L) and (plain_char not in U):
            cipher_text += plain_char
        else:
            cipher_text += coder[plain_char]
    return cipher_text

#print applyCoder("Hello, world!", buildCoder(3))     

"""
1. Set the maximum number of real words found to 0.
2. Set the best shift to 0.
3. For each possible shift from 0 to 26:
	4. Shift the entire text by this shift.
	5. Split the text up into a list of the individual words.
	6. Count the number of valid words in this list.
	7. If this number of valid words is more than the largest number of
	   real words found, then:
		8. Record the number of valid words.
		9. Set the best shift to the current shift.
	10. Increment the current possible shift by 1. Repeat the loop
	   starting at line 3.
11. Return the best shift.
"""
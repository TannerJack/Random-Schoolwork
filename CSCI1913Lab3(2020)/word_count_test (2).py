from word_count import *

# set to True to do the longer tests for Count, otherwise you will just get true/false for if your counts match the expected.
# The longer tests will help you debug if there are issues, as they are much more descriptive, but they do occupy a lot of space
PRINT_LONG_TESTS = False

# Simple -- no punctuation
print(my_split('apple dog cat'))                # ['apple', 'dog', 'cat']
print(my_split('apple'))                        # ['apple']
print(my_split('apple dog cat apple apple'))    # ['apple', 'dog', 'cat', 'apple', 'apple']

# Hard, punctuation
print(my_split('apple? Dog car! Taco. car, wolf, fox'))     # ['apple', 'Dog', 'car', 'Taco', 'car', 'wolf', 'fox']
print(my_split('tacos?'))                       # ['tacos']

poe = ['Once', 'upon', 'a', 'midnight', 'dreary', 'while', 'I', 'pondered', 'weak', 'and', 'weary', 'Over', 'many', 'a', 'quaint', 'and', 'curious', 'volume', 'of', 'forgotten', 'lore', 'While', 'I', 'nodded', 'nearly', 'napping', 'suddenly', 'there', 'came', 'a', 'tapping', 'As', 'of', 'some', 'one', 'gently', 'rapping', 'rapping', 'at', 'my', 'chamber', 'door', 'Tis', 'some', 'visiter,', 'I', 'muttered', 'tapping', 'at', 'my', 'chamber', 'door', 'Only', 'this', 'and', 'nothing', 'more.']
counted = count(poe)
# Instead of printed this directly, I'm going to split it over lines and sort it
# This should make it easier to compare...
if PRINT_LONG_TESTS:
    print("POE======")
    for item in sorted(list(counted.items())):
        print(item)
    print("POE======")
# My Output:
#POE======
#('As', 1)
#('I', 3)
#('Once', 1)
#('Only', 1)
#('Over', 1)
#('Tis', 1)
#('While', 1)
#('a', 3)
#('and', 3)
#('at', 2)
#('came', 1)
#('chamber', 2)
#('curious', 1)
#('door', 2)
#('dreary', 1)
#('forgotten', 1)
#('gently', 1)
#('lore', 1)
#('many', 1)
#('midnight', 1)
#('more.', 1)
#('muttered', 1)
#('my', 2)
#('napping', 1)
#('nearly', 1)
#('nodded', 1)
#('nothing', 1)
#('of', 2)
#('one', 1)
#('pondered', 1)
#('quaint', 1)
#('rapping', 2)
#('some', 2)
#('suddenly', 1)
#('tapping', 2)
#('there', 1)
#('this', 1)
#('upon', 1)
#('visiter,', 1)
#('volume', 1)
#('weak', 1)
#('weary', 1)
#('while', 1)
#POE======

# Directly comparing against expected, worse for debugging, but if this says "true" don't bother with the above...
poe_dict = {'Once': 1, 'upon': 1, 'a': 3, 'midnight': 1, 'dreary': 1, 'while': 1, 'I': 3, 'pondered': 1, 'weak': 1, 'and': 3, 'weary': 1, 'Over': 1, 'many': 1, 'quaint': 1, 'curious': 1, 'volume': 1, 'of': 2, 'forgotten': 1, 'lore': 1, 'While': 1, 'nodded': 1, 'nearly': 1, 'napping': 1, 'suddenly': 1, 'there': 1, 'came': 1, 'tapping': 2, 'As': 1, 'some': 2, 'one': 1, 'gently': 1, 'rapping': 2, 'at': 2, 'my': 2, 'chamber': 2, 'door': 2, 'Tis': 1, 'visiter,': 1, 'muttered': 1, 'Only': 1, 'this': 1, 'nothing': 1, 'more.': 1}
print(counted == poe_dict)

seuss = ['One', 'fish', 'Two', 'fish', 'Red', 'fish', 'Blue', 'fish', 'Black', 'fish', 'Blue', 'fish', 'Old', 'fish', 'New', 'fish', 'This', 'one', 'has', 'a', 'littlecar', 'This', 'one', 'has', 'a', 'little', 'star', 'Say', 'What', 'a', 'lot', 'of', 'fish', 'there', 'are', 'Yes', 'Some', 'are', 'red', 'and', 'some', 'are', 'blue', 'Some', 'are', 'old', 'and', 'some', 'are', 'new', 'Some', 'are', 'sad', 'and', 'some', 'are', 'glad', 'And', 'some', 'are', 'very', 'very', 'bad', 'Why', 'are', 'they', 'sad', 'and', 'glad', 'and', 'bad', 'I', 'do', 'not', 'know', 'go', 'ask', 'your', 'dad']

counted = count(seuss)
# Instead of printed this directly, I'm going to split it over lines and sort it
# This should make it easier to compare...
if PRINT_LONG_TESTS:
    print("seuss======")
    for item in sorted(list(counted.items())):
        print(item)
    print("seuss======")

#seuss======
#('And', 1)
#('Black', 1)
#('Blue', 2)
#('I', 1)
#('New', 1)
#('Old', 1)
#('One', 1)
#('Red', 1)
#('Say', 1)
#('Some', 3)
#('This', 2)
#('Two', 1)
#('What', 1)
#('Why', 1)
#('Yes', 1)
#('a', 3)
#('and', 5)
#('are', 9)
#('ask', 1)
#('bad', 2)
#('blue', 1)
#('dad', 1)
#('do', 1)
#('fish', 9)
#('glad', 2)
#('go', 1)
#('has', 2)
#('know', 1)
#('little', 1)
#('littlecar', 1)
#('lot', 1)
#('new', 1)
#('not', 1)
#('of', 1)
#('old', 1)
#('one', 2)
#('red', 1)
#('sad', 2)
#('some', 4)
#('star', 1)
#('there', 1)
#('they', 1)
#('very', 2)
#('your', 1)
#seuss======


# Directly comparing against expected, worse for debugging, but if this says "true" don't bother with the above...
seuss_dict = {'One': 1, 'fish': 9, 'Two': 1, 'Red': 1, 'Blue': 2, 'Black': 1, 'Old': 1, 'New': 1, 'This': 2, 'one': 2, 'has': 2, 'a': 3, 'littlecar': 1, 'little': 1, 'star': 1, 'Say': 1, 'What': 1, 'lot': 1, 'of': 1, 'there': 1, 'are': 9, 'Yes': 1, 'Some': 3, 'red': 1, 'and': 5, 'some': 4, 'blue': 1, 'old': 1, 'new': 1, 'sad': 2, 'glad': 2, 'And': 1, 'very': 2, 'bad': 2, 'Why': 1, 'they': 1, 'I': 1, 'do': 1, 'not': 1, 'know': 1, 'go': 1, 'ask': 1, 'your': 1, 'dad': 1}
print(counted == seuss_dict)

seuss2 = {'Some': 7, 'are': 8, 'thin': 1, 'and': 3, 'some': 4, 'fat': 2, 'The': 1, 'one': 2, 'has': 1, 'a': 3, 'yellow': 1, 'hat': 1, 'From': 2, 'there': 2, 'to': 3, 'here': 2, 'Funny': 1, 'things': 2, 'everywhere': 1, 'Here': 1, 'who': 1, 'like': 2, 'run': 2, 'They': 1, 'for': 1, 'fun': 1, 'in': 1, 'the': 1, 'hot': 2, 'sun': 1, 'Oh': 3, 'me': 2, 'my': 2, 'oh': 1, 'What': 1, 'lot': 1, 'of': 2, 'funny': 1, 'go': 3, 'by': 1, 'have': 5, 'two': 1, 'feet': 2, 'four': 1, 'six': 1, 'more': 1, 'Where': 1, 'do': 1, 'they': 2, 'come': 3, 'from': 1, 'I': 2, 'can': 1, 't': 2, 'say': 1, 'But': 1, 'bet': 1, 'long': 2, 'way': 1, 'we': 2, 'see': 2, 'them': 3, 'fast': 1, 'slow': 1, 'high': 1, 'low': 1, 'Not': 1, 'is': 1, 'another': 1, 'Don': 1, 'ask': 2, 'us': 1, 'why': 1, 'your': 1, 'mother': 1}
poe2 = {'And': 1, 'the': 2, 'silken': 1, 'sad': 1, 'uncertain': 1, 'rustling': 1, 'of': 2, 'each': 1, 'purple': 1, 'curtain': 1, 'Thrilled': 1, 'me': 2, 'filled': 1, 'with': 1, 'fantastic': 1, 'terrors': 1, 'never': 1, 'felt': 1, 'before': 1, 'So': 1, 'that': 1, 'now': 1, 'to': 1, 'still': 1, 'beating': 1, 'my': 3, 'heart': 1, 'I': 1, 'stood': 1, 'repeating': 1, 'Tis': 1, 'some': 1, 'visiter': 2, 'entreating': 2, 'entrance': 2, 'at': 2, 'chamber': 2, 'door': 2, 'Some': 1, 'late': 1, 'This': 1, 'it': 1, 'is': 1, 'and': 1, 'nothing': 1, 'more': 1}

print(word_count_similarity(poe_dict, seuss_dict))    # 0.0015532171009202812
print(word_count_similarity(poe_dict, poe2))          # 0.004341337674671008
print(word_count_similarity(seuss_dict, seuss2))      # 0.0016165300560604333
print(word_count_similarity(poe2, seuss2))            # 0.0013395604793454256


print(best_guess({"poe1":poe_dict, "poe2":poe2, "seuss1":seuss_dict}, seuss2))      # seuss1
print(best_guess({"poe1":poe_dict, "poe2":poe2, "suess2":seuss2}, seuss_dict))      # suess2
print(best_guess({"poe1":poe_dict, "seuss1":seuss_dict, "suess2":seuss2}, poe2))    # poe1
print(best_guess({"poe2":poe2, "seuss1":seuss_dict, "suess2":seuss2}, poe_dict))    # poe2


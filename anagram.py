def is_anagram(word1, word2):
    return sorted(word1.lower()) == sorted(word2.lower())

name = input("enter a name: ")
word_check = input("enter another name: ")

if is_anagram(name, word_check):
    print("yes! it's an anagram")
else:
    print("no! it's not an anagram")

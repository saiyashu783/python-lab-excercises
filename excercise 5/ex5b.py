# Write a Python class to reverse a string word by word.

class Reverse:
    def rev_words(self, x):
        words = x.split()
        words = list(reversed(words))
        rev = ' '.join(words)
        return rev


string = input("enter a string: ")
print("in reverse order: ", Reverse().rev_words(string))

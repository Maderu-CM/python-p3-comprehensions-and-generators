#!/usr/bin/env python3

def return_evens(sequence):
    even_elements = [x for x in sequence if x % 2 == 0]
    return even_elements

# Example usage
result = return_evens([0, 1, 3, 5, 7, 8, 9])
print(result)  # Output: [0, 8]


def make_exclamation(sentences):
    exclamated_sentences = [sentence + '!' for sentence in sentences]
    return exclamated_sentences

# Example usage
result = make_exclamation(["Hello", "I'm doing great", "Python is fun"])
print(result)
# Output: ["Hello!", "I'm doing great!", "Python is fun!"]

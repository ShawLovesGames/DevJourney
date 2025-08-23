# Modules are code written by other programmers which we can use in our programs to make life easy.

import pyjokes # I used "pip install pyjokes" to install pyjokes module.

# Get a random joke.
joke = pyjokes.get_joke()

# Print the joke.
print("Here's a joke for you:")
print(joke)
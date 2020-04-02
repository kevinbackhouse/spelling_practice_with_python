from time import sleep
from playsound import playsound

# List of words
words = ['bicycle', 'peculiar', 'sentence']
num_words = len(words)

# Iterate through the list of words.
for i in range(num_words):
    # The word to test on this iteration.
    word = words[i]

    # Load the audio for the word. For example, the audio for
    # "bicycle" is stored in a file called "bicycle.wav"
    playsound(word + '.m4a')

    print('Spell the word that you just heard.')
    answer = input()

    if answer == word:
        print('Correct!')
    else:
        print('Wrong! It is spelled like this: ' + word)

    # Print extra newline character.
    print()

    # Pause for a second before the next word.
    sleep(1)

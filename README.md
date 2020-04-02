# Coding project for kids who hate spelling homework

Do you like coding but hate spelling?
Then you might find this project a fun way to practice your coding
and improve your spelling at the same time.
The goal is to create an application that helps you practice your spelling.
The file [spelling.py](/spelling.py) contains a very simple first version,
which only has three words:
"bicycle", "peculiar", and "sentence".
Your task is to improve it by adding more words and by making the
code better.

# Getting started

The project uses [Python](https://www.python.org/),
so you need to make sure that your computer has Python installed.
You can download it from [python.org](https://www.python.org/downloads/).

After you have installed Python, start [IDLE](https://docs.python.org/3/library/idle.html),
which is Python's "Integrated Development and Learning Environment".
If you haven't used IDLE before, you might find this
[getting started guide](https://realpython.com/python-idle/) useful.

[spelling.py](/spelling.py) uses a module called `playsound`,
which you also need to install.
You can do that by opening a terminal (or Windows command prompt)
and running these commands:

```bash
pip install playsound
pip3 install playsound
```

Finally, you need to download this project,
which you can do by clicking the "Download ZIP" button
on [GitHub](https://github.com/kevinbackhouse/spelling_practice_with_python):

![](/documentation/download.png)

# Project ideas

## Add more words

The initial version of the code only has three words: "bicycle", "peculiar", and "sentence".
To make the spelling practice more interesting, you need to add more words.
If you live in the UK,
then you can find the list of words that the government wants you to learn by following
[this link](https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/239784/English_Appendix_1_-_Spelling.pdf).
The words for years 3 and 4 (ages 7 to 9) are on page 16 of the document.
The words for years 5 and 6 (ages 9 to 11) are on page 23.
Similar lists are probably available for other countries and languages.
There are a lot of words in those lists,
so you don't need to add them all in one go.
In fact, it is probably better to add them in smaller batches,
so that you learn how to spell them while you are adding them.
For example, try to add 10 new words a day until you have added them all.

To add a word, you first need to make an audio recording of yourself saying the word.
You can do that with a voice recorder app, either on a phone or on a computer.
For example, on an Android phone you can use the
[Recorder](https://play.google.com/store/apps/details?id=com.google.android.apps.recorder&hl=en_GB)
app to record a word.
The Recorder app allows you to save the recording to Google Drive,
so that you then easily access the file from a computer.
(Please check with your parent or carer before you upload audio recordings to Google Drive.)

## Use a random number generator to choose the next word

The initial version of code iterates through the list of words sequentially.
Try using a random number generator to pick the next word randomly.
For example, you can use
[`random.randint`](https://docs.python.org/3/library/random.html#random.randint)
to generate a random number between 1 and 10 like this:

```
i = random.randint(1,10)
```

(Don't forget to add `import random` at the top the file.)

## Repeat the words that you got wrong

When you get a word wrong, remember it and ask it again later.
For example, change the code so that it starts by asking 20
randomly chosen words.
Then add a second loop that repeats all the words that you
spelled wrong during the first loop.

You can create an empty list like this:

```python
mistakes = []
```

You can add a word to the list like this:

```python
mistakes.append('bicycle')
```

## Create a log file

Create a log file to store the history of all the words that
you have ever practiced, and whether you got them right or wrong.
In python, you can open a file like this:

```python
f = open('log.txt', 'a')
```

The `'a'` argument means "append" mode, so new text will be added to
the end of the file, rather than overwriting what was there before.

You can write to the file like this:

```python
f.write('Hello')
```

And don't forget to close the file when you're done:

```python
f.close()
```

## Add a new word automatically when a new audio file is added

In the initial version of the code, every time you add an audio file
for a new word, you also have to update the list of words on
[line 5](/spelling.py#L5).
It would be more convenient if you could just add a new audio file
and it automatically gets discovered by the code.

The first step is to move the audio files into a sub-directory.
Create a sub-directory named "words" and move the audio files into it.
Now you can change the code to automatically build the list of words by scanning the directory.
Try using [`os.scandir`](https://docs.python.org/3/library/os.html#os.scandir)
to iterate through the files in the directory and read their names.

## Use images

Rather than playing an audio recording of the word, why not display
an image that represents it? You can open an image and display it
like this:

```python
from PIL import Image

image = Image.open('bicycle.png')
image.show()
```

If that doesn't work, you might need to install the `Image` package.
You can do that by opening a terminal (or Windows command prompt)
and running these two commands:

```bash
pip install Image
pip3 install Image
```

## Learn about version control

This project uses the [git](https://git-scm.com/) version control system and is hosted on [GitHub](https://github.com/).
You can create a free account on GitHub. (Please check with your parent or carer before creating an account.)
Then you can [fork](https://help.github.com/github/getting-started-with-github/fork-a-repo) this project
and create your own version.
GitHub's getting started guide is [here](https://help.github.com/github/getting-started-with-github).

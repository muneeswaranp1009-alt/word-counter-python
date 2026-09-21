# Word Counter

A simple Python program that counts the total number of words in a sentence or paragraph and display the frequency of each word.

## Features

- Take as input a sentence or a paragraph from the user

- Convert user input to lowercase
- Remove punctuation marks
- Count the total number of words

- Count the occurrence of each word
- Option for viewing individual count of each word
- Handle invalid input in the menu
  
## Tech Stack
- Python
  
## How It Works
1. The user is prompted to enter a sentence or a paragraph.
2. The program converts the sentence to lower case.
3. Punctuation marks are removed.
4. The words are split into a list.
5. The total number of words are counted.
6. The words are stored in a dictionary where the key is the word and the value is the count of that word.
7. The user is given an option to view the full list of words and their count.
The word processing function returns the total count of words and the dictionary with words and their count. :contentReference[oaicite:0]{index=0}

## Example
```text
Enter a sentence or paragraph to count words:
Python is easy and Python is powerful
Total Words : 7
For view Full Words Count | Enter --> (yes) otherwise (No) to exit
Yes or No: yes

--- Count of Different Words ---
python : 2
is : 2
easy : 1
and : 1
powerful : 1
Concepts Practiced
Functions
Strings
String methods
Lists
Dictionaries
Loops
Conditional statements
User input
Basic text processing
Word frequency counting

How to Run
1. Clone the repository

git clone https://github.com/your-username/word-counter-python.git

2. Open the project folder
cd word-counter-python

3. Run the program
python "Word Counter.py"

Project Structure

word-counter-python/
│
├── Word Counter.py
└── README.md

Learning Purpose

This project was created to practice Python fundamentals and basic text processing using functions, loops, lists, dictionaries, and string operations.

Future Improvements

Add character counting
Add sentence counting
Ignore common stop words
Display the most frequently used word
Add a graphical user interface
Support reading text from files

Author

Muneeswaran P

B.Sc. Artificial Intelligence and Machine Learning Student

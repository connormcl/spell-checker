# Spell Checker
Python script that uses a modified version of the Levenshtein Distance algorithm to offer spelling correction suggestions for misspelled words.

## Usage
Clone the repository
```
$ git clone git@github.com:connormcl/spell-checker.git
```
Switch to the project directory
```
$ cd spell-checker
```
Run the Python script
```
$ python spelling_correction.py DICT MISSPELLINGS
```
* DICT - the dictionary file from which the program will offer a suggestion
* MISSPELLINGS - the file of misspellings

Note: this is a simple, brute force algorithm. The larger the dict and misspelling files are, the longer it will take to complete.

## Example
One dictionary file and four misspelling files of various sizes have been provided for testing.

Run the program on the small misspellings file:
```
$ python spelling_correction.py dict.txt misspellings-small.txt
```
This will create a file called 'suggestions.txt' with the spelling correction suggestions of the provided words.


## More information
Completed as a part of **LING 227: Language and Computation** taught by  Claire Moore-Cantwell during Fall 2015

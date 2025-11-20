Lab 2: Plagiarism Detector

This project is a Python application that compares two text documents to determine how similar their content is. The program processes the text, removes punctuation, converts it to lowercase, filters out common stop words, and analyzes the remaining words. It then calculates a similarity percentage using the Jaccard similarity method.

Project Structure

The project contains the following main components. First, there is a Python script named plagiarism-detector.py. This script performs all the text processing, word searching, finding common words, and calculating the similarity percentage. It also allows the user to save a report of the similarity and the common words.

Second, there is a shell script named setup.sh. This script sets up the project environment by creating the necessary directories, including essays and reports. It also logs the setup process in a file called setup.log and creates sample essay files if they do not already exist.

Finally, the essays directory contains two text files named essay1.txt and essay2.txt. These are sample essays used to test the program. The reports directory is where the similarity report is saved if the user chooses to save it.

How to Run

To run the project, first execute the setup.sh script. This will create the directories, log the setup, and generate sample essay files if they are missing. After the setup is complete, run the Python script plagiarism-detector.py. The program will prompt you to enter a word to search for in both essays, display the common words between the essays, calculate the similarity percentage, and ask if you want to save a report.

Features

The main features of the project include text processing, word search, common words report, and plagiarism calculation. The text processing function reads the essay files, removes punctuation, converts all text to lowercase, and filters out stop words. The word search feature counts how many times a specific word appears in each essay. The common words report shows the words that appear in both essays. The plagiarism calculation uses the Jaccard similarity formula to calculate a percentage indicating how similar the essays are.

Learning Outcomes

This project helps to develop skills in file handling by reading and processing text files, in data structures by using lists and sets to store and manipulate text data, in string manipulation by cleaning and splitting the text, in loops and iterations by analyzing the words, and in input/output operations by allowing the user to search for words and save reports.

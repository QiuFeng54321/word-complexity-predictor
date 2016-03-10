This program is a Python XML-RPC server that accepts an English
word and returns a continuous value (from 0 to 1, inclusive) on how complex that
word is seen to second-language English speakers.

It uses a Decision Tree Regressor (implemented by scikit-learn) to perform its
work. The model uses five different features of a word:
-- Lemma length
-- Average age-of-acquisition (at what age a word is most likely to enter
   someone's vocabulary)
-- Average concreteness (a score of 1 to 5, with 5 being very concrete)
-- Frequency in a certain corpus
-- Lemma frequency in a certain corpus

This work is based off of a machine learning system submitted to a natural
language processing workshop, called the Semantic Evaluation Exercises
International Workshop on Semantic Evaluation 2016 (SemEval-2016). More
specifically, this system was submitted to compete in Task 11, Complex Word
Identification. It ranked 5 out of 40 systems according to its G-score--the
harmonic mean between accuracy and recall--on a test set.

The machine learning system comes already trained on the data provided by Task
11, so you don't have to worry about finding data to train it with.


TO RUN
======
1. First, ensure that you install the requirements by activating your virtualenv
and running "pip install -r requirements.txt".
3. Edit "constants.py" to change the port number to something that's convenient
for you.
2. In one Terminal window, run "python3 server.py" to start the server.
3. In another window, run "python3 client.py" to test that the server workshop
correctly.


REQUIREMENTS
============
Python 3+
nltk 3.0.1+
numpy 1.9.1+
pandas 0.17.1+
scikit-learn 0.17+


LINKS
=====
Final Paper on System: TBD
SemEval-2016 Task 11 Description: http://alt.qcri.org/semeval2016/task11/
Related Work: https://hmcsimplification.wordpress.com/author/mauryquijada/


RESOURCES USED
==============
Word frequency -- M Davies. 2008. The corpus of contemporary american english:
  520 million words, 1990-present.
Word age-of-acquisition -- V Kuperman et al. 2012. Age-of-acquisition ratings
  for 30,000 english words. Behavior Research Methods, 44(4):978–990.
Word concreteness -- M Brysbaert et al. 2013. Concreteness ratings for 40
  thousand generally known english word lemmas. Behavior Research Methods,
  46(3):904–911.

# Poker Hands
This is my solution to the poker hands challenge on Project Euler.  
https://projecteuler.net/problem=54

## Description
The application runs through lines in a txt file and determines how many times player 1 has won.

## Example format for txt file  
7S 5S 9S JD KD 9C JC AD 2D 7C   
4S 5H AH JH 9C 5D TD 7C 2D 6S  
KC 6C 7H 6S 9C QD 5S 4H KS TD  
6S 8D KS 2D TH TD 9H JD TS 3S  
KH JS 4H 5D 9D TC TD QC JD TS  
QS QD AC AD 4C 6S 2D AS 3H KC  
4C 7C 3C TD QS 9C KC AS 8D AD  
KC 7H QC 6D 8H 6S 5S AH 7S 8C  
3S AD 9H JC 6D JD AS KH 6S JH  
AD 3D TS KS 7H JH 2D JS QD AC  
9C JD 7C 6D TC 6H 6C JC 3D 3S  
QC KC 3S JC KD 2C 8D AH QS TS  
AS KD 3D JD 8H 7C 8C 5C QD 6C  

## Description of txt file from Project Euler:
"The file, poker.txt, contains one-thousand random hands dealt to two players. Each line of the file contains ten cards (separated by a single space): the first five are Player 1's cards and the last five are Player 2's cards. You can assume that all hands are valid (no invalid characters or repeated cards), each player's hand is in no specific order, and in each hand there is a clear winner."

### Prerequisites
You will need the following installed:
* [Git](https://git-scm.com/)
* [Python](https://www.python.org/downloads/) (was created with Python 3.7.0)

### Installation
`git clone https://github.com/ronaldnwilliams/poker-challenge.git`  
`cd poker-challenge`  

### Run
`python3 poker_hands.py`  
or  
`python3 poker_hands.py --print_mode`  

### Testing  
`python3 test_poker_hands.py`  

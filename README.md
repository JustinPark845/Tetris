# Personal-Code
# Overview
This is the first project that I have attempted using the python turtle GUI along with Python. The resulting product was my take on a "modern" version of Tetris, which boasts the ability to hold pieces and instantly drop.
# How To Run
To run the app, one must have python3 downloaded and run the command "python3 -m pip install keyboard", which enables the keyboard to be read for moving the pieces.
# Challenges
Unlike traditional methods of coding Tetris, be careful if attempting to extend from this code as the turtle GUI is a continuous graphical interface, meaning that the lines will oftentimes be rounded off at very small decimal values - even if enforced with an int(). This is due to the fact that the turtle GUI draws objects over time and is susceptible to cutting corners, meaning that its values may actually be 0.000001 and an endcase of " x == 0" will never be met.

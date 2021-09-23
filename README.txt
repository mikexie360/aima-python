Mike Xie
mxx170002@utdallas.edu
AI CS6364.001
HW1
This is my submission for Homework 1

This README.txt file will
1. list all commands which will compile the code on csgrads1.utdallas.edu
2. a list of commands which will run the code on csgrads1.utdallas.edu

----------------------------------------------------------------------
First download the elearning submission with the aima code and HW code
Send the file to csgrads1.utdallas.edu, through some FTP or ssh

-------------------------------------------------------------
cd into the aima code and  install numpy in your terminal
    run the following command in the aima directory
    pip3 install numpy --user

------------------------------------------------
p1.py is for kitty world with ability to control kitty
    does not solve any particular problem but is for problem 1
p2.py is for missionary and cannibal problem with various search aglorithms
    solves Problem 2.1 and 2.2
p3.py is for roadmap problem with RBFS and Astar
    Solves Problem 3.1 , 3.2 , 3.3 and 3.4
p4.py is for extra credit in problem 3
    Solves Problem 3 extra-credit

--------------------------------------------------
All python files are using python 3.
to run p1.py run
    python3 p1.py
you can then control kitty until kitty runs out of battery or you quit

to run p2.py run
    python3 p2.py
you will then see the solution path for the missionary problem

to run p3.py run
    python3 p3.py
you will then see the solution path for roadproblem with RBFS and Astar

to run p4.py run
    python3 p4.py
You will then see that the hueristic is inconsistent
------------------------------------------------------
All python runs on AIMA code, but some modifcations may have been made to into
p1.py kitty program may not have been needed.

For p3.py , I am assuming the direct flight distance is a good heuristic.

p4.py shows that flight distance is actually a pretty bad heuristic for road path.
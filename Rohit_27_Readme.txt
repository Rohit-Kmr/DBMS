################################################### DBMS PROGRAM ############################################################

HOW TO RUN THE PROGRAM:-

 RECOMMENDED:-
 
 1) INSTALL ANACONDA NAVIGATOR with python 3.x
 2) RUN JUPYTER NOTEBOOK INSIDE ANACONDA
 3) FIND THE 'Rohit_27_FD.ipynb' file and run it using jupyter notebook
 4) Run all the commands
 
 OR
 
 1) Install python 3.x
 2) Run 'Rohit_27_DBMS.py' file

Note:-The code is same in both files but Jupyter provides better GUI to understand the code
      But output is best in Simple python file 

------------------------------------------------------ Methodology used --------------------------------------------------------


Here we have seprated the FD's RHS into individual attributes i.e A->BC is A->B and A->C

CLOSURE :-
		IN this we append the given elements to Closure ( as A->A is trivial). if any FD's LHS i.e X->Y here X is 
		subset of Closure then we append RHS of FD i.e. Y to the closure.
			The loop end if Length of Closure is same at the begining of loop and at the end of loop

Candidate keys :-
		In this we find all the superkeys of the FD i.e finding closure of all 2^n combination of attributes 
		where n is number of attributes.
			Now we check if the smallest size key is a subset of any super key if yes then remove that super key
		we keep doing this untill all superkeys are checked

Minimal set :- 
		First we remove duplicate FDs (Here all FD have only 1 element in RHS) 
		Then we remove every fd and check whether it belong to minimal set or not
		now we check if LHS has DUplicate element or not.

Equivalance :- 
		We check if FD1 is Subset of FD2 or NOT
		THen we Check if FD2 is Subset of FD1 or NOT
		IF any FD is not a subset of other we return false else true

2NF :-
		Here we check whether each FD's LHS is a KEY or not and RHS is PRime or not
		if lhs is not a key and rhs is not Prime attribute 
		THen we check if LHS Contain a prime attribute or not if yes then we return fals else we return true

3NF :-
		Here we check whether it is 2NF or not if not then we return false else 
		we check whether LHS of each FD is a key or not OR RHS is prime attribute or not 
		if not then we return False else we return True

BCNF :-
		Here we check whether it is 3NF or not if not then we return false else 
		we check whether LHS of each FD is a key or not if not then we return false else we return true
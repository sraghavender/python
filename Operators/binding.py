print(9 % 6 % 2)

#There are two possible ways of evaluating this expression:

#from left to right: first 9 % 6 gives 3, and then 3 % 2 gives 1;
#from right to left: first 6 % 2 gives 0, and then 9 % 0 causes a fatal error.
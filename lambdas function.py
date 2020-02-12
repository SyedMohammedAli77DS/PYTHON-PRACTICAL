#lambda function
adder = lambda x, y: x + y
print (adder (1, 2))

#What a lambda returns
string='some kind of a useless lambda'
print(lambda string : print(string))

#What a lambda returns #2
x="some kind of a useless lambda"
(lambda x : print(x))(x)

#A REGULAR FUNCTION
def guru( funct, *args ):
    funct( *args )
def printer_one( arg ):
    return print (arg)
def printer_two( arg ):
    print(arg)
#CALL A REGULAR FUNCTION 
guru( printer_one, 'printer 1 REGULAR CALL' )
guru( printer_two, 'printer 2 REGULAR CALL \n' )
#CALL A REGULAR FUNCTION THRU A LAMBDA
guru(lambda: printer_one('printer 1 LAMBDA CALL'))
guru(lambda: printer_two('printer 2 LAMBDA CALL'))

#lambdas in filter()
sequences = [10,2,8,7,5,4,3,11,0, 1]
filtered_result = filter (lambda x: x > 4, sequences) 
print(list(filtered_result))

#lambdas in map()
sequences = [10,2,8,7,5,4,3,11,0, 1]
filtered_result = map (lambda x: x*x, sequences) 
print(list(filtered_result))

#lambdas in reduce[vV2][J3]()
from functools import reduce
sequences = [1,2,3,4,5]
product = reduce (lambda x, y: x*y, sequences)
print(product)

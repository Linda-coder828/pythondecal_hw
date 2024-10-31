#2 Practicing Slicing & Striding
"""In this problem, you will practice slicing and striding lists!
2.1 Making a List Variable
Create a variable (name it anything you want, but make it descriptive!) that is assigned to a list with numbers 0 through 20. You should not write each number manually.
>>> whateverNameYouWant = # Your code here
>>> print(whateverNameYouWant)
[0, 1, 2, ..., 20] # It should print all numbers 1-20 in a list"""
numbers_list = list(range(21))
print(numbers_list) 

#2.2 Working with List Elements
"""Write a function that will take in your list from Part 2.1 and square each element in the list. Assign the result to a new variable.
>>> whateverNameYouWant = # Your code from Part 2.1
>>>
>>> def squareList():
>>> """
def square_list(list):
    squared_list = [x ** 2 for x in list]
    return squared_list
squared_numbers_list = square_list(numbers_list)
print(squared_numbers_list)

#2.3 Slicing
"""Write a function that takes in your new list from Part 2.2 and returns the first 15 elements of the list using slicing.
>>> anotherNameYouWant = squareList(list)
>>> first_fifteen_elements(anotherNameYouWant)
[0, 1, 4, ..., 196]"""
def first_fifteen_elements(lst):
    return lst[:15]
i = first_fifteen_elements(squared_numbers_list)
print(i)

#2.4 Striding
"""Write a function that takes in your list from Part 2.2 and returns every 5th element from the list using striding.
>>> anotherNameYouWant = squareList(list)
>>> every_fifth_element(anotherNameYouWant)
[16, 81, 196, 361]"""
def every_fifth_element(list):
    return list[::5]
j = every_fifth_element(squared_numbers_list)
print(j)

#2.5 Slicing & Striding
"""Write a function that takes your list from Part 2.2, slices the last 30 elements of the list, and then returns every 3rd element from that list in reverse order.
>>> anotherNameYouWant = squareList(list)
>>> fancy_function(anotherNameYouWant)
[400, 289, 196, 121, 64, 25, 4]"""
def fancy_function(lst):
    last_30 = lst[-30:] 
    every_3rd_reversed = last_30[::-3]
    return every_3rd_reversed
v=fancy_function(squared_numbers_list)
print(v)

#3 3D Lists
"""3.1 Creating a 5x5 2D List
Write a function that uses nested for loops to create a 5x5 2D list where the numbers 1 through 25 are stored sequentially. Assign the result to a new vari- able.
>>> matrix = create_2d_list()
>>> print(matrix)
[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15],
[16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]
"""
def create_2d_list():
    matrix = [] 
    for i in range(5): 
        row = [] 
        for j in range(1, 6): 
            row.append(5 * i + j)  
        matrix.append(row) 
    return matrix 
matrix = create_2d_list()
print(matrix)

#3.2 Replacing 2D List with Multiples of 3
"""With the 2D list you created in Part 3.1, write a function that will replace all multiples of 3 with the character “?”.
>>> matrix = create_2d_list()
>>> modified_2d_list(matrix)
[[1, 2, ‘?’, 4, 5],
[‘?’, 7, 8, ‘?’, 10],
[11, ‘?’, 13, 14, ‘?’],
[16, 17, ‘?’, 19, 20],
[‘?’, 22, 23, ‘?’, 25]]"""

def modified_2d_list(matrix):
    for i in range(5):  
        for j in range(5): 
            if matrix[i][j] % 3 == 0: 
                matrix[i][j] = "?" 
    return matrix
matrix = create_2d_list()
modified_matrix = modified_2d_list(matrix)
print(modified_matrix)

#3.3 Summing None-’ ?’ Elements
"""Assign the result of your function from Part 3.2 to a variable. Write a function that will iterate through the new 2D list variable and return the sum of all the elements that are not “?”. Hint: Try using “!=”.
>>> matrix = create_2d_list()
>>> new_matrix = modified_2d_list(matrix)
>>> sum_non_question_elements(new_matrix)
217"""

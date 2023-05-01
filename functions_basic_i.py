#1 will return 5 and print it to the console
def number_of_food_groups():
    return 5
print(number_of_food_groups())


# #2 will give us an error becasue the first function about slides is not defined
def number_of_military_branches():
    return 5
print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())


#3 will return 5, exit the function and print 5
def number_of_books_on_hold():
    return 5
    return 10
print(number_of_books_on_hold())


#4 will return 5, exit the function and print 5
def number_of_fingers():
    return 5
    print(10)
print(number_of_fingers())


#5 will print 5 and then nothing because the function didn't return 5, it only printed it
def number_of_great_lakes():
    print(5)
x = number_of_great_lakes()
print(x)


#6 will print 3 and then 5 to the console but won't add together the final print statement because it didn't return anything
def add(b,c):
    print(b+c)
print(add(1,2) + add(2,3))


#7 will return 25 as it will turn 2 and 5 into a string and then concatenate them
def concatenate(b,c):
    return str(b)+str(c)
print(concatenate(2,5))


#8 prints 100 inside of the function and then it will return 10 and print that
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(number_of_oceans_or_fingers_or_continents())


#9 prints 7, 14, 21
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))


#10 prints 8
def addition(b,c):
    return b+c
    return 10
print(addition(3,5))


#11 prints 500 2 times, then prints 300, then 500 again
b = 500
print(b)
def foobar():
    b = 300
    print(b)
print(b)
foobar()
print(b)


#12 prints 500 twice, 300, and then 500 
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
foobar()
print(b)


#13 prints 500 twice, then 300, then 300 again
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
b=foobar()
print(b)


#14prints 1, 3 then 2
def foo():
    print(1)
    bar()
    print(2)
def bar():
    print(3)
foo()


#15 prints 1, 3, 5, 10
def foo():
    print(1)
    x = bar()
    print(x)
    return 10
def bar():
    print(3)
    return 5
y = foo()
print(y)
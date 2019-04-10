# Here's a chance to play around with lists for a bit before you continue
# Take a look at what the following code does and try to guess how it works.

print "EXAMPLE 1: Lists can contain strings"
string_list = ['HTML', 'CSS', 'Python']
print string_list

print "EXAMPLE 2: Lists can contain numbers"
number_list = [3.14159, 2.71828, 1.61803]
print number_list

print "EXAMPLE 3: Lists can be 'accessed' and 'sliced' like how we accessed and sliced strings in the previous lessons"
pi = number_list[0]
not_pi = number_list[1:]
print pi
print not_pi

print "EXAMPLE 4: Lists can contain strings AND numbers"
mixed_list = ['Hello!', 42, "Goodbye!"]
print mixed_list

print "Example 5: Lists can even contain other lists"
list_with_lists = [3, 'colors:', ['red', 'green', 'blue'], 'your favorite?']
print list_with_lists

# Define a variable, stooges, which value is a list of the names of the Three Stooges in this order: 
# "Moe" 
# "Larry" 
# "Curly"
list_names = ['Moe', 'Larry', 'Curly']

print list_names
print list_names[0]
print list_names[1:]


# Given the variable,

days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]

# define a procedure, how_many_days,
# that takes as input a number
# representing a month, and returns
# the number of days in that month.

def how_many_days(month_number):
    if month_number < 1 or month_number > 12:
        return
    return days_in_month[month_number - 1]


print how_many_days(1)
#>>> 31

print how_many_days(4)
#>>> 30



# Every entry in the following list is itself a list
nested_list = [['HTML', 'Hypertext Markup Language forms the structure of webpages'],
               ['CSS' , 'Cascading Style Sheets give pages style'],
               ['Python', 'Python is a programming language'],
               ['Lists', 'Lists are a data structure that let you organize information']]

first_concept = nested_list[0]

print "What do you think this will print?"
print first_concept 

print "Since first_concept was itself a list, we can access its elements"
first_title = first_concept[0]
first_description = first_concept[1]


print "What will this print?"
print first_title
print first_description


# Given the variable countries defined as:

#             Name    Capital  Populations (millions)
countries = [['China','Beijing',1350],
             ['India','Delhi',1210],
             ['Romania','Bucharest',21],
             ['United States','Washington',307]]

# Write code to print out the capital of India
# by accessing the list

print countries[1][1]

# What multiple of Romania's population is the population
# of China? Calculate this by accessing the list and
# dividing the population of China (1350)
# by the population of Romania (21).
# Please print your result.
print countries[0][2] / countries[2][2]



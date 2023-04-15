
#Check the data type of all your variables using type() built-in function
#Using the len() built-in function, find the length of your first name
#Compare the length of your first name and your last name

full_name="Kabonge Hajarah"
last_name="Hajarah"
print(type(full_name))
print(len(full_name))
print(len(full_name)==len(last_name))

# Declare 5 as num_one and 4 as num_two
#Apply all operators
num_one=5
num_two=4
total=num_two + num_one
print(total)

diff=num_two - num_one
print(diff)

Multiply=num_two *num_one
print(Multiply)

division=num_one /num_two
print(division)

remainder=num_two %num_one
print(remainder)

floor_division=num_two // num_one
print(floor_division)

exp=num_one **num_two
print(exp)

# The radius of a circle is 30 meters.
# Calculate the area of a circle and assign the value to a variable name of area_of_circle
# Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
# Take radius as user input and calculate the area.
radius=30
area_of_circle=(3.14 * (radius**2))
print(area_of_circle)

circum_of_circle= (3.14* (2 *radius))
print(circum_of_circle)

# radius = float(input("Input Radius: " ))
# area= 3.14 * (radius ** 2)
# print(area)

# Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
#  Enter base: 20
    # Enter height: 10
    # The area of the triangle is 100
# base=float(input("Enter base :" ))
# height=float(input("Enter height :" ))
# area_of_the_triangle= base * height
# print(f"The area_of the triangle is : {area_of_the_triangle}")


# #Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
# # Enter side a: 5
# # Enter side b: 4
# # Enter side c: 3
# # The perimeter of the triangle is 12

# a=int(input("Enter side a:" ))
# b=int(input("Enter side b:" ))
# c=int(input("Enter side c:" ))
# perimeter=(a+b+c)
# print(f"The perimeter of the triangle is {perimeter}")

word="python"
word2="dragon"
print(len(word)==len(word2))
print( "on" in (word and word2))
print( not("on") in (word and word2))


#string formating
first_name = 'Hajarah'
last_name = 'Kabonge'
language = 'Python'
formated_string = 'I am %s %s. I love %s' %(first_name, last_name, language)
print(formated_string)

ages = [22, 19, 24, 25, 26, 24, 25, 24]

newsorted=ages.sort()
min_age = ages[0]
max_age = ages[-1]
print(f"max_age:{min_age}, min_age:{max_age}")
ages.append(min_age)
ages.append(max_age)
print(ages)

print(ages) 
#decending-order
ages.sort(reverse=True)
print(ages)


#Check if an item exists in tuple:
# Check if 'Estonia' is a nordic country
# Check if 'Iceland' is a nordic country
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)


#for loop
person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}
for key in person:
    print(key)

for key ,value in person.items():
    print(key,value)  
    print(key,value)
    



















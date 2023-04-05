#Name: Robert King

import datetime

#prompt user to enter the size of pizza
print('Please choose type pf pizza')
print('1. Small Pizza for $9.99')
print('2. Medium Pizza for $12.99')
print('3. Large Pizza for $14.99')
print('4. Extra Large Pizza for $17.99')
pizza_price = {1:9.99,2:12.99,3:14.99,4:17.99}

pizza = int(input("What is your choice :"))
#prompt user to enter the number of pizzas
number = int(input('How many of the above type of pizza do you want\n'))
print('Your cost for one pizza if {} and the cost of toping are $0.5 * {}. which a make a total of {} for each complete pizza')
format(pizza_price[pizza] *0.5 + pizza_price[pizza])
#display the final output
print('Your total cost for {} pizzas is {}'.format(number,number*(len *0.5 + pizza_price[pizza])))
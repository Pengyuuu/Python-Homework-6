#Ingredient Adjuster

#calculate how many cups for one cookie
sgr = 1.5 / 48
btt = 1 / 48
flr = 2.75 / 48

#prompt user for how many cookies they want
ckie = int(input('How many cookies do you want to make? '))

#multiply measurements for one cookie with user's amount
sgr = ckie * sgr
btt = ckie * btt
flr = ckie * flr

#output how many cups are required
print('To make',ckie,'cookies, you need')
print(format(sgr, '.2f'), \
      'cups of sugar')
print(format(btt, '.2f'), \
      ' cups of butter')
print(format(flr, '.2f'), \
      ' cups of flour')

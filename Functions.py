from encodings.idna import ToASCII
#//////////////////////////////////////////////////////////////
#Function for area of the circle third attempt
#idk but pi isnt giving me the exact exact number but like incredibly close


def circle_area(radius, pi):
    return pi * radius * radius

radius = int(input("Enter the radius: "))
pi = 3.1415
Area = circle_area(radius, pi)

print("The area of the circle is: " + str(round(Area, 2)))
#////////////////////////////////////////////////////////////////
#////////////////////////////////////////////////////////////////


#Function for total due fifth attempt (Did it on the fourth attempt by
#putting the / 100 in the return
#ok now i realize u cant put % on an int
#had to do some research on the :.2f stuff

def total_due(money, tax):
    return money + (money*tax) / 100

money = int(input("Enter the amount of money: "))
tax = float(input("Enter the tax: "))
Total = total_due(money, tax)
print (f"Your total due is: $ {Total:.2f}") #testing F string and the .2f

#////////////////////////////////////////////////////////////////
#////////////////////////////////////////////////////////////////


#First attempt at farenheit to celsius (did this on the first attempt)
#first attempt fr returned "0.0" im cooked (editor note: im actually -
#stupid because thats the amount that its supposed to return bruh)

def Celsius(Farenheit):
    return (Farenheit-32) * (5 / 9)

Farenheit = int(input("Enter the Farenheit amount to convert: "))
NewFarenheit = Celsius(Farenheit)
print(f"The celsius amount is now: {NewFarenheit:.4f}") #4f works too lol

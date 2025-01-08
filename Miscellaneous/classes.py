# Cookie class
class Cookie: 
    def __init__(self, color):
        self.color = color

    def getColor(self):
        return self.color
    
    def setColor(self, color):
        self.color = color

# this is where we create the cookie objects
cookie_one = Cookie('green')
cookie_two = Cookie('blue')

# this is where we print the cookie
print("Cookie one is ", cookie_one.getColor())
print("Cookie two is", cookie_two.getColor())

# setting the color to different color
cookie_one.setColor('yellow')

# again printing the color

print("Cookie one is now", cookie_one.getColor())

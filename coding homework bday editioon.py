class Airplane(object):

def_init_(self, x, y, company, colour):
self.x = x
self.y = y
self.speed = speed
self.company = company 
self.colour = colour

def_init_(self, max_width=700, max_height=700):
self.x = random.randint(0, max_width)
self.y = random.randint(0, max_height)
self.speed = random.randint(0, max_speed)
self.company = random.choice(colours)

def __str__(self):
return  "Airplane {} {} {} {} "> format(self.company, self.x, self.y, self.speed)

a = Airplane()
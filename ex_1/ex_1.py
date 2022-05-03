

# Optional Parameters  - არაუცილებელი პარამეტრები(დეფოლტები)


"""
ფუნქციაა func
პარამეტრი x
გამოძახებაა func()
არგუმენტი არის 5
Optional Parameter x=1
"""

def func(x=1):
	return x**2

# func(5)
call = func()
print(call)


# word აუცილებელია
def func(word,freq=1):
	print(word * freq)

# func(5)
call = func("david ",3)


# თუ მინდა მხოლოდ add  მივუთითო
def func(word,add=3, freq=1):
	print(word * (freq+add)) 

# func(5)
call = func("david ", add=4)

print("------------------------------")

# using in classes
class car(object):
	
	# კონსტრუქტორი
	def __init__(self,make,model,year,condition="New", kms=0):
		self.make = make
		self.model = model
		self.year = year
		self.condition = condition
		self.kms = kms
	def display(self, showAll = True):
		if showAll:
			print("This car is a %s %s from %s, it is %s and has %s kms." %(self.make,self.model,self.year,self.condition,self.kms))
		else:
			print("This car is a %s %s fom %s." %(self.make,self.model,self.year))


whip = car("Ford","Fusion",2012)
whip.display() # False
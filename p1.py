## made by Mike Xie
## Problem 1: Intelligent Agents
## Enhance kitty robot discussed in class to a model-based agent
## in which the state has 3 components
## [position, happiness, battery]
## where the battery has a value of 100 for FULL initally and 0 when discharged
## 6 possible positions of kitty, [1, ...,  6]
## -1 for battery when change of position by walking, -4 when turns around
## -5 when it bumps against a wall, -3 when kitty purrs and -2 every time it meows
## write a utility function taht combines the happiness with the state of the batrery.

## Describe the state space
stateSpaceDescription = '''
The state space is all possible states in the system
For position of kitty, there are 6 possible states
For battery of kitty, there are 6 possible states
For happiness of kitty, it is arbitrary. we can say that kitty happyiness states can be [very happy, happy, sad, curious], so kitty's happiness possible states is 4 states

kitty gains happiness when kitty purs and meows.
kitty loses happiness when kitty bumps into a wall.
so the upperbound for the entire state space for kitty is 144 states.
'''

class Kitty():
	def __init__(self):
	## states
		self.location = 1
		self.battery = 100
	## 0 happiness is very happy, 1 happiness is happy, 3 happiness is sad and 4 happiness is curious
		self.happinessList = ["Very Happy","Happy","Sad","Curious"]
		self.happinessCurrentIndex = 0

	## -1 is kitty facing left, 1 is kitty facing right
		self.currentFacingDirection = -1
## Write a state-update function that changes the value of the battery
## -1 for every new change in position by walking
## -4 for turning around
## -5 when it bumps against a wall
## -3 when kitty purrs
## -2 when kitty meows
## when battery is discharged, no more actions are possible.
	def walk(self):
		## out of battery
		if self.battery <= 0:
			print("out of battery, kitty will now quit")
			self.quit()
		## bump into wall 
		elif (self.location == 1) and (self.currentFacingDirection == -1):
			self.battery = self.battery - 5
			if self.happinessCurrentIndex != 3:
				self.happinessCurrentIndex = self.happinessCurrentIndex + 1
			return "bumped into western wall!"
		elif (self.location == 6) and (self.currentFacingDirection == 1):
			self.battery = self.battery - 5
			if self.happinessCurrentIndex != 3:
				self.happinessCurrentIndex = self.happinessCurrentIndex + 1
			return "bumped into eastern wall!"
		## walk successfully
		else:
			# decrease battery by 1
			self.battery = self.battery - 1
			# change location of kitty depending on current facing direction
			self.location = self.location + self.currentFacingDirection
			return "walk successful"
	def turnAround(self):
		## out of battery
		if self.battery <= 0:
			print("out of battery, kitty will now quit")
			self.quit()
		## Turn Around successfully
		else:
			# decrease battery
			self.battery = self.battery - 4
			## change direction
			if self.currentFacingDirection == 1:
				self.currentFacingDirection = -1
				return "Kitty is turned to the west now"
			else:
				self.currentFacingDirection = 1
				return "Kitty is turned to the east now"
			
	def purr(self):
		## out of battery
		if self.battery <= 0:
			print("out of battery, kitty will now quit")
			self.quit()
		## purr sucessfully
		else:
			#decrease battery
			self.battery = self.battery - 3
			#increase happiness
			if self.happinessCurrentIndex != 0:
				self.happinessCurrentIndex = self.happinessCurrentIndex - 1
			return "Kitty purr!"
	def meow(self):
		## out of battery
		if self.battery <= 0:
			print("out of battery, kitty will now quit")
			self.quit()
		## meow successfully
		else:
			## decrease battery
			self.battery = self.battery - 2
			# increase happiness
			if self.happinessCurrentIndex != 0:
				self.happinessCurrentIndex = self.happinessCurrentIndex - 1
			return "Kitty meow!"
	def quit(self):
		print("quitting...")
		print("last position")
		print("Current Position\t", self.location)
		print("Current Battery\t\t", self.battery)
		print("Current happiness\t", self.happinessList[self.happinessCurrentIndex])
		print("Current Direction\t", self.currentFacingDirection)
		print("\n")
		quit()

		pass
	def stateUpdate(self):
		print("Current Position\t", self.location)
		print("Current Battery\t\t", self.battery)
		print("Current happiness\t", self.happinessList[self.happinessCurrentIndex])
		print("Current Direction\t", self.currentFacingDirection)
		print("\n")
		## menu
		print("Kitty Command List")
		print("walk\t\tw")
		print("turn around\tt")
		print("purr\t\tp")
		print("meow\t\tm")
		print("util\t\tu")
		print("quit\t\tq")
		
		# user command
		print("Enter a Kitty Command")
		command = input()
		if command == "w":
			print(self.walk())
		if command == "t":
			print(self.turnAround())
		if command == "p":
			print(self.purr())
		if command == "m":
			print(self.meow())
		if command == "u":
			self.utility()
		if command == "q":
			self.quit()
		


## write a utility function that combines the happiness with the state of the battery
	def utility(self):
		utility = ((4 - self.happinessCurrentIndex)*25) + self.battery
		print("the current utility of the state is,\t\t", utility)

def main():
	k1 = Kitty()
	while(True):
		k1.stateUpdate()

main()









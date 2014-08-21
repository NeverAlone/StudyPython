"""
    多重继承
"""


class Animal():
    """docstring for Animal"""
    pass


class Mammal(Animal):
    """docstring for Mammal"""
    pass


class Bird(Animal):
    """docstring for Bird"""
    pass


class Dog(Mammal):
	"""docstring for Dog"""
	pass


class Bat(Mammal):
	"""docstring for ClassName"""
	pass


class Ostrich(Bird):
	"""docstring for Ostrich"""
	pass


class Runnable():
	"""docstring for Runnable"""
	pass		


class Flyable():
	"""docstring for Flyable"""
	pass


class Dog(Mammal, Runnable):
	"""docstring for Dog"""
	pass


class Bat(Mammal, Flyable):
	"""docstring for Bat"""
	pass
			


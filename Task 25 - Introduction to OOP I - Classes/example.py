# Welcome to the example file for Object Orientated Programming (Part 1).
# Please ensure that you have read through the task file (pdf) before continuing here as some of
# the examples and explanations assume you have done so.

# ==== LET'S OOP! ====

# Breaking our programs into multiple classes (instead of doing everything in one big class) is an essential tool for
# managing bigger tasks with more complexity.

# We'll want our classes to encapsulate the data and the functionality for an object - the blueprint.
# Encapsulate means to enclose, as if in a capsule.
# One of the popular ways of figuring out how to break a complex system into more
# manageable components is to write this information on an index card that is divided into three parts:
# What is the name of the class?
# What responsibilities will it (or the objects we instantiate from it) have?
# What other (types of) objects will it collaborate with?

# =====================================
#  A trivial example of a class
# =====================================

class Cow(object):
    '''
    A triple-quote string is called a docstring and is used to store information
    about the class, function, or file/module in which it is contained.
    It is stored in the 'special variable' __doc__ and may be viewed
    in any of the following ways.

    >>> help(Cow)
    >>> print Cow.__doc__
    >>> cow = Cow()
    >>> help(cow)
    >>> print cow.__doc__

    Documenting the code you write is of fundamental importance.
    Docstrings allow you to somewhat automate the process; there are tools
    like Sphinx and Doxygen that generate documentation from docstrings.
    IDEs like Eclipse can also display them as part of their autocompletion.
    '''
    _noise = 'moo!'
    def __init__(self, colour):
        '''
        This is the constructor for the class SimpleCow.
        A constructor creates a new instance of a class (see the introductory reading).

        To instantiate a class with the constructor, you simply call the class name like a function:
        >>> blue_cow = Cow('blue')
        '''
        self.colour = colour

        

    def make_noise(self):
        '''
        This method prints the cow's noise to the standard output...

        A method is simply a function attached to an object (see reading).
        In Python, methods and properties are accessed with the dot operator:
        >>> blue_cow.make_noise()
        '''
        print(self._noise)

    def set_colour(self, new_colour):
        '''
        To paint the cow a different colour.
        This method is meant to be an example of the way that methods can modify an object's state.

        Get/set methods for object properties are a common sight in object-oriented code,
        but in Python they are not really necessary because Python lacks something called privacy.
        The first expression below is generally considered to be more 'Pythonic' (i.e. idiomatic) than the second:
        >>> blue_cow.colour = 'red'
        >>> blue_cow.set_colour('red')
        '''
        self.colour = new_colour

    def get_colour(self):
        '''
        This method returns the cow's colour.
        '''
        return self.colour

    def __eq__(self, other):
        '''
        This is a comparison special method.  It returns True if the two cows are the same
        colour, and false if they are not.
        This strange-looking method is one of the so-called 'special methods'
        that are part of the Python language.
        Some of the special methods, like __del__(),
        have very specific functions.
        Others, like __eq__, provide the functionality for 'operators'
        like ==, +, -, *, >, etc.  __eq__ corresponds to the equality comparison
        operator ==.

        In other words, the following expressions are equivalent:
        >>> blue_cow == red_cow
        >>> blue_cow.__eq__(red_cow)

        And so are these:
        >>> 'a'.__add__('b')
        >>> 'a' + 'b'

        Implementating these methods for custom classes is called 'operator overloading.'.
        A list of these special methods and their purposes
        may be found at https://docs.python.org/3/reference/datamodel.html#specialnames.

        In practice, it is often better to avoid operator overloading, as it can lead
        to reduced code clarity and strange bugs if errors are not handled correctly.
        '''
        if self.colour == other.colour:
            return True
        else:
            return False

    def __str__(self):
        '''
        This special method is called by Python when you use the 'print' command
        on an object.
        >>> print blue_cow
        'blue moo'
        >>> print blue_cow.__str__()
        'blue moo'
        '''
        return self.colour + ' ' + self._noise

# Create objects
cow_1 = Cow('blue')
cow_2 = Cow('red')

# Call the make noise method
cow_1.make_noise()

# Compare cows
print("Cows are the same:", cow_1 == cow_2)

# Change the colour of a cow
cow_1.set_colour('red')

# Compare the two cows again
print("Cows are the same:", cow_1 == cow_2)

# ==== End of Trivial Example ====

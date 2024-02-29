# @Property
## What is a decorator function?
- A function that adds new functionality to a function that is passed as argument
- wraps in a function and appends several functionalities to existing code and returns it 
- callable = can be called
- decorator is also a callable that returns callable
- metaprogramming 
- Adds without modifying the existing function
## @Property definition
- @property is a built-in decorator for the property() function in Python
- don't have to manually call the inbuilt function | property()
- It gives "special" functionality to certain methods to make them act as getters, setters, or deleters when we define properties in a class
- add getters and setters behind the scenes without affecting the syntax used to access/modify the attribute
## Example use of @property

` # defining class
class Example_class:
    def __init__(self, name): 
        self.__name = name

    @property

    def name(self)
        return self.__name

    @name.setter # to be explained below
        def name(self, val)
        self.__name = val

#setting name
Example_class.name = "Gemma Porrill"

print(Example_class.name)
`
### Example Output:
- Gemma Porrill

### What is happening above?
- @property decorator is used to define the property name in the class Example_class, that has two methods(getter and setter) with similar names i.e, name(), but they have different number of parameters
- `name(self)` -> labelled with @property | getter method
- `name(self, val)` ->used to set the value of name and it is labelled with @name.setter | setter method | continuation to follow

# @Setter
## What is setter method
- A method that allows to set or mutate the value of an attribute in a class
- Public attributes should be used only when sure that no one will ever need to attach behavior to them
- If an attribute is likely to change the internal implementation, then we use getter and setter methods
- Implementation requires:
1. Making attributes non-public 
2. Writing getter and setter methods for each attribute
## Example
`
class Label:
    def __init__(self, text, font):
        self._text = text
        self._font = font

    def get_text(self):
        return self._text

    def set_text(self, value):
        self._text = value

    def get_font(self):
        return self._font

    def set_font(self, value):
        self._font = value
`

- The constructor of Label takes two arguments, text and font
- These arguments are stored in the ._text and ._font non-public instance attributes
- Then define getter and setter methods for both attributes
- Getter methods return the target attribute’s value
- Setter methods take a new value and assign it to the underlying attribute
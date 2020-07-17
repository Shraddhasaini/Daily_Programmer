#Write a Python program to make a chain of function decorators (bold, italic, underline etc.) in Python.
def bold(x):
    def func():
        return "<b>" + x() + "</b>"
    return func

def italic(x):
    def func():
        return "<i>" + x() + "</i>"
    return func

def underline(x):
    def func():
        return "<u>" + x() + "</u>"
    return func

@bold
@italic
@underline
def functoprint():
    return "Hello world"
print(functoprint())

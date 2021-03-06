#!/usr/bin/env python3
if __name__ == '__main__':
    def yell(text):
        return text.upper() + '!'
    
    print(yell('hello'))
    bark = yell
    print(bark('hello'))
    del yell
    print(bark('hello'))
    
    # prints 'yell'
    print(bark.__name__)
    print(bark.__qualname__)

    funcs = [bark, str.lower, str.capitalize]
    for f in funcs:
        print(f('hey there'))

    def greet(func):
        greeting = func('Hi, I am a Python program')
        print(greeting)

    greet(bark)
    print(list(map(bark, ['hello', 'hey', 'hi'])))

    def speak(text):
        def whisper(t):
            return t.lower() + '...'
        return whisper(text)

    print(speak('Hello, World'))
    try:
        whisper('Yo')
    except NameError:
        print("name 'whisper' is not defined")
    try:
        speak.whisper
    except AttributeError:
        print("'function' object has no attribute 'whisper")

    def get_speak_func(text, volume):
        def whisper():
            return text.lower() + '...'
        def yell():
            return text.upper() + '!'
        if volume > 0.5:
            return yell
        else:
            return whisper

    get_speak_func('Hello, World', 0.7)()

    def make_adder(n):
        def add(x):
            return x + n
        return add
    plus_3 = make_adder(3)
    assert plus_3(4) == 7

    # Callable objects
    class Adder:
        def __init__(self, n):
            self.n = n
        def __call__(self, x):
            return self.n + x
        
    plus_3 = Adder(3)
    assert plus_3(4) == 7

    assert callable(plus_3) == True
    assert callable(bark) == True
    assert callable('hello') == False


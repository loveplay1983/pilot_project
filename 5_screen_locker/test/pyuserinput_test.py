# http://www.voidcc.com/project/pyuserinput
#
# from pymouse import PyMouseEvent
# import time
#
#
# class Clickonacci(PyMouseEvent):
#
#     def __init__(self):
#         PyMouseEvent.__init__(self)
#
#     def click(self, x, y, button, press):
#         print(time.time(), button, press)
#
# c = Clickonacci()
# c.run()

from pymouse import PyMouseEvent


def fibo():
    a = 0
    yield a
    b = 1
    yield b
    while True:
        a, b = b, a + b
        yield b


class Clickonacci(PyMouseEvent):
    def __init__(self):
        PyMouseEvent.__init__(self)
        self.fibo = fibo()

    def click(self, x, y, button, press):
        '''Print Fibonacci numbers when the left click is pressed.'''
        if button == 1:
            if press:
                print(self.fibo.__next__())
        else:  # Exit if any other mouse button used
            self.stop()


C = Clickonacci()
C.run()

"""
Traceback (most recent call last):
  File “<pyshell#32>”, line 1, in <module>
    f.next()
AttributeError: ‘generator’ object has no attribute ‘next’

原因是在python 3.x中 generator（有yield关键字的函数则会被识别为generator函数）中的next变为__next__了,next是python 3.x以前版本中的方法
"""

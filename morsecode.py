import winsound
import time



# Define Dots and Stuff
freq=440
def dash():
	winsound.Beep(freq, 600)
	time.sleep(.05)
def dot():
 winsound.Beep(freq, 200)
 time.sleep(.05)
def wait():
	time.sleep(3)

# Define Alphabet
def a():
	dot()
	dash()
	time.sleep(.7)
def b():
	dash()
	dot()
	dot()
	dot()
	time.sleep(.7)
def c():
	dash()
	dot()
	dash()
	dot()
	time.sleep(.7)
def d():
	dash()
	dot()
	dot()
	time.sleep(.7)
def e():
	dot()
	time.sleep(.7)
def f():
	dot()
	dot()
	dash()
	dot()
	time.sleep(.7)
def g():
	dash()
	dash()
	dot()
	time.sleep(.7)
def h():
	dot()
	dot()
	dot()
	dot()
	time.sleep(.7)
def i():
	dot()
	dot()
	time.sleep(.7)

#Code Goes Here
a()
b()
c()
d()
e()
f()
g()
h()
i()

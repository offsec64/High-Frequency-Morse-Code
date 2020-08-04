import winsound
import time
# Define Dots, Dashes, and Frequency.
freq=200
def dash():
    winsound.Beep(freq, 600)
    time.sleep(.05)
def dot():
 winsound.Beep(freq, 200)
 time.sleep(.05)

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
def j():
    dot()
    dash()
    dash()
    dash()
def k():
    dash()
    dot()
    dash()
def l():
    dot()
    dash()
    dot()
    dot()
def m():
    dash()
    dash()
def n():
    dash()
    dot()
def o():
    dash()
    dash()
    dash()
def p():
    dot()
    dash()
    dash()
    dot() 

# Define a Space
def space():
    time.sleep(3)
globals()[' '] = space
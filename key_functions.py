import winsound
import time

# User Define Area
# This is so YOU can tweak the code
freq=880 # Frequency that the morse code is played at in Hz
dotdur=600 # Duration that the dash is played in MSEC
dashdur=200 # Duration that the dot is played in MSEC
spacedur=2 # Duration that the space is in SEC

# Now for the boring definitions for the characters.
# Define Dots and Dashes.
def dash():
    winsound.Beep(freq, dotdur)
    time.sleep(.05)
def dot():
 winsound.Beep(freq, dashdur)
 time.sleep(.05)

# Define Lowercase Alphabet
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
    time.sleep(.7)
def k():
    dash()
    dot()
    dash()
    time.sleep(.7)
def l():
    dot()
    dash()
    dot()
    dot()
    time.sleep(.7)
def m():
    dash()
    dash()
    time.sleep(.7)
def n():
    dash()
    dot()
    time.sleep(.7)
def o():
    dash()
    dash()
    dash()
    time.sleep(.7)
def p():
    dot()
    dash()
    dash()
    dot()
    time.sleep(.7)
def q():
    dash()
    dash()
    dot()
    dash()
    time.sleep(.7)
def r():
    dot()
    dash()
    dot()
    time.sleep(.7)
def s():
    dot()
    dot()
    dot()
    time.sleep(.7)
def t():
    dash()
    time.sleep(.7)
def u():
    dot()
    dot()
    dash()
    time.sleep(.7)
def v():
    dot()
    dot()
    dot()
    dash()
    time.sleep(.7)
def w():
    dot()
    dash()
    dash()
    time.sleep(.7)
def x():
    dash()
    dot()
    dot()
    dash()
    time.sleep(.7)
def y():
    dash()
    dot()
    dash()
    dash()
    time.sleep(.7)
def z():
    dash()
    dash()
    dot()
    dot()
    time.sleep(.7)

# Define Uppercase Alphabet
def A():
    dot()
    dash()
    time.sleep(.7)
def B():
    dash()
    dot()
    dot()
    dot()
    time.sleep(.7)
def C():
    dash()
    dot()
    dash()
    dot()
    time.sleep(.7)
def D():
    dash()
    dot()
    dot()
    time.sleep(.7)
def E():
    dot()
    time.sleep(.7)
def F():
    dot()
    dot()
    dash()
    dot()
    time.sleep(.7)
def G():
    dash()
    dash()
    dot()
    time.sleep(.7)
def H():
    dot()
    dot()
    dot()
    dot()
    time.sleep(.7)
def I():
    dot()
    dot()
    time.sleep(.7)
def J():
    dot()
    dash()
    dash()
    dash()
    time.sleep(.7)
def K():
    dash()
    dot()
    dash()
    time.sleep(.7)
def L():
    dot()
    dash()
    dot()
    dot()
    time.sleep(.7)
def M():
    dash()
    dash()
    time.sleep(.7)
def N():
    dash()
    dot()
    time.sleep(.7)
def O():
    dash()
    dash()
    dash()
    time.sleep(.7)
def P():
    dot()
    dash()
    dash()
    dot()
    time.sleep(.7)
def Q():
    dash()
    dash()
    dot()
    dash()
    time.sleep(.7)
def R():
    dot()
    dash()
    dot()
    time.sleep(.7)
def S():
    dot()
    dot()
    dot()
    time.sleep(.7)
def T():
    dash()
    time.sleep(.7)
def U():
    dot()
    dot()
    dash()
    time.sleep(.7)
def V():
    dot()
    dot()
    dot()
    dash()
    time.sleep(.7)
def W():
    dot()
    dash()
    dash()
    time.sleep(.7)
def X():
    dash()
    dot()
    dot()
    dash()
    time.sleep(.7)
def Y():
    dash()
    dot()
    dash()
    dash()
    time.sleep(.7)
def Z():
    dash()
    dash()
    dot()
    dot()
    time.sleep(.7)

# Define a Space
def space():
    time.sleep(spacedur)
globals()[' '] = space
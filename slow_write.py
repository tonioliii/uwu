from sys import stdout
from time import sleep

def slow_write(text,time):
    for x in range(len(text)):
        sleep(time)
        stdout.write(text[x])
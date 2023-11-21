import RPi.GPIO as IO
IO.setwarnings(False)
IO.setmode(IO.BOARD)
IO.setup(8,IO.IN)
IO.setup(3,IO.OUT)
num = 0
while 1:
    if (IO.input(8) == True):
       print(f"{num}.Obstacle Detected!!")
       num += 1
       IO.output(3, True)
    else:
        IO.output(3, False)

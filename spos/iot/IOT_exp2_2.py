import Adafruit_DHT
import RPi.GPIO as IO
import time

DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4
IO.setwarnings(False)
IO.setmode(IO.BOARD)
IO.setup(3, IO.OUT)
IO.output(3, False)

while True:
	humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
	if humidity is not None and temperature is not None:
		print("temp={0:0.1f}C Humidity={1:0.1f}%".format(temperature, humidity))
		if temperature >= 32.0:
			IO.output(3, True)
		else:
			IO.output(3, False)
	else:
		print("Sensor failure.")
	time.sleep(2)

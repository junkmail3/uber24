# NeoPixel library strandtest example
# Author: Tony DiCola (tony@tonydicola.com)
#
# Direct port of the Arduino NeoPixel library strandtest example.  Showcases
# various animations on a strip of NeoPixels.
import time

from neopixel import *


# LED strip configuration:
LED_COUNT      = 2       # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 64      # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53
LED_STRIP      = ws.WS2811_STRIP_GRB   # Strip type and colour ordering


# Define functions which animate LEDs in various ways.
def colorWipe(strip, color, wait_ms=50):
	"""Wipe color across display a pixel at a time."""
	for i in range(strip.numPixels()):
		strip.setPixelColor(i, color)
		strip.show()
		time.sleep(wait_ms/1000.0)

def wheel(pos):
	"""Generate rainbow colors across 0-255 positions."""
	if pos < 85:
		return Color(pos * 3, 255 - pos * 3, 0)
	elif pos < 170:
		pos -= 85
		return Color(255 - pos * 3, 0, pos * 3)
	else:
		pos -= 170
		return Color(0, pos * 3, 255 - pos * 3)

def fade(c1, c2, wait_ms=50):
	"""Fade start to end in Hex."""
        c1     = "000001"
        c2     = "0000FF"
        
        # endpoint colors are converted from RGB ASCII to HEX values
        start = int(c1, 16)
        end   = int(c2, 16)
        
	for j in range(start, end, 0x01):
                hexj = "%x" % j
                print ('End of Run',hexj)
                #for i in range(strip.numPixels()):
                strip.setPixelColor(1, j+1)
                strip.show()
                time.sleep(wait_ms/100000.0)

def allOff(wait_ms=50):
	for i in range(strip.numPixels()):
		strip.setPixelColor(i, Color(00,00,00))
		strip.show()
		time.sleep(wait_ms/1000.0)


def rainbow(strip, wait_ms=20, iterations=1):
	"""Draw rainbow that fades across all pixels at once."""
	for j in range(256*iterations):
		for i in range(strip.numPixels()):
			strip.setPixelColor(i, wheel((i+j) & 255))
		strip.show()
		time.sleep(wait_ms/1000.0)

def rainbowCycle(strip, wait_ms=20, iterations=5):
	"""Draw rainbow that uniformly distributes itself across all pixels."""
	for j in range(256*iterations):
		for i in range(strip.numPixels()):
			strip.setPixelColor(i, wheel((int(i * 256 / strip.numPixels()) + j) & 255))
		strip.show()
		time.sleep(wait_ms/1000.0)

def theaterChaseRainbow(strip, wait_ms=50):
	"""Rainbow movie theater light style chaser animation."""
	for j in range(256):
		for q in range(3):
			for i in range(0, strip.numPixels(), 3):
				strip.setPixelColor(i+q, wheel((i+j) % 255))
			strip.show()
			time.sleep(wait_ms/1000.0)
			for i in range(0, strip.numPixels(), 3):
				strip.setPixelColor(i+q, 0)


def smoothRGB(R, G, B, step): # moves to new color directly from old color. step mean speed
        global prevR
        global prevG
        global prevB

        for i in range(255):
                time.sleep(50/10000.0) 
                #MoveRed
                if (i >= prevR - R and prevR < R):
                        prevR = prevR + step
                if (i >= R - prevR and prevR > R):
                        prevR = prevR - step
                
                #MoveGreen
                if (i >= prevG - G and prevG < G):
                        prevG = prevG + step
                if (i >= G - prevG and prevG > G):
                        prevG = prevG - step
                
                #MoveBlue
                if (i >= prevB - B and prevB < B):
                        prevB = prevB + step
                if (i >= B - prevB and prevB > B):
                        prevB = prevB - step

                # Show the colors
                for j in range(0,2):
                        strip.setPixelColor(j,Color(prevR,prevG,prevB))
                        strip.show()


def eyePowerUp(LED, wait_ms=50):
	"""Start from zero,spark up, then ramp to full glow. Pulse near full glow."""
        smoothRGB(0,0,0,16)                             #blackout
        #strip.setPixelColor(LED,Color(122,122,122))     #instant then out
        #strip.show()
        allOff()
        time.sleep(wait_ms/1000.0)
        smoothRGB(25,25,25,16)   #dull grey
        smoothRGB(250,0,0,1)   #to black
        smoothRGB(80,0,0,1)   #ramp up to red
        print (prevR, prevG, prevB)


        
# Main program logic follows:
if __name__ == '__main__':
	# Create NeoPixel object with appropriate configuration.
	strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
	# Intialize the library (must be called once before other functions).
	strip.begin()

        prevR = 0
        prevG = 0
        prevB = 0

	print ('Press Ctrl-C to quit.')
        print ('All Off.')
        allOff()
	
        print ('Eye Power Up.')
        eyePowerUp(1)

#	while True:
		#print ('Color wipe animations.')
		#colorWipe(strip, Color(255, 0, 0))  # Red wipe
		#colorWipe(strip, Color(0, 255, 0))  # Blue wipe
		#colorWipe(strip, Color(0, 0, 255))  # Green wipe
		
		#print ('Theater chase animations.')
		#theaterChase(strip, Color(127, 127, 127))  # White theater chase
		#theaterChase(strip, Color(127,   0,   0))  # Red theater chase
		#theaterChase(strip, Color(  0,   0, 127))  # Blue theater chase

		#print ('Rainbow animations.')
		#rainbow(strip)
		#rainbowCycle(strip)
		#theaterChaseRainbow(strip)

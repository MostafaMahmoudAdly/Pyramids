"""""
import RPi.GPIO as GPIO
import time
 
# Pin Definitions
led_pin = 18  # The GPIO pin number where the LED is connected
 
# Set up GPIO mode
GPIO.setmode(GPIO.BCM)  # Use BCM pin numbering
GPIO.setup(led_pin, GPIO.OUT)  # Set pin as output
 
try:
    while True:
        GPIO.output(led_pin, GPIO.HIGH)  # Turn on the LED
        time.sleep(1)  # Wait for 1 second
        GPIO.output(led_pin, GPIO.LOW)  # Turn off the LED
        time.sleep(1)  # Wait for 1 second
 
except KeyboardInterrupt:
    # Cleanup GPIO settings before exiting
    GPIO.cleanup()
"""

import time
from mock_gpio import GPIO  # Replace with actual RPi.GPIO if running on a Pi

# Pin Definitions
led_pin = 18  # The GPIO pin number where the LED is connected

# Set up GPIO mode
GPIO.setmode(GPIO.BCM)  # Use BCM pin numbering
GPIO.setup(led_pin, GPIO.OUT)  # Set pin as output

try:
    while True:
        GPIO.output(led_pin, GPIO.HIGH)  # Turn on the LED
        time.sleep(1)  # Wait for 1 second
        GPIO.output(led_pin, GPIO.LOW)  # Turn off the LED
        time.sleep(1)  # Wait for 1 second

except KeyboardInterrupt:
    # Cleanup GPIO settings before exiting
    GPIO.cleanup()

from microbit import *
import neopixel
import pca9685

# Initialize PCA9685
pca9685.init()
pca9685.set_pwm_freq(50)  # 50Hz for Servo & Motor

# Initialize NeoPixel (WS2812B)
np = neopixel.NeoPixel(pin0, 8)  # 8 NeoPixels on Pin 0

# Function to move Servo
def move_servo(channel, angle):
    pulse = int((angle / 180) * (600 - 150) + 150)  # Convert angle to pulse
    pca9685.set_pwm(channel, 0, pulse)

# Function to set motor speed (0-4095)
def set_motor_speed(channel, speed):
    pca9685.set_pwm(channel, 0, speed)

# Function to change LED color
def set_led_color(r, g, b):
    for i in range(8):
        np[i] = (r, g, b)
    np.show()

# Main loop
while True:
    # Move Servo between 0° and 180°
    move_servo(0, 0)
    sleep(500)
    move_servo(0, 180)
    sleep(500)

    # Set DC Motor Speed (Half Speed)
    set_motor_speed(1, 2048)
    sleep(1000)
    set_motor_speed(1, 0)  # Stop motor
    sleep(1000)

    # Change LED Color
    set_led_color(255, 0, 0)  # Red
    sleep(500)
    set_led_color(0, 255, 0)  # Green
    sleep(500)
    set_led_color(0, 0, 255)  # Blue
    sleep(500)

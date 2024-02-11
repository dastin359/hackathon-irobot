import os
import time

from  pycreate2 import Create2
import time

def launch_irobot():
    port = "/dev/ttyUSB0"  # where is your serial port?
    bot = Create2(port)
    
    # Start the Create 2
    bot.start()
    
    # Put the Create2 into 'safe' mode so we can drive it
    # This will still provide some protection
    bot.safe()
    
    # You are responsible for handling issues, no protection/safety in
    # this mode ... becareful
    # bot.full()
    
    # directly set the motor speeds ... move forward
    # bot.drive_direct(100, 100)
    # time.sleep(5)
    
    # turn in place
    bot.drive_direct(100,0)  # inputs for motors are +/- 500 max
    time.sleep(10)
    
    # Stop the bot
    bot.drive_stop()
    
    # query some sensors
    sensors = bot.get_sensors()  # returns all data
    print(sensors.light_bumper_left)
    
    # Close the connection
    bot.close()


def main():
    #example of using micro and speakers
    print("Start recording audio")
    sample_name = "aaaa.wav"
    cmd = f'arecord -vv --format=cd --device={os.environ["AUDIO_INPUT_DEVICE"]} -r 48000 --duration=10 -c 1 {sample_name}'
    print(cmd)
    os.system(cmd)
    print("Playing sound")
    os.system(f"ffplay -nodisp -autoexit -loglevel quiet {sample_name}")
    
    # Capture image
    import cv2
    camera_capture = cv2.VideoCapture(0)
    rv, image = camera_capture.read()
    print(f"Image Dimensions: {image.shape}")
    camera_capture.release()

    # Use wrapper in context manager to lease control, turn on E-Stop, power on the robot and stand up at start
    # and to return lease + sit down at the end

    # launch_irobot()

if __name__ == '__main__':

    import subprocess
    result = subprocess.run(['lscpu'], stdout=subprocess.PIPE)
    print(result.stdout.decode('utf-8'))

    result = subprocess.run(['nvidia-smi'], stdout=subprocess.PIPE)
    print(result.stdout.decode('utf-8'))

    import cv2
    print(200)
    camera_capture = cv2.VideoCapture(0)
    rv, image = camera_capture.read()
    print(f"Image Dimensions: {image.shape}")
    camera_capture.release()
    # main()
    # launch_irobot()

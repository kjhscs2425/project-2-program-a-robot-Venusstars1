# Import the robot control commands from the library
from simulator import robot
import time

#left, right = robot.sonars()
#robot.motors(1, -1, 10)

#every second it goes 60 milimeters
#In the top and botttom walls it runs into it if you spin and then dance
#1.5 to spin 90 degrees

def sonar_dimensions(forwards, backwards):
    remainder = float(input("How many seconds would you like to go move? "))
    left_distance, right_distance = robot.sonars()
    while remainder > 0.5:
        left_distance, right_distance = robot.sonars()
        robot.motors(forwards, backwards, 0.1)
        remainder -= 0.1
        if left_distance <= 100 and right_distance <= 100:
            robot.motors(0, 0, 5)
            print("I am sorry but I am going to run into the wall")
            beginning()
            return
    if left_distance <= 100 and right_distance <= 100:
            robot.motors(0, 0, 5)
            print("I am sorry but I am going to run into the wall")
            beginning()
            return
    else:
        beginning()

def sonar_dimension():
    remainder = 3
    left_distance, right_distance = robot.sonars()
    print(left_distance, right_distance)
    while remainder >= 0.5:
        left_distance, right_distance = robot.sonars()
        robot.motors(1, 1, 0.1)
        print(left_distance, right_distance)
        remainder -= 0.1
        if left_distance <= 100 and right_distance <= 100:
            robot.motors(0, 0, 1)
            print("I am sorry but I am going to run into the wall")
            return
    if left_distance <= 100 and right_distance <= 100:
            robot.motors(0, 0, 1)
            print("I am sorry but I am going to run into the wall")
            return

def move():
    moving = input("Would you like to move forward or backward? ")
    if moving == "forward" or moving == "Forward":
        def forward():
            print("Thank you for picking the drive forward option")
            sonar_dimensions(1, 1)
        go = forward
        go()
        beginning()
    elif moving == "backwards" or moving == "Backward" or moving == "Backwards" or moving == "backward":
        def backward(forward_2, backward_2):
            print("Thank you for picking the drive backward option")
            back = float(input("How many seconds would you like to drive backwards for?"))
            if back <= 3:
                robot.motors(forward_2, backward_2, back)
            else:
                print("I am sorry but the amount of time has to be under 3 seconds, please try again")
                backward(-1, -1)
        backward(-1, -1)
        beginning()
    else:
        print("I am sorry but that is not a valid request, please try again ")
        move()

def spin():
    time = (float(input("How many seconds would you like to spin? ")))
    def turn():
        spin = (input("Would you like to turn left or right? "))
        if spin == "left":
            def turn_left(left):
                robot.motors(1, left, time)
            turn_left(-1)
            beginning_2()
        elif spin == "right":
            def turn_right(right):
                robot.motors(right, 1, time)
            turn_right(-1)
            beginning_2()
        else:
            print("I am sorry but that is not a valid request, please try again: ")
            turn()
    turn()
    spin()

def dance():
    print("Thank you for selecting the dance option, please enjoy this beautiful dance")
    dance_seconds = 2
    dance_loop = (input("How many seconds would you like the robot to dance? 8, 16, 24, or 32 seconds? "))
    dance_loop = int(dance_loop)
    if dance_loop == 8 or dance_loop == 16 or dance_loop == 24 or dance_loop == 32:
        for i in range(dance_loop//8):
            robot.motors(-1, 1, dance_seconds)
            robot.motors(1, -1, dance_seconds)
            sonar_dimension()
            robot.motors(-1, -1, dance_seconds)
        print("Thank you for picking the dance option, I hope you enjoyed")
        beginning()
    else:
        print("I am sorry but that is not a valid amount of time, please try again")
        dance()

def drive_around(spin):
    print("Thank you for picking the drive around options, please enjoy ")
    range_1 = 5
    robot.motors(1, 1, 2.8)
    robot.motors(1, -1, spin)
    robot.motors(1, 1, 1)
    robot.motors(1, -1, spin)
    robot.motors(1, 1, 2.8)
    for i in range(range_1):
        robot.motors(1, 1, 2.5)
        robot.motors(1, -1, spin)
        robot.motors(1, 1, 1.5)
        robot.motors(1, -1, spin)
        robot.motors(1, 1, 2.5)
    robot.motors(0, 0, 2)
    robot.motors(1, -1, 1.5319148936170213)
    robot.motors(1, 1, 0.45)
    robot.motors(-1, 1, 1.5319148936170213)
    beginning()

def beginning ():
    option = input("Which of the following activities would you like the robot to perform?: Moving, Spinning, or Dancing? ")
    if option == "Moving" or option == "moving":
        move()
    elif option == "Spinning" or option == "spinning":
        spin()
    elif option == "Dancing" or option == "dancing" or option == "Dance" or option == "dance":
        dance()
    else:
        print("I am sorry but that is not a valid input, please try again: ")
        beginning()

def beginning_2 ():
    option = input("Which of the following activities would you like the robot to perform?: Moving or Spinning? ")
    if option == "Moving" or option == "moving":
        move()
    elif option == "Spinning" or option == "spinning":
        spin()
    else:
        print("I am sorry but that is not a valid input, please try again: ")
        beginning_2()

def beginning_1 ():
    option = input("Which of the following activities would you like the robot to perform?: Moving, Spinning, Dancing, or Drive-Around? ")
    if option == "Moving" or option == "moving":
        move()
    elif option == "Spinning" or option == "spinning":
        spin()
    elif option == "Dancing" or option == "dancing" or option == "Dance" or option == "dance":
        dance()
    elif option == "Drive-Around" or option == "drive-around" or option == "Drive-around" or option == "drive-around" or option == "drive around" or option == "Drive around" or option == "Drive Around":
        drive_around(1.5319148936170213)
    else:
        print("I am sorry but that is not a valid input, please try again: ")
        beginning_1()
beginning_1()
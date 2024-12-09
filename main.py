# Import the robot control commands from the library
from simulator import robot
from time import *

# left, right = robot.sonars()

def spin(spin_direction,spin_duration):
    spin_direction = input("do you want to spin left (L) or right (R)? ")
    spin_duration = float(input("how long do you want to spin for? "))
    if spin_direction == "r" or spin_direction == "R" or spin_direction == "right" or spin_direction == "Right":
        robot.motors(-1, 1, spin_duration)
    if spin_direction == "l" or spin_direction == "L" or spin_direction == "left" or spin_direction == "Left":
        robot.motors(1,-1, spin_duration)

def turn90():
    turn_direction = input("do you want to turn left (L) or right (R)? ")
    if turn_direction == "r" or turn_direction == "R" or turn_direction == "right" or turn_direction == "Right":
        robot.motors(-1, 1, (90/58.8))
    if turn_direction == "l" or turn_direction == "L:" or turn_direction == "left" or turn_direction == "Left":
        robot.motors(1, -1, (90/58.8))

def dance():
    robot.motors(-1,1,1)
    robot.motors(1,-1,2)
    robot.motors(-1,1,1)
    robot.motors(1,1,1)
    robot.motors(-1,-1,2)
    robot.motors(1,1,1)
    robot.motors(1,-1,1)
    robot.motors(-1,1,2)
    robot.motors(1,-1,1)
    robot.motors(-1,-1,1)
    robot.motors(1,1,2)
    robot.motors(-1,-1,1)
    robot.motors(-1,1,1)
    robot.motors(1,-1,2)
    robot.motors(-1,1,1)

def drive():
    drive_duration = float(input("how long do you want to drive for? "))
    l = 1
    r = 1
    def forward_drive(drive_duration):
        remainder = drive_duration
        left,right=robot.sonars()
        if left<100 or right<100:
            robot.motors(-r, l, 3.04)
            if remainder <0.1:
                return
            forward_drive(remainder)
        else:
            robot.motors(r, l, 0.1)
            remainder = remainder-0.1
            if remainder <0.1:
                return
            forward_drive(remainder)

    forward_drive(drive_duration)
            
    # robot.motors(r,l,drive_duration)

# def center():
#     no=2
# # def backup():
# #     robot.motors(1,1,30)
def stay():
    stay_in_place = float(input("How long do you want to stay for? "))
    robot.motors(0,0,stay_in_place)
    move()

def move():
    hi = input("Hi! I'm robobunny. What would you like me to do? I can spin, turn90, dance, drive, or stay \n")
    if hi == str("spin"):
        spin()
    if hi == str("turn90"):
        turn90()
    if hi == str("dance"):
        dance()
    if hi == str("drive"):
        drive()
    if hi == str("stay"):
        stay()
    else:
        print("Sorry, I don't know how to do that. Please try again")
    move()
       
move()

# def play_snake(position):
#     new_position=position
#     position_angle=90 or position_angle=-90 or position_angle=180 or position_angle=-180
        
#     return new_postition

           











# def right_spin(seconds):
#             seconds = float(input("How long do you want to spin right for(in seconds)? \n"))
#             robot.motors(-1, 1, seconds)

# def left_spin(seconds):
#             seconds = float(input("How long do you want to spin left for(in seconds)? \n"))
#             robot.motors(-1, 1, seconds)
#         # left_spin = float(input("How long do you want to spin left for(in seconds)? \n"))
#         # robot.motors(1, -1, left_spin)
# def go():
#             seconds = float(input("How long do you want to go for(in seconds)? \n"))
#             robot.motors(1, 1, seconds)

# while True:
#     command = input("Whatchawannado?")
#     if command == "exit":
#         robot.exit()
#     else:
#         def whatyawannado():
#             command = input("Whatchawannado?")
#             if command == "exit":
#                 robot.exit()
#             if command == str("go"):
#                 go()
#             if command == str("right_spin"):
#                    right_spin()
#             if command == str("left_spin"):
#                    left_spin()       
        
#         whatyawannado()
 
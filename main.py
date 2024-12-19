# Import the robot control commands from the library
from simulator import robot
from time import *
# import matplotlib
# matplotlib.use("macOSX")

# left, right = robot.sonars()

degree = 0

def spin(spin_direction, spin_duration):
    global degree
    if spin_direction == "r" or spin_direction == "R" or spin_direction == "right" or spin_direction == "Right":
        robot.motors(-1, 1, spin_duration)
        degree = (degree-(spin_duration*58.8))%360
        print(degree)
    if spin_direction == "l" or spin_direction == "L" or spin_direction == "left" or spin_direction == "Left":
        robot.motors(1,-1, spin_duration)
        degree = (degree+(spin_duration*58.8))%360
        print(degree)

def turn90():
    global degree
    turn_direction = input("do you want to turn left (L) or right (R)? ")
    if turn_direction == "r" or turn_direction == "R" or turn_direction == "right" or turn_direction == "Right":
        robot.motors(-1, 1, (90/58.8))
        degree = (degree-90)%360
    if turn_direction == "l" or turn_direction == "L:" or turn_direction == "left" or turn_direction == "Left":
        robot.motors(1, -1, (90/58.8))
        degree = (degree+90)%360

def dance():
    global degree
    dancing = float(input("how many dance loops do you want me to do (one loop is 10 seconds)? "))
    while dancing > 0:
        robot.motors(-1,1,0.5)
        robot.motors(1,-1,1)
        robot.motors(-1,1,0.5)
        robot.motors(1,1,0.5)
        robot.motors(-1,-1,1)
        robot.motors(1,1,0.5)
        robot.motors(1,-1,0.5)
        robot.motors(-1,1,1)
        robot.motors(1,-1,0.5)
        robot.motors(-1,-1,0.5)
        robot.motors(1,1,1)
        robot.motors(-1,-1,0.5)
        robot.motors(-1,1,0.5)
        robot.motors(1,-1,1)
        robot.motors(-1,1,0.5)
        dancing-=1
        degree = degree%360

def drive():
    global degree
    drive_duration = float(input("how long do you want to drive for? "))
    l = 1
    r = 1
    def forward_drive(drive_duration):
        global degree
        #print(drive_duration)
        remainder = drive_duration
        left,right=robot.sonars()
        if left<100 or right<100:
            robot.motors(-r, l, 3.06)
            remainder = remainder-0.1
            degree = (degree+180)%360
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

def center():
    global degree
    print(degree)
    if (degree%360)<=180:
        print("less than 180")
        robot.motors(-1, 1, (degree)/58.8)
    if degree%360>180:
        robot.motors(1,-1, 180-(degree-180))
    #og sensor reading is 260
    left,right=robot.sonars()
    print(left, right)
    if left<=260 or right<=260:
        robot.motors(-1,-1, 260-left)
    if left>260 or right>260:
        robot.motors(1,1, left-260)

def stay():
    global degree
    stay_in_place = float(input("How long do you want to stay for? "))
    robot.motors(0,0,stay_in_place)
    degree = (degree)%360
    move()

def move():
    global degree
    hi = input("Hi! I'm robobunny. What would you like me to do? I can spin, turn90, dance(before you run this, make sure you are in the middle of the box), drive, or stay \n")

    if hi == str("spin"):
        spin_direction = input("do you want to spin left (L) or right (R)? ")
        spin_duration = float(input("how long do you want to spin for? "))
        spin(spin_direction,spin_duration)
    if hi == str("turn90"):
        turn90()
    if hi == str("dance"):
        dance()
    if hi == str("drive"):
        drive()
    if hi == str("stay"):
        stay()
    if hi == str("center"):
        center()
    else:
        print("Sorry, I don't know how to do that. Please try again")
    move()

# def move():
#     spin("l", 1)
#     center()
       
move()

# def play_snake(position):
#     new_position=position
    # position_angle==90 or position_angle==-90 or position_angle==180 or position_angle=0

# def turn_1(position):
#         if input == ("w"):
#             if direction == 90:
#                 wait
#             elif direction == right:
#                 w

#     if position_angle==90:
        
#     return new_postition
# else:
#     go(posit
       
# def go(position):
#     new_position=position
#     instructions = "you can press wasd to go in different directions"
#     wasd = input(instructions)
#     if wasd == w:
#         w(position)
#     if wasd == a:
#         a(position)
#     if wasd == s:
#         s(position)
#     if wasd == d:
#         d(position)

# def turn_right(position):
#     robot.motors(-1, 1, (90/58.8))
#     go(position)

# def turn_left(position):
#     robot.motors(1, -1, (90/58.8))
#     go(position)

# def w(position):
#     #90 degrees
#     if position==90:
#         w(position)
#         new_position=90
#     if position==0:
#         turn_left(position)
#         new_position=90
#     if position==180:
#         turn_right(position)
#         new_position=90
#     if position==-90:
#         w(position)
        
# def a(position):
#     #180 degrees
#     if position==90:
#         turn_left(position)
#         new_position=180
#     if position==0:
#         a(position)
#     if position==180:
#         a(position)
#     if position==-90:
#         turn_right(position)
#         new_position=180

# def s(position):
#     #-90 degrees
#     if position==90:
#         s(position)
#     if position==0:
#         turn_right(position)
#         new_position=-90
#     if position==180:
#         turn_left(position)
#         new_position=180
#     if position==-90:
#         s(position)

# def d(position):
#     #0 degrees
#     if position==90:
#         turn_right()
#         new_position=0
#     if position==0:
#         d(position)
#     if position==180:
#         d(position)
#     if position==-90:
#         turn_left(position)


# def begin(position):
#     hi=input("hi, we're going to play snake! press space to begin.")
#     if hi == ("m"):
#         go(position)
#     else:
#         begin(position)

# begin(0)

    # def turn90():
#     turn_direction = input("do you want to turn left (L) or right (R)? ")
#     if turn_direction == "r" or turn_direction == "R" or turn_direction == "right" or turn_direction == "Right":
#         robot.motors(-1, 1, (90/58.8))
#     if turn_direction == "l" or turn_direction == "L:" or turn_direction == "left" or turn_direction == "Left":
#         robot.motors(1, -1, (90/58.8))
           











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
 
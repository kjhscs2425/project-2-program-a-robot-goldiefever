import pygame

left_motor = 0
right_motor = 0

pygame.init()

while True:
    for event in pygame.event.get(): 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w: 
                def w(position):
                    #90 degree
                    if position==90:
                        w(position)
                        new_position=90
                    if position==0:
                        turn_left(position)
                        new_position=90
                    if position==180:
                        turn_right(position)
                        new_position=90
                    if position==-90:
                        w(position)

            elif event.key == pygame.K_a: 
                def a(position):
                    #180 degrees
                    if position==90:
                        turn_left(position)
                        new_position=180
                    if position==0:
                        a(position)
                    if position==180:
                        a(position)
                    if position==-90:
                        turn_right(position)
                        new_position=180

            elif event.key == pygame.K_s:
                def s(position):
                #-90 degrees
                    if position==90:
                        s(position)
                    if position==0:
                        turn_right(position)
                        new_position=-90
                    if position==180:
                        turn_left(position)
                        new_position=180
                    if position==-90:
                        s(position)

            elif event.key == pygame.K_d: 
                 def d(position):
                    #0 degrees
                    if position==90:
                        turn_right()
                        new_position=0
                    if position==0:
                        d(position)
                    if position==180:
                        d(position)
                    if position==-90:
                        turn_left(position)

            

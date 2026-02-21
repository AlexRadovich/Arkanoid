from raylib import *
from settings import *
from pyray import *



class Player():
    def __init__(self,position,size,num_lives,speed=300):
        self.position = position
        self.size = size
        self.life = num_lives
        self.speed = speed

    def update(self):
        motion = Vector2(0, 0)

        if is_key_down(KeyboardKey.KEY_RIGHT):
            motion.x += 1
        elif is_key_down(KeyboardKey.KEY_LEFT):
            motion.x -= 1
        
        motion_this_frame = vector2_scale(motion, get_frame_time() * self.speed)
        self.position = vector2_add(self.position, motion_this_frame)


    def draw(self):
        draw_rectangle_v(self.position,self.size,WHITE)
    

class Ball():

    def __init__(self,position,speed,radius,active):
        self.position = position
        self.speed = speed
        self.radius = radius
        self.active = active

    def draw(self):
        draw_circle_v(self.position,self.radius,WHITE)

    def update(self,playerx,playery,playerwidth,playerheight):

        if (self.position.x > WINDOW_WIDTH or self.position.x <= 0):
            self.speed.x = self.speed.x * -1.0

        if (self.position.y <= self.radius):
            self.speed.y =  self.speed.y * - 1.0

        if(self.position.y >=  WINDOW_HEIGHT):
            pass
            #loselife

        if(check_collision_circle_rec(self.position,self.radius,Rectangle(playerx,playery,playerwidth,playerheight))):
            if self.speed.y > 0:
                self.speed.y *= -1
                self.speed.x = (self.position.x - (playerx+(.5*playerwidth)))  * 7
        #do ball-brick collision

        motion_this_frame = vector2_scale(self.speed, get_frame_time())
        self.position = vector2_add(self.position, motion_this_frame)



    



class Brick():
    bricksize = Vector2(WINDOW_WIDTH//(NUM_COLS+1) , 40)

    def __init__(self, position, active):
        self.position = position
        self.active = active

    def update(self):
        pass

    def draw(self,color):
        draw_rectangle_v(self.position,self.bricksize,color)


class Game():

    def __init__(self):
        bricksize = Vector2(WINDOW_WIDTH//(NUM_COLS+1) , 40)
        self.player = Player(Vector2(WINDOW_WIDTH//2 , WINDOW_HEIGHT *7//8) , Vector2(WINDOW_WIDTH//10,20), MAX_LIVES)
        self.ball = Ball(Vector2(self.player.position.x + (.5) * self.player.size.x,self.player.position.y - self.player.size.y//2 - BALL_RADIUS) , Vector2(0,400), BALL_RADIUS , False)
        self.bricks = [[0 for i in range(NUM_COLS)] for j in range(NUM_ROWS)]

        for i in range(NUM_ROWS):
            for j in range(NUM_COLS):
                self.bricks[i][j] = Brick(Vector2(j*bricksize.x + bricksize.x//2, i*bricksize.y + INIT_DOWN_POS) , True)


    def update(self):
        self.player.update()
        self.ball.update(self.player.position.x,self.player.position.y,self.player.size.x,self.player.size.y)

        
    def draw(self):
        self.player.draw()
        self.ball.draw()
        for i in range(NUM_ROWS):
            for j in range(NUM_COLS):
                if((i+j) %2 == 0):
                    self.bricks[i][j].draw(DARKGRAY)
                else:
                    self.bricks[i][j].draw(GRAY)
        #draw life lines




    def startup(self):
        pass


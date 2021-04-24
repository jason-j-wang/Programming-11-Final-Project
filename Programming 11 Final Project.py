import simplegui, random
#1v1 multiplayer game written by Jason Wang

# Global fixed variables

#images
TITLE = simplegui.load_image("https://i.imgur.com/dOOfQtW.png")
BACKGROUND = simplegui.load_image("https://i.imgur.com/g8jzZGy.png")
MAIN_MENU_BG = simplegui.load_image("https://i.imgur.com/ZcaUSEw.png")
MAIN_MENU_BG_BUILDING = simplegui.load_image("https://i.imgur.com/ARyhm9L.png")
CONTROLS = simplegui.load_image("https://i.imgur.com/amx0Tik.png")
RULES = simplegui.load_image("https://i.imgur.com/Jw3xeWB.png")
PAUSE_BUTTON = simplegui.load_image("https://i.imgur.com/Ecu4sSm.png")
PLAY_BUTTON = simplegui.load_image("https://i.imgur.com/ZZKSsgq.png")
BACK_BUTTON = simplegui.load_image("https://i.imgur.com/zOiSoe6.png")
CONTROLS_BUTTON = simplegui.load_image("https://i.imgur.com/nklW9s9.png")
CONTINUE_BUTTON = simplegui.load_image("https://i.imgur.com/fHh2rgx.png")
RESUME_BUTTON = simplegui.load_image("https://i.imgur.com/Uhl4xG5.png")
RETURN_TO_MAIN_MENU_BUTTON = simplegui.load_image("https://i.imgur.com/oSa0Mp2.png")
RESTART_BUTTON = simplegui.load_image("https://i.imgur.com/NLPFtK7.png")
INFO_BUTTON = simplegui.load_image("https://i.imgur.com/qApcCMO.png")
PLAY_AGAIN_BUTTON = simplegui.load_image("https://i.imgur.com/BTyu6P2.png")
IDLE_LEFT = simplegui.load_image("https://i.imgur.com/JCXglog.png")
IDLE_RIGHT = simplegui.load_image("https://i.imgur.com/pdlyVjG.png")
RUN_LEFT = simplegui.load_image("https://i.imgur.com/D9dGuAq.png")
RUN_RIGHT = simplegui.load_image("https://i.imgur.com/YBtZxgP.png")
LADDER_CLIMB = simplegui.load_image("https://i.imgur.com/W3FL6Z8.png")
IDLE_GUN_LEFT = simplegui.load_image("https://i.imgur.com/XOHauOp.png")
IDLE_GUN_RIGHT = simplegui.load_image("https://i.imgur.com/mUV3uyH.png")
IDLE_KNIFE_LEFT = simplegui.load_image("https://i.imgur.com/KPy0rSO.png")
IDLE_KNIFE_RIGHT = simplegui.load_image("https://i.imgur.com/9K9keBA.png")
RUN_LEFT_GUN = simplegui.load_image("https://i.imgur.com/ujaSlDc.png")
RUN_RIGHT_GUN = simplegui.load_image("https://i.imgur.com/O60EfoG.png")
RUN_LEFT_KNIFE = simplegui.load_image("https://i.imgur.com/8eiRGcy.png")
RUN_RIGHT_KNIFE = simplegui.load_image("https://i.imgur.com/SWHjr5b.png")
SHOOTING_LEFT = simplegui.load_image("https://i.imgur.com/9wgpkZx.png")
SHOOTING_RIGHT = simplegui.load_image("https://i.imgur.com/3CJ56vL.png")
PUNCHING_LEFT = simplegui.load_image("https://i.imgur.com/TuyMEW7.png")
PUNCHING_RIGHT = simplegui.load_image("https://i.imgur.com/eUXy3KR.png")
MELEE_LEFT = simplegui.load_image("https://i.imgur.com/0TN6Lc0.png")
MELEE_RIGHT = simplegui.load_image("https://i.imgur.com/2iRkhCO.png")
DIE_LEFT = simplegui.load_image("https://i.imgur.com/8ti2mfw.png")
DIE_RIGHT = simplegui.load_image("https://i.imgur.com/i9DAqWL.png")
DEAD_LEFT = simplegui.load_image("https://i.imgur.com/I19b1LQ.png")
DEAD_RIGHT = simplegui.load_image("https://i.imgur.com/e4teMiZ.png")
GUN = simplegui.load_image("https://i.imgur.com/FtF34t1.png")
GUN_PROMPT = simplegui.load_image("https://i.imgur.com/200ASMz.png")
KNIFE = simplegui.load_image("https://i.imgur.com/TzOdQyX.png")
KNIFE_PROMPT = simplegui.load_image("https://i.imgur.com/pCslETb.png")
BULLET_LEFT = simplegui.load_image("https://i.imgur.com/kNilD1e.png")
BULLET_RIGHT = simplegui.load_image("https://i.imgur.com/NlhtEay.png")
HEALTH_PACKAGE = simplegui.load_image("https://i.imgur.com/luqWFQY.png")
HEALTH_PACKAGE_PROMPT = simplegui.load_image("https://i.imgur.com/7E7NXva.png")
HP_FADE = simplegui.load_image("https://i.imgur.com/Zr3XcBL.png")
GUN_FADE = simplegui.load_image("https://i.imgur.com/xQ7kSXu.png")
KNIFE_FADE = simplegui.load_image("https://i.imgur.com/PkrJgg4.png")
PLATFORM = simplegui.load_image("https://i.imgur.com/rlHXVLb.png")
WALL = simplegui.load_image("https://i.imgur.com/s4n6iIz.png")
LADDER = simplegui.load_image("https://i.imgur.com/kUY5GNU.png")
GROUND_IMG = simplegui.load_image("https://i.imgur.com/pfDKDCq.png")
P1_FIST_SLOT = simplegui.load_image("https://i.imgur.com/FfIq7EF.png")
P1_KNIFE_SLOT = simplegui.load_image("https://i.imgur.com/8qzekM2.png")
P1_GUN_SLOT = simplegui.load_image("https://i.imgur.com/Olw2njv.png")
P2_FIST_SLOT = simplegui.load_image("https://i.imgur.com/2J5F3qq.png")
P2_KNIFE_SLOT = simplegui.load_image("https://i.imgur.com/ESBstJo.png")
P2_GUN_SLOT = simplegui.load_image("https://i.imgur.com/s6UGI34.png")

#game constants
FRAME_WIDTH = 1400
FRAME_HEIGHT = 850
GRAVITY = 1
GROUND = 800
BGRD_SPEED = 3
BGRD_SPEED_SKY = 1

PLAYER_SIZE = (300, 200)
PLAYER_WIDTH = 90
PLAYER_HEIGHT = 90
PLAYER_SPEED = 5
PLAYER_HEALTH = 100
PLAYER_1_STARTING_POS = [[1300, 100], [1200, 300], [1200, 700]]
PLAYER_2_STARTING_POS = [[70, 150], [70, 400], [70, 700]]

CLIMB_VEL = 5
JUMP_VEL = 15

BULLET_SIZE = (100, 100)
BULLET_WIDTH = 20
BULLET_HEIGHT = 3
BULLET_SPEED = 30 # horizontal only

GUN_SIZE = (250, 250)
GUN_WIDTH = 80
GUN_HEIGHT = 20
KNIFE_SIZE = (300, 300)
KNIFE_WIDTH = 70
KNIFE_HEIGHT = 18
HP_SIZE = (200, 200)
HP_WIDTH = 50
HP_HEIGHT = 40
ITEM_LIFE_SPAN = 1200
ITEM_FADE_SPAN = 450

PUNCH_RANGE = 65 #from center
WEAPON_RANGE = 75 #from center

DURABILITY = 7
EXTRA_MAGS = 1
AMMO = 31

player_1_score = 0
player_2_score = 0
round_winner = 'none'
winner = 'none'


#sounds
bgrd_music = simplegui.load_sound('https://opengameart.org/sites/default/files/Planetrise%20v1_0.mp3')
in_game_music = simplegui.load_sound('https://opengameart.org/sites/default/files/Fight%20Amidst%20the%20Destruction%20-intro%20-loop%4029.825s.mp3')
gun_shot = simplegui.load_sound('https://retired.sounddogs.com/previews/28/mp3/296715_SOUNDDOGS__ri.mp3')
empty_gun_shot = simplegui.load_sound('https://retired.sounddogs.com/previews/25/mp3/309407_SOUNDDOGS__gu.mp3')
punch_sound = simplegui.load_sound('https://retired.sounddogs.com/previews/25/mp3/386871_SOUNDDOGS__sp.mp3')
weapon_swing = simplegui.load_sound('https://retired.sounddogs.com/previews/42/mp3/432447_SOUNDDOGS__wh.mp3')
weapon_breaking = simplegui.load_sound('https://retired.sounddogs.com/previews/2665/mp3/1122611_SOUNDDOGS__sm.mp3')
cocking_gun = simplegui.load_sound('https://retired.sounddogs.com/previews/2665/mp3/1143055_SOUNDDOGS__sm.mp3')
weapon_shing = simplegui.load_sound('https://retired.sounddogs.com/previews/106/mp3/529560_SOUNDDOGS__kn.mp3')
player_death = simplegui.load_sound('https://opengameart.org/sites/default/files/game_over_bad_chest.wav')
button_selected = simplegui.load_sound('https://retired.sounddogs.com/previews/3179/mp3/317962_SOUNDDOGS__tw.mp3')
button_selected.set_volume(0.2)

                        #img size
IMG_DICT = {BACKGROUND: (200, 200), GUN: (100, 100), GUN_PROMPT: (100, 100),
            KNIFE: (100, 100), KNIFE_PROMPT: (100, 100), BULLET_LEFT: (100, 100), BULLET_RIGHT: (100, 100), 
            HEALTH_PACKAGE: (100, 100), HEALTH_PACKAGE_PROMPT: (100, 100), PLATFORM: (100, 100), WALL: (100, 100),
            LADDER: (100, 100), GROUND_IMG: (100, 100), P1_FIST_SLOT: (100, 100), P1_KNIFE_SLOT: (100, 100),
            P1_GUN_SLOT: (100, 100), P2_FIST_SLOT: (100, 100), P2_KNIFE_SLOT: (100, 100), P2_GUN_SLOT: (100, 100),
            MAIN_MENU_BG: (400, 200), MAIN_MENU_BG_BUILDING: (400, 200), PAUSE_BUTTON: (48, 48), CONTROLS: (200, 200),
            PLAY_BUTTON: (56, 24), BACK_BUTTON: (56, 24), CONTROLS_BUTTON: (56, 24), RESUME_BUTTON: (56, 24), 
            RETURN_TO_MAIN_MENU_BUTTON: (56, 24), RESTART_BUTTON: (56, 24), PLAY_AGAIN_BUTTON: (56, 24), CONTINUE_BUTTON: (56, 24),
            INFO_BUTTON: (56, 24), RULES: (200, 200), TITLE: (301, 37)}

                          # col,  row,  cols
SPRITE_DICT = {IDLE_LEFT: (200/2, 100/1, 2), IDLE_RIGHT: (200/2, 100/1, 2),
               RUN_LEFT: (200/2, 200/2, 2), RUN_RIGHT: (200/2, 200/2, 2),
               LADDER_CLIMB: (200/2, 100, 2),
               IDLE_GUN_LEFT: (200/2, 100/1, 2), IDLE_GUN_RIGHT: (200/2, 100/1, 2),
               IDLE_KNIFE_LEFT: (200/2, 100/1, 2), IDLE_KNIFE_RIGHT: (200/2, 100/1, 2),
               RUN_LEFT_GUN: (200/2, 200/2, 2), RUN_RIGHT_GUN: (200/2, 200/2, 2),
               RUN_LEFT_KNIFE: (200/2, 200/2, 2), RUN_RIGHT_KNIFE: (200/2, 200/2, 2),
               SHOOTING_LEFT: (500/5, 100/1, 5), SHOOTING_RIGHT: (500/5, 100/1, 5),
               PUNCHING_LEFT: (500/5, 100/1, 5), PUNCHING_RIGHT: (500/5, 100/1, 5),
               MELEE_LEFT: (200/2, 200/2, 2), MELEE_RIGHT: (200/2, 200/2, 2),
               HP_FADE: (400/4, 500/5, 4), GUN_FADE: (400/4, 500/5, 4), KNIFE_FADE: (400/4, 500/5, 4),
               DIE_LEFT: (200/2, 200/2, 2), DIE_RIGHT: (200/2, 200/2, 2), DEAD_LEFT: (100/1, 100/1, 1),
               DEAD_RIGHT: (100/1, 100/1, 1)}

#code for the scrolling background in main menu
scroll_width, scroll_height = IMG_DICT[MAIN_MENU_BG]
bgrd_pos_sky = [FRAME_WIDTH/2, FRAME_HEIGHT/2]
bgrd_pos_building = [FRAME_WIDTH/2, FRAME_HEIGHT/2]

def new_game():
    global player_1_score, player_2_score, should_check
    should_check = True
    player_1_score = 4
    player_2_score = 0
    new_round()
    
#for each round
def new_round():
    global players, player_1, player_2, bullets, guns, health_packages, walls, platforms, ladders, weapons, game_time, should_check
    
    # Object lists
    players = []
    bullets = []
    guns = []
    weapons = []
    health_packages = []
    walls = []
    platforms = []
    ladders = []
    game_time = 1000
    should_check = True
    
    #choosing between 1 of 3 spawn locations    
    player_1 = Player(IDLE_LEFT, 30, random.choice(PLAYER_1_STARTING_POS), [0, 0], PLAYER_HEALTH)
    player_2 = Player(IDLE_RIGHT, 30, random.choice(PLAYER_2_STARTING_POS), [0, 0], PLAYER_HEALTH)
    player_1.left = True
    player_2.right = True
    
    players.append(player_1)
    players.append(player_2)
    walls.append(Wall(WALL, 1300, 1400, 240, 800, [1350, 520], [290, 840]))
    platforms.append(Platform(PLATFORM, 1100, 1400, 700, 702, [1250, 701]))
    platforms.append(Platform(PLATFORM, 1100, 1400, 598, 600, [1250, 599]))
    platforms.append(Platform(PLATFORM, 800, 1400, 496, 498, [1100, 497]))
    platforms.append(Platform(PLATFORM, 600, 1300, 240, 242, [950, 241])) 
    platforms.append(Platform(PLATFORM, 0, 300, 298, 300, [150, 299]))
    platforms.append(Platform(PLATFORM, 0, 150, 548, 550, [75, 549]))
    platforms.append(Platform(PLATFORM, 250, 350, 548, 550, [300, 549]))        
    ladders.append(Ladder(LADDER, 699, 799, 242, 800, [749, 521], [370, 720])) 
    ladders.append(Ladder(LADDER, 150, 250, 300, 800, [200, 550], [370, 645]))
    
    #guns.append(Gun(GUN, [500, 500], False, 1, 31))
    #guns.append(Gun(GUN, [700, 700], False, 1, 31))
    #weapons.append(Weapon(KNIFE, [300, 300], False, 7))
    #health_packages.append(HealthPackage(HEALTH_PACKAGE, [1000, 750]))    

##########################################################################
    
# Helper methods
#for generating random coords for item spawning
def random_pos(object):
    valid = False
    while not valid:
      
        x_pos = random.randint(0, FRAME_WIDTH)
        y_pos = random.randint(0, FRAME_HEIGHT)
        
        #checks to make sure the object doesn't spawn in a wall or in the ground
        if object == 'knife':
            for wall in walls:
                if not wall.collide([x_pos, y_pos], KNIFE_WIDTH, KNIFE_HEIGHT) and inbounds([x_pos, y_pos], KNIFE_WIDTH, KNIFE_HEIGHT) and y_pos < GROUND:
                    valid = True
        elif object == 'gun':
            for wall in walls:
                if not wall.collide([x_pos, y_pos], GUN_WIDTH, GUN_HEIGHT) and inbounds([x_pos, y_pos], GUN_WIDTH, GUN_HEIGHT) and y_pos < GROUND:
                    valid = True
        elif object == 'hp':
            for wall in walls:
                if not wall.collide([x_pos, y_pos], HP_WIDTH, HP_HEIGHT) and inbounds([x_pos, y_pos], HP_WIDTH, HP_HEIGHT) and y_pos < GROUND:
                    valid = True
        
    pos = [x_pos, y_pos]
        
    return pos

#boolean for checking if an object is inbounds
def inbounds(pos, width, height):
    in_x = pos[0] > 0 + width/2 and pos[0] < FRAME_WIDTH - width/2
    in_y = pos[1] > 0 + height/2 and pos[1] <= FRAME_HEIGHT - height/2
    return in_x and in_y

#boolean for seeing if a player takes damage from a punch
def can_punch(attacker, victim):
    can_y = victim.pos[1] <= attacker.pos[1] + PLAYER_HEIGHT/2 and victim.pos[1] >= attacker.pos[1] - PLAYER_HEIGHT/2
    if attacker.left:
        can_x = victim.pos[0] <= attacker.pos[0] and victim.pos[0] + PLAYER_WIDTH/2 >= attacker.pos[0] - PUNCH_RANGE
        
    else:
        can_x = victim.pos[0] >= attacker.pos[0] and victim.pos[0] - PLAYER_WIDTH/2 <= attacker.pos[0] + PUNCH_RANGE
        
    return can_x and can_y

#boolean for seeing if a player take damage from a melee strike
def can_melee(attacker, victim):
    can_y = victim.pos[1] <= attacker.pos[1] + PLAYER_HEIGHT/2 and victim.pos[1] >= attacker.pos[1] - PLAYER_HEIGHT/2
    if attacker.left:
        can_x = victim.pos[0] <= attacker.pos[0] and victim.pos[0] + PLAYER_WIDTH/2 >= attacker.pos[0] - WEAPON_RANGE
        
    else:
        can_x = victim.pos[0] >= attacker.pos[0] and victim.pos[0] - PLAYER_WIDTH/2 <= attacker.pos[0] + WEAPON_RANGE
        
    return can_x and can_y

#boolean for seeing if a player has been shot
def been_shot(player_pos, bullet_pos):
    x = bullet_pos[0] >= player_pos[0] - PLAYER_WIDTH/2 and bullet_pos[0] <= player_pos[0] + PLAYER_WIDTH/2
    y = bullet_pos[1] <= player_pos[1] + PLAYER_HEIGHT/2 and bullet_pos[1] >= player_pos[1] - PLAYER_HEIGHT/2
    return x and y

should_check = True
#checks if a player has died yet, and if a player has 5 points or not
def check():
    global player_1_score, player_2_score, should_check, round_winner, winner
    
    #if player 2 won the round   
    if not player_1.alive and player_2.alive:
        player_2_score += 1 
        should_check = False
        round_winner = 'player_2'
        if player_2_score == 5:
            winner = 'player_2'
            
    #if player 1 won the round
    elif not player_2.alive and player_1.alive:
        player_1_score += 1  
        should_check = False
        round_winner = 'player_1'
        if player_1_score == 5:
            winner = 'player_1'
            
    #if there is a draw (both die at the same time)
    elif not player_1.alive and not player_1.alive:
        should_check = False
        round_winner = 'draw'
    
##########################################################################

# Classes
class Player:
    def __init__(self, image, diff, position, velocity, health):
        self.image = image        
        self.pos = [position[0], position[1]]
        self.vel = velocity
        self.hp = health
        self.time = 0
        self.diff = diff #adjusts the FPS of sprite drawings
        self.alive = True
        self.frames = 2 #the number of frames in each sprite
        self.done_dying = False
        
        self.can_climb = False #can climb or not
        self.climbing = False #in the action of climbing or not
        self.left = False
        self.right = False
        self.is_jumping = False
        self.can_run = True
        self.is_running = False
        self.idling = True
        self.falling_from_ladder = False
        self.on_wall = False
        self.stuck = False
        self.shooting = False
        self.shooting_time = 0 #prevents player from being able to shoot faster by single tapping compared to holding
        self.punching = False
        self.meleeing = False
        
        self.has_gun = False
        self.using_gun = False
        self.has_weapon = False
        self.using_weapon = False
        
        self.dura = 0 #durability 
        self.extra_mags = 0
        self.ammo = 0
        
    def draw(self, canvas):
        if self.alive and not self.stuck:
            #climbing ladder
            if self.can_climb and self.climbing:
                self.image = LADDER_CLIMB
                self.diff = 12
                self.frames = 2
            #standing still on ladder
            elif self.can_climb and not self.idling and not self.can_run:
                self.image = LADDER_CLIMB
                self.diff = 999999999
                self.frames = 1
            #running with gun    											 #falling off ladder scenario
            elif self.is_running and not self.climbing and self.using_gun or self.is_running and self.falling_from_ladder and self.using_gun:
                self.image = RUN_LEFT_GUN if self.left else RUN_RIGHT_GUN
                self.diff = 10
                self.frames = 4           
            #running with weapon												#falling off ladder scenario
            elif self.is_running and not self.climbing and self.using_weapon or self.is_running and self.falling_from_ladder and self.using_weapon:
                self.image = RUN_LEFT_KNIFE if self.left else RUN_RIGHT_KNIFE
                self.diff = 10
                self.frames = 4
            #running										#falling off ladder scenario
            elif self.is_running and not self.climbing or self.is_running and self.falling_from_ladder:
                self.image = RUN_LEFT if self.left else RUN_RIGHT
                self.diff = 10
                self.frames = 4
            #idling with gun           
            elif self.idling and not self.climbing and self.using_gun:
                self.image = IDLE_GUN_LEFT if self.left else IDLE_GUN_RIGHT
                self.diff = 30
                self.frames = 2          
            #idling with weapon
            elif self.idling  and not self.climbing and self.using_weapon:
                self.image = IDLE_KNIFE_LEFT if self.left else IDLE_KNIFE_RIGHT
                self.diff = 30
                self.frames = 2
            #idling
            elif self.idling and not self.climbing:
                self.image = IDLE_LEFT if self.left else IDLE_RIGHT
                self.diff = 30
                self.frames = 2
                
        elif self.alive and self.stuck:
            #shooting with gun
            if self.using_gun:
                if self.ammo > 0 and self.shooting:
                    self.image = SHOOTING_LEFT if self.left else SHOOTING_RIGHT
                    self.diff = 4
                    self.frames = 5                    
                else:
                    self.image = IDLE_GUN_LEFT if self.left else IDLE_GUN_RIGHT
                    self.diff = 30
                    self.frames = 2
            #punching
            elif self.punching:
                self.image = PUNCHING_LEFT if self.left else PUNCHING_RIGHT
                self.diff = 3
                self.frames = 4
                
                if self.time == self.diff * self.frames - 1:
                    self.punching = False
                    self.stuck = False
                    self.time = 0
            #using weapon        
            elif self.meleeing:
                if self.using_weapon and self.meleeing:
                    self.image = MELEE_LEFT if self.left else MELEE_RIGHT
                    self.diff = 6
                    self.frames = 4
                    
                    if self.time == self.diff * self.frames -1:
                        self.meleeing = False
                        self.stuck = False
                        self.time = 0
                        
                        #if durability of weapon is 0
                        if self.dura == 0:
                            self.has_weapon = False
                            self.using_weapon = False
                            weapon_breaking.set_volume(0.4)
                            weapon_breaking.rewind()
                            weapon_breaking.play()
                            
            else:
                self.image = IDLE_LEFT if self.left else IDLE_RIGHT
                self.diff = 30
                self.frames = 2
                
        else:
            
            #death animation, in the midst of dying
            if not self.done_dying:
                self.image = DIE_LEFT if self.left else DIE_RIGHT
                self.diff = 10
                self.frames = 4
                if self.time == self.diff * self.frames -1:
                    self.done_dying = True
                    
            #if death animation is done
            else:
                self.image = DEAD_LEFT if self.left else DEAD_RIGHT
                self.diff = 1
                self.frames = 1
                
                            
        width, height, cols = SPRITE_DICT[self.image]        
        col = int(self.time/self.diff) % cols
        row = int(self.time/self.diff) // cols
        center_x = width / 2 + (col)*width
        center_y = height/2 + (row)*height
        canvas.draw_image(self.image,
                          (center_x, center_y),
                          (width, height),
                          self.pos,
                          PLAYER_SIZE)                          
    
    def update(self):
        global next_pos
        current_vel = self.vel[1]
       
        if self.stuck:
            if not self.is_jumping:
                self.vel[0] = 0
            self.is_running = False
            self.idling = True
        
        next_pos = [self.pos[0] + self.vel[0], self.pos[1] + self.vel[1]]        
        wall_collision = False
        on_platform = False
        self.can_climb = False
        on_top_ladder = False        
        
        #checking for wall collision
        for wall in walls:
            if wall.collide(next_pos, PLAYER_WIDTH, PLAYER_HEIGHT):
                self.on_wall = True
                wall_collision = True
          
                if self.pos[1] <= wall.top - PLAYER_HEIGHT/2:
                    self.pos[1] = wall.top - PLAYER_HEIGHT/2
                    self.vel[1] = 0
                    self.on_wall = True
                    self.is_jumping = False
            else:
                self.on_wall = False
        
        #checking if on a platform
        for platform in platforms:
            near = platform.on_top(next_pos, PLAYER_WIDTH, PLAYER_HEIGHT)
            if near:
                if self.pos[1] <= platform.top - PLAYER_HEIGHT/2:
                    self.pos[1] = platform.top - PLAYER_HEIGHT/2
                    self.vel[1] = 0
                    self.is_jumping = False
                    on_platform = True
                    self.falling_from_ladder = False
                    
        #checking if in the range of a ladder         
        for ladder in ladders:
            if ladder.in_ladder(next_pos, PLAYER_WIDTH, PLAYER_HEIGHT) and not self.is_jumping:
                self.can_climb = True
                if self.pos[1] + PLAYER_HEIGHT/2 < ladder.bot:
                    if not self.pos[1] < ladder.top:
                        self.idling = False
            if self.inside_ladder(self.pos) and next_pos[1] < ladder.top - PLAYER_HEIGHT/2:
                self.idling = True
                on_top_ladder = True
        
        #checks if player is falling from a ladder
        if self.inside_ladder(self.pos) and not self.inside_ladder(next_pos):
            self.falling_from_ladder = True
            self.can_climb = False
            self.climbing = False
            if not on_top_ladder:
                self.is_running = True
            
        if not self.can_climb:
            self.climbing = False
            self.can_run = True                    
        
        if self.shooting:
            if self.shooting_time % 15 == 0:
                self.shoot()
                
        #movement restrictions
        
        #border restriction
        if not inbounds(next_pos, PLAYER_WIDTH, PLAYER_HEIGHT):            
            self.vel[0] = 0
            self.pos[1] += self.vel[1]               
            self.vel[1] += GRAVITY
                        
            if self.pos[1] >= GROUND - PLAYER_HEIGHT/2:            
                self.pos[1] = GROUND - PLAYER_HEIGHT/2
                self.vel[1] = 0
                self.is_jumping = False
                
        #ladder movement        
        elif self.can_climb and not self.is_jumping and not self.falling_from_ladder and not wall_collision:
            self.pos[0] += self.vel[0]
            self.pos[1] += self.vel[1]           
               
        #normal movement
        elif not wall_collision and not on_platform and not self.climbing and inbounds(next_pos, PLAYER_WIDTH, PLAYER_HEIGHT):            
            self.pos[0] += self.vel[0]
            self.pos[1] += self.vel[1]               
            self.vel[1] += GRAVITY           
            if self.pos[1] >= GROUND - PLAYER_HEIGHT/2:            
                self.pos[1] = GROUND - PLAYER_HEIGHT/2
                self.vel[1] = 0
                self.is_jumping = False
                self.falling_from_ladder = False
            
        #movement on/beside wall
        elif wall_collision:
           
            if self.pos[1] < wall.top:
                self.pos[0] += self.vel[0]
                self.pos[1] += self.vel[1]
                                
            else:
                self.pos[1] += self.vel[1]
                self.vel[1] += GRAVITY
                if self.pos[1] >= GROUND - PLAYER_HEIGHT/2:            
                    self.pos[1] = GROUND - PLAYER_HEIGHT/2
                    self.vel[1] = 0
                    self.falling_from_ladder = False
                                    
        #movement on platform
        elif on_platform and not self.climbing:
            self.pos[0] += self.vel[0]
            self.pos[1] += self.vel[1]
        
        #checks for fall damage
        if current_vel >= 30 and self.vel[1] == 0:
            self.take_damage('fall')  
            
        self.time += 1        
        self.time %= self.diff * self.frames
        self.shooting_time += 1
            
    def jump(self):
        self.vel[1] = -JUMP_VEL
        self.is_jumping = True
        
    def climb_ladder(self):
        self.vel[1] += -CLIMB_VEL
        
    def down_ladder(self):
        self.vel[1] += CLIMB_VEL
    
    #boolean determining if player is inside a ladder
    def inside_ladder(self, pos):
        for ladder in ladders:
            if ladder.in_ladder(pos, PLAYER_WIDTH, PLAYER_HEIGHT):
                return True
        return False
    
    def take_damage(self, type):
        if type == 'fall':
            self.hp -= 4
        elif type == 'bullet':
            self.hp -= 6
        elif type == 'punch':
            self.hp -= 1
        elif type == 'weapon':
            self.hp -= 3            
        if self.hp <= 0:
            self.alive = False
            #plays death sound
            player_death.set_volume(0.3)
            player_death.play()
            
    def reload(self):
        if self.using_gun:
            if self.extra_mags > 0:
                self.extra_mags -= 1
                self.ammo = 31
            
    def shoot(self):
        #distance relationship between center of player and bullet
        if self.ammo >0:
            
            self.ammo -= 1
            x_diff = -70 if self.left else 70
            y_diff = 15
            pos = [self.pos[0] + x_diff, self.pos[1] - y_diff]
            speed = -BULLET_SPEED if self.left else BULLET_SPEED

            bullet_spray = random.uniform(-0.05, 0.05)
            image = BULLET_LEFT if self.left else BULLET_RIGHT
            bullets.append(Bullet(image, pos, [speed * (1-bullet_spray), speed * bullet_spray], bullet_spray))  
            
            gun_shot.set_volume(0.2)
            gun_shot.rewind()
            gun_shot.play()
      
    def punch(self, attacker):
        if attacker == 'player_1':
            if can_punch(player_1, player_2):
                player_2.take_damage('punch')
                punch_sound.set_volume(0.2)
                punch_sound.rewind()
                punch_sound.play()
                
        elif attacker == 'player_2':
            if can_punch(player_2, player_1):
                player_1.take_damage('punch')
                punch_sound.set_volume(0.2)
                punch_sound.rewind()
                punch_sound.play()
                        
    def melee(self, attacker):
        if attacker == 'player_1':
            if can_melee(player_1, player_2):
                player_2.take_damage('weapon')
                player_1.dura -= 1
                
        elif attacker == 'player_2':
            if can_melee(player_2, player_1):
                player_1.take_damage('weapon')
                player_2.dura -= 1   
    
class Bullet:
    def __init__(self, image, position, velocity, rotation):
        self.image = image
        self.pos = position
        self.vel = velocity
        self.rot = rotation
        
    def draw(self, canvas):
        width, height = IMG_DICT[self.image]
        canvas.draw_image(self.image,
                          [width/2, height/2],
                          [width, height],
                          self.pos,
                          BULLET_SIZE,
                          self.rot)
    
    def update(self):
        for i in range(2):
            self.pos[i] += self.vel[i]        

class Platform:
    def __init__(self, image, left, right, top, bottom, center):        
        self.image = image
        self.left = left
        self.right = right
        self.top = top
        self.bot = bottom
        self.size = ((self.right - self.left) * 1.7, 150)
        self.cent = center
        
    def draw(self, canvas):
        width, height = IMG_DICT[self.image]
        canvas.draw_image(self.image,
                          [width/2, height/2],
                          [width, height],
                          self.cent,
                          self.size)
        
    #determines if there is something on top of the platform   
    def on_top(self, pos, width, height):
        on_x = pos[0] > self.left - width/2 and pos[0] < self.right + width/2
        near_y = pos[1] >= self.top - height/2
        on_y = pos[1] == self.top - height/2
        return on_x and near_y if not on_y else on_x and on_y

class Wall:
    def __init__(self, image, left, right, top, bottom, center, size):        
        self.image = image
        self.left = left
        self.right = right
        self.top = top
        self.bot = bottom
        self.cent = center
        self.size = size
        
    def draw(self, canvas):
        #canvas.draw_polygon(self.corners,2,"white","white")
        width, height = IMG_DICT[self.image]
        canvas.draw_image(self.image,
                          [width/2, height/2],
                          [width, height],
                          self.cent,
                          self.size)
     
    #determines if something is about to collide with the wall
    def collide(self, pos, width, height):        
        in_x = pos[0] > self.left - width/2 and pos[0] < self.right + width/2
        in_y = pos[1] > self.top - height/2 and pos[1] < self.bot + height/2
        return in_x and in_y

class Ladder:
    def __init__(self, image, left, right ,top, bottom, center, size):
        self.image = image
        self.left = left
        self.right = right
        self.top = top
        self.bot = bottom
        self.cent = center
        self.size = size
        
    def draw(self, canvas):
        #canvas.draw_polygon(self.corners,2,"red","red")
        width, height = IMG_DICT[self.image]
        canvas.draw_image(self.image,
                          [width/2, height/2],
                          [width, height],
                          self.cent,
                          self.size)
    
    #determines if a player is in the range of a ladder
    def in_ladder(self, pos, width, height):       
        in_x = pos[0] >= self.left and pos[0] <= self.right
        in_y = pos[1] >= self.top - height/2 and pos[1] <= self.bot - height/2
        return in_x and in_y        
                 
class HealthPackage:
    def __init__(self, image, position):
        self.image = image
        self.pos = position
        self.vel = [0, 0]
        self.stuck = False
        self.fading = False #close to being despawned
        self.diff = 3
        self.time = 0
        self.living_time = 0 
        
    def draw(self, canvas):
        #if not about to despawn
        if not self.fading:
            width, height = IMG_DICT[self.image]
            canvas.draw_image(self.image,
                              [width/2, height/2],
                              [width, height],
                              self.pos,
                              HP_SIZE)
            
        else:
            width, height, cols = SPRITE_DICT[self.image]        
            col = int(self.time/self.diff) % cols
            row = int(self.time/self.diff) // cols
            center_x = width / 2 + (col)*width
            center_y = height/2 + (row)*height
            canvas.draw_image(self.image,
                              (center_x, center_y),
                              (width, height),
                              self.pos,
                              HP_SIZE)
                    
    def update(self):
        self.pos[1] += self.vel[1]
        if not self.stuck:
            self.vel[1] += GRAVITY
        next_pos = self.pos[1] + self.vel[1]
        
        #prevents from going into wall
        for wall in walls:
            if next_pos - HP_HEIGHT/2 >= wall.top and self.pos[0] >= wall.left and self.pos[0] <= wall.right:
                self.vel[1] = 0
                self.pos[1] = wall.top - HP_HEIGHT/2
                self.stuck = True
        
        #checking for platform collision (if falling fast enough will go past)
        for platform in platforms:
                #y check																							#x check
            if next_pos - HP_HEIGHT/2 - 10 <= platform.top and next_pos - HP_HEIGHT/2 >= platform.top and self.pos[0] >= platform.left and self.pos[0] <= platform.right and not self.vel[1] == 0:
                self.vel[1] = 0
                self.pos[1] = platform.top - HP_HEIGHT/2
                self.stuck = True
        
        #if about to hit the ground
        if next_pos - HP_HEIGHT/2 >= GROUND:
            self.vel[1] = 0
            self.pos[1] = GROUND - HP_HEIGHT/2
            self.stuck = True
         
        self.living_time += 1
        self.time += 1
        self.time %= self.diff * 20 #20 will always be the number of frames
     
    #determines if the package is near a player
    def near_player(self, pos):
        in_x = pos[0] >= self.pos[0] - HP_WIDTH and pos[0] <= self.pos[0] + HP_WIDTH
        in_y = pos[1] >= self.pos[1] - HP_HEIGHT - PLAYER_HEIGHT and pos[1] <= self.pos[1] + HP_HEIGHT
        return in_x and in_y    
        
class Gun:
    def __init__(self, image, position, used, mags, ammo):
        self.image = image
        self.pos = position
        self.time = 0
        self.vel = [0, 0]
        self.stuck = False
        self.used = used
        self.fading = False #close to being despawned
        self.time = 0
        self.diff = 3
        self.living_time = 1100 if self.used else 0
        self.extra_mags = mags
        self.ammo = ammo
        
    def draw(self, canvas):
        #if not about to despawn
        if not self.fading:
            width, height = IMG_DICT[self.image]
            canvas.draw_image(self.image,
                              [width/2, height/2],
                              [width, height],
                              self.pos,
                              GUN_SIZE)
        else:
            width, height, cols = SPRITE_DICT[self.image]        
            col = int(self.time/self.diff) % cols
            row = int(self.time/self.diff) // cols
            center_x = width / 2 + (col)*width
            center_y = height/2 + (row)*height
            canvas.draw_image(self.image,
                              (center_x, center_y),
                              (width, height),
                              self.pos,
                              GUN_SIZE)
    
    def update(self):
        self.pos[1] += self.vel[1]
        if not self.stuck:
            self.vel[1] += GRAVITY
        next_pos = self.pos[1] + self.vel[1]
        
        #prevents from going into wall
        for wall in walls:
            if next_pos - GUN_HEIGHT/2 >= wall.top and self.pos[0] >= wall.left and self.pos[0] <= wall.right:
                self.vel[1] = 0
                self.pos[1] = wall.top - GUN_HEIGHT/2
                self.stuck = True
        
        #checking for platform collision (if falling fast enough will go past)
        for platform in platforms:
                #y check																							#x check
            if next_pos - GUN_HEIGHT/2 - 10 <= platform.top and next_pos - GUN_HEIGHT/2 >= platform.top and self.pos[0] >= platform.left and self.pos[0] <= platform.right and not self.vel[1] == 0:
                self.vel[1] = 0
                self.pos[1] = platform.top - GUN_HEIGHT/2
                self.stuck = True
        
        #if about to hit the ground
        if next_pos - GUN_HEIGHT/2 >= GROUND:
            self.vel[1] = 0
            self.pos[1] = GROUND - GUN_HEIGHT/2
            self.stuck = True
            
        self.time += 1
        self.time %= self.diff * 20 #will always be 20 for frames
        self.living_time += 1
    
    #determines if near a player
    def near_player(self, pos):
        in_x = pos[0] >= self.pos[0] - GUN_WIDTH and pos[0] <= self.pos[0] + GUN_WIDTH
        in_y = pos[1] >= self.pos[1] - GUN_HEIGHT - PLAYER_HEIGHT and pos[1] <= self.pos[1] + GUN_HEIGHT
        return in_x and in_y
            
class Weapon:
    def __init__(self, image, position, used, durability):
        self.image = image
        self.pos = position
        self.vel = [0, 0]
        self.time = 0
        self.stuck = False
        self.used = used
        self.fading = False #close to being despawned
        self.time = 0
        self.diff = 3
        self.living_time = 1100 if self.used else 0
        self.dura = durability
                
    def draw(self, canvas):
        #if not about to despawn
        if not self.fading:
            width, height = IMG_DICT[self.image]
            canvas.draw_image(self.image,
                              [width/2, height/2],
                              [width, height],
                              self.pos,
                              KNIFE_SIZE)
        else:
            width, height, cols = SPRITE_DICT[self.image]        
            col = int(self.time/self.diff) % cols
            row = int(self.time/self.diff) // cols
            center_x = width / 2 + (col)*width
            center_y = height/2 + (row)*height
            canvas.draw_image(self.image,
                              (center_x, center_y),
                              (width, height),
                              self.pos,
                              KNIFE_SIZE)
    def update(self):
        self.pos[1] += self.vel[1]
        if not self.stuck:
            self.vel[1] += GRAVITY
        next_pos = self.pos[1] + self.vel[1]
                
        #prevents from going into wall
        for wall in walls:
            if next_pos - KNIFE_HEIGHT/2 >= wall.top and self.pos[0] >= wall.left and self.pos[0] <= wall.right:
                self.vel[1] = 0
                self.pos[1] = wall.top - KNIFE_HEIGHT/2
                self.stuck = True
        
        #checks for platform collision (if fast enough will go through)
        for platform in platforms:
                    #y check																							#x check
            if next_pos - KNIFE_HEIGHT/2 - 10 <= platform.top and next_pos - KNIFE_HEIGHT/2 >= platform.top and self.pos[0] >= platform.left and self.pos[0] <= platform.right and not self.vel[1] == 0:
                self.vel[1] = 0
                self.pos[1] = platform.top - KNIFE_HEIGHT/2
                self.stuck = True
        
        #if about to hit the ground
        if next_pos - KNIFE_HEIGHT/2 >= GROUND:
            self.vel[1] = 0
            self.pos[1] = GROUND - KNIFE_HEIGHT/2
            self.stuck = True
            
        self.time += 1
        self.time %= self.diff * 20 #will always be 20 frames
        self.living_time += 1
    
    #determines of near a player
    def near_player(self, pos):
        in_x = pos[0] >= self.pos[0] - KNIFE_WIDTH and pos[0] <= self.pos[0] + KNIFE_WIDTH
        in_y = pos[1] >= self.pos[1] - KNIFE_HEIGHT - PLAYER_HEIGHT and pos[1] <= self.pos[1] + KNIFE_HEIGHT
        return in_x and in_y

class Button:
    def __init__(self, image, pos, size):
        self.image = image
        self.pos = pos
        self.size = size
        self.left = pos[0] - size[0]/2
        self.right = pos[0] + size[0]/2
        self.top = pos[1] - size[1]/2
        self.bot = pos[1] + size[1]/2
        
    def draw(self, canvas):
        b_width, b_height = IMG_DICT[self.image]
        canvas.draw_image(self.image,
                          [b_width/2, b_height/2],
                          [b_width, b_height],
                          self.pos,
                          self.size)
    
    #collision with the mouse to determine if the mouse click is within the button range
    def is_selected(self, click_pos):
        in_x = click_pos[0] >= self.left and click_pos[0] <= self.right
        in_y = click_pos[1] >= self.top and click_pos[1] <= self.bot
        return in_x and in_y
    
##########################################################################

#globally stating button positions
play_button = Button(PLAY_BUTTON, [700, 400], (336, 146))
controls_button = Button(CONTROLS_BUTTON, [700, 575], (336, 146))
back_button = Button(BACK_BUTTON, [1000, 800], (224, 96))
pause_button = Button(PAUSE_BUTTON, [830, 40], (48, 48))
return_to_main_menu_button = Button(RETURN_TO_MAIN_MENU_BUTTON, [700, 400], (336, 146))
restart_button = Button(RESTART_BUTTON, [700, 750], (336, 146))
resume_button = Button(RESUME_BUTTON, [700, 225], (336, 146))
continue_button = Button(CONTINUE_BUTTON, [700, 425], (336, 146)) 
play_again_button = Button(PLAY_AGAIN_BUTTON, [700, 575], (336, 146))
info_button = Button(INFO_BUTTON, [700, 750], (336, 146))

#button booleans
in_match = False
paused = False
looking_at_controls = False
on_winning_screen = False
on_end_screen = False
looking_at_info = False

#draw handler helper codes (for buttons)

#pause buttom while match is on going
def during_match(canvas):
    pause_button.draw(canvas)

#menu displayed once paused
def pause_menu(canvas):
    resume_button.draw(canvas)
    restart_button.draw(canvas)
    controls_button.draw(canvas)
    return_to_main_menu_button.draw(canvas)
    
    if looking_at_controls:
        width, height = IMG_DICT[CONTROLS]
        canvas.draw_image(CONTROLS,
                          [width/2, height/2],
                          [width, height],
                          [FRAME_WIDTH/2, FRAME_HEIGHT/2],
                          (850, 850))        
        back_button.draw(canvas)

#when a player has won a match/round
def win_match_screen(canvas):
    global on_winning_screen
    continue_button.draw(canvas)    
    on_winning_screen = True
    
    if round_winner == 'player_1':
        canvas.draw_text("Player 1 has won the round!", (400, 200),40, "yellow", "monospace") 
    elif round_winner == 'player_2':
        canvas.draw_text("Player 2 has won the round!", (400, 200),40, "yellow", "monospace")
    elif round_winner == 'draw':
        canvas.draw_text("It's a draw!", (570, 200), 40, "yellow", "monospace")

#when a player has won the game
def end_match_screen(canvas):
    global on_end_screen 
    on_end_screen = True
    play_again_button.draw(canvas)
    return_to_main_menu_button.draw(canvas)
    if winner == 'player_1':
        canvas.draw_text("Player 1 has won the game!", (420, 200), 40, "yellow", "monospace")
    elif winner == 'player_2':
        canvas.draw_text("Player 2 has won the game!", (420, 200), 40, "yellow", "monospace")
    
#main menu
def main_menu(canvas):
    play_button.draw(canvas)    
    controls_button.draw(canvas)
    info_button.draw(canvas)
    if looking_at_controls:
        width, height = IMG_DICT[CONTROLS]
        canvas.draw_image(CONTROLS,
                          [width/2, height/2],
                          [width, height],
                          [FRAME_WIDTH/2, FRAME_HEIGHT/2],
                          (850, 850))        
        back_button.draw(canvas)
        
    elif looking_at_info:
        width, height = IMG_DICT[RULES]
        canvas.draw_image(RULES,
                          [width/2, height/2],
                          [width, height],
                          [FRAME_WIDTH/2, FRAME_HEIGHT/2],
                          (850, 850))  
        back_button.draw(canvas)

# Handers
def draw(canvas):
    
    if in_match: 
        in_game_music.play()
        in_game_music.set_volume(0.05)
        
        #check boolean makes it so it only checks once if one player is dead (so score doesn't add to infinity)
        if should_check:
            check()
        global game_time
        game_time += 1
        
        #draws background and ground
        bgrd_width, bgrd_height = IMG_DICT[BACKGROUND]
        canvas.draw_image(BACKGROUND,
                          [bgrd_width/2, bgrd_height/2],
                          [bgrd_width, bgrd_height],
                          [FRAME_WIDTH/2, FRAME_HEIGHT/2],
                          [FRAME_WIDTH, FRAME_HEIGHT])

        ground_width, ground_height = IMG_DICT[GROUND_IMG]
        canvas.draw_image(GROUND_IMG,
                          [ground_width/2, ground_height/2],
                          [ground_width, ground_height],
                          [FRAME_WIDTH/2, 825], #center of the ground
                          [1500, 370])
        
        #draws the pause button
        during_match(canvas)       
        
        #displaying the score
        canvas.draw_text('|', [700, 50], 40, 'white', 'monospace')
        canvas.draw_text(str(player_2_score), [650, 50], 40, 'blue')
        canvas.draw_text(str(player_1_score), [750, 50], 40, 'red')
        
        #for the icons inside the display board showing player slots
        item_image_size = [100, 100]
        
        #drawing player slot display boards   
        if player_1.using_gun:
            p1_display_image = P1_GUN_SLOT    
        elif player_1.using_weapon:
            p1_display_image = P1_KNIFE_SLOT
        else:
            p1_display_image = P1_FIST_SLOT

        canvas.draw_image(p1_display_image,
                          [item_image_size[0]/2, item_image_size[1]/2],
                          item_image_size,
                          [1250, 45],
                          (300, 275))
        if player_2.using_gun:
            p2_display_image = P2_GUN_SLOT    
        elif player_2.using_weapon:
            p2_display_image = P2_KNIFE_SLOT
        else:
            p2_display_image = P2_FIST_SLOT

        canvas.draw_image(p2_display_image,
                          [item_image_size[0]/2, item_image_size[1]/2],
                          item_image_size,
                          [150, 45],
                          (300, 275))
        
        #drawing the items the player has inside of the display board
        if player_1.has_gun:
            canvas.draw_image(GUN,
                              [item_image_size[0]/2, item_image_size[1]/2],
                              item_image_size,
                              [1350, 45],
                              [150, 150])
            #displays gun's ammo and mags left
            if player_1.using_gun:
                canvas.draw_text(str(str(player_1.ammo) + " | " + str(player_1.extra_mags)), [1350, 85], 12, 'white', 'monospace')
                
        if player_1.has_weapon:
            canvas.draw_image(KNIFE,
                              [item_image_size[0]/2, item_image_size[1]/2],
                              item_image_size,
                              [1250, 45],
                              [150, 150])
        if player_2.has_gun:
            canvas.draw_image(GUN,
                              [item_image_size[0]/2, item_image_size[1]/2],
                              item_image_size,
                              [250, 45],
                              [150, 150])
            
            #displays gun's ammo and mags left
            if player_2.using_gun:
                canvas.draw_text(str(str(player_2.ammo) + " | " + str(player_2.extra_mags)), [250, 85], 12, 'white', 'monospace')

        if player_2.has_weapon:
            canvas.draw_image(KNIFE,
                              [item_image_size[0]/2, item_image_size[1]/2],
                              item_image_size,
                              [150, 45],
                              [150, 150])
            
        #displays player's health
        canvas.draw_line([1100 + 3 * (100 - player_1.hp), 100], [1400, 100], 20, 'red')
        canvas.draw_line([1100, 100], [1100 + 3 * (100 - player_1.hp), 100], 20, 'gray')
        canvas.draw_line([0, 100], [300 -  3 * (100 - player_2.hp), 100], 20, 'red')
        canvas.draw_line([300 - 3 * (100 - player_2.hp), 100], [300, 100], 20, 'gray')       

        for platform in platforms:
            platform.draw(canvas)
            
        for wall in walls:
            wall.draw(canvas)

        for ladder in ladders:
            ladder.draw(canvas)

        for player in players:
            player.draw(canvas)
            if not paused:
                player.update()

        #code for random spawn of items
        if not paused:
            #spawns a new object every 20 seconds
            if game_time % 1200 == 0:
                number = random.randint(1, 5)
                if number == 1 or number == 2:
                    weapons.append(Weapon(KNIFE, random_pos('knife'), False, DURABILITY))
                    game_time %= 1200
                elif number == 3 or number == 4:
                    guns.append(Gun(GUN, random_pos('gun'), False, EXTRA_MAGS, AMMO))
                    game_time %= 1200
                elif number == 5:
                    health_packages.append(HealthPackage(HEALTH_PACKAGE, random_pos('hp')))
                    game_time %= 1200
        
        #drawing and updating guns
        for gun in guns: 
            #checks if gun is about to despawn 
            if not paused:
                if gun.living_time >= ITEM_LIFE_SPAN:
                    gun.fading = True
                    gun.image = GUN_FADE
                    if gun.living_time >= ITEM_LIFE_SPAN + ITEM_FADE_SPAN:
                        guns.remove(gun)
                else: 
                    #checks to see if player is in range of the gun
                    if gun.near_player(player_1.pos) or gun.near_player(player_2.pos):
                        gun.image = GUN_PROMPT
                    else:
                        gun.image = GUN
                gun.update()
            gun.draw(canvas)
         
       #drawing and updating weapons
        for weapon in weapons:
            if not paused:
                #checks if weapon is about to despawn
                if weapon.living_time >= ITEM_LIFE_SPAN:
                    weapon.fading = True
                    weapon.image = KNIFE_FADE
                    if weapon.living_time >= ITEM_LIFE_SPAN + ITEM_FADE_SPAN:
                        weapons.remove(weapon)
                else:
                    #checks to see if player is in range of the gun
                    if weapon.near_player(player_1.pos) or weapon.near_player(player_2.pos):
                        weapon.image = KNIFE_PROMPT
                    else:
                        weapon.image = KNIFE
                weapon.update()
            weapon.draw(canvas)
         
       #drawing and updating health packages
        for hp in health_packages:
            if not paused:
                #checks if package is about to despawn
                if hp.living_time >= ITEM_LIFE_SPAN:
                    hp.fading = True
                    hp.image = HP_FADE
                    if hp.living_time >= ITEM_LIFE_SPAN + ITEM_FADE_SPAN:
                        health_packages.remove(hp)            
                else: 
                    #checks to see if player is in range of a package
                    if hp.near_player(player_1.pos) or hp.near_player(player_2.pos):
                        hp.image = HEALTH_PACKAGE_PROMPT
                    else:
                        hp.image = HEALTH_PACKAGE
                hp.update()
            hp.draw(canvas)
         
       #drawing and updating bullets
        for bullet in bullets:
            if not paused:
                bullet.update()
                #removes if not inbounds
                if not inbounds(bullet.pos, BULLET_WIDTH, BULLET_HEIGHT):
                    bullets.remove(bullet)
                #removes if collided with wall
                for wall in walls:
                    if wall.collide(bullet.pos, BULLET_WIDTH, BULLET_HEIGHT):
                        bullets.remove(bullet)
                #checks if a bullet hit a player       
                for player in players:
                    if been_shot(player.pos, bullet.pos):
                        player.take_damage('bullet')
                        bullets.remove(bullet)
                        if not player.alive:
                            player.stuck = True                        
            bullet.draw(canvas)
            
        if paused:
            pause_menu(canvas)
        
        #if one of the players died, or both
        if player_1.alive and not player_2.alive or player_2.alive and not player_1.alive or not player_1.alive and not player_2.alive:
            player_1.stuck = True
            player_2.stuck = True
            player_1.shooting = False
            player_2.shooting = False
            if player_1_score == 5:
                end_match_screen(canvas)
            elif player_2_score == 5:
                end_match_screen(canvas)
            else:
                win_match_screen(canvas)
            
    #if in main menu
    else:
        bgrd_music.play()
        bgrd_music.set_volume(0.5)
        
        #drawing scrolling background
        canvas.draw_image(MAIN_MENU_BG,
                          [scroll_width/2, scroll_height/2],
                          [scroll_width, scroll_height],
                          bgrd_pos_sky,
                          [FRAME_WIDTH * 2, FRAME_HEIGHT])
        bgrd_pos_sky[0] = (bgrd_pos_sky[0] - BGRD_SPEED_SKY) % (FRAME_WIDTH)
        
        canvas.draw_image(MAIN_MENU_BG_BUILDING,
                          [scroll_width/2, scroll_height/2],
                          [scroll_width, scroll_height],
                          bgrd_pos_building,
                          [FRAME_WIDTH * 2 , FRAME_HEIGHT])
        bgrd_pos_building[0] = (bgrd_pos_building[0] - BGRD_SPEED) % (FRAME_WIDTH)
        
        width, height = IMG_DICT[TITLE]
        canvas.draw_image(TITLE,
                          [width/2, height/2],
                          [width, height],
                          [700, 175],
                          (1000, 200))
        main_menu(canvas)

def mouse_handler(mouse_position):
    global in_match, paused, looking_at_controls, on_winning_screen, on_end_screen, looking_at_info
    #pause button
    if in_match:
        if pause_button.is_selected(mouse_position):
            paused = True
            button_selected.rewind()
            button_selected.play()
    
    if not in_match:
        if not looking_at_controls and not looking_at_info:
            #play button
            if play_button.is_selected(mouse_position):
                new_game()
                in_match = True
                bgrd_music.pause()
                in_game_music.rewind()
                button_selected.rewind()
                button_selected.play()

            #info button
            if info_button.is_selected(mouse_position):
                looking_at_info = True
                button_selected.rewind()
                button_selected.play()

    #controls button
    if not in_match or paused:
        if not looking_at_controls and not looking_at_info:
            if controls_button.is_selected(mouse_position):
                looking_at_controls = True
                button_selected.rewind()
                button_selected.play()
    
    #back button
    if back_button.is_selected(mouse_position):
        looking_at_controls = False
        looking_at_info = False
        button_selected.rewind()
        button_selected.play()
     
    #return to main menu button
    if paused or on_end_screen: 
        if not looking_at_controls:
            if return_to_main_menu_button.is_selected(mouse_position):
                paused = False
                in_match = False
                on_end_screen = False
                bgrd_music.rewind()
                in_game_music.pause()
                button_selected.rewind()
                button_selected.play()
    
    
    if paused:
        if not looking_at_controls:
            
            #resume button
            if resume_button.is_selected(mouse_position):
                button_selected.rewind()
                button_selected.play()
                paused = False

                #updates the player's attributes once pause ended
                for player in players:
                    player.vel[0] = 0
                    if player.is_running:
                        player.is_running = False
                        player.idling = True
                    if player.climbing:
                        player.vel[1] = 0
                        player.climbing = False
                    if player.shooting:
                        player.shooting = False
                        player.stuck = False                    
                    if player.punching or player.meleeing:
                        player.punching = False
                        player.meleeing = False
                        player.stuck = False 
                        
            #restart button
            if restart_button.is_selected(mouse_position):
                paused = False
                new_game()
                in_game_music.rewind()
                button_selected.rewind()
                button_selected.play()  
                
    #continue button
    if on_winning_screen:
        if continue_button.is_selected(mouse_position):
            new_round()
            on_winning_screen = False
            in_game_music.rewind()
            player_death.rewind()
            button_selected.rewind()
            button_selected.play()
    
    #play again button
    if on_end_screen:
        if play_again_button.is_selected(mouse_position):
            new_game()
            in_game_music.rewind()
            button_selected.rewind()
            button_selected.play()
        
def key_press(key):
    #player won't be able to do anything if they are stuck, dead, or the game is paused
    if not player_1.stuck and player_1.alive and not paused:
        
        if key == simplegui.KEY_MAP['right']: 
            player_1.idling = False 
            player_1.right = True
            player_1.left = False            
            player_1.vel[0] = PLAYER_SPEED                        
            player_1.is_running = True
            player_1.diff = 10      
            
            #prevents bug where you'd run right but with the left animation
            if player_1.using_weapon:
                player_1.image = RUN_RIGHT_KNIFE
            elif player_1.using_gun:
                player_1.image = RUN_RIGHT_GUN
            else:
                player_1.image = RUN_RIGHT

        if key == simplegui.KEY_MAP['left']:        
            player_1.idling = False            
            player_1.left = True
            player_1.right = False        
            player_1.vel[0] = -PLAYER_SPEED
            player_1.is_running = True
            player_1.diff = 10      
            
            #prevents bug where you'd run left but with the right animation
            if player_1.using_weapon:
                player_1.image = RUN_LEFT_KNIFE
            elif player_1.using_gun:
                player_1.image = RUN_LEFT_GUN
            else:
                player_1.image = RUN_LEFT

        if key == simplegui.KEY_MAP['up']:
            #if player is on ground
            if not player_1.can_climb and player_1.pos[1] == GROUND - PLAYER_HEIGHT/2:
                player_1.jump()

            #if player is inside a ladder
            if player_1.inside_ladder(player_1.pos):
                player_1.falling_from_ladder = False
                player_1.vel[1] = 0
                player_1.is_jumping = False
                player_1.is_running = False
                player_1.can_run = False
                player_1.can_climb = True
                player_1.climbing = True
                player_1.climb_ladder()
            else:
                #if on top of a wall
                for wall in walls:                
                    if player_1.pos[1] == wall.top - PLAYER_HEIGHT/2 and not player_1.can_climb:
                        player_1.jump() 

                #if on top of a platform
                for platform in platforms:
                    if player_1.pos[1] == platform.top - PLAYER_HEIGHT/2 and not player_1.can_climb:
                        player_1.jump()                    

        if key == simplegui.KEY_MAP['down']:
            player_1.idling = False
            for wall in walls:
                if player_1.pos[0] >= wall.left and player_1.pos[0] <= wall.right and player_1.pos[1] == wall.top - PLAYER_HEIGHT/2:
                    player_1.on_wall = True

            #if player isn't on the ground
            if player_1.pos[1] != GROUND - PLAYER_HEIGHT/2 and not player_1.on_wall:
                if player_1.inside_ladder(player_1.pos):
                    player_1.climbing = True

                #if player is on a platform
                for platform in platforms:
                    if player_1.pos[1] == platform.top - PLAYER_HEIGHT/2 and not player_1.on_wall:                   
                        player_1.pos[1] += 3
                        if player_1.inside_ladder(player_1.pos):
                            player_1.can_climb = True
                            player_1.climbing = True

                #if player is on a ladder
                if player_1.can_climb and player_1.pos[1] < GROUND - PLAYER_HEIGHT/2 and not player_1.on_wall:
                    player_1.down_ladder()
                    
        #dropping an item:
        if key == simplegui.KEY_MAP['u']:
            pos = [player_1.pos[0], player_1.pos[1]]
            if player_1.using_gun:
                guns.append(Gun(GUN, pos, True, player_1.extra_mags, player_1.ammo))
                player_1.has_gun = False
                player_1.using_gun = False
                player_1.extra_mags = 0
                player_1.ammo = 0 
                
            elif player_1.using_weapon:
                weapons.append(Weapon(KNIFE, pos, True, player_1.dura))
                player_1.using_weapon = False
                player_1.has_weapon = False
                player_1.dura = 0
        
        #picking up items            
        if key == simplegui.KEY_MAP['i']:
            pos = [player_1.pos[0], player_1.pos[1]]            
            for gun in guns:
                if gun.near_player(player_1.pos):
                    if player_1.has_gun:
                        guns.append(Gun(GUN, pos, True, player_1.extra_mags, player_1.ammo))

                    player_1.has_gun = True
                    player_1.ammo = gun.ammo
                    player_1.extra_mags = gun.extra_mags
                    guns.remove(gun)
                    
            for weapon in weapons:                 
                if weapon.near_player(player_1.pos):
                    if player_1.has_weapon:
                        weapons.append(Weapon(KNIFE, pos, True, player_1.dura))

                    player_1.has_weapon = True
                    player_1.dura = weapon.dura
                    weapons.remove(weapon)
                    
            for hp in health_packages:
                if hp.near_player(player_1.pos):
                    if player_1.hp > 70:
                        player_1.hp = 100
                    else:
                        player_1.hp += 30
                    health_packages.remove(hp)

        #punching/meleeing
        if key == simplegui.KEY_MAP['o']:            
            if not player_1.using_weapon and not player_1.using_gun and not player_1.punching:
                player_1.time = 0
                player_1.stuck = True
                player_1.punching = True
                player_1.punch('player_1')
            elif player_1.using_weapon and not player_1.meleeing:
                player_1.time = 0
                player_1.stuck = True
                player_1.meleeing = True
                player_1.melee('player_1')
                weapon_swing.set_volume(0.1)
                weapon_swing.rewind()
                weapon_swing.play()
                
        #shooting
        if key == simplegui.KEY_MAP['p']:
            if not player_1.climbing and player_1.can_run and player_1.using_gun:
                player_1.shooting = True
                player_1.shooting_time = 0 if player_1.shooting_time >= 15 else player_1.shooting_time
                player_1.stuck = True
            
                #if gun has no more ammo
                if player_1.ammo == 0:
                    empty_gun_shot.set_volume(0.1)
                    empty_gun_shot.rewind()
                    empty_gun_shot.play()
                
        #reloading
        if key == simplegui.KEY_MAP['l']:
            player_1.reload()

        #fist slot
        if key == simplegui.KEY_MAP['8']:
            player_1.using_gun = False
            player_1.using_weapon = False

        #weapon slot
        if key == simplegui.KEY_MAP['9']:
            if player_1.using_weapon:
                player_1.using_weapon = False
                player_1.using_gun = False
                
            elif player_1.has_weapon:
                player_1.using_weapon = True
                player_1.using_gun = False
                weapon_shing.set_volume(0.1)
                weapon_shing.rewind()
                weapon_shing.play()

        #gun slot
        if key == simplegui.KEY_MAP['0']:
            if player_1.using_gun:
                player_1.using_gun = False
                player_1.using_weapon = False
            
            elif player_1.has_gun:
                player_1.using_gun = True
                player_1.using_weapon = False
                cocking_gun.set_volume(0.1)
                cocking_gun.rewind()
                cocking_gun.play()

###################player 2######################### 

    #player won't be able to do anything if they are stuck, dead, or the game is paused
    if not player_2.stuck and player_2.alive and not paused:        
        if key == simplegui.KEY_MAP['d']:
            player_2.idling = False 
            player_2.right = True
            player_2.left = False            
            player_2.vel[0] = PLAYER_SPEED                        
            player_2.is_running = True
            player_2.diff = 10
            
            #prevents bug where you'd run right but with the left animation
            if player_2.using_weapon:
                player_2.image = RUN_RIGHT_KNIFE
            elif player_2.using_gun:
                player_2.image = RUN_RIGHT_GUN
            else:
                player_2.image = RUN_RIGHT

        if key == simplegui.KEY_MAP['a']:
            player_2.idling = False            
            player_2.left = True
            player_2.right = False        
            player_2.vel[0] = -PLAYER_SPEED
            player_2.is_running = True
            player_2.diff = 10
            
            #prevents bug where you'd run left but with the right animation
            if player_2.using_weapon:
                player_2.image = RUN_LEFT_KNIFE
            elif player_2.using_gun:
                player_2.image = RUN_LEFT_GUN
            else:
                player_2.image = RUN_LEFT

        if key == simplegui.KEY_MAP['w']:
            #if player is on ground
            if not player_2.can_climb and player_2.pos[1] == GROUND - PLAYER_HEIGHT/2:
                player_2.jump()

            #if player is inside a ladder
            if player_2.inside_ladder(player_2.pos):
                player_2.falling_from_ladder = False
                player_2.vel[1] = 0
                player_2.is_jumping = False
                player_2.is_running = False
                player_2.can_run = False
                player_2.can_climb = True
                player_2.climbing = True
                player_2.climb_ladder()
            else:
                #if on top of a wall
                for wall in walls:                
                    if player_2.pos[1] == wall.top - PLAYER_HEIGHT/2 and not player_2.can_climb:
                        player_2.jump() 

                #if on top of a platform
                for platform in platforms:
                    if player_2.pos[1] == platform.top - PLAYER_HEIGHT/2 and not player_2.can_climb:
                        player_2.jump()

        if key == simplegui.KEY_MAP['s']:
            player_2.idling = False
            for wall in walls:
                if player_2.pos[0] >= wall.left and player_2.pos[0] <= wall.right and player_2.pos[1] == wall.top - PLAYER_HEIGHT/2:
                    player_2.on_wall = True

            #if player isn't on the ground
            if player_2.pos[1] != GROUND - PLAYER_HEIGHT/2 and not player_2.on_wall:
                if player_2.inside_ladder(player_2.pos):
                    player_2.climbing = True

                #if player is on a platform
                for platform in platforms:
                    if player_2.pos[1] == platform.top - PLAYER_HEIGHT/2 and not player_2.on_wall:                   
                        player_2.pos[1] += 3
                        if player_2.inside_ladder(player_2.pos):
                            player_2.can_climb = True
                            player_2.climbing = True

                #if player is on a ladder
                if player_2.can_climb and player_2.pos[1] < GROUND - PLAYER_HEIGHT/2 and not player_2.on_wall:
                    player_2.down_ladder()
        
        #dropping an item:
        if key == simplegui.KEY_MAP['x']:
            pos = [player_2.pos[0], player_2.pos[1]]
            if player_2.using_gun:
                guns.append(Gun(GUN, pos, True, player_2.extra_mags, player_2.ammo))
                player_2.has_gun = False
                player_2.using_gun = False
                player_2.extra_mags = 0
                player_2.ammo = 0 
                
            elif player_2.using_weapon:
                weapons.append(Weapon(KNIFE, pos, True, player_2.dura))
                player_2.using_weapon = False
                player_2.has_weapon = False
                player_2.dura = 0
                
        #picking up items            
        if key == simplegui.KEY_MAP['c']:
            pos = [player_2.pos[0], player_2.pos[1]]                                                
            for gun in guns:
                if gun.near_player(player_2.pos):
                    if player_2.has_gun:
                        guns.append(Gun(GUN, pos, True, player_2.extra_mags, player_2.ammo))
                    player_2.has_gun = True
                    player_2.extra_mags = gun.extra_mags
                    player_2.ammo = gun.ammo
                    guns.remove(gun)

            for weapon in weapons:
                if weapon.near_player(player_2.pos):
                    if player_2.has_weapon:
                        weapons.append(Weapon(KNIFE, pos, True, player_2.dura))
                    player_2.has_weapon = True
                    player_2.dura = weapon.dura
                    weapons.remove(weapon)
                    
            for hp in health_packages:
                if hp.near_player(player_2.pos):
                    if player_2.hp > 70:
                        player_2.hp = 100
                    else:
                        player_2.hp += 30
                    health_packages.remove(hp)

        #punching/meleeing
        if key == simplegui.KEY_MAP['v']:
            if not player_2.using_weapon and not player_2.using_gun and not player_2.punching:
                player_2.time = 0
                player_2.stuck = True
                player_2.punching = True
                player_2.punch('player_2')
            elif player_2.using_weapon and not player_2.meleeing:
                player_2.time = 0
                player_2.stuck = True
                player_2.meleeing = True
                player_2.melee('player_2')
                weapon_swing.set_volume(0.1)
                weapon_swing.rewind()
                weapon_swing.play()

        #shooting
        if key == simplegui.KEY_MAP['b']:
            if not player_2.climbing and player_2.can_run and player_2.using_gun:
                player_2.shooting = True
                player_2.shooting_time = 0 if player_2.shooting_time >= 15 else player_2.shooting_time
                player_2.stuck = True
                
                #if gun has no more ammo
                if player_2.ammo == 0:
                    empty_gun_shot.set_volume(0.1)
                    empty_gun_shot.rewind()
                    empty_gun_shot.play()
                
        #reloading:
        if key == simplegui.KEY_MAP['n']:
            player_2.reload()        

        #fist slot
        if key == simplegui.KEY_MAP['1']:
            player_2.using_gun = False
            player_2.using_weapon = False

        #weapon slot
        if key == simplegui.KEY_MAP['2']:
            if player_2.using_weapon:
                player_2.using_weapon = False
                player_2.using_gun = False
            
            elif player_2.has_weapon:
                player_2.using_weapon = True
                player_2.using_gun = False
                weapon_shing.set_volume(0.1)
                weapon_shing.rewind()
                weapon_shing.play()

        #gun slot
        if key == simplegui.KEY_MAP['3']:
            if player_2.using_gun:
                player_2.using_gun = False
                player_2.using_weapon = False
            
            elif player_2.has_gun:
                player_2.using_gun = True
                player_2.using_weapon = False
                cocking_gun.set_volume(0.1)
                cocking_gun.rewind()
                cocking_gun.play()
                
###############################################################################################        
def key_release(key):
    if not paused:
        
        if key == simplegui.KEY_MAP['right']:
            player_1.is_running = False
            #if player is not running or climbing a ladder
            if player_1.right and not player_1.climbing and not player_1.is_running or player_1.right and not player_1.climbing and player_1.can_climb:            
                player_1.idling = True
                player_1.vel[0] = 0
                player_1.image = IDLE_RIGHT
                player_1.diff = 30
            #if player is climbing a ladder
            elif not player_1.can_run or player_1.climbing:
                player_1.vel[0] = 0

        if key == simplegui.KEY_MAP['left']:
            player_1.is_running = False
            #if player is not running or climbing a ladder
            if player_1.left and not player_1.climbing and not player_1.is_running or player_1.left and not player_1.climbing and player_1.can_climb:
                player_1.idling = True                        
                player_1.vel[0] = 0
                player_1.image = IDLE_LEFT
                player_1.diff = 30
            #if player is climbing a ladder  
            elif not player_1.can_run or player_1.climbing:
                player_1.vel[0] = 0

        if key == simplegui.KEY_MAP['up']:
            player_1.climbing = False        
            if player_1.can_climb and not player_1.is_jumping: 
                player_1.idling = False
                player_1.vel[1] = 0

        if key == simplegui.KEY_MAP['down']:
            player_1.idling = True
            if player_1.can_climb:
                player_1.can_run = False
                player_1.climbing = False
                player_1.idling = False
                player_1.vel[1] = 0
                player_1.diff = 999999999

        #release from shooting
        if key == simplegui.KEY_MAP['p']:
            player_1.shooting = False
            player_1.stuck = False

    ##################player 2############################        
        if key == simplegui.KEY_MAP['d']:
            player_2.is_running = False
            #if player is not running or climbing a ladder
            if player_2.right and not player_2.climbing and not player_2.is_running or player_2.right and not player_2.climbing and player_2.can_climb:            
                player_2.idling = True
                player_2.vel[0] = 0
                player_2.image = IDLE_RIGHT
                player_2.diff = 30
            #if player is climbing a ladder
            elif not player_2.can_run or player_2.climbing:
                player_2.vel[0] = 0

        if key == simplegui.KEY_MAP['a']:
            player_2.is_running = False
            #if player is not running or climbing a ladder
            if player_2.left and not player_2.climbing and not player_2.is_running or player_2.left and not player_2.climbing and player_2.can_climb:
                player_2.idling = True                        
                player_2.vel[0] = 0
                player_2.image = IDLE_LEFT
                player_2.diff = 30
            #if player is climbing a ladder  
            elif not player_2.can_run or player_2.climbing:
                player_2.vel[0] = 0

        if key == simplegui.KEY_MAP['w']:
            player_2.climbing = False        
            if player_2.can_climb and not player_2.is_jumping: 
                player_2.idling = False
                player_2.vel[1] = 0

        if key == simplegui.KEY_MAP['s']:
            player_2.idling = True
            if player_2.can_climb:
                player_2.can_run = False
                player_2.climbing = False
                player_2.idling = False
                player_2.vel[1] = 0
                player_2.diff = 999999999

        #release from shooting
        if key == simplegui.KEY_MAP['b']:
            player_2.shooting = False
            player_2.stuck = False

# Creating frame
frame = simplegui.create_frame("Game", FRAME_WIDTH, FRAME_HEIGHT)
frame.set_draw_handler(draw)
frame.set_mouseclick_handler(mouse_handler)
frame.set_keydown_handler(key_press)
frame.set_keyup_handler(key_release)
frame.start()
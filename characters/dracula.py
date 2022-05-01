from assets.lifebar import LifeBar
from assets.projectile import Projectile

from pygame import transform, image, Surface, Vector2, sprite, key, event
from pygame.locals import K_SPACE, K_UP, K_RIGHT, K_LEFT, KEYDOWN


class Dracula(sprite.Sprite):

    def __init__(self, *pos) -> None:
        super().__init__()

        self.__pos = Vector2(pos)
        self.image = self.fit_image()
        self.rect = self.image.get_rect()
        self.rect.bottomleft = self.pos
        
        # EXTERNAL ATTRIBUTES
        self.__lifebar = LifeBar()
        self.__projectile = Projectile()

        # self.__projectile.pos = self.pos + (self.rect.width/2, -self.rect.height/4)
        # self.__projectile.rect.bottomleft = self.__projectile.pos
        # CONTROL ATTRIBUTES
        self.__speed = 2
        self.__isJumping = False
        self.__jumpCounter = 0

    @property
    def lifebar(self):
        return self.__lifebar
    @lifebar.setter
    def lifebar(self, lb):
        self.__lifebar = lb
    
    @property
    def projectile(self):
        return self.__projectile

    @property
    def pos(self):
        return self.__pos

    @pos.setter
    def pos(self, pos: Vector2):
        self.__pos = pos

    def fit_image(self):
        img = image.load("imags/dracula.png")
        size = Vector2(img.get_size())
        img = transform.flip(img, True, False)
        img = transform.scale(img, size/5)

        return img

    def collide_player_npc(self, s1: sprite.Sprite, s2: sprite.Sprite):
        if s1.rect.colliderect(s2.rect):
            s2.update()
            self.lifebar.update_size_life(-10)
        return s1.rect.colliderect(s2.rect)

    def isInScreenRange(self, posx: Vector2, win: Surface)  -> bool:
        testposx = self.__pos.x + posx
        if testposx >= 0 and testposx <= win.get_rect().width:
                return True
        else: 
            return False

    def update(self, win: Surface):
        dpos = Vector2((0, 0))
        JUMP_RANGE = 200
        JUMP_STEP_HEIGHT = 2

        if self.__isJumping:
            if self.__jumpCounter in range(JUMP_RANGE//2):
                dpos.y = -self.__speed*JUMP_STEP_HEIGHT
                self.__jumpCounter += 1
            elif self.__jumpCounter in range(JUMP_RANGE//2, JUMP_RANGE -1, 1):
                dpos.y += self.__speed*JUMP_STEP_HEIGHT
                self.__jumpCounter += 1
            else:
                dpos.y = self.__speed*JUMP_STEP_HEIGHT
                self.__jumpCounter = 0
                self.__isJumping = False
            if key.get_pressed()[K_LEFT]:
                posx = -self.__speed*JUMP_STEP_HEIGHT
                if self.isInScreenRange(posx, win): 
                    dpos.x += posx 
            if key.get_pressed()[K_RIGHT]:
                posx = self.__speed*JUMP_STEP_HEIGHT
                if self.isInScreenRange(posx, win): 
                    dpos.x += posx

        else:

            if key.get_pressed()[K_UP]:
                self.__isJumping = True

            if key.get_pressed()[K_LEFT]:
                posx = -self.__speed
                if self.isInScreenRange(posx, win):
                    dpos.x +=posx 
            if key.get_pressed()[K_RIGHT]:
                posx = self.__speed
                if self.isInScreenRange(posx, win):
                    dpos.x +=posx 
            
        self.__pos += dpos
        self.rect.bottomleft = self.__pos

        #UPDATE PROJECTILE'S POSITION

        for e in event.get(KEYDOWN):
            if e.key == K_SPACE:
                self.__projectile.pos = self.pos + (self.rect.width/2, -self.rect.height/4)
                self.__projectile.rect.bottomleft = self.__projectile.pos
        
        if self.__projectile.resetProjectilePos:
            self.__projectile.pos = self.pos + (self.rect.width/2, -self.rect.height/4)
            self.__projectile.resetProjectilePos = False



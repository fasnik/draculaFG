from pygame import Surface, Vector2, image, transform, sprite, key
from pygame.locals import K_SPACE


class Projectile(sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()

        self.__pos = None
        self.image = self.fit_fireball()
        self.rect = self.image.get_rect()
        
        self.__speedFireball = 4
        self.__isProjectileActive = False
        self.__resetProjectilePos = False

    @property
    def resetProjectilePos(self):
        return self.__resetProjectilePos
    @resetProjectilePos.setter
    def resetProjectilePos(self, b):
        self.__resetProjectilePos = b

    @property
    def isProjectileActive(self):
        return self.__isProjectileActive

    @property
    def pos(self):
        return self.__pos

    @pos.setter
    def pos(self, pos):
        self.__pos = pos


    def collide_projectile_npc(self,s1: sprite.Sprite, s2: sprite.Sprite):
        if s1.rect.colliderect(s2.rect):
            s2.kill()
            self.__isProjectileActive = False
            self.resetProjectilePos = True
        return s1.rect.colliderect(s2.rect)

    def fit_fireball(self):
        img = image.load("imags/fireball.png")
        size = Vector2(img.get_size())/5
        img = transform.rotate(img, 120)
        img = transform.scale(img, size)

        return img

    def update(self, win: Surface):
        if self.__isProjectileActive:
            self.pos += Vector2((self.__speedFireball, 0))
            self.rect.bottomleft = self.pos
            
            if self.pos.x > win.get_width():
                self.__isProjectileActive = False
                self.resetProjectilePos = True

        else:    
            if key.get_pressed()[K_SPACE]:
                self.__isProjectileActive = True
        

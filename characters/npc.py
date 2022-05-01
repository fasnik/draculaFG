from pygame import Vector2, sprite, image, transform

class NPC(sprite.Sprite):
    def __init__(self, *pos) -> None:
        super().__init__()
        self.__pos = Vector2(pos)
        self.image = self.fit_img()
        self.rect = self.image.get_rect()
        self.rect.bottomright = self.__pos


    def fit_img(self):
        img = image.load('imags/npc1.png')
        size = Vector2(img.get_size())/3
        img = transform.scale(img, size)
        return img


    def update(self) -> None:
        
        self.__pos+= Vector2(50,0)
        self.rect.bottomright = self.__pos


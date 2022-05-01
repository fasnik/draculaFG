from pygame import sprite,image, Rect,Surface

class Spritesheet(sprite.Sprite):
    def __init__(self, imagePath) -> None:
        super().__init__()
        self.image = image.load(imagePath).convert()
        self.rect = Rect(0,0,200,200)
    
    def image_at(self, rect: Rect):
        rect = rect
        image = Surface(rect.size).convert()
        image.blit(self.image, (0, 0), rect)
        return image

    
    




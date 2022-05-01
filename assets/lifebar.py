from pygame import Surface, Rect, draw, Color, Vector2, font, sprite


class LifeBar(sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()

        blue = Color((0, 50, 200))
        self.__Font2 = font.Font(None, 40)
        self.__lifebar_txt = self.__Font2.render('Lifebar', True, blue)

        self.__pos = Vector2((10, 30))
        self.__pos_frame = Vector2((0, 0))
        self.__pos_back = Vector2((2, 2))
        self.__pos_life = Vector2((6, 6))

        self.__size = Vector2((500, 50))
        self.__size_back = self.size_back
        self.__size_life = self.size_life

        self.lifebar_frame = Rect(self.__pos_frame, self.__size)
        self.lifebar_back = Rect(self.__pos_back, self.__size_back)
        self.lifebar_life = Rect(self.__pos_life, self.__size_life)

        self.lifebar_surf = self.lifebarSurf()

    @property
    def size(self):
        return self.__size

    @property
    def size_back(self):
        return Vector2(self.__size - 2*self.__pos_back)

    @property
    def size_life(self):
        return self.__size - 2*self.__pos_life

    def update_size_life(self, dw):
        newlife = self.__size_life + Vector2((dw, 0))
        if newlife.x < 0:
            self.__size_life.x = 0
        elif newlife.x >= self.size_life.x:
            self.__size_life = self.size_life
        else:
            self.__size_life = newlife
        
        self.lifebar_life = Rect(self.__pos_life, self.__size_life)
        self.lifebar_surf = self.lifebarSurf()
        return self.lifebar_surf

    @property
    def pos(self):
        return self.__pos

    def lifebarSurf(self):

        # Colors
        black = Color((50, 0, 0, 200))
        gray = Color((200, 200, 200, 200))
        yellow = Color((255, 255, 0, 50))

        # Surface to render
        surf = Surface(self.size)

        # Draw Rects

        draw.rect(surf, gray, self.lifebar_frame)
        draw.rect(surf, black, self.lifebar_back)
        draw.rect(surf, yellow, self.lifebar_life)

        surf.blit(self.__lifebar_txt, self.pos+(10,self.__lifebar_txt.get_height()/2-self.size.y/2))
        return surf

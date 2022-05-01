from pygame import Surface, Vector2, sprite, font, Color
class GameOver(sprite.Sprite):


    def __init__(self) -> None:
        super().__init__()
        self.surf = self.game_over_surf()
        self.rect = self.surf.get_rect()


    def game_over_surf(self) -> Surface:
        size = Vector2(1000,500)
        surf = Surface(size)
        red = Color((255,0,0))         
        Font1 = font.Font(None, 80)
        
        gameover = Font1.render("Você morreu!", True, red)
        playagain = Font1.render("Jogar novamente? Aperte ENTER",True, red)

        surf.blit(playagain, size - playagain.get_size())
        surf.blit(gameover, (size.x/2 - gameover.get_width()/2,30))

        return surf

    def update(self) -> None:
        ...


    
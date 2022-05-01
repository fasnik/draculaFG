from pygame import image, transform

class Logo:
    def __init__(self) -> None:
        self.__logo = transform.scale(image.load('imags/logo.png'), (300, 100))

    @property
    def imag(self):
        return self.__logo
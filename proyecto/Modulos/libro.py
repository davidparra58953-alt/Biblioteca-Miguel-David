class Libro():
    """
    Representa al objeto libro

    Atributos:
    ISBN (int):
    title (String):
    author (String):
    weigth (int):
    price (int):
    borrowed (bool):
    """
    def __init__(self,ISBN,title, author, weigth, price, borrowed):

        self.__ISBN=ISBN
        self.__title=title
        self.__author=author
        self.__weigth=weigth
        self.__price=price
        self.__borrowed=borrowed

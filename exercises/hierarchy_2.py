class Character:

    def __init__(self, x, y, img_file, speed, life_counter):
        self.x = x
        self.y = y
        self.img_file = img_file
        self.speed = speed
        self.life_counter = life_counter


class Enemy(Character):

    def __init__(self, x, y, img_file, speed, life_counter):
        super().__init__(x, y, img_file, speed, life_counter)
        self.message = "I'm here to protect my master"


class Player(Character):

    def __init__(self, x, y, img_file, life_counter):
        super().__init__(x, y, img_file, 56, life_counter)


class DifficultEnemy(Enemy):

    def __init__(self, x, img_file, speed, life_counter):
        super().__init__(x, 80, img_file, speed, life_counter)


class EasyEnemy(Enemy):

    def __init__(self, x, y, img_file):
        super().__init__(x, y, img_file, 40, 1)

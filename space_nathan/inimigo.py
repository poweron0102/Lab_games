from PPlay.sprite import *


class Inimigo(Sprite):
    def __init__(self, x, y):
        super().__init__("imagens_jogo_principal/inimigo.png")

        self.hp = 2
        self.offset = x
        self.speed = 0.5
        self.x = x
        self.xs = x
        self.y = y

    def update(self):
        if self.hp <= 0:
            return
        self.offset += self.speed
        if self.offset > self.xs + self.width or self.offset < self.xs:
            self.speed *= -1
            self.y += 5
            if self.y + self.height > 510:
                print("Vc morreu!")
                exit()
        self.set_position(self.offset, self.y)
        self.draw()


class Inimigos:
    def __init__(self, tiros):
        self.tiros = tiros
        self.num_inimigos = 0

        self.inimigos = [[]]
        for i in range(4):
            inimigos_linha = []
            for j in range(8):
                inimigos_linha.append(Inimigo(20 + j * 140, 90 * i))
            self.inimigos.append(inimigos_linha)

    def update(self):
        self.num_inimigos = 0
        for i in range(1, len(self.inimigos)):
            for j in range(len(self.inimigos[i])):
                for tiro in self.tiros:
                    if self.inimigos[i][j].hp > 0 and self.inimigos[i][j].collided(tiro):
                        self.inimigos[i][j].hp -= 1
                        self.tiros.remove(tiro)
                        break
                self.inimigos[i][j].update()
                if self.inimigos[i][j].hp > 0:
                    self.num_inimigos += 1

from PPlay.sprite import *
import random


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
    def __init__(self, tiros, vars: dict):
        self.variaves = vars
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
                if i == len(self.inimigos) - 1 and random.randint(0, 200) == 0:
                    tiro = Sprite("imagens_jogo_principal/tiro.png")
                    tiro.x = self.inimigos[i][j].x + (self.inimigos[i][j].width // 2)
                    tiro.y = self.inimigos[i][j].y + self.inimigos[i][j].height + 10
                    tiro.speed = 300
                    self.tiros.append(tiro)
                for tiro in self.tiros:
                    if self.inimigos[i][j].hp > 0 and self.inimigos[i][j].collided(tiro):
                        self.inimigos[i][j].hp -= 1
                        self.tiros.remove(tiro)
                        self.variaves['pontucao'] += 10
                        break
                self.inimigos[i][j].update()
                if self.inimigos[i][j].hp > 0:
                    self.num_inimigos += 1

        if self.num_inimigos == 0:
            print("Vc ganhou!")
            self.variaves['pontucao'] += 1000
            self.variaves['vitorias'] += 1

            self.inimigos = [[]]
            for i in range(4):
                inimigos_linha = []
                for j in range(8):
                    inimigos_linha.append(Inimigo(20 + j * 140, 90 * i))
                self.inimigos.append(inimigos_linha)
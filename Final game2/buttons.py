import pygame as pg


class Button:
    """
    Uma classe que representa um botão gráfico em uma interface de usuário.

    Atributos:
        x (int): A coordenada x do canto superior esquerdo do botão.
        y (int): A coordenada y do canto superior esquerdo do botão.
        text (str): O texto exibido no botão.
        font_size (int, opcional): O tamanho da fonte para o texto do botão.
        color (tuple, opcional): A cor do texto.
        font (str, opcional): O arquivo da fonte para o texto do botão.
        img_base (str, opcional): O arquivo de imagem base para o botão.
        img_hover (str, opcional): O arquivo de imagem para o botão quando estiver com o cursor sobre ele.
        function (callable, opcional): A função a ser chamada quando o botão for clicado.
        arg_click (qualquer, opcional): Um argumento a ser passado para a função quando o botão for clicado.

    Uso:
        # Criando um botão
        meu_botao = Button(100, 100, "Clique em mim", font_size=20, color=(255, 255, 255), function=lambda: print("Clique"))

        # Atualizando o estado do botão em um loop de jogo
        meu_botao.update()
    """
    def __init__(
            self,
            x: int, y: int,
            text: str,
            font_size=25,
            color=(255, 255, 255),
            font="Inter-Bold.ttf",
            img_base="button_base",
            img_hover="button_hover",
            func_click=None, arg_click=None,
            func_hover=None, arg_hover=None
    ):
        self.img = None
        self.pressed = True
        self.hover = True

        self.img_base = pg.image.load(f"assets/gui/{img_base}.png").convert_alpha()
        self.img_hover = pg.image.load(f"assets/gui/{img_hover}.png").convert_alpha()

        self.x, self.y = x, y

        self.width = self.img_base.get_width()
        self.height = self.img_base.get_height()

        font = pg.font.Font(f"fonts/{font}", font_size)
        self.text_img = font.render(text, False, color)
        self.font_x = self.x + (self.width // 2 - self.text_img.get_width() // 2)
        self.font_y = self.y + (self.height // 2 - self.text_img.get_height() // 2)

        self.func_click = func_click
        self.arg_click = arg_click
        self.func_hover = func_hover
        self.arg_hover = arg_hover

    def update(self):
        """
        Atualiza o estado do botão, incluindo a verificação de passagem do mouse e eventos de clique.

        Se o mouse estiver sobre o botão e um evento de clique for detectado,
        a função associada será chamada com o argumento especificado (se houver).
        """
        mouse_x, mouse_y = pg.mouse.get_pos()
        if self.x <= mouse_x <= self.x + self.width and self.y <= mouse_y <= self.y + self.height:
            self.img = self.img_hover
            pressed = pg.mouse.get_pressed()[0]

            if pressed and not self.pressed:
                if self.func_click:
                    if self.arg_click:
                        self.func_click(self.arg_click)
                    else:
                        self.func_click()
            if not self.hover:
                if self.func_hover:
                    if self.arg_hover:
                        self.func_hover(self.arg_hover)
                    else:
                        self.func_hover()

            self.pressed = pressed
            self.hover = True
        else:
            self.pressed = False
            self.img = self.img_base

        if self.img:
            pg.display.get_surface().blit(
                self.img,
                (self.x, self.y)
            )
            pg.display.get_surface().blit(
                self.text_img,
                (self.font_x, self.font_y)
            )

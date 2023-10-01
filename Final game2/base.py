from main import *



def init(in_game: InGame):
    in_game.map = Map(in_game)
    in_game.player = Player(in_game)
    in_game.ray_caster = RayCaster(in_game)
    in_game.action = Actions(in_game)
    in_game.drawer = Drawer(in_game)
    in_game.dialogue_handler = DialogueHandler(in_game)

    in_game.sprite_handler = SpriteHandler(in_game)
    in_game.sprite_handler.add(Sprite(in_game, 'platelet', 545, 610, action='construction'))


def loop(in_game: InGame):
    in_game.player.update()
    in_game.action.update()
    in_game.ray_caster.update()
    in_game.dialogue_handler.update()
    in_game.drawer.update()
    in_game.sprite_handler.update()

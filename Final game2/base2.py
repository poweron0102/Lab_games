from main import *
from map import Tile
from textures import Texture
from actions import add_action


@add_action
def Next_map(in_game: InGame, *args):
    in_game.player.x = 50
    in_game.player.y = 50
    in_game.new_game('base')


TileSet = [
    Tile(False, False, [255, 255, 255], None, 0),
    Tile(True, True, 'darkgray', None, 1),
    Tile(True, True, 'red', None, 2),
    Tile(True, True, 'Purple', None, 3),
    Tile(False, False, 'green', 'Next_map', 0),
    Tile(False, False, '#c92a2a', 'Lose', 0),
]

TextureSet = [
    None,
    Texture('quartz_bricks'),
    Texture('furnace_side none furnace_front_on none'),
    Texture('n s l w'),
]

TextureFloor = [
    'birch_planks',
    'dirt',
    'acacia_log_top',
    'acacia_planks_s',
    'cobblestone',
]

world_map = np.array([
    [  # Wall
        [0, 0, 1, 0, 0, 0, 0, 2, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 2, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 4, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],

    ],
    [  # Floor
        [0, 0, 1, 0, 0, 0, 0, 2, 1, 2, 3, 4, 1, 0, 0, 0, 0, 0, 1, 1],
        [0, 0, 1, 0, 0, 0, 0, 1, 2, 3, 4, 5, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 2, 2, 3, 4, 1, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 3, 5, 5, 2, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 0, 0, 2, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 3, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 3],
        [0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    ],
    [  # Ceiling
        [0, 2, 1, 0, 0, 0, 0, 2, 0, 3, 3, 3, 1, 2, 1, 0, 0, 0, 1, 1],
        [0, 0, 1, 0, 0, 0, 0, 0, 0, 3, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 4, 0, 0, 0, 0, 0, 2, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 3, 3, 3, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 3, 3, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 2, 0, 0, 0, 3, 0, 3, 2, 2, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0, 2, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 2, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 4, 1, 5, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 2, 0, 4, 1, 0, 0, 0, 0, 0, 2],
        [0, 2, 1, 0, 0, 1, 0, 2, 0, 1, 0, 3, 4, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    ]
])


def init(in_game: InGame):
    in_game.map = Map(in_game, world_map, TileSet, TextureSet, TextureFloor)
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
    in_game.sprite_handler.update()

    in_game.drawer.update()

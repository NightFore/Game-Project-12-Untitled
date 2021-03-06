import pygame
from os import path

from Class import *
from Function import *

def init_menu(game, menu, clear=True, ui=True, button=True, entity=True, wall=True):
    if clear:
        clear_menu(game)
    if ui:
        if menu in game.ui_dict:
            for ui in game.ui_dict[menu]:
                UI(game, game.ui_dict, game.uis, data=menu, item=ui)
    if button:
        if menu in game.button_dict:
            for button in game.button_dict[menu]:
                Button(game, game.button_dict, game.buttons, data=menu, item=button)
    if entity:
        if menu in game.entity_dict:
            for entity in game.entity_dict[menu]:
                if game.entity_dict[menu][entity]["type"] == "player":
                    Player(game, game.entity_dict, game.player, data=menu, item=entity)
                else:
                    Entity(game, game.entity_dict, game.entities, data=menu, item=entity)
    if wall:
        if menu in game.wall_dict:
            for wall in game.wall_dict[menu]:
                Wall(game, game.wall_dict, game.walls, data=menu, item=wall)

def clear_menu(game):
    for sprite in game.all_sprites:
        sprite.kill()

def main_menu(game, menu):
    init_menu(game, menu)

def tutorial_menu(game, menu):
    init_menu(game, menu)

def level_menu(game, menu):
    init_menu(game, menu, entity=False)
    game.level.init(menu)

def pause_menu(game, menu):
    game.paused = not game.paused



MENU_DICT = {
    "main_menu": main_menu,
    "tutorial_menu": tutorial_menu,
    "level_menu": level_menu,
    "pause_menu": pause_menu,
}

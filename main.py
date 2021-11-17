#!/usr/bin/env python3

import copy
import traceback

import tcod

import color

#from actions import EscapeAction, MovementAction
from engine import Engine

import entity_factories
import exceptions
import input_handlers

from procgen import generate_dungeon

def main() -> None:
    screen_width = 80
    screen_height = 50

    map_width = 80
    map_height = 43

    room_max_size = 10
    room_min_size = 6
    max_rooms = 30

    max_monsters_per_room = 2
    max_items_per_room = 2

    tileset = tcod.tileset.load_tilesheet(
        "dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD
    )

    player = copy.deepcopy(entity_factories.player)

    engine = Engine(player=player)

    engine.game_map = generate_dungeon(
        max_rooms=max_rooms,
        room_min_size=room_min_size,
        room_max_size=room_max_size,
        map_width=map_width,
        map_height=map_height,
        max_monsters_per_room=max_monsters_per_room,
        max_items_per_room=max_items_per_room,
        engine=engine,)

    engine.update_fov()

    engine.message_log.add_message(
        "Hello and welcome, adventurer, to yet another dungeon!",
        color.welcome_text
    )

    handler: input_handlers.BaseEventHandler = input_handlers.MainGameEventHandler(engine)

    """ TODO - suppress the OpenGL error on cration of new terminal """
    with tcod.context.new_terminal(
        screen_width,
        screen_height,
        tileset=tileset,
        title="Another Roguelike Tutorial",
        vsync=True
    ) as context:
        root_console = tcod.Console(screen_width, screen_height, order="F")
        try:
            while True:
                root_console.clear()
                handler.on_render(console=root_console)
                context.present(root_console)

                try:
                    for event in tcod.event.wait():
                        context.convert_event(event)
                        handler = handler.handle_events(event)
                except Exception:   # handle exceptions in game
                    traceback.print_exc()   # print error to stderr
                    # write to the message log
                    if isinstance(handler, input_handlers.EventHandler):
                        handler.engine.message_log.add_message(traceback.format_exc(), color.error)
        except exceptions.QuitWithoutSaving:
            raise
        except SystemExit:
            # TODO: add the save function here
            raise
        except BaseException:   # save on any other unexpected exception
            # TODO: add the save function here
            raise


if __name__ == "__main__":
    main()

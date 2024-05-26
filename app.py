import dearpygui.dearpygui as dpg
from Objects import *


def GeneratePlayer():
    newPlayer = Player()
    newPlayer.generatePlayer()

dpg.create_context()

##Main window
with dpg.window(label="Main"):

    with dpg.menu_bar():
        with dpg.menu(label="File"):
            dpg.add_menu_item(label="Save")
            dpg.add_menu_item(label="Settings")
            dpg.add_menu_item(label="Quit")
        dpg.add_menu_item(label="Home")
        with dpg.menu(label="Team Management"):
            dpg.add_menu_item(label="My Team")
            dpg.add_menu_item(label="Game Plan")
            dpg.add_menu_item(label="Practice")
            dpg.add_menu_item(label="Generate Player", callback=GeneratePlayer)
        with dpg.menu(label="League"):
            dpg.add_menu_item(label="Top 25")
            dpg.add_menu_item(label="Conference Standings")
        with dpg.menu(label="Stats"):
            dpg.add_menu_item(label="Team Stats")
            dpg.add_menu_item(label="Player Stats")
            dpg.add_menu_item(label="Coach Stats")


##Recruting window            
with dpg.window(label="Recruiting"):
    with dpg.menu_bar():
        dpg.add_menu_item(label="Available Targets")
        dpg.add_menu_item(label="My Targets")
        dpg.add_menu_item(label="Calendar")
        dpg.add_menu_item(label="Class Rankings")

##Schedule window
with dpg.window(label="Schedule"):
    with dpg.menu_bar():
        dpg.add_menu_item(label="Practice")
        dpg.add_menu_item(label="Depth Chart")
        dpg.add_menu_item(label="Calendar")
    dpg.add_button(enabled=True, label="Save and Advance to next game")
            


dpg.create_viewport(title='College Basketball Dynasty', width=1000, height=600)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
import dearpygui.dearpygui as dpg
from Objects import *
from Player import *

global myRoster
myRoster = []


def GeneratePlayer(pos):
    newPlayer = Player(pos)
    print(newPlayer.ht)
    myRoster.append(newPlayer)

dpg.create_context()

GeneratePlayer("PG")
GeneratePlayer("SG")
GeneratePlayer("SF")
GeneratePlayer("PF")
GeneratePlayer("C")
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
    
    with dpg.table(header_row=True, resizable=True, policy=dpg.mvTable_SizingStretchProp,
                   borders_outerH=True, borders_innerV=True, borders_innerH=True, borders_outerV=True):
        ##Player stats start at index 5
        dpg.add_table_column(label="Player ID")
        dpg.add_table_column(label="Player First Name")
        dpg.add_table_column(label="Player Last Name")
        dpg.add_table_column(label="Player Position")
        dpg.add_table_column(label="Player HT")
        dpg.add_table_column(label="Player WT")
        dpg.add_table_column(label="Player Length")
        dpg.add_table_column(label="midshooting")
        dpg.add_table_column(label="postscoring")
        dpg.add_table_column(label="deepthreeshooting")
        dpg.add_table_column(label="threeptshooting")
        dpg.add_table_column(label="speed")
        dpg.add_table_column(label="strength")
        dpg.add_table_column(label="interiordefense")
        dpg.add_table_column(label="perimeterdefense")
        dpg.add_table_column(label="steal")
        dpg.add_table_column(label="block")
        dpg.add_table_column(label="offrb")
        dpg.add_table_column(label="defrb")
        dpg.add_table_column(label="passing")
        dpg.add_table_column(label="FT Shooting")
        for i in myRoster:
            with dpg.table_row():
                for j in range(0,22):
                    with dpg.table_cell():
                        if(j<1):
                            dpg.add_button(label=f"{i.id}")
                        if(j==1):
                            dpg.add_button(label=f"{i.fname}")
                        if(j==2):
                            dpg.add_button(label=f"{i.lname}")
                        if(j==3):
                            dpg.add_button(label=f"{i.pos}")
                        if(j==4):
                            dpg.add_button(label=f"{i.ht}")
                        if(j==5):
                            dpg.add_button(label=f"{i.wt}")
                            
                        if(j==6):
                            dpg.add_button(label=f"{i.length}")
                        if(21>j>6):
                            cat = statcat[j-7]
                            dpg.add_button(label=f"{i.stats[cat]}")



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
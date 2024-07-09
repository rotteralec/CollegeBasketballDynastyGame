import dearpygui.dearpygui as dpg
from App import *
from DynastyGenerator import *
import json

def loadRoster(id, conf):
    myRoster = []
    for i,k in conf[str(id)].items():
        tPlayer = loadPlayer(i,k)
        myRoster.append(tPlayer)
    myTeam = loadTeam(174, "Michigan State", myRoster, [])
    return myTeam
    




##run backend##
resetSave("testsave.json")

myRosterID = genConference("Big Ten")
myConf = readSave("testsave.json")
""" print("MSU'S ROSTER: ")
print(myConf[str(myRosterID)])
print("MICHIGAN's ROSTER: ")
print(myConf[str(173)]) """
myTeam =loadRoster(myRosterID, myConf)
myTeam.calcRatings()
curClass = genClass()
saveRecruits(curClass)
newClass = readRecruits()
curSeason = genSeason()


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
    dpg.add_text("Overall: "+str(myTeam.getRatings()[0]))
    dpg.add_text("Offense: "+str(myTeam.getRatings()[1]))
    dpg.add_text("Defense: "+str(myTeam.getRatings()[2]))

    with dpg.table(header_row=True, resizable=True, policy=dpg.mvTable_SizingStretchProp,
                   borders_outerH=True, borders_innerV=True, borders_innerH=True, borders_outerV=True):
        ##Player stats start at index 5
        dpg.add_table_column(label="Player ID")
        dpg.add_table_column(label="Player First Name")
        dpg.add_table_column(label="Player Last Name")
        dpg.add_table_column(label="Player Position")
        dpg.add_table_column(label="Year")
        dpg.add_table_column(label="HT")
        dpg.add_table_column(label="WT")
        dpg.add_table_column(label="Player Length")
        dpg.add_table_column(label="Overall")
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
        for i in myTeam.getRoster():
            with dpg.table_row():
                for j in range(0,23):
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
                            dpg.add_button(label=f"{i.year}")
                        if(j==5):
                            dpg.add_button(label=f"{i.ht}")
                            
                            
                        if(j==6):
                            dpg.add_button(label=f"{i.wt}")
                            

                        if(j ==7):
                            dpg.add_button(label=f"{i.length}")
                        if(j ==8):
                            dpg.add_button(label=f"{i.overall}")

                        if(23>j>8):
                            cat = statcat[j-9]
                            dpg.add_button(label=f"{i.stats[cat]}")



##Recruting window            
with dpg.window(label="Recruiting"):
    with dpg.menu_bar():
        with dpg.menu(label="Selection"):
            dpg.add_menu_item(label="Target")
            dpg.add_menu_item(label="Remove")
            dpg.add_menu_item(label="Scout")
        dpg.add_menu_item(label="Available Targets")
        dpg.add_menu_item(label="My Targets")
        dpg.add_menu_item(label="My Commits")
        dpg.add_menu_item(label="Outstanding Offers")
        dpg.add_menu_item(label="Class Rankings")
    with dpg.table(header_row=True, resizable=True, policy=dpg.mvTable_SizingStretchProp,
                   borders_outerH=True, borders_innerV=True, borders_innerH=True, borders_outerV=True):
        ##Player stats start at index 5
        dpg.add_table_column(label="Select")
        dpg.add_table_column(label="Player ID")
        dpg.add_table_column(label="Player First Name")
        dpg.add_table_column(label="Player Last Name")
        dpg.add_table_column(label="Player Position")
        dpg.add_table_column(label="School ")
        dpg.add_table_column(label="Overall")
        dpg.add_table_column(label="Priority")
        dpg.add_table_column(label="Offer")
        dpg.add_table_column(label="NIL")
        dpg.add_table_column(label="Action")
        for i in newClass:
            with dpg.table_row():
                for j in range(0, 11):
                    with dpg.table_cell():
                        if(j<1):
                            dpg.add_checkbox()
                        if(j==1):
                            dpg.add_button(label=f"{i.getPlayer().id}")
                        if(j==2):
                            dpg.add_button(label=f"{i.getPlayer().fname}")
                        if(j==3):
                            dpg.add_button(label=f"{i.getPlayer().lname}")
                        if(j==4):
                            dpg.add_button(label=f"{i.getPlayer().pos}")
                        if(j==5):
                            dpg.add_button(label=f"{i.getSchools()[0]}")
                        if(j==6):
                            dpg.add_button(label=f"{i.getPlayer().overall}")
                        if(j==7):
                            dpg.add_button(label=f"{i.getPriority()[0]}")
                        if(j==8):
                            dpg.add_button(label=f"No Offer")
                        if(j==9):
                            dpg.add_button(label=f"{i.getSchools()[0][3]}")
                        if(j==10):
                            dpg.add_listbox(items=["Head Coach Call", "Head Coach Text", "Assistant Coach Call", "Assistant Coach Text"]) #Add recruit action score to each option
                            

##Schedule window
with dpg.window(label="Training"):
    with dpg.menu_bar():
        dpg.add_menu_item(label="Practice")
        dpg.add_menu_item(label="Depth Chart")
        dpg.add_menu_item(label="Game Plan")
    #dpg.add_button(enabled=True, label="Save and Advance to next game")

#currOpp = 

def callbackSimWeekGame(sender, data):
    print(sender)
    print(data)
    curSeason.advanceSeason()
    dpg.set_value("homeTeam", curSeason.getCurrentGame().getHomeName())
    dpg.set_value("awayTeam", curSeason.getCurrentGame().getAwayName())
    dpg.set_value("homeScore", curSeason.getScheduleGame(curSeason.getTimeFrame()-1).getHomeScore())
    dpg.set_value("awayScore", curSeason.getScheduleGame(curSeason.getTimeFrame()-1).getAwayScore())

#game window Will be shown only when advanced to simulating game
with dpg.window(label="Current Game"):
    dpg.add_text("Current Game: ")
    dpg.add_text(curSeason.getCurrentGame().getHomeName(), tag="homeTeam")
    dpg.add_text(curSeason.getCurrentGame().getAwayName(), tag="awayTeam")
    dpg.add_button(label="Sim Game and Advance week", callback=callbackSimWeekGame)
    dpg.add_text("Previous Game Result: ")
    dpg.add_text(0, tag="homeScore")
    dpg.add_text(0, tag="awayScore")

            


dpg.create_viewport(title='College Basketball Dynasty', width=1000, height=600)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
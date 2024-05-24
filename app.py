import dearpygui.dearpygui as dpg

dpg.create_context()

with dpg.window(label="Primary Window"):

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
        with dpg.menu(label="League"):
            dpg.add_menu_item(label="Top 25")
            dpg.add_menu_item(label="Conference Standings")
        with dpg.menu(label="Stats"):
            dpg.add_menu_item(label="Team Stats")
            dpg.add_menu_item(label="Player Stats")
            dpg.add_menu_item(label="Coach Stats")
            


dpg.create_viewport(title='College Basketball Dynasty', width=1000, height=600)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
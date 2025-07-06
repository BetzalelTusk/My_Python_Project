import dearpygui.dearpygui as dpg

default_Width = 600
default_SetBack = 200
dpg.create_context()
dpg.create_viewport(title='DPG Demo', width=default_Width, height=300)

with dpg.window(label="Example Window"):
    dpg.add_text("This is a simple DearPyGui demo")
    dpg.add_button(label="Click Me")
    dpg.add_text("Hello, world")
    dpg.add_button(label="Save")
    dpg.add_input_text(label="string", default_value="Quick brown fox")
    dpg.add_slider_int(label="integer", default_value=0, max_value=10000000)
    with dpg.child_window(width=default_Width - default_SetBack, height=100):
        dpg.add_text("This is a child window")
        dpg.add_button(label="Child Button")
        dpg.add_slider_int(label="Child_Slider_Demo",
                           default_value=50, max_value=100)

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()

# I am temporarily naming this project "Probo" for Productivity Booster, AKA Project Probo

import dearpygui.dearpygui as dpg

DEFAULT_WIDTH = 700
DEFAULT_HEIGHT = 350
DEFAULT_WINDOW_WIDTH = 750
DEFAULT_WINDOW_HEIGHT = 400
DEFAULT_WINDOW_TITLE = "DearPyGui Demo"
DEFAULT_SETBACK = 200
DEFAULT_VIEWPORT_TITLE = "My Grade Book"


class gameApp:
    def __init__(self, name: str, grade: int, Student_ID: str):
        self.name = name
        self.grade = grade
        self.Student_ID = Student_ID
        dpg.create_context()
        dpg.create_viewport(
            title=DEFAULT_VIEWPORT_TITLE,
            width=DEFAULT_WINDOW_WIDTH,
            height=DEFAULT_WINDOW_HEIGHT)

        with dpg.window(label="Demo Window", autosize=False,
                        height=DEFAULT_HEIGHT,
                        width=DEFAULT_WIDTH):
            dpg.add_text("Student's Grade Page ")
            dpg.add_button(label="Calculate Grade")
            # Grade Input
            dpg.add_input_text(label="Grade II",
                               default_value="Input Grade Here")

        with dpg.window(label="Demo Window II",
                        autosize=False,
                        height=DEFAULT_HEIGHT,
                        width=DEFAULT_WIDTH):
            dpg.add_text("Student's Grade Page")
            dpg.add_button(label="Calculate Grade")
            # Grade Input
            dpg.add_input_text(
                label="Grade", default_value="Input Grade Here",
                tag="Student Grade")
        dpg.setup_dearpygui()
        dpg.show_viewport()
        dpg.start_dearpygui()
        dpg.destroy_context()

    # def decide_grade():


obj = gameApp("Josh", 80, "483920_MD")
print(obj)
print('hi')

import dearpygui.dearpygui as dpg


class gameApp:
    def __init__(self):

        # This is a simple DearPyGui demo script

        # It creates a window with various widgets including buttons,
        # text, input fields, and sliders.

        dpg.create_context()
        dpg.create_viewport(title=self.DEFAULT_WINDOW_TITLE,
                            width=self.DEFAULT_WINDOW_WIDTH,
                            height=self.DEFAULT_WINDOW_HEIGHT)

        dpg.setup_dearpygui()
        dpg.show_viewport()
        dpg.start_dearpygui()
        dpg.destroy_context()
        with dpg.window(
            label="Grade Book",
            width=700,
            height=400
        ):
            # This is the main window where all widgets will be added
            dpg.add_button(label="Enter", callback=game.search_grade)
            dpg.add_input_text(
                label="Student Name",
                default_value="Name of student",
                tag="Student Name"
            )
            dpg.add_input_text(
                label="Student ID",
                default_value="08394023-MD",
                tag="Student ID"
            )

            # Adding a slider for the student grade input
            # The slider allows the user to select a grade between 0 and 100
            dpg.add_slider_int(
                label="Student Grade",
                default_value=0,
                max_value=100,
                tag="Student Grade"
            )

            dpg.add_text("", tag="Result Text")
            # This line adds a text widget to the window with the tag "Result Text"

            dpg.add_text()

    def search_grade():
        print(type(dpg.get_value("Student Grade")))

        score = dpg.get_value("Student Grade")
        name = dpg.get_value("Student Name")
        student_id = dpg.get_value("Student ID")

        if score >= 90 and score <= 100:
            grade = "A"
        elif score >= 80 and score < 90:
            grade = "B"
        elif score >= 70 and score < 80:
            grade = "C"
        elif score >= 60 and score < 70:
            grade = "D"
        else:
            grade = "F"

        dpg.set_value(
            "Result Text", f"{name} ({student_id}) has an {grade} grade.")

# This function is called when the button is clicked
# It prints a message to the console

# Define default values for the window and widgets


# Create a window with specified purpose and dimensions
# The window will contain various widgets for user interaction
# "Grade Book" is the label for the window

DEFAULT_WIDTH = 700
DEFAULT_WINDOW_WIDTH = 750
DEFAULT_WINDOW_HEIGHT = 400
DEFAULT_WINDOW_TITLE = "DearPyGui Demo"
DEFAULT_SETBACK = 200

gameApp()

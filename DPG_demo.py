# Documentation in this code is EXREMELY important and necessary as
# the goal of this script is ENTIRELY for learning purposes.

# This script is a simple demonstration of how to use DearPyGui,
# a Python GUI framework.
#
# Copilot and other AI tools were used to assist in writing this code.
# The code creates a window with various widgets including buttons, text,
# input fields, and sliders.

# Import the DearPyGui library
import dearpygui.dearpygui as dpg


def decide_grade():

    # This function is called when the button is clicked.
    # It retrieves the values from the input fields,
    # and prints the student's grade based on the input.

    print(type(dpg.get_value("Student Grade")))

    grade = dpg.get_value("Student Grade")
    name = dpg.get_value("Student Name")
    student_id = dpg.get_value("Student ID")

    if grade >= 90 and grade <= 100:
        dpg.set_value("Result Text", f"{name} ({student_id}) has an A grade.")
    elif grade >= 80 and grade < 90:
        dpg.set_value("Result Text", f"{name} ({student_id}) has a B grade.")
    elif grade >= 70 and grade < 80:
        dpg.set_value("Result Text", f"{name} ({student_id}) has a C grade.")
    elif grade >= 60 and grade < 70:
        dpg.set_value("Result Text", f"{name} ({student_id}) has a D grade.")
    else:
        dpg.set_value("Result Text", f"{name} ({student_id}) has an F grade.")


# This function is called when the button is clicked
# It prints a message to the console

# Define default values for the window and widgets
DEFAULT_WIDTH = 700
DEFAULT_WINDOW_WIDTH = 750
DEFAULT_WINDOW_HEIGHT = 400
DEFAULT_WINDOW_TITLE = "DearPyGui Demo"
DEFAULT_SETBACK = 200
# This is a simple DearPyGui demo script

# It creates a window with various widgets including buttons,
# text, input fields, and sliders.

dpg.create_context()
dpg.create_viewport(title=DEFAULT_WINDOW_TITLE,
                    width=DEFAULT_WINDOW_WIDTH, height=DEFAULT_WINDOW_HEIGHT)

with dpg.window(
    label="Example Window",
    width=DEFAULT_WIDTH,
    height=DEFAULT_WINDOW_HEIGHT
):
    # This is the main window where all widgets will be added
    dpg.add_text(
        "This is a simple DearPyGui demo"
    )
    dpg.add_button(label="Click Me", callback=decide_grade)
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


dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()

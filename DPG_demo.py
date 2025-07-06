# Documentation in this code is EXREMELY important and necessary as the goal of this script is ENTIRELY for learning purposes.
# This script is a simple demonstration of how to use DearPyGui, a Python GUI framework.
# Copilot and other AI tools were used to assist in writing this code.
# The code creates a window with various widgets including buttons, text, input fields, and sliders

# Import the DearPyGui library
import dearpygui.dearpygui as dpg


def callback():
    print("Button clicked!")


def decide_grade():
    grade = dpg.get_value("Student Grade")
    name = dpg.get_value("Student Name")
    student_id = dpg.get_value("Student ID")

    if grade >= 90:
        dpg.set_value("Student Grade", "A")
    elif grade >= 80:
        dpg.set_value("Student Grade", "B")
    elif grade >= 70:
        dpg.set_value("Student Grade", "C")
    elif grade >= 60:
        dpg.set_value("Student Grade", "D")
    else:
        dpg.set_value("Student Grade", "F")


# This function is called when the button is clicked
# It prints a message to the console
print()

# Define default values for the window and widgets
default_Width = 700
default_Window_Width = 750
default_Window_Height = 400
default_Window_Title = "DearPyGui Demo"
default_SetBack = 200
# This is a simple DearPyGui demo script

# It creates a window with various widgets including buttons, text, input fields, and sliders
dpg.create_context()
dpg.create_viewport(title=default_Window_Title,
                    width=default_Window_Width, height=default_Window_Height)


with dpg.window(label="Example Window", width=default_Width, height=default_Window_Height):
    # This is the main window where all widgets will be added
    dpg.add_text("This is a simple DearPyGui demo")
    dpg.add_button(label="Click Me", callback=callback)
    dpg.add_input_text(
        label="Student Name", default_value="Name of student")
    dpg.add_input_text(label="Student ID", default_value="Default ID")
    dpg.add_slider_int(label="Student Grade", default_value=0, max_value=100)
    with dpg.child_window(width=default_Width - default_SetBack, height=100):
        dpg.add_text("This is a child window")
        dpg.add_button(label="Child Button", callback=callback)
        dpg.add_slider_int(label="Child Slider Demo",
                           default_value=50, max_value=100)

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()

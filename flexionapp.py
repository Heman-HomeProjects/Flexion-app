import tkinter
from tkinter import *

my_window =Tk()  ## Defines the root window where all the button and lables and other GUI interface will be built 
my_window.title("Flexion Conversion app")
my_window.geometry("500x400")

## Defining a method to do numeric checks on the Source and Target numeric fields
def isNumeric_validation(input_field):
    try:
        user_input = float(input_field.get())
    except ValueError:
        print("Invalid Input - Not a numeric value!")
        display_value_label["text"] = "Invalid input - Not a numeric value!"
        raise Exception 
    return user_input

## This defines the Submit method when a user clicks on the submit button after entering the source and target unit conversions

def submit():
    numerical_entry = ""
    student_unit_entry = ""
    acutal_value_label["text"] = ""
    
    numerical_entry = isNumeric_validation(numerical_value_entry)  ## numeric validation 
    student_unit_entry = isNumeric_validation(student_unit_of_response_entry) ## numeric validation
    temperatue_unit = ["kelvin","celsius","fahrenheit","rankine"] ## List of temperature units a user can select
    volume_unit = ["liters","tablespoons","cubic-inches","cups","cubic-feet","gallons"] ## List of volume units a user can select

    ## whenever a user enters the temperature or volumne units, the system automatically converts it to lower case and also removes spaces to avoid case sensitivity and checks against the list defined above
    
    unit_entry = unit_measure_entry.get().lower().strip()
    target_entry = target_measure_entry.get().lower().strip()

    ## Logic to define that Source and target unit conversions should be of the same type else it genereates the error " Invalid Unit of Measure" 
    if unit_entry in temperatue_unit:
        if target_entry not in temperatue_unit:
           display_value_label["text"] = 'Invalid Target Unit of Measure'
    elif unit_entry in volume_unit:
        if target_entry not in volume_unit:
           display_value_label["text"] = 'Invalid Target Unit of Measure'
    else:
        display_value_label["text"] = 'Invalid Input Unit of Measure'

    ## Dictionary that contains all the different combination of logical calculations for both temmperature and volume conversions
    
    dic = { "celsius":{"fahrenheit": float((numerical_entry * 1.8) + 32), "kelvin": float(numerical_entry + 273.15),"rankine":float((numerical_entry * 1.8) + 491.67)},
            "fahrenheit":{"celsius":float((numerical_entry-32) / 1.8),"Kevin": float((numerical_entry-32)* 1.8 + 273.15),"rankine":float(numerical_entry + 459.67)},
            "rankine":{"celsius":float((numerical_entry - 491.67)*(5/9)),"fahrenheit":float(numerical_entry - 459.67),"kelvin":float(numerical_entry * (5/9)) },
            "kelvin":{"celsius": float(numerical_entry - 273.15), "fahrenheit": float((numerical_entry - 273.15) * (9/5) +32),"rankine":float(numerical_entry * 1.8)},
            "liters":{"gallons": float(numerical_entry / 3.785), "cups": float(numerical_entry * 4.227),"tablespoons":float(numerical_entry * 67.628),"cubic-inches": float(numerical_entry * 61.024),"cubic-feet":float(numerical_entry / 28.317)},
            "gallons":{"liters": float(numerical_entry * 3.785), "cups": float(numerical_entry * 16),"tablespoons":float(numerical_entry * 256),"cubic-inches": float(numerical_entry * 231),"cubic-feet":float(numerical_entry / 7.481)},
            "cups":{"liters": float(numerical_entry / 4.227), "gallons": float(numerical_entry / 16),"tablespoons":float(numerical_entry * 16),"cubic-inches": float(numerical_entry * 14.438),"cubic-feet":float(numerical_entry / 120)},
            "tablespoons":{"liters": float(numerical_entry / 67.628), "gallons": float(numerical_entry / 256),"cups":float(numerical_entry / 16),"cubic-inches": float(numerical_entry / 1.108),"cubic-feet":float(numerical_entry / 1915)},
            "cubic-inches":{"liters": float(numerical_entry / 61.024), "gallons": float(numerical_entry / 231),"cups":float(numerical_entry / 14.438),"tablespoons": float(numerical_entry * 1.108),"cubic-feet":float(numerical_entry / 1728)},
            "cubic-feet":{"liters": float(numerical_entry * 28.317), "gallons": float(numerical_entry * 7.481),"cups":float(numerical_entry * 120),"tablespoons": float(numerical_entry * 1915.01),"cubic-inches":float(numerical_entry * 1728)}
        }
    for key,value in dic.items():
        if unit_entry == key:
            for key, value in value.items():
                if target_entry == key:
                    F = value
                    acutal_value_label["text"] = str(round(F,1))
                    display_value_label["text"] = 'Correct' if round(student_unit_entry,1) == round(F,1) else "Incorrect"  ## If student response matches to the actual result to the tenths place then system displays correct else incorrect
                    break

## defines all the labels and buttons for the GUI interface

label1 = Label(my_window, text="Input Numerical Value")
label2 = Label(my_window, text="Input Unit of Measure")
label3 = Label(my_window, text="Target Unit of Measure")
label4 = Label(my_window, text="Student's Unit of Response")
label5 = Label(my_window, text="Output")
label6 = Label(my_window, text="Correct Answer")
numerical_value_entry = Entry(my_window)
unit_measure_entry = Entry(my_window)
target_measure_entry = Entry(my_window)
student_unit_of_response_entry =Entry(my_window)
display_value_label = Label(my_window)
acutal_value_label = Label(my_window)
submit_button = Button(my_window,text="Submit",padx=30, pady=30,fg="blue",command=submit)

## defines the position of labels and button the application window
label1.grid(row=0,column=0)
numerical_value_entry.grid(row=0,column=1)
label2.grid(row=1,column=0)
unit_measure_entry.grid(row=1,column=1)
label3.grid(row=2,column=0)
target_measure_entry.grid(row=2,column=1)
label4.grid(row=3,column=0)
student_unit_of_response_entry.grid(row=3,column=1)
label5.grid(row=4,column=0)
display_value_label.grid(row=4,column=1)
label6.grid(row=5,column=0)
acutal_value_label.grid(row=5,column=1)
submit_button.grid(row=6,column=0)



my_window.mainloop()
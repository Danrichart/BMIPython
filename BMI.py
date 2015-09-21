from Tkinter import *

class App(Tk):
    def __init__(self):
        Tk.__init__(self)
        
app = App()
lblHeader = Label(app, text = "BMI Calculater")
lblHeader.grid(row=0, column=1, columnspan=2, padx=150, pady=10)

lblHeight = Label(app, text="Please enter the Height")
lblHeight.grid(row=1, column=1, columnspan=2, pady=10)


lblFeet = Label(app, text = "Feet:")
lblFeet.grid(row=2, column=0, columnspan=2)
txtFeet = Entry(app)
txtFeet.grid(row=2, column=1, columnspan=2)

lblInches = Label(app, text = "Inches:")
lblInches.grid(row=3, column=0, columnspan=2)
txtInches = Entry(app)
txtInches.grid(row=3, column=1, columnspan=2)

lblWeight = Label(app, text = "Please enter the Weight:")
lblWeight.grid(row=5, column=1, columnspan=2, pady=10)

lblLbs = Label(app, text = "Pounds:")
lblLbs.grid(row=6, column=0, columnspan=2)
txtWeight = Entry(app)
txtWeight.grid(row=6, column=1, columnspan=2)



btnCalculate = Button(app, text = "Calculate")
btnCalculate.grid(row=7, column=1, columnspan=2, pady=10)

lblOutput = Label(app, text = "")
lblOutput.grid(row=8, column=1, columnspan=2, pady=20)

def bmiCalculate():
    inches = (float(txtFeet.get()) * 12) + float(txtInches.get())
    weight = float(txtWeight.get()) 
    bmi = round(weight * 703 / inches**2, 2)

    if bmi >= 30:
        status = "Obese"
    elif bmi >= 25:
        status = "Overweight"
    elif bmi >= 18.51:
        status = "Normal"
    else:
        status = "Underweight"

    result = "BMI: " + str(bmi)
    result += "\n"
    result += "Status: " + str(status)
    
    
    lblOutput["text"] = result

btnCalculate["command"] = bmiCalculate

app.mainloop()

import tkinter as tk

LARGE_FONT_STYLE = ("Arial", 40, "bold")
SMALL_FONT_STYLE = ("Arial", 16)
LIGHT_BLUE = "#ADD8E6"
white = "#FFFFFF"
fg_color = "#ffcccb"
button_font = ("Arial", 24, "bold")
class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("700x700")
        self.window.resizable(0,0)
        self.window.title("Calculator")

        self.history = "" #for calculating history
        self.calculate = "" #for actual calculation

        self.display_frame = self.create_display_frame()

        self.history_label, self.label = self.create_display_labels()


        self.buttons_frame = self.create_display_frame()

        self.digits ={
            7: (1,1), 8: (1,2), 9: (1,3),
            4: (2, 1), 5: (2, 2), 6: (2, 3),
            1: (3, 1), 2: (3, 2), 3: (3, 3),
            0: (4, 2), '.':(4, 1)
        }
        self.calculations = {"/": "\u00F7", "*": "\u00D7", "-": "-", "+": "+"} #maps every operation to its equivelent in python

        self.buttons_frame.rowconfigure(0,weight=1)


        for x in range(1,5):
            self.buttons_frame.rowconfigure(x,weight=1)
            self.buttons_frame.columnconfigure(x, weight=1)
        self.create_digit_buttons()
        self.create_operator_buttons()
        self.create_C_button()
        self.create_calculate_button()


    def create_display_labels(self):
        history_label = tk.Label(self.display_frame, text=self.history, anchor=tk.E, bg=LIGHT_BLUE, fg="black", padx=24, font=SMALL_FONT_STYLE) #anchor makes the history be at the top or East of the window
        history_label.pack(expand=True, fill="both")


        label = tk.Label(self.display_frame, text=self.calculate, anchor=tk.E, bg=LIGHT_BLUE, fg="black", padx=24, font=LARGE_FONT_STYLE) #anchor makes the history be at the top or East of the window
        label.pack(expand=True, fill="both")

        return history_label, label

    def create_display_frame(self):
        frame = tk.Frame(self.window, height=221, bg=LIGHT_BLUE)
        frame.pack(expand=True, fill="both") #allows the frame to hide any empty space and expand to the full resolution
        return frame

    def create_digit_buttons(self):
        for digit,grid_value in self.digits.items():
            button = tk.Button(self.buttons_frame, text=str(digit), bg=white, fg="black", font=button_font, borderwidth=0, command=lambda x=digit: self.add_to_calculate(x))
            button.grid(row=grid_value[0], column=grid_value[1], sticky=tk.NSEW) #puts the buttons in a grid and sticks them to all sides

    def append_operator(self, calculations):
        self.calculate = self.calculate + calculations
        self.history = self.history + self.calculate
        self.calculate = ""
        self.update_history_label()
        self.update_label()

    def add_to_calculate(self, value):
        self.calculate = self.calculate + str(value)
        self.update_label()


    def create_operator_buttons(self):
        i=0
        for calculations, symbol in self.calculations.items():
            button = tk.Button(self.buttons_frame, text=symbol, bg="#FFDCD1", fg="black",
                               borderwidth=0, font=button_font, command=lambda y=calculations: self.append_operator(y))

            button.grid(row=i,column=4,sticky=tk.NSEW)
            i = i+1


    def evaluate(self): #finally
        self.history = self.history + self.calculate
        self.update_history_label()
        try:

            self.calculate = str(eval(self.history))
            self.history = ""
        except Exception as e:
            self.calculate = "Error, Can't do that!"
        finally:
            self.update_label()


        self.update_label()


    def clear(self):
        self.calculate = ""
        self.history = ""
        self.update_history_label()
        self.update_label()


    def create_C_button(self):
        for calculations,symbol in self.calculations.items():
            button = tk.Button(self.buttons_frame, text="C",
                               bg="#FFDCD1", fg="black", borderwidth=0, font=button_font, command=self.clear)
        button.grid(row=0, column=1, sticky=tk.NSEW, columnspan=3)



    def create_calculate_button(self):
        for calculations,symbol in self.calculations.items():
            button = tk.Button(self.buttons_frame, text="=", bg="#90EE90", fg="black",
                               borderwidth=0, font=button_font, command=self.evaluate)
        button.grid(row=4, column=3, sticky=tk.NSEW, columnspan=2)

    def create_buttons_frame(self):
        frame = tk.Frame(self.window)
        frame.pack(expand=True, fill="both")
        return frame

    def update_history_label(self):
        expression = self.history
        for calculations, symbol in self.calculations.items():
            expression = expression.replace(calculations, f' {symbol} ')
        self.history_label.config(text=expression)

    def update_label(self):
        self.label.config(text=self.calculate)



    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    calc = Calculator()
    calc.run()



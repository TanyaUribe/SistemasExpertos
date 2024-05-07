import random
import tkinter as tk
from tkinter import messagebox

class ClueSolverGUI:
    def __init__(self, master):
        self.master = master
        master.title("Clue Solver")

        self.suspects = ["Rojo", "Naranja", "Amarillo", "Verde", "Azul"]
        self.weapons = ["Candelabro", "Cuchillo", "Tubería", "Pistola", "Cuerda"]
        self.rooms = ["Cocina", "Sala", "Conservatorio", "Comedor", "Sótano"]
        self.num_trials = 5

        self.crime_scene = self.generate_random_combinations()

        self.label = tk.Label(master, text=f"La escena del crimen es: {self.crime_scene[0]} con {self.crime_scene[1]} en {self.crime_scene[2]}")
        self.label.pack()

        self.start_button = tk.Button(master, text="Comenzar investigación", command=self.start_investigation)
        self.start_button.pack()

        self.num_attempts = 0
        self.final_guess = []

    def generate_random_combinations(self):
        random_suspect = random.choice(self.suspects)
        random_weapon = random.choice(self.weapons)
        random_room = random.choice(self.rooms)
        return random_suspect, random_weapon, random_room

    def generate_testimony(self, category, choice):
        if category == "suspect":
            return choice, random.choice(self.weapons), random.choice(self.rooms)
        elif category == "weapon":
            return random.choice(self.suspects), choice, random.choice(self.rooms)
        elif category == "room":
            return random.choice(self.suspects), random.choice(self.weapons), choice

    def start_investigation(self):
        self.start_button.config(state=tk.DISABLED)
        self.label.config(text="¿Por cuál categoría le gustaría ver un testimonio?")

        self.category_var = tk.StringVar()
        self.category_var.set("suspect")

        self.category_menu = tk.OptionMenu(self.master, self.category_var, "suspect", "weapon", "room", command=self.show_options)
        self.category_menu.pack()

        self.options_frame = tk.Frame(self.master)
        self.options_frame.pack()

    def show_options(self, *args):
        if hasattr(self, "option_buttons"):
            for button in self.option_buttons:
                button.pack_forget()

        if self.num_attempts < self.num_trials:
            if self.category_var.get() == "suspect":
                options = self.suspects
            elif self.category_var.get() == "weapon":
                options = self.weapons
            elif self.category_var.get() == "room":
                options = self.rooms

            self.option_buttons = [tk.Button(self.options_frame, text=option, command=lambda o=option: self.show_testimony(o)) for option in options]
            for button in self.option_buttons:
                button.pack()
        else:
            self.show_final_guess()

    def show_testimony(self, option):
        category = self.category_var.get()
        self.label.config(text=f"Testimonio sobre {category}: {option}")
        testimony = self.generate_testimony(category, option)
        messagebox.showinfo("Testimonio", f"Testimonio: {testimony[0]} con {testimony[1]} en {testimony[2]}")

        self.num_attempts += 1
        self.final_guess.append((category, option))
        self.show_options()

    def show_final_guess(self):
        self.label.config(text="¿Cuál es su conclusión sobre la escena del crimen?")

        self.final_guess_frame = tk.Frame(self.master)
        self.final_guess_frame.pack()

        self.final_guess_vars = []
        for category in ("suspect", "weapon", "room"):
            var = tk.StringVar()
            self.final_guess_vars.append(var)
            label = tk.Label(self.final_guess_frame, text=f"Elija {category}:")
            label.pack()
            for option in getattr(self, f"{category}s"):
                rb = tk.Radiobutton(self.final_guess_frame, text=option, variable=var, value=option)
                rb.pack()

        submit_button = tk.Button(self.final_guess_frame, text="Enviar", command=self.check_final_guess)
        submit_button.pack()

    def check_final_guess(self):
        final_guess = [(category, var.get()) for category, var in zip(("suspect", "weapon", "room"), self.final_guess_vars)]
    
        is_correct = all(item in self.crime_scene for item in final_guess)
    
        if is_correct:
            messagebox.showinfo("Resultado", "¡Felicidades! Has resuelto el crimen.")
        else:
            messagebox.showinfo("Resultado", "Lo siento, tu respuesta no es correcta.")
  
root = tk.Tk()
app = ClueSolverGUI(root)
root.mainloop()


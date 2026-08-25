import tkinter as tk
from tkinter import ttk, messagebox


# -----------------------------
# Conversion function
# -----------------------------
def convert():
    try:
        value = float(input_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")
        return

    from_unit = from_unit_var.get()
    to_unit = to_unit_var.get()

    if from_unit == to_unit:
        result = value

    # Length
    elif from_unit == "Kilometers" and to_unit == "Miles":
        result = value * 0.621371

    elif from_unit == "Miles" and to_unit == "Kilometers":
        result = value * 1.60934

    elif from_unit == "Meters" and to_unit == "Feet":
        result = value * 3.28084

    elif from_unit == "Feet" and to_unit == "Meters":
        result = value * 0.3048

    elif from_unit == "Inches" and to_unit == "Centimeters":
        result = value * 2.54

    elif from_unit == "Centimeters" and to_unit == "Inches":
        result = value * 0.393701

    # Weight
    elif from_unit == "Pounds" and to_unit == "Kilograms":
        result = value * 0.453592

    elif from_unit == "Kilograms" and to_unit == "Pounds":
        result = value * 2.20462

    elif from_unit == "Grams" and to_unit == "Kilograms":
        result = value / 1000

    elif from_unit == "Kilograms" and to_unit == "Grams":
        result = value * 1000

    # Temperature
    elif from_unit == "Celsius" and to_unit == "Fahrenheit":
        result = (value * 9 / 5) + 32

    elif from_unit == "Fahrenheit" and to_unit == "Celsius":
        result = (value - 32) * 5 / 9

    elif from_unit == "Celsius" and to_unit == "Kelvin":
        result = value + 273.15

    elif from_unit == "Kelvin" and to_unit == "Celsius":
        result = value - 273.15

    elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
        result = (value - 32) * 5 / 9 + 273.15

    elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
        result = (value - 273.15) * 9 / 5 + 32

    else:
        messagebox.showerror(
            "Error",
            f"Conversion from {from_unit} to {to_unit} is not supported."
        )
        return

    result_label.config(
        text=f"{value} {from_unit} = {result:.4f} {to_unit}"
    )


# -----------------------------
# Main Window
# -----------------------------
root = tk.Tk()

root.title("Unit Converter")
root.geometry("450x400")
root.resizable(False, False)


# -----------------------------
# Title
# -----------------------------
title_label = tk.Label(
    root,
    text="Unit Converter",
    font=("Arial", 22, "bold")
)

title_label.pack(pady=20)


# -----------------------------
# Value input
# -----------------------------
input_label = tk.Label(
    root,
    text="Enter Value:",
    font=("Arial", 12)
)

input_label.pack()

input_entry = tk.Entry(
    root,
    font=("Arial", 14),
    width=20
)

input_entry.pack(pady=10)


# -----------------------------
# From Unit
# -----------------------------
from_label = tk.Label(
    root,
    text="From:",
    font=("Arial", 12)
)

from_label.pack()

units = [
    "Kilometers",
    "Miles",
    "Meters",
    "Feet",
    "Inches",
    "Centimeters",
    "Pounds",
    "Kilograms",
    "Grams",
    "Celsius",
    "Fahrenheit",
    "Kelvin"
]

from_unit_var = tk.StringVar()
from_unit_var.set("Kilometers")

from_dropdown = ttk.Combobox(
    root,
    textvariable=from_unit_var,
    values=units,
    state="readonly",
    width=20
)

from_dropdown.pack(pady=5)


# -----------------------------
# To Unit
# -----------------------------
to_label = tk.Label(
    root,
    text="To:",
    font=("Arial", 12)
)

to_label.pack()

to_unit_var = tk.StringVar()
to_unit_var.set("Miles")

to_dropdown = ttk.Combobox(
    root,
    textvariable=to_unit_var,
    values=units,
    state="readonly",
    width=20
)

to_dropdown.pack(pady=5)


# -----------------------------
# Convert Button
# -----------------------------
convert_button = tk.Button(
    root,
    text="Convert",
    command=convert,
    font=("Arial", 12, "bold"),
    width=15
)

convert_button.pack(pady=20)


# -----------------------------
# Result
# -----------------------------
result_label = tk.Label(
    root,
    text="Result will appear here",
    font=("Arial", 13, "bold")
)

result_label.pack(pady=10)


# -----------------------------
# Start application
# -----------------------------
root.mainloop()
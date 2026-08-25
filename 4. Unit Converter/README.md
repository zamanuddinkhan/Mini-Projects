# Unit Converter

A simple **Unit Converter desktop application** built using **Python and Tkinter**.

This project allows users to convert values between different units of **length, weight, time, and temperature** through a simple graphical user interface.

## Features

* Convert length units
* Convert weight units
* Convert time units
* Convert temperature units
* User-friendly Tkinter GUI
* Input validation
* Error messages for invalid conversions
* Clear button to reset the application
* Supports conversions in both directions

## Supported Units

### Length

* Kilometers
* Meters
* Centimeters
* Millimeters
* Miles
* Yards
* Feet
* Inches

### Weight

* Kilograms
* Grams
* Milligrams
* Pounds
* Ounces

### Time

* Seconds
* Minutes
* Hours
* Days

### Temperature

* Celsius
* Fahrenheit
* Kelvin

## Technologies Used

* **Python 3**
* **Tkinter**
* **ttk**
* **messagebox**

Tkinter is included with most standard Python installations, so no external Python packages are required.

## How It Works

The application uses a graphical interface created with Tkinter.

The user:

1. Enters a value.
2. Selects the unit to convert from.
3. Selects the unit to convert to.
4. Clicks the **Convert** button.
5. The converted value is displayed on the screen.

For length, weight, and time, the program first converts the input into a **base unit** and then converts the base unit into the selected target unit.

## Temperature Conversion

Temperature conversion is handled separately because it requires formulas rather than a simple multiplication factor.

### Celsius to Fahrenheit

```text
F = (C × 9/5) + 32
```

### Fahrenheit to Celsius

```text
C = (F - 32) × 5/9
```

### Celsius to Kelvin

```text
K = C + 273.15
```

### Kelvin to Celsius

```text
C = K - 273.15
```

The program also supports Fahrenheit ↔ Kelvin conversions.

## Error Handling

The application handles invalid numeric input.

For example, if the user enters:

```text
abc
```

the application displays:

```text
Please enter a valid number.
```

The application also prevents conversions between incompatible categories, such as:

```text
Kilometers → Kilograms
```

and displays:

```text
These units cannot be converted.
```
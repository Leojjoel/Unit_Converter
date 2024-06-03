import tkinter as tk

selected_quantity = None

def select_quantity():
    global selected_quantity
    selected_quantity = quantity_var.get()
    create_converter_interface(selected_quantity)

def convert():
    from_unit = from_unit_var.get()
    to_unit = to_unit_var.get()
    value = float(value_entry.get())

    result = None
    if selected_quantity == "Length":
        result = convert_length(from_unit, to_unit, value)
    elif selected_quantity == "Mass":
        result = convert_mass(from_unit, to_unit, value)
    elif selected_quantity == "Time":
        result = convert_time(from_unit, to_unit, value)
    elif selected_quantity == "Temperature":
        result = convert_temperature(from_unit, to_unit, value)

    if result is not None:
        result_label.config(text=f"{value} {from_unit} = {result} {to_unit}")

def convert_length(from_unit, to_unit, value):
    conversions = {
        "Centimetre": 0.00001,
        "Metre": 0.001,
        "Kilometre": 1
    }
    result = value * conversions[from_unit] / conversions[to_unit]
    return "{:.6f}".format(result)

def convert_mass(from_unit, to_unit, value):
    conversions = {
        "Milligram": 0.000001,
        "Gram": 0.001,
        "Kilogram": 1
    }
    result = value * conversions[from_unit] / conversions[to_unit]
    return "{:.6f}".format(result)

def convert_time(from_unit, to_unit, value):
    conversions = {
        "Second": 1/3600,
        "Minute": 1 / 60,
        "Hour": 1
    }
    return value * conversions[from_unit] / conversions[to_unit]

def convert_temperature(from_unit, to_unit, value):
    if from_unit == "Celsius":
        if to_unit == "Fahrenheit":
            return (value * 9/5) + 32
        elif to_unit == "Kelvin":
            return value + 273.15
    elif from_unit == "Fahrenheit":
        if to_unit == "Celsius":
            return (value - 32) * 5/9
        elif to_unit == "Kelvin":
            return (value + 459.67) * 5/9
    elif from_unit == "Kelvin":
        if to_unit == "Celsius":
            return value - 273.15
        elif to_unit == "Fahrenheit":
            return (value * 9/5) - 459.67

def create_converter_interface(selected_quantity):
    global from_unit_var, to_unit_var, value_entry, result_label

    units = {
        "Length": ["Centimetre", "Metre", "Kilometre"],
        "Mass": ["Milligram", "Gram", "Kilogram"],
        "Time": ["Second", "Minute", "Hour"],
        "Temperature": ["Celsius", "Fahrenheit", "Kelvin"]
    }

    from_unit_var = tk.StringVar(root)
    from_unit_var.set(units[selected_quantity][0])

    from_unit_label = tk.Label(root, text="From:", padx=10, pady=5, fg="blue")
    from_unit_label.grid(row=2, column=0, sticky="e")

    from_unit_menu = tk.OptionMenu(root, from_unit_var, *units[selected_quantity])
    from_unit_menu.grid(row=2, column=1, padx=10, pady=5)

    to_unit_var = tk.StringVar(root)
    to_unit_var.set(units[selected_quantity][1])

    to_unit_label = tk.Label(root, text="To:", padx=10, pady=5, fg="blue")
    to_unit_label.grid(row=3, column=0, sticky="e")

    to_unit_menu = tk.OptionMenu(root, to_unit_var, *units[selected_quantity])
    to_unit_menu.grid(row=3, column=1, padx=10, pady=5)

    value_label = tk.Label(root, text="Value:", padx=10, pady=5, fg="blue")
    value_label.grid(row=4, column=0, sticky="e")

    value_entry = tk.Entry(root)
    value_entry.grid(row=4, column=1, padx=10, pady=5)

    convert_button = tk.Button(root, text="Convert", command=convert, bg="green", fg="white")
    convert_button.grid(row=5, columnspan=2, padx=10, pady=5)

    global result_label
    result_label = tk.Label(root, text="", padx=10, pady=5, fg="red")
    result_label.grid(row=6, columnspan=2)

root = tk.Tk()
root.title("Unit Converter")

quantity_var = tk.StringVar(root)
quantity_var.set("Length")

quantity_label = tk.Label(root, text="Select Quantity:", padx=10, pady=5, fg="blue")
quantity_label.grid(row=0, column=0, sticky="e")

quantity_menu = tk.OptionMenu(root, quantity_var, "Length", "Mass", "Time", "Temperature")
quantity_menu.grid(row=0, column=1, padx=10, pady=5)

select_button = tk.Button(root, text="Select", command=select_quantity, bg="green", fg="white")
select_button.grid(row=1, columnspan=2, padx=10, pady=5)

root.mainloop()
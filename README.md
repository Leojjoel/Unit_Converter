# Desktop Unit Converter

A lightweight, intuitive desktop application built in Python using the **Tkinter** library. This application provides a graphical user interface (GUI) to seamlessly convert units across various measurement categories in real-time.

---

## Features

* **Dynamic Interface:** The UI dynamically adapts its unit selections based on the physical quantity you choose.
* **Precision Output:** Length and Mass conversions are accurately calculated up to 6 decimal places.
* **Diverse Categories:** Supports 4 major types of measurement calculations.
* **User-Friendly Design:** Clear color-coded labels and dropdown menus for effortless navigation.

---

## Supported Conversions

The application currently supports the following quantities and units:

| Category | Supported Units |
| --- | --- |
| **Length** | Centimetre, Metre, Kilometre |
| **Mass** | Milligram, Gram, Kilogram |
| **Time** | Second, Minute, Hour |
| **Temperature** | Celsius, Fahrenheit, Kelvin |

---

## Installation & Setup

### Prerequisites

* **Python 3.x** must be installed on your system.
* `tkinter` is built into the standard Python library, so no external package installations (like `pip`) are required.

### Steps to Run

1. **Clone the repository:**
```bash
git clone https://github.com/your-username/unit-converter-tkinter.git
cd unit-converter-tkinter

```


2. **Save the code:** Ensure your code is saved in a file named `main.py` (or preferred name).
3. **Launch the application:**
```bash
python main.py

```



---

## How to Use

1. Launch the app and select your desired category (e.g., *Length*, *Temperature*) from the **Select Quantity** dropdown menu.
2. Click the **Select** button to generate the specific converter interface.
3. Choose the target units in the **From** and **To** dropdown menus.
4. Input the numerical value you want to convert into the **Value** entry box.
5. Click **Convert** to view the computed result highlighted at the bottom.

> **Note:** If you switch categories mid-session, make sure to click the **Select** button again to update the available unit choices.

---

# Qr-Code-Generator-using-python

 # QR Code Generator

This repository contains a Python script for generating QR codes using the `qrcode` library. The script demonstrates how to create a QR code that links to a specific URL or displays plain text when scanned. The QR code is saved as an image file.

---

## Features

- Generates QR codes for URLs, text, or any other data.
- Customizable QR code:
  - **Version**: Controls the size of the QR code matrix.
  - **Box size**: Adjusts the size of each square in the QR code.
  - **Border**: Adds padding around the QR code.
- Saves the QR code image in `.png` format with customizable colors.

---

## Script Overview

### **Dependencies**
- `qrcode`: For generating QR codes.
- `image`: For handling image operations.

### **Steps in the Script**
1. **QR Code Initialization**:
   The `QRCode` object is initialized with customizable parameters such as `version`, `box_size`, and `border`.

2. **Adding Data**:
   Data for the QR code is added using `qr.add_data(data)`. In this example, the data is a GitHub link:  
   `https://github.com/anvesh741`

3. **Generating the Image**:
   The QR code is converted into an image using `qr.make_image(fill="black", back_color="white")`.

4. **Saving the Image**:
   The generated QR code image is saved as `github.png`.

---

## Installation

To run this script, you need to have Python installed along with the required libraries.

### **1. Install Python**
Download and install Python from the [official Python website](https://www.python.org/).

### **2. Install Required Libraries**
Run the following commands in your terminal or command prompt:
```bash
pip install qrcode
pip install image


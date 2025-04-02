import win32print
import win32ui
import win32con
from PIL import Image, ImageDraw, ImageFont
import os

def print_label(text1, text2, text3, barcode_data, printer_name=None):
    # If no printer specified, use default
    if printer_name is None:
        printer_name = win32print.GetDefaultPrinter()
    
    print(f"Using printer: {printer_name}")
    
    try:
        # Create a device context for the printer
        hDC = win32ui.CreateDC()
        hDC.CreatePrinterDC(printer_name)
        
        # Start a new document
        hDC.StartDoc("Label Document")
        hDC.StartPage()
        
        # Set the mapping mode to device units (pixels)
        hDC.SetMapMode(win32con.MM_TEXT)
        
        # Create fonts
        title_font = win32ui.CreateFont({
            "name": "Arial",
            "height": 36,
            "weight": 700  # Bold
        })
        
        normal_font = win32ui.CreateFont({
            "name": "Arial",
            "height": 28,
            "weight": 400  # Normal
        })
        
        barcode_font = win32ui.CreateFont({
            "name": "Arial",
            "height": 24,
            "weight": 700  # Bold
        })
        
        # Draw the text lines
        hDC.SelectObject(title_font)
        hDC.TextOut(100, 50, text1)  # Title/name at the top
        
        hDC.SelectObject(normal_font)
        hDC.TextOut(100, 100, text2)  # Second line
        hDC.TextOut(100, 140, text3)  # Third line
        
        # Draw barcode data as text
        hDC.SelectObject(barcode_font)
        hDC.TextOut(100, 200, f"*{barcode_data}*")  # Using asterisks to indicate barcode
        
        # End the page and document
        hDC.EndPage()
        hDC.EndDoc()
        
        print("Print job sent successfully")
        
    except Exception as e:
        print(f"Error: {e}")
        
    finally:
        # Delete the device context to free resources
        if 'hDC' in locals():
            hDC.DeleteDC()

# Example usage
print_label(
    "John Doe",              # Name/title
    "ID: 12345",             # Second line
    "Department: IT",        # Third line
    "123456789012"           # Barcode data
)
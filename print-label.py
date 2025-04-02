import win32print
import win32ui
import win32con

# Get the default printer
printer_name = win32print.GetDefaultPrinter()
print(f"Using printer: {printer_name}")

try:
    # Create a device context for the printer
    hDC = win32ui.CreateDC()
    hDC.CreatePrinterDC(printer_name)
    
    # Start a new document
    hDC.StartDoc("Test Document")
    hDC.StartPage()
    
    # Set the mapping mode to device units (pixels)
    hDC.SetMapMode(win32con.MM_TEXT)
    
    # Create a font
    font = win32ui.CreateFont({
        "name": "Arial",
        "height": 36,  # Larger font size
        "weight": 700  # Bold
    })
    
    # Select the font into the device context
    old_font = hDC.SelectObject(font)
    
    # Draw multiple lines of text with proper positioning
    """hDC.TextOut(100, 100, "Line 1: Test Print")
    hDC.TextOut(100, 150, "Line 2: Python Label")
    hDC.TextOut(100, 200, "Line 3: Additional Info")
    hDC.TextOut(300, 200, "Line 4: Additional Info")"""

    hDC.TextOut(0, 100, "Line 1: Test Print")
    hDC.TextOut(200, 10, "Line 2: Python Label")
    hDC.TextOut(300, 20, "Line 3: Additional Info")
    hDC.TextOut(40, 30, "Line 4: Additional Info")
    
    # Restore the old font
    hDC.SelectObject(old_font)
    
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
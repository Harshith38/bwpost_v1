import win32print
import win32api

def print_zebra_label(name, id_number, department, barcode_data, printer_name=None):
    # If no printer specified, use default
    if printer_name is None:
        printer_name = win32print.GetDefaultPrinter()
    
    print(f"Using printer: {printer_name}")
    
    # Get printer information to find the port
    printer_info = win32print.GetPrinter(win32print.OpenPrinter(printer_name), 2)
    port_name = printer_info['pPortName']
    print(f"Printer port: {port_name}")
    
    # Create ZPL code for the label with proper positioning
    zpl_code = f"""
^XA

^CF0,30
^FO50,50^FD{name}^FS
^FO50,100^FD{id_number}^FS
^FO50,150^FD{department}^FS

^FO50,200^BY3
^BCN,100,Y,N,N
^FD{barcode_data}^FS

^XZ
"""
    
    try:
        # Method 1: Try direct file write to printer port
        try:
            print(f"Attempting to write directly to port {port_name}")
            with open(port_name, 'w') as f:
                f.write(zpl_code)
                print("Print job sent via direct port write")
                return
        except Exception as e:
            print(f"Direct port write failed: {e}")
        
        # Method 2: Use Windows API
        print("Trying Windows API method...")
        handle = win32print.OpenPrinter(printer_name)
        try:
            job = win32print.StartDocPrinter(handle, 1, ("Zebra Label", None, "RAW"))
            try:
                win32print.StartPagePrinter(handle)
                win32print.WritePrinter(handle, bytes(zpl_code, "utf-8"))
                win32print.EndPagePrinter(handle)
                print("Print job sent via Windows API")
            finally:
                win32print.EndDocPrinter(handle)
        finally:
            win32print.ClosePrinter(handle)
            
    except Exception as e:
        print(f"Error: {e}")
        
        # Method 3: Last resort - try using ShellExecute with a temporary file
        try:
            print("Trying ShellExecute method...")
            temp_file = "C:\\Users\\Hari\\Documents\\Excel\\python\\bwpost_v1\\label.zpl"
            with open(temp_file, 'w') as f:
                f.write(zpl_code)
            
            win32api.ShellExecute(0, "print", temp_file, None, ".", 0)
            print(f"Print job sent via ShellExecute to {temp_file}")
        except Exception as e:
            print(f"ShellExecute method failed: {e}")

# Example usage
print_zebra_label(
    "John Doe",          # Name
    "ID: 12345",         # ID number
    "Department: IT",    # Department
    "123456789012"       # Barcode data
)
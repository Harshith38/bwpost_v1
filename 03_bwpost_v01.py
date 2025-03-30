import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd

import os



class TrennkarteErstellen:
    def __init__(self, root):
        self.root = root
        self.root.title("Trennkarte Erstellen")
        self.root.geometry("1160x370")
        self.font_name = 'Helvetica'
        #root.configure(bg="red")
        

        self.kunde_data = None
        self.current_customer= None
        self.previous_customer=None


        self.kundendaten_laden()

        self.scan_rahmen_erstellen()
        self.display_rahmen_erstellen()
        self.weitere_labels()
        
        self.kunde_nummer.focus_set()


    def kundendaten_laden(self):
        """
        Ladung von Kundendaten von Excel
         """
        
        try:
            self.kunde_data = pd.read_excel('customer_database.xlsx')
            print(f"{len(self.kunde_data)} Kundendaten geladen")
            if not self.kunde_data.empty:
                print(f"First customer: ID={self.kunde_data.iloc[0]['ID']}, Name={self.kunde_data.iloc[0]['CustomerName']}")
        except Exception as e:
            messagebox.showerror("Fehler", f"Kundendaten konnten nicht geladen werden: {str(e)}")
            self.kunde_data = pd.DataFrame(columns=['ID', 'CustomerName'])

    def scan_rahmen_erstellen(self):
        """Frame zum Scannen von Barcodes erstellen"""
        """scan_rahmen = ttk.LabelFrame(self.root, text="Kunde einlesen")
        scan_rahmen.pack(padx=10, pady=10, fill="x")

        ttk.Label(scan_rahmen, text="Kundenummer eingeben:").pack(side=tk.LEFT, padx=5)

        self.scan_eingabe = ttk.Entry(scan_rahmen, width=30)
        self.scan_eingabe.pack(side=tk.LEFT, padx=5)
        #self.scan_eingabe.bind("<Return>", self.process_scan)
        #self.scan_eingabe.bind("<Return>", self.process_scan)

        #ttk.Button(scan_rahmen, text="OK", command=self.process_scan).pack(side=tk.LEFT, padx=5)
        ttk.Button(scan_rahmen, text="OK").pack(side=tk.LEFT, padx=5)"""

        self.content1 = ttk.Frame(self.root, padding=(13))#, style='My.TFrame')
        #scan_frame = ttk.LabelFrame(root, text="Scan Barcode")
        self.kunde_einlesen = ttk.Label(self.content1, text="Kunde einlesen oder\nweitere Labels drucken:" ,font=(self.font_name, 13), background="white")
        self.kunde_nummer = ttk.Entry(self.content1,width=18,font=(self.font_name, 16))
        self.kunde_nummer.bind('<Return>', self.process_scan)

        self.frame1 = ttk.Frame(self.content1, width=200, height=150)#, style='My.TFrame')
        # Status message
        #self.status_frame = ttk.Frame(self.frame1)
        #status_frame.pack(fill="x", padx=5, pady=5)
        self.status_label = ttk.Label(self.frame1, text="Ready to scan", background="light green",
                                      font=("Arial", 10),
                                      wraplength=200)
        self.status_label.grid(column=0, row=0,pady=20)
        #self.status_label.pack(side=tk.LEFT, padx=10)
    

        self.content4 = ttk.Frame(self.content1)
        #content4 = ttk.LabelFrame(root, text="info")
        self.destop_name = ttk.Label(self.content4, text="name of destop", font=(self.font_name, 10), background="white")
        self.date_time = ttk.Label(self.content4, text="current time", font=(self.font_name, 10))
        self.last_update = ttk.Label(self.content4, text="Letztes Update: ",  font=(self.font_name, 10))

        self.content1.grid(column=0, row=0, padx=20, pady=20)#, sticky=(N, E))
        self.kunde_einlesen.grid(column=0, row=0)#, columnspan=2)
        self.kunde_nummer.grid(column=0, row=1,pady=10)#, columnspan=2)

        self.frame1.grid(column=0, row=2)
        self.content4.grid(column=0, row=3, sticky=("N"))#, pady=4)
        """destop_name.grid(column=0, row=3)
        date_time.grid(column=0, row=4)
        last_update.grid(column=0, row=5)"""
        self.destop_name.grid(column=0, row=0)
        self.date_time.grid(column=1, row=0)
        self.last_update.grid(column=0, row=2)

    def display_rahmen_erstellen(self):
        # middle section- customer info, OK and cancel buttons

        self.content2= ttk.Frame(self.root, style='My.TFrame')
        self.frame2 = ttk.Frame(self.content2, borderwidth=5, relief="ridge", width=600, height = 260)
        
        #maintaing frame size
        self.frame2.grid_propagate(False)
        
        # Current customer
        current_frame = ttk.Frame(self.frame2)
        current_frame.grid(column=0, row=0)
        #current_frame.pack(fill="x", padx=5, pady=5)
        #self.current_customer_nummer = ttk.Label(current_frame, text="0000", font=("Roboto Mono", 12, "bold"), anchor= "w")#.pack(side=tk.LEFT)
        #self.current_customer_nummer.grid(column=0, row=0)
        self.current_customer_label = ttk.Label(current_frame, text="None",
                                                font=("Roboto Mono", 14, "bold"),
                                                wraplength=550,
                                                width=50, 
                                                anchor= "w")
        
        self.current_customer_label.grid(column=0, row=1)
        #self.current_customer_label.pack(side=tk.LEFT, padx=10)
        
        # Previous customer
        previous_frame = ttk.Frame(self.frame2)
        previous_frame.grid(column=0, row=1)
        #previous_frame.pack(fill="x", padx=5, pady=5)
        #self.previous_customer_nummer = ttk.Label(previous_frame, text="0000", font=("Arial", 12), anchor="w")#.pack(side=tk.LEFT)
        #self.previous_customer_nummer.grid(column=0, row=1)
        self.previous_customer_label = ttk.Label(previous_frame, text="None",
                                                font=("Roboto Mono", 12),
                                                wraplength=400,
                                                width=60, 
                                                anchor= "w")
        self.previous_customer_label.grid(column=0, row=2, pady=30)
        #self.previous_customer_label.pack(side=tk.LEFT, padx=10)


        self.ok = ttk.Button(self.content2, text="OK", command=self.process_scan, padding=(20))

        self.update = ttk.Button(self.content2, text="Update", padding=(20))

        self.content2.grid(column=1, row=0)
        self.frame2.grid(column=1, row=0, columnspan=2)
        self.ok.grid(column=1, row=1,pady=10)
        self.update.grid(column=2, row=1)

    def weitere_labels(self):
                
        #right section- print extra labels

        self.content3 = ttk.Frame(self.root, style='My.TFrame')
        #content3 = ttk.LabelFrame(root, text="Weitere Labels drucken:")
        self.print_labels= ttk.Label(self.content3, text="Weitere Labels drucken:", font=(self.font_name, 10))
        self.one_button = ttk.Button(self.content3, text="1", padding=15)
        self.two_button = ttk.Button(self.content3, text="2", padding=15)
        self.three_button = ttk.Button(self.content3, text="3", padding=15)
        self.four_button = ttk.Button(self.content3, text="4", padding=15)
        self.five_button = ttk.Button(self.content3, text="5", padding=15)
        self.six_button = ttk.Button(self.content3, text="6", padding=15)
        """
        content3.grid(column=2, row=0,sticky=(N,E,W,S), padx=50, pady=15)#, sticky=(N,W))
        print_labels.grid(column=0,row=0)#, columnspan=2)
        one_button.grid(column=0, row=1, padx= 0, pady=17)
        two_button.grid(column=1, row=1,padx= 0)
        three_button.grid(column=0, row=2, padx= 0, pady=17)
        four_button.grid(column=1, row=2,padx= 0)
        five_button.grid(column=0, row=3,padx= 0)
        six_button.grid(column=1, row=3, padx= 0, pady=17)
        """
        self.content3.grid(column=2, row=0,sticky=("N,E,W,S"), padx=10, pady=15)#, sticky=(N,W))
        self.print_labels.grid(column=0,row=0, columnspan=2, sticky="W")
        self.one_button.grid(column=0, row=1, sticky="W")
        self.two_button.grid(column=1, row=1,sticky="W", padx=15, pady=15)
        self.three_button.grid(column=0, row=2, sticky="W")
        self.four_button.grid(column=1, row=2,sticky="W", padx=15, pady=15)
        self.five_button.grid(column=0, row=3,sticky="W")
        self.six_button.grid(column=1, row=3,sticky="W", padx=15, pady=15)

    def process_scan(self, event=None):
        """Process the barcode scan"""
        barcode_value = self.kunde_nummer.get().strip()
        print(f"DEBUG: Scanned barcode value: '{barcode_value}', type: {type(barcode_value)}")
        self.kunde_nummer.delete(0, tk.END)
        
        if not barcode_value:
            self.status_label.config(text="Please scan a barcode")
            return
        
        # Check if we're in verification mode
        if hasattr(self, 'verification_mode') and self.verification_mode:
            self.verify_label(barcode_value)
            return
        
        # Find customer by barcode
        if self.kunde_data is not None:
            customer_match = self.kunde_data[self.kunde_data['ID'].astype(str) == barcode_value]
            if not customer_match.empty:
                # Update previous customer
                if self.current_customer:
                    self.previous_customer = self.current_customer
                    self.previous_customer_label.config(text=self.previous_customer)
                
                # Update current customer
                #self.current_customer_num = customer_match.iloc[0]['ID']
                self.current_customer = customer_match.iloc[0]['CustomerName']
                #self.current_customer_nummer.config(text=self.current_customer_num)
                self.current_customer_label.config(text=self.current_customer)
                
                # Print label
                #self.print_label(barcode_value, self.current_customer)
                
                # Enable verification mode
                self.verification_mode = True
                self.status_label.config(text="Scan the printed label to verify")
                self.status_label.config(background="Yellow")
                self.status_label.config(foreground="black")
            else:
                self.status_label.config(text=f"No customer found for barcode: {barcode_value}")
        else:
            self.status_label.config(text="Customer data not loaded")
    
    def verify_label(self, barcode_value):
        """Verify the printed label"""
        # Find customer by barcode
        if self.kunde_data is not None:
            customer_match = self.kunde_data[self.kunde_data['ID'].astype(str) == barcode_value]
            if not customer_match.empty:
                verified_customer = customer_match.iloc[0]['CustomerName']
                if verified_customer == self.current_customer:
                    self.status_label.config(text="Verification successful! Ready for next scan.")
                    self.status_label.config(background="Green")
                    self.status_label.config(foreground="White")
                    self.verification_mode = False
                else:
                    self.status_label.config(text="Verification failed! Customer mismatch.")
                    self.status_label.config(background="Red")
                    self.status_label.config(foreground="White")
            else:
                self.status_label.config(text=f"No customer found for barcode: {barcode_value}")
        else:
            self.status_label.config(text="Customer data not loaded")
    

if __name__ == "__main__":
    root = tk.Tk()
    app = TrennkarteErstellen(root)
    root.mainloop()

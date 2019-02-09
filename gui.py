from tkinter import *
from data import data_pull
import time
from error_handler import Error_Handler
from datastore import insertData
from encryption import encrypt_private_key, generate_keys
from alert_system import page_doctor

private_key, pub_key = generate_keys()

# Time intervals for retrieving data
hr_interval = 5
bp_interval = 5
bo_interval = 5

min_int = 5

# Run the UI
def runUI():

    window = Tk()
    
    hr = IntVar()
    bp = IntVar()
    bo = IntVar()

    window.title("EC500 Health Monitor System")
    
    label1 = Label(window, text='Heart Rate')
    label1.grid(row=0, column=0)

    textBox1 = Label(window, height=2, width=10, textvariable = hr)
    textBox1.grid(row=1, column=0)
    
    label2 = Label(window, text='Blood Pressure')
    label2.grid(row=0, column=1)

    textBox2 = Label(window, height=2, width=10, textvariable = bp)
    textBox2.grid(row=1, column=1)

    label3 = Label(window, text='Blood Oxygen')
    label3.grid(row=0, column=2)

    textBox3 = Label(window, height=2, width=10, textvariable = bo)
    textBox3.grid(row=1, column=2)
    
    def dataLoop():
        mainLoop(hr, bp, bo)
        window.after(min_int * 1000, dataLoop)
    
    window.after(min_int * 1000, dataLoop)

    window.mainloop()

# Grab data
# Send to UI
# Attempt to encrypt data
# Store (theoretically encrypted) data
# Handle errors
def mainLoop(hr, bp, bo):
    min_int = min(hr_interval, bp_interval, bo_interval)
    data_obj = data_pull()
    hr.set(data_obj.get("heart_rate"))
    bp.set(data_obj.get("blood_pressure1"))
    bo.set(data_obj.get("blood_oxygen"))

    ##data encryption
    #encrypted_message = encrypt_private_key(data_obj.get("heart_rate"), private_key)

    ##data storage
    #insertData(1, encrypted_message)
    insertData(1, data_obj.get("heart_rate"))
    insertData(1, data_obj.get("blood_pressure1"))
    insertData(1, data_obj.get("blood_pressure2"))
    insertData(1, data_obj.get("blood_oxygen"))

    #error handling
    page_doctor(data_obj, 0x01, Error_Handler(data_obj))

def main():
    runUI()

if __name__ == "__main__":
    main()

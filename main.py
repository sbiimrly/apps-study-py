import sqlite3
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from ttkbootstrap import style

#Create database tables if they dont exist
def create_tables(conn):
    cursor = conn.cursor()

    #Create flashcards_sets table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS flaschcard_sets (
                  id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name TEXT NOT NULL
         )
    ''')

    #Create flashcards table with foreign key reference to flashcard_Sets
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS flashcards (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   SET_ID integer not null,
                   word TEXT NOT NULL,
                   definition TEXT NOT NULL,
                   FOREIGN KEY (set_id) REFERENCES flashcard_sets(id)
        )
    ''')

    #Add a new flashcards set to the database
    def add_set(conn, name):
        cursor = conn.curosr()

        #Insert the set name into flashcard_sets table
        cursor.execute('''
            INSERT INTO flashcard_sets (name)
            VALUE (?)
    ''', (name,))
        
        set_id = cursor.lastrowid
        conn.commit()

        return set_id

#function to add a flashcard to the database
def add_card(conn, set_id, word, definiton):
    cursor = conn.cursor()

    #Execute SQL query to insert a new flasgcard into the databse
    cursor.execute('''
        INSERT INTO flashcards (set_id, word, definiton)
        VALUES (?, ?, ?)
    ''', (set_id, word, definiton))

    #GET the ID of the newly inserted card
    card_id = cursor.lastrowid
    conn.commit()

    return card_id

#Function to retrieve all flashcard sets from the database

if __name__ == '__main__':
    #Connect to the SQLite database and create tables
    conn = sqlite3.connect('flashcards.db')
    create_tables(conn)

    #Crate the main GUI window
    root =tk.Tk()
    root.title('Flashcards App')
    root.geometry('500x400')

    #Apply styling to the GUI elements
    style = ttk.Style()
    style.configure('Tlabel', font=('TkDefaultFont,18'))
    style.configure('TButton', font=('TkDefaultFont,16'))

    #Set up variables for storing user input
    set_name_var = tk.StringVar()
    word_var = tk.StringVar()
    definition_var = tk.StringVar()

    #Create a notebook widget to manage tabs
    notebook = ttk.Notebook(root)
    notebook.pack(fill='both', expand=True)

    #Crate the "Crate Set" tab and its content
    create_set_frame = ttk.Frame(notebook)
    notebook.add(create_set_frame, text="Create Set")


    #Lable and Entry widgets for entering set name, word and definition
    ttk.Label(create_set_frame, text='Set Name:').pack(padx=5, pady=5)
    ttk.Entry(create_set_frame, textvariable=set_name_var, width=30).pack(padx=5, pady=5)

    ttk.Label(create_set_frame, text='Word:').pack(padx=5, pady=5)
    ttk.Entry(create_set_frame, textvariable=word_var, width=30).pack(padx=5, pady=5)

    ttk.Label(create_set_frame, text='Definiton:').pack(padx=5, pady=5)
    ttk.Entry(create_set_frame, textvariable=definition_var, width=30).pack(padx=5, pady=5)

    #Button to add a word to the set (command=add_word) +> for the next part
    ttk.Button(create_set_frame, text='Add Word').pack(padx=5, pady=10)

    #Button to save the set (command=create_set)
    ttk.Button(create_set_frame, text='Save Set').pack(padx=5, pady=10)

    #Create the "Select Set" tab and its content
    select_set_frame = ttk.Frame(notebook)
    notebook.add(select_set_frame, text="Select Set")

    # Combobox widget for selecting existing flashcard sets
    sets_combobox = ttk.Combobox(select_set_frame, state='readonly')
    sets_combobox.pack(padx=5, pady=40)

    #Button to select a set (command=select_set)
    ttk.Button(select_set_frame, text="Select Set").pack(padx=5, pady=5)
    
    #Button to delete a set (command=delete_select_set)
    ttk.Button(select_set_frame, text="Delete Set").pack(padx=5, pady=5)

    #Create the "Learn Mode" tab and its content
    flashcards_frame = ttk.Frame(notebook)
    notebook.add(flashcards_frame, text='Learn Mode')

    # Initialize varianles for tracking card index and current cards
    card_index = 0
    currents_tabs = []

    #Label to display the word on flaschcards
    word_label = tk.Label(flashcards_frame, text='', font={'TkDefaultFont', 24})
    word_label.pack(padx=5, pady=40)

    #Label to display the definiton on flashcards
    definition_label = ttk.Label(flashcards_frame, text='')
    definition_label.pack(padx=5, pady=5)

    #Button to flip the flascard (command=flip_card)
    ttk.Button(flashcards_frame, text='flip').pack(side='left', padx=5, pady=5)

    #Button to view the next flascard (command=next_card)
    ttk.Button(flashcards_frame, text='Next').pack(side='right', padx=5, pady=5)

    #Button ot view the previous flashcard (command=prev_card)
    ttk.Button(flashcards_frame, text='Previous').pack(side='right', padx=5, pady=5)

    root.mainloop()
import tkinter as t
from tkinter import messagebox as m
def exit_button():
    print("Exiting main window loop")
    window.destroy()
def ref_select_button_enter():
    print("\nChecking user choice")
    if ref_select_var.get() == "Book":
        print("User choice: Book")
        print("Hiding the main menu GUI")
        ref_select_frame.forget()
        print("Setting resolution to 300x360")
        window.geometry("300x360")
        print("Drawing book reference GUI")
        ref_book_entry_sur_frame.pack()
        ref_book_entry_for_frame.pack()
        ref_book_entry_year_frame.pack()
        ref_book_entry_tie_frame.pack()
        ref_book_entry_edi_frame.pack()
        ref_book_entry_pub_frame.pack()
        ref_book_output_box_frame.pack()
        ref_book_entr_button_frame.pack()
        print("\nDone!\nWaiting for input...")
    else:
        print("Other options do not yet exist :|")
        m.showinfo("Under Development", "Sorry, but this program only creates references for books as of now.")
def book_back_button():
    print("\nHiding the book reference GUI")
    ref_book_entry_sur_frame.forget()
    ref_book_entry_for_frame.forget()
    ref_book_entry_year_frame.forget()
    ref_book_entry_tie_frame.forget()
    ref_book_entry_edi_frame.forget()
    ref_book_entry_pub_frame.forget()
    ref_book_entr_button_frame.forget()
    ref_book_output_box_frame.forget()
    print("Setting resolution to 400x90")
    window.geometry("400x90")
    print("Drawing main menu GUI")
    ref_select_frame.pack()
    print("\nDone!\nWaiting for input...")
def book_submit_button():
    temp = ""
    temp2 = ""
    int_checker = 0
    empty = False
    int_error = False
    print("Getting all entered text")
    surn = ref_book_entr_entry_surname.get()
    fore = ref_book_entr_entry_forename.get()
    year = ref_book_entr_entry_year.get()
    boo_t = ref_book_entr_entry_title.get()
    edit = ref_book_entr_entry_edition.get()
    pub = ref_book_entr_entry_publisher.get()
    print("Checking if any entry boxes are empty")
    if surn != "":
        print("surn = ", surn)
    else:
        empty = True
        print("surn = !!!!")
    if fore != "":
        print("fore = ", fore)
    else:
        empty = True
        print("fore = !!!!")
    if year != "":
        print("year = ", year)
    else:
        empty = True
        print("year = !!!!")
    if boo_t != "":
        print("boo_t = ", boo_t)
    else:
        empty = True
        print("boo_t = !!!!")
    if edit != "":
        try:
            int_checker = int(edit)
        except:
            int_error = True
        if int_error is False:
            if int_checker == 1:
                temp2 = "st"
            elif int_checker == 2:
                temp2 = "nd"
            elif int_checker == 3:
                temp2 = "rd"
            else:
                temp2 = "th"
        print("edit = ", edit)
    else:
        empty = True
        print("edit = !!!!")
    if pub != "":
        print("pub = ", pub)
    else:
        empty = True
        print("pub = !!!!")
    if empty is True:
        m.showinfo("Empty Warning", "Please enter text for all of the fields")
        print("Minor error: User did not enter text in one or more of the entry boxes. Infobox displayed.")
    elif int_error is True:
        m.showerror("Error!", "Error: Please make sure the edition is a number and contains no text or special characters!")
        print("ERROR: Unable to convert edition number to ineger!")
    else:
        print("Deleting contents of entry boxes")
        ref_book_entr_entry_surname.delete(0, "end")
        ref_book_entr_entry_forename.delete(0, "end")
        ref_book_entr_entry_year.delete(0, "end")
        ref_book_entr_entry_title.delete(0, "end")
        ref_book_entr_entry_edition.delete(0, "end")
        ref_book_entr_entry_publisher.delete(0, "end")
        print("Combing all inputs into single reference")
        final_book_reference = surn
        temp = fore[0]
        final_book_reference = final_book_reference + ", " + temp
        final_book_reference = final_book_reference + ". (" + year + "). "
        final_book_reference = final_book_reference + boo_t
        final_book_reference = final_book_reference + " (" + edit + temp2 + " ed.). "
        final_book_reference = final_book_reference + pub + "."
        print("Reference created")
        print("Reference: ", final_book_reference)
        print("Outputting reference to output box")
        ref_book_output_box.configure(state="normal")
        ref_book_output_box.delete("1.0", "end")
        ref_book_output_box.insert("1.0", "Output: \n")
        ref_book_output_box.insert("end", final_book_reference)
        ref_book_output_box.configure(state="disabled")
        print("\nDone!\nWaiting for input...")
print("Creating window")
window = t.Tk()
print("Setting window title to [Reference Creator]")
window.title("Reference Creator")
print("Setting resolution to 400x90")
window.geometry("400x90")
ref_select_var = t.StringVar()
ref_select_var.set("Book")
print("Creating the main menu GUI")
ref_select_frame = t.Frame(window)
ref_select_label = t.Label(ref_select_frame, text="Please select the type of reference you want to create:").pack(side=t.TOP)
ref_select_option = t.OptionMenu(ref_select_frame, ref_select_var, "Book", "Journal Article", "Website")
ref_select_option.pack(fill=t.X)
ref_select_button = t.Button(ref_select_frame, text="Okay", command=ref_select_button_enter).pack(side=t.LEFT, padx=112)
ref_select_frame.pack()
ref_info_entrance_frame = t.Frame()
#Book reference GUI
print("Creating the book reference GUI")
ref_book_entry_sur_frame = t.Frame()
ref_book_entry_info_label = t.Label(ref_book_entry_sur_frame, text="Please enter the following information:").pack(side=t.TOP)
ref_book_entr_label_surname = t.Label(ref_book_entry_sur_frame, text="Surname:").pack(side=t.LEFT, padx=14)
ref_book_entr_entry_surname = t.Entry(ref_book_entry_sur_frame)
ref_book_entr_entry_surname.pack(side=t.LEFT)
ref_book_entry_for_frame = t.Frame()
ref_book_entr_label_forename = t.Label(ref_book_entry_for_frame, text="Forename:").pack(side=t.LEFT, padx=9)
ref_book_entr_entry_forename = t.Entry(ref_book_entry_for_frame)
ref_book_entr_entry_forename.pack(side=t.LEFT)
ref_book_entry_year_frame = t.Frame()
ref_book_entr_label_year = t.Label(ref_book_entry_year_frame, text="Year:").pack(side=t.LEFT, padx=24)
ref_book_entr_entry_year = t.Entry(ref_book_entry_year_frame)
ref_book_entr_entry_year.pack(side=t.LEFT)
ref_book_entry_tie_frame = t.Frame()
ref_book_entr_label_title = t.Label(ref_book_entry_tie_frame, text="Book Title:").pack(side=t.LEFT, padx=10)
ref_book_entr_entry_title = t.Entry(ref_book_entry_tie_frame)
ref_book_entr_entry_title.pack(side=t.LEFT)
ref_book_entry_edi_frame = t.Frame()
ref_book_entr_label_edition = t.Label(ref_book_entry_edi_frame, text="Edition:").pack(side=t.LEFT, padx=17)
ref_book_entr_entry_edition = t.Entry(ref_book_entry_edi_frame)
ref_book_entr_entry_edition.pack(side=t.LEFT)
ref_book_entry_pub_frame = t.Frame()
ref_book_entr_label_publisher = t.Label(ref_book_entry_pub_frame, text="Publisher:").pack(side=t.LEFT, padx=11)
ref_book_entr_entry_publisher = t.Entry(ref_book_entry_pub_frame)
ref_book_entr_entry_publisher.pack(side=t.LEFT)
ref_book_output_box_frame = t.Frame(window)
ref_book_output_box = t.Text(ref_book_output_box_frame, height=7.5, width=36)
ref_book_output_box.pack(side=t.BOTTOM, pady=5)
ref_book_output_box.insert("1.0", "Output:")
ref_book_output_box.configure(state="disabled")
ref_book_entr_button_frame = t.Frame()
ref_book_entr_submit_button = t.Button(ref_book_entr_button_frame, text="Submit", command=book_submit_button).pack(fill=t.X)
ref_book_entr_back_button = t.Button(ref_book_entr_button_frame, text="Back", command=book_back_button).pack(side=t.LEFT, fill=t.X, padx=2, pady=2)
ref_book_entry_exit_button = t.Button(ref_book_entr_button_frame, text="Exit", command=exit_button).pack(side=t.RIGHT, fill=t.X, padx=2, pady=2)
print("Drawing the main menu GUI")
print("\nDone!\nWaiting for input...")
window.mainloop()
print("End of program")

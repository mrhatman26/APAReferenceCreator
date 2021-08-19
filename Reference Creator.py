import tkinter as t
from tkinter import messagebox as m
import pyperclip as p
#Begin Definitions
def select_okay_button(): #Okay button on reference selection screen
    print("\nUpdate: User clicked okay button\nUpdate: Checking user choice...")
    if ref_select_current_option.get() == "Book":
        print("Done!\nUpdate: User choice == Book\nUpdate: Hiding selection screen...")
        ref_select_frame.forget()
        print("Done!\nUpdate: Setting resolution to 400x430...")
        window.geometry("400x430")
        print("Done!\nDrawing book reference screen...")
        ref_book_input_frame.pack(fill=t.Y)
        ref_book_submit_frame.pack(pady=5)
        ref_book_output_frame.pack()
        ref_book_menu_button_frame.pack()
        ref_book_frame.pack(fill=t.Y)
        print("Done!\n\nFunction complete!\nWaiting for user input...")
    elif ref_select_current_option.get() == "Journal Article":
        print("Done!\nUpdate: User choice == Journal Article\nUpdate: Hidiing selection screen...")
        ref_select_frame.forget()
        print("Done!\nUpdate: Setting resolution to 400x515...")
        window.geometry("400x515")
        print("Done!\nUpdate: Drawing journal article reference screen...")
        ref_journal_input_frame.pack(fill=t.Y)
        ref_journal_submit_frame.pack(pady=5)
        ref_journal_output_frame.pack()
        ref_journal_menu_button_frame.pack()
        ref_journal_frame.pack(fill=t.Y)
        print("Done!\n\nFunction Done!\nWaiting for user input...")
    elif ref_select_current_option.get() == "Website":
        print("Done!\nUpdate: User choice == Website\nUpdate: Hidiing selection screen...")
        ref_select_frame.forget()
        print("Done!\nUpdate: Setting resolution to 400x450...")
        window.geometry("400x450")
        ref_website_input_frame.pack(fill=t.Y)
        ref_website_submit_frame.pack(pady=5)
        ref_website_output_frame.pack()
        ref_website_menu_button_frame.pack()
        ref_website_frame.pack(fill=t.Y)
        print("Done!\nUpdate: Drawing website reference screen...")
    else:
        m.showerror("Error!", "Error: Incorrect option from drop down picked! (Error Code: IncorrectDrop")
def book_submit_button():
    print("\nUpdate: The user clicked the submit button")
    output_reference = ""
    temp_str = ""
    temp_str2 = ""
    print("Update: Checking if entry boxes are empty...")
    if ref_book_fname_entry.get() != "" and ref_book_sname_entry.get() != "" and ref_book_title_entry.get() != "" and ref_book_year_entry.get() != "" and ref_book_edition_entry.get() != "" and ref_book_publisher_entry.get() != "":
        print("Done!\nUpdate: All entry boexes are full\nUpdate: Creating reference...")
        output_reference = ref_book_sname_entry.get()
        print("Update: output_reference == ", output_reference)
        temp_str = ref_book_fname_entry.get()
        temp_str2 = temp_str[0]
        temp_str2 = ", " + temp_str2
        output_reference = output_reference + temp_str2
        print("Update: output_reference == ", output_reference)
        output_reference = output_reference + ". "
        output_reference = output_reference + ref_book_year_entry.get()
        print("Update: output_reference == ", output_reference)
        output_reference = output_reference + ". "
        output_reference = output_reference + ref_book_title_entry.get()
        print("Update: output_reference == ", output_reference)
        output_reference = output_reference + " ("
        output_reference = output_reference + ref_book_edition_entry.get()
        output_reference = output_reference + ".)"
        print("Update: output_reference == ", output_reference)
        output_reference = output_reference + ". "
        output_reference = output_reference + ref_book_publisher_entry.get()
        output_reference = output_reference + "."
        print("Update: output_reference == ", output_reference)
        print("Update: Reference creation complete\nUpdate: Outputting reference to output textbox...")
        ref_book_output_textbox.configure(state="normal")
        ref_book_output_textbox.delete("1.0", "end")
        ref_book_output_textbox.insert("1.0", output_reference)
        ref_book_output_textbox.insert("end", "\nCopied to clipboard!")
        ref_book_output_textbox.configure(state="disabled")
        print("Done!\nUpdate: Copying reference to the clipboard...")
        p.copy(output_reference)
        print("Done!\nDeleting text from entry boxes...")
        ref_book_fname_entry.delete(0, "end")
        ref_book_sname_entry.delete(0, "end")
        ref_book_title_entry.delete(0, "end")
        ref_book_year_entry.delete(0, "end")
        ref_book_edition_entry.delete(0, "end")
        ref_book_publisher_entry.delete(0, "end")
        print("Done!\n\nFunction complete!\nWaiting for user input...")
    else:
        print("Done!\nUpdate: One or more entry boxes are empty!\nUpdate: Warning user...")
        m.showinfo("Empty Input", "One of the entry boxes is empty, please enter the information and try again.", icon="info")
        print("Done!\n\nFunction complete!\nWaiting for user input...")
def book_back_button():
    print("Update: User clicked back button\nUpdate:Hiding book reference screen...")
    ref_book_input_frame.forget()
    ref_book_submit_frame.forget()
    ref_book_output_frame.forget()
    ref_book_frame.forget()
    print("Done!\nResetting resolution to 400x130")
    window.geometry("400x130")
    print("Done!\nDrawing reference selection screen...")
    ref_select_frame.pack()
    print("Done!\n\nFunction complete!\nWaiting for user input...")
def journal_submit_button():
    print("\nUpdate: The user clicked the submit button")
    output_reference = ""
    temp_str = ""
    temp_str2 = ""
    if ref_journal_fname_entry.get() != "" and ref_journal_sname_entry.get() != "" and ref_journal_art_title_entry.get() != "" and ref_journal_jrn_title_entry.get() != "" and ref_journal_vnum_entry.get() != "" and ref_journal_inum_entry.get() != "" and ref_journal_first_page_entry.get() != "" and ref_journal_end_page_entry.get() != "" and ref_journal_doi_entry.get() != "" and ref_journal_year_entry.get() != "":
        print("Done!\nUpdate: All entry boexes are full\nUpdate: Creating reference...")
        output_reference = ref_journal_sname_entry.get()
        print("Update: output_reference == ", output_reference)
        temp_str = ref_journal_fname_entry.get()
        temp_str2 = temp_str[0]
        temp_str2 = ", " + temp_str2
        output_reference = output_reference + temp_str2
        print("Update: output_reference == ", output_reference)
        output_reference = output_reference + ". ("
        output_reference = output_reference + ref_journal_year_entry.get()
        output_reference = output_reference + "). "
        print("Update: output_reference == ", output_reference)
        output_reference = output_reference + ref_journal_art_title_entry.get()
        output_reference = output_reference + ". "
        print("Update: output_reference == ", output_reference)
        output_reference = output_reference + ref_journal_jrn_title_entry.get()
        output_reference = output_reference + ", "
        print("Update: output_reference == ", output_reference)
        output_reference = output_reference + ref_journal_vnum_entry.get()
        output_reference = output_reference + "("
        print("Update: output_reference == ", output_reference)
        output_reference = output_reference + ref_journal_inum_entry.get()
        output_reference = output_reference + "), "
        print("Update: output_reference == ", output_reference)
        output_reference = output_reference + ref_journal_first_page_entry.get()
        output_reference = output_reference + "-"
        output_reference = output_reference + ref_journal_end_page_entry.get()
        output_reference = output_reference + ". "
        print("Update: output_reference == ", output_reference)
        output_reference = output_reference + ref_journal_doi_entry.get()
        print("Update: output_reference == ", output_reference)
        print("Update: Reference creation complete\nUpdate: Outputting reference to output textbox...")
        ref_journal_output_textbox.configure(state="normal")
        ref_journal_output_textbox.delete("1.0", "end")
        ref_journal_output_textbox.insert("1.0", output_reference)
        ref_journal_output_textbox.insert("end", "\nCopied to clipboard!")
        ref_journal_output_textbox.configure(state="disabled")
        print("Done!\nUpdate: Copying reference to the clipboard...")
        p.copy(output_reference)
        print("Done!\nDeleting text from entry boxes...")
        ref_journal_fname_entry.delete(0, "end")
        ref_journal_sname_entry.delete(0, "end")
        ref_journal_art_title_entry.delete(0, "end")
        ref_journal_jrn_title_entry.delete(0, "end")
        ref_journal_vnum_entry.delete(0, "end")
        ref_journal_inum_entry.delete(0, "end")
        ref_journal_first_page_entry.delete(0, "end")
        ref_journal_end_page_entry.delete(0, "end")
        ref_journal_doi_entry.delete(0, "end")
        ref_journal_year_entry.delete(0, "end")
        print("Done!\n\nFunction complete!\nWaiting for user input...")
    else:
        print("Done!\nUpdate: One or more entry boxes are empty!\nUpdate: Warning user...")
        m.showinfo("Empty Input", "One of the entry boxes is empty, please enter the information and try again.", icon="info")
        print("Done!\n\nFunction complete!\nWaiting for user input...")
def journal_back_button():
    print("Update: User clicked back button\nUpdate:Hiding book reference screen...")
    ref_journal_input_frame.forget()
    ref_journal_submit_frame.forget()
    ref_journal_output_frame.forget()
    ref_journal_menu_button_frame.forget()
    ref_journal_frame.forget()
    print("Done!\nResetting resolution to 400x130")
    window.geometry("400x130")
    print("Done!\nDrawing reference selection screen...")
    ref_select_frame.pack()
    print("Done!\n\nFunction complete!\nWaiting for user input...")
def website_submit_button():
    print("\nUpdate: The user clicked the submit button")
    print("\nUpdate: The user clicked the submit button")
    output_reference = ""
    temp_str = ""
    temp_str2 = ""
    if ref_website_fname_entry.get() != "" and ref_website_sname_entry.get() != "" and ref_website_name_entry.get() != "" and ref_website_title_entry.get() != "" and ref_website_url_entry.get() != "" and ref_website_year_entry.get() != "" and ref_website_month_entry.get() != "":
        print("Done!\nUpdate: All entry boexes are full\nUpdate: Creating reference...")
        output_reference = ref_website_sname_entry.get()
        print("Update: output_reference == ", output_reference)
        temp_str = ref_website_fname_entry.get()
        temp_str2 = temp_str[0]
        temp_str2 = ", " + temp_str2
        output_reference = output_reference + temp_str2
        print("Update: output_reference == ", output_reference)
        output_reference = output_reference + ". ("
        output_reference = output_reference + ref_website_year_entry.get()
        print("Update: output_reference == ", output_reference)
        output_reference = output_reference + ", "
        output_reference = output_reference + ref_website_month_entry.get()
        output_reference = output_reference + "). "
        print("Update: output_reference == ", output_reference)
        output_reference = output_reference + ref_website_title_entry.get()
        output_reference = output_reference + ". "
        print("Update: output_reference == ", output_reference)
        output_reference = output_reference + ref_website_name_entry.get()
        output_reference = output_reference + ". "
        print("Update: output_reference == ", output_reference)
        output_reference = output_reference + ref_website_url_entry.get()
        print("Update: output_reference == ", output_reference)
        print("Update: Reference creation complete\nUpdate: Outputting reference to output textbox...")
        ref_website_output_textbox.configure(state="normal")
        ref_website_output_textbox.delete("1.0", "end")
        ref_website_output_textbox.insert("1.0", output_reference)
        ref_website_output_textbox.insert("end", "\nCopied to clipboard!")
        ref_website_output_textbox.configure(state="disabled")
        print("Done!\nUpdate: Copying reference to the clipboard...")
        p.copy(output_reference)
        print("Done!\nDeleting text from entry boxes...")
        ref_website_fname_entry.delete(0, "end")
        ref_website_sname_entry.delete(0, "end")
        ref_website_name_entry.delete(0, "end")
        ref_website_title_entry.delete(0, "end")
        ref_website_url_entry.delete(0, "end")
        ref_website_year_entry.delete(0, "end")
        ref_website_month_entry.delete(0, "end")
        print("Done!\n\nFunction complete!\nWaiting for user input...")
    else:
        print("Done!\nUpdate: One or more entry boxes are empty!\nUpdate: Warning user...")
        m.showinfo("Empty Input", "One of the entry boxes is empty, please enter the information and try again.", icon="info")
        print("Done!\n\nFunction complete!\nWaiting for user input...")
def website_back_button():
    print("Update: User clicked back button\nUpdate:Hiding book reference screen...")
    ref_website_input_frame.forget()
    ref_website_submit_frame.forget()
    ref_website_output_frame.forget()
    ref_website_menu_button_frame.forget()
    ref_website_frame.forget()
    print("Done!\nResetting resolution to 400x130")
    window.geometry("400x130")
    print("Done!\nDrawing reference selection screen...")
    ref_select_frame.pack()
    print("Done!\n\nFunction complete!\nWaiting for user input...")
def exit_button():
    print("\nUpdate: User clicked exit button")
    exit_alert = t.messagebox.askquestion('Exit?', 'Are you sure you want to exit?', icon='info')
    print("Update: Message box displayed")
    if exit_alert == "yes":
        print("Update: The user has clicked yes\nUpdate: Terminating GUI")
        window.destroy()
    else:
        print("Update: The user has clicked no\nUpdate: Exit aborted")
#Begin Python Tkinter GUI
print("Update: Creating main window...")
window = t.Tk()
print("Done!")
print("Update: Setting the window to 400x130...")
window.geometry("400x130")
window.title("Reference Creator")
print("Done!")
#Begin Reference Screen GUI
print("Update: Creating the reference selection screen GUI...")
ref_select_current_option = t.StringVar() #This variable holds the value of the drop down menu. The default value is "Book"
ref_select_current_option.set("Book")
ref_select_frame = t.Frame(window)
ref_select_label = t.Label(ref_select_frame, text="Please select the type of reference you would like to create:")
ref_select_label.grid(column=0, row=1, pady=3)
ref_select_option = t.OptionMenu(ref_select_frame, ref_select_current_option, "Book", "Journal Article", "Website")
ref_select_option.grid(column=0, row=2, pady=3)
ref_select_option.config(width=45)
ref_select_okay_button = t.Button(ref_select_frame, text="Okay", command=select_okay_button, width = 21).grid(column=0, row=3, pady=1)
ref_select_exit_button = t.Button(ref_select_frame, text="Exit", command=exit_button, width = 21).grid(column=0, row=4)
ref_select_frame.pack(fill=t.Y)
print("Done!")
#Begin Book Reference Screen GUI
print("Update: Creating the book reference screen GUI...")
ref_book_frame = t.Frame(window)
ref_book_input_frame = t.Frame(ref_book_frame)
ref_book_enter_label = t.Label(ref_book_frame, text="Please enter the following information about the book:").pack(side=t.TOP)
ref_book_fname_label = t.Label(ref_book_input_frame, text="Forename:").grid(column=0, row=0)
ref_book_fname_entry = t.Entry(ref_book_input_frame, width = 20)
ref_book_fname_entry.grid(column=1, row=0)
ref_book_sname_label = t.Label(ref_book_input_frame, text="Surname:").grid(column=0, row=1)
ref_book_sname_entry = t.Entry(ref_book_input_frame, width = 20)
ref_book_sname_entry.grid(column=1, row=1)
ref_book_title_label = t.Label(ref_book_input_frame, text="Book Title:").grid(column=0, row=2)
ref_book_title_entry = t.Entry(ref_book_input_frame, width = 20)
ref_book_title_entry.grid(column=1, row=2)
ref_book_year_label = t.Label(ref_book_input_frame, text="Year of Publication:").grid(column=0, row=3)
ref_book_year_entry = t.Entry(ref_book_input_frame, width = 20)
ref_book_year_entry.grid(column=1, row=3)
ref_book_edition_label = t.Label(ref_book_input_frame, text="Edition:").grid(column=0, row=4)
ref_book_edition_entry = t.Entry(ref_book_input_frame, width = 20)
ref_book_edition_entry.grid(column=1, row=4)
ref_book_publisher_label = t.Label(ref_book_input_frame, text="Publisher:").grid(column=0, row=5)
ref_book_publisher_entry = t.Entry(ref_book_input_frame, width = 20)
ref_book_publisher_entry.grid(column=1, row=5)
ref_book_submit_frame = t.Frame(ref_book_frame)
ref_book_submit_button = t.Button(ref_book_submit_frame, text="Submit", command=book_submit_button, width = 40).pack()
ref_book_output_frame = t.Frame(ref_book_frame)
ref_book_output_label = t.Label(ref_book_output_frame, text="Reference Output:").pack()
ref_book_output_textbox = t.Text(ref_book_output_frame, width = 40, height = 10)
ref_book_output_textbox.pack()
ref_book_output_textbox.configure(state="disabled")
ref_book_menu_button_frame = t.Frame(ref_book_frame)
ref_book_back_button = t.Button(ref_book_menu_button_frame, text="Back", command=book_back_button, width = 40).pack()
ref_book_exit_button = t.Button(ref_book_menu_button_frame, text="Exit", command=exit_button, width = 40).pack()
print("Done!")
#Begin Journal Article Reference Screen GUI
print("Update: Creating the journal article reference screen GUI...")
ref_journal_frame = t.Frame(window)
ref_journal_input_frame = t.Frame(ref_journal_frame)
ref_journal_enter_label = t.Label(ref_journal_frame, text="Please enter the following information about the journal article:").pack(side=t.TOP)
ref_journal_fname_label = t.Label(ref_journal_input_frame, text="Forename:").grid(column=0, row=0)
ref_journal_fname_entry = t.Entry(ref_journal_input_frame, width = 20)
ref_journal_fname_entry.grid(column=1, row=0)
ref_journal_sname_label = t.Label(ref_journal_input_frame, text="Surname:").grid(column=0, row=1)
ref_journal_sname_entry = t.Entry(ref_journal_input_frame, width = 20)
ref_journal_sname_entry.grid(column=1, row=1)
ref_journal_art_title_label = t.Label(ref_journal_input_frame, text="Article Title:").grid(column=0, row=2)
ref_journal_art_title_entry = t.Entry(ref_journal_input_frame, width = 20)
ref_journal_art_title_entry.grid(column=1, row=2)
ref_journal_jrn_title_label = t.Label(ref_journal_input_frame, text="Journal Title:").grid(column=0, row=3)
ref_journal_jrn_title_entry = t.Entry(ref_journal_input_frame, width = 20)
ref_journal_jrn_title_entry.grid(column=1, row=3)
ref_journal_vnum_label = t.Label(ref_journal_input_frame, text="Volume No.:").grid(column=0, row=4)
ref_journal_vnum_entry = t.Entry(ref_journal_input_frame, width = 20)
ref_journal_vnum_entry.grid(column=1, row=4)
ref_journal_inum_label = t.Label(ref_journal_input_frame, text="Issue No.:").grid(column=0, row=5)
ref_journal_inum_entry = t.Entry(ref_journal_input_frame, width = 20)
ref_journal_inum_entry.grid(column=1, row=5)
ref_journal_first_page_label = t.Label(ref_journal_input_frame, text="Start Page:").grid(column=0, row=6)
ref_journal_first_page_entry = t.Entry(ref_journal_input_frame, width = 20)
ref_journal_first_page_entry.grid(column=1, row=6)
ref_journal_end_page_label = t.Label(ref_journal_input_frame, text="End Page:").grid(column=0, row=7)
ref_journal_end_page_entry = t.Entry(ref_journal_input_frame, width = 20)
ref_journal_end_page_entry.grid(column=1, row=7)
ref_journal_doi_label = t.Label(ref_journal_input_frame, text="DOI:").grid(column=0, row=8)
ref_journal_doi_entry = t.Entry(ref_journal_input_frame, width = 20)
ref_journal_doi_entry.grid(column=1, row=8)
ref_journal_year_label = t.Label(ref_journal_input_frame, text="Year of Publication").grid(column=0, row=9)
ref_journal_year_entry = t.Entry(ref_journal_input_frame, width = 20)
ref_journal_year_entry.grid(column=1, row=9)
ref_journal_submit_frame = t.Frame(ref_journal_frame)
ref_journal_submit_button = t.Button(ref_journal_submit_frame, text="Submit", command=journal_submit_button, width = 40).pack()
ref_journal_output_frame = t.Frame(ref_journal_frame)
ref_journal_output_label = t.Label(ref_journal_output_frame, text="Reference Output:").pack()
ref_journal_output_textbox = t.Text(ref_journal_output_frame, width = 48, height = 10)
ref_journal_output_textbox.pack()
ref_journal_output_textbox.configure(state="disabled")
ref_journal_menu_button_frame = t.Frame(ref_journal_frame)
ref_journal_back_button = t.Button(ref_journal_menu_button_frame, text="Back", command=journal_back_button, width = 40).pack()
ref_journal_exit_button = t.Button(ref_journal_menu_button_frame, text="Exit", command=exit_button, width = 40).pack()
print("Done!")
#Begin Website Reference Screen GUI
print("Update: Creating the website reference screen GUI...")
ref_website_frame = t.Frame(window)
ref_website_input_frame = t.Frame(ref_website_frame)
ref_website_enter_label = t.Label(ref_website_frame, text="Please enter the following information about the book:").pack(side=t.TOP)
ref_website_fname_label = t.Label(ref_website_input_frame, text="Forename:").grid(column=0, row=0)
ref_website_fname_entry = t.Entry(ref_website_input_frame, width = 20)
ref_website_fname_entry.grid(column=1, row=0)
ref_website_sname_label = t.Label(ref_website_input_frame, text="Surname:").grid(column=0, row=1)
ref_website_sname_entry = t.Entry(ref_website_input_frame, width = 20)
ref_website_sname_entry.grid(column=1, row=1)
ref_website_name_label = t.Label(ref_website_input_frame, text="Website Name:").grid(column=0, row=2)
ref_website_name_entry = t.Entry(ref_website_input_frame, width = 20)
ref_website_name_entry.grid(column=1, row=2)
ref_website_title_label = t.Label(ref_website_input_frame, text="Website Title:").grid(column=0, row=3)
ref_website_title_entry = t.Entry(ref_website_input_frame, width = 20)
ref_website_title_entry.grid(column=1, row=3)
ref_website_url_label = t.Label(ref_website_input_frame, text="URL:").grid(column=0, row=4)
ref_website_url_entry = t.Entry(ref_website_input_frame, width = 20)
ref_website_url_entry.grid(column=1, row=4)
ref_website_year_label = t.Label(ref_website_input_frame, text="Year:").grid(column=0, row=5)
ref_website_year_entry = t.Entry(ref_website_input_frame, width = 20)
ref_website_year_entry.grid(column=1, row=5)
ref_website_month_label = t.Label(ref_website_input_frame, text="Month:").grid(column=0, row=6)
ref_website_month_entry = t.Entry(ref_website_input_frame, width = 20)
ref_website_month_entry.grid(column=1, row=6)
ref_website_submit_frame = t.Frame(ref_website_frame)
ref_website_submit_button = t.Button(ref_website_submit_frame, text="Submit", command=website_submit_button, width = 40).pack()
ref_website_output_frame = t.Frame(ref_website_frame)
ref_website_output_label = t.Label(ref_website_output_frame, text="Reference Output:").pack()
ref_website_output_textbox = t.Text(ref_website_output_frame, width = 40, height = 10)
ref_website_output_textbox.pack()
ref_website_output_textbox.configure(state="disabled")
ref_website_menu_button_frame = t.Frame(ref_website_frame)
ref_website_back_button = t.Button(ref_website_menu_button_frame, text="Back", command=website_back_button, width = 40).pack()
ref_website_exit_button = t.Button(ref_website_menu_button_frame, text="Exit", command=exit_button, width = 40).pack()
print("Done!")
#Start GUI mainloop
window.resizable(False, False) #Prevents the user from resizing the window
print("Update: Drawing the main menu GUI")
print("\nDone!\nWaiting for input...")
window.mainloop()
print("End of program")

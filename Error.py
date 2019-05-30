import tkinter
from tkinter import ttk
from tkinter import messagebox as msg

def generic_error_message(text, title='ERROR', exception='generic_error_message thrown'):
    msg.showwarning(title, text)
    raise Exception(exception)


# Throw an error message when a required field is empty
def empty_field_error_message(field):
    msg.showwarning('Required Field Missing', 'The required field ' + field + ' is missing')
    raise ValueError('Required field must be filled')


# Takes a list of widgets and makes sure none are empty
def check_if_empty(widget):
    if getattr(widget, "get")() == '':
        self.empty_field_error_message(getattr(widget, "name"))
'''
Allows for the creation of multiple windows (frames), which link to each other via 'back' and 'next' buttons.

To use, use the Navigate_frames class.  The Make_frame class is only used to draw frames into the
Navigate_frames object.  Should really be a class nested in a class.

Pass in n (number of frames you want linked) and master_frame (the frame you want them drawn on)
'''

import tkinter as tk
from tkinter import ttk

class Navigate_frames(object):
    def __init__(self, n, master_frame):
        self.n = n
        self.frame_list = [0] * n
        for i in range(n):
            self.frame_list[i] = Make_frame(i, master_frame, self.frame_list)
        self.frame_list[0].frame.grid()
        #self.frame_list[0].backbutton.config(state = tk.DISABLED)
        #self.frame_list[-1].nextbutton.config(state = tk.DISABLED)



class Make_frame(object):
    def __init__(self, i, master_frame, frame_list):
        self.i = i
        self.frame = tk.Frame(master_frame)
        self.frame_list = frame_list
        #self.nextbutton = ttk.Button(self.frame,text='next',command = self.next)
        #self.nextbutton.grid(column=2,row=100)
        #self.backbutton = ttk.Button(self.frame,text='back',command = self.back)
        #self.backbutton.grid(column=0,row=100)
        #self.label = ttk.Label(self.frame,text='%i'%(self.i+1)).grid(column=1,row=0)

    def next(self):
        self.frame.grid_forget()
        self.frame_list[self.i+1].frame.grid()
    def back(self):
        self.frame.grid_forget()
        self.frame_list[self.i-1].frame.grid()










if __name__ == "__main__":

    master = tk.Tk()
    master.title("Note that Title is from master; does not change")
    navigate_frames = Navigate_frames(7, master)

    print(navigate_frames.frame_list[1].frame)
    label = ttk.Label(navigate_frames.frame_list[1].frame, text = "This is a test label").grid(column = 1, row = 1)

    master.mainloop()
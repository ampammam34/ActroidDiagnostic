# -*- coding: cp932 -*-

import Tkinter as tk

class JointFrame(tk.Frame):

        def __init__(self,root,number,label,min_,max_,init_):
                tk.Frame.__init__(self,root)
                self.root = root
                self.slider = tk.Scale(self,from_ = max_, to = min_)
                self.slider.set(init_)
                row = 0
                column = 0
                self.slider.grid(row=row, column=column, rowspan=2)
                self.label = tk.Label(self,text=label)
                row = 0
                column = 1
                self.label.grid(row=row, column=column)
                self.strvar = tk.StringVar()
                self.strvar.set("0")
                self.entry =tk.Entry(self,textvariable=self.strvar)
                row = 1
                self.entry.grid(row=row,column=column)

        def setvalue(self, value):
                #value = self.slider.get()
                self.strvar.set(value)
                
                #self.strvar.set()
                
        def getvalue(self):
                return self.slider.get()
        
def test():
        root = tk.Tk()
        my_tuple = (("0:Eyebrows up&down  ",0,240,150),
                    ("1:Eyelids open&shut ",0,255,150),
                    ("2:Eyes right&left   ",0,255,128),
                    ("3:Eyes up&down      ",0,255,128),
                    ("4:Mouth open&shut   ",0,255,0),
                    ("5:left neck         ",0,255,0),
                    ("6:right neck        ",0,255,200),
                    ("7:Neck turning      ",0,255,0),
                    ("8:left arm up       ",-14,130,0),#L1
                    ("9:left arm open    ",0,56,40),#L2
                    ("10:left upper arm   ",0,90,45),#L3
                    ("11:left elbow       ",0,112,0),#L4
                    ("12:left forearm     ",-90,90,0),#L5
                    ("13:left hand length ",-40,28,-6),#L6
                    ("14:left hand side   ",-15,25,5),#L7
                    ("15:right arm up     ",-14,130,130),#R1
                    ("16:right arm open   ",0,56,50),#R2
                    ("17:right upper arm  ",0,90,0),#R3
                    ("18:right elbow      ",0,112,0),#R4
                    ("19:right forearm    ",-90,90,-90),#R5
                    ("20:right hand length",0,255,0),
                    ("21:right hand side  ",0,255,0),
                    ("22:Body front&back  ",0,255,255),
                    ("23:Body turning     ",0,255,155))
        frames =[]
        
        row = 0
        column = 0
        for elem in my_tuple:
                title = elem[0]
                value1 = elem[1]
                value2 = elem[2]
                value3 = elem[3]
                jf = JointFrame(root,0,elem[0],elem[1],elem[2],elem[3])
                jf.grid(row=row,column=column)
                frames.append(jf)
                column = column + 1
                if column > 5:
                        row = row +1
                        column = 0

                print title
                print '--',value1
                print '--',value2
                print '--',value3
        return root, frames

        #root.mainloop()


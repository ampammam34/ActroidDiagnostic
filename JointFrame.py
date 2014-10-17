# -*- coding: cp932 -*-

import Tkinter as tk

class JointFrame(tk.Frame):

        def __init__(self,root,number,label,min_,max_):
                tk.Frame.__init__(self,root)
                self.root = root
                self.slider = tk.Scale(self,from_ = 255, to = 0)
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
                value1 = self.slider.get()
                self.strvar.set(str(value1))
                
                #self.strvar.set()
                
        def getvalue(self):
                return self.slider.get()
        
def test():
        root = tk.Tk()
        my_tuple = (("1:Eyebrows up&down  ",0,255),
                    ("2:Eyelids open&shut ",0,255),
                    ("3:Eyes right&left   ",0,255),
                    ("4:Eyes up&down      ",0,255),
                    ("5:Mouth open&shut   ",0,255),
                    ("6:left neck         ",0,255),
                    ("7:right neck        ",0,255),
                    ("8:Neck turning      ",0,255),
                    ("9:left arm up       ",0,255),
                    ("10:left arm open    ",0,255),
                    ("11:left upper arm   ",0,255),
                    ("12:left elbow       ",0,255),
                    ("13:left forearm     ",0,255),
                    ("14:left hand length ",0,255),
                    ("15:left hand side   ",0,255),
                    ("16:right arm up     ",0,255),
                    ("17:right arm open   ",0,255),
                    ("18:right upper arm  ",0,255),
                    ("19:right elbow      ",0,255),
                    ("20:right forearm    ",0,255),
                    ("21:right hand length",0,255),
                    ("22:right hand side  ",0,255),
                    ("23:Body front&back  ",0,255),
                    ("24:Body turning     ",0,255))
        frames =[]
        
        row = 0
        column = 0
        for elem in my_tuple:
                title = elem[0]
                value1 = elem[1]
                value2 = elem[2]
                jf = JointFrame(root,0,elem[0],elem[1],elem[2])
                jf.grid(row=row,column=column)
                frames.append(jf)
                column = column + 1
                if column > 5:
                        row = row +1
                        column = 0

                print title
                print '--',value1
                print '--',value2
        return root, frames

        #root.mainloop()


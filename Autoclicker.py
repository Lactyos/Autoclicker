from tkinter import *
import pyautogui as ac
import time
import keyboard as kb

root = Tk()

#Titulo
title = Label(root, text='Autoclicker', borderwidth=5, relief="ridge", width=20, height=3);
title.pack(pady=15);


#Frame dos check buttons
ClickFrame = Frame(root, pady=15);
ClickFrame.pack();

#CheckButtons
CheckV1 = IntVar();
CheckV2 = IntVar();
LeftBtn = Checkbutton(ClickFrame, text = "Left Click", padx=10, variable=CheckV1, onvalue=1, offvalue=0, command=lambda:[clearCheck1()]);
RightBtn = Checkbutton(ClickFrame, text= "Right Click", padx=10, variable=CheckV2, onvalue=1, offvalue=0, command=lambda:[clearCheck2()]);
LeftBtn.grid(row=0, column=0);
RightBtn.grid(row=0, column=1);

#Frame dos cliques por segundo
SpeedFrame = Frame(root, pady=10);
SpeedFrame.pack(fill="x");
SpeedFrame.columnconfigure(0, weight=1);
SpeedFrame.columnconfigure(1, weight=1);

#Widgets dos cliques por segundo
Label1 = Label(SpeedFrame, text='Time between clicks(ms):', font=('Arial', 10));
Speed = Text(SpeedFrame, width=15, height=1, font=('Arial', 10));
SubmitBtn = Button(SpeedFrame, text='Submit', command=lambda:Submit(), width=8);
Speed.grid(row=1, column=0, sticky='w,e');
SubmitBtn.grid(row=1, column=1, sticky='w,e');
Label1.grid(row=0, column=0);

#Frame dos startstop
StartStop = Frame(root, pady=15);
StartStop.pack();

#Butoes startstop
StartBtn = Button(StartStop, text='Start (\ key)', font=('Arial', 10), width=11, height=2, command=lambda:Start());
StopBtn = Button(StartStop, text='Stop(Esc key)', font=('Arial', 10), width=11, height=2);
StartBtn.grid(row=0, column=0, padx=5);
StopBtn.grid(row=0, column=1, padx=5);

#Functions

#Checkboxes 
def clearCheck1():
    if (CheckV2.get() == 1):
        RightBtn.deselect()
        
def clearCheck2():
    if (CheckV1.get() == 1):
        LeftBtn.deselect()

#Submit button
def Submit():
    IntervalInput = int(Speed.get("1.0", "end-1c"))
    global Interval
    Interval = IntervalInput/1000
    print(Interval)


#StartButton
def Start(event):
    while not kb.is_pressed("1"):
        ac.click()
        time.sleep(Interval)
        root.update()  
    
root.bind("<Delete>", Start)

#Autodestroy
def destroy(event):
    root.destroy()

root.bind("<Escape>", destroy)


#root['bg'] = "grey"
root.resizable(False, False);
root.geometry('250x320');
root.title("Autoclicker");
root.mainloop();
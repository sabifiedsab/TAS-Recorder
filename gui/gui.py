from tkinter import Tk, Label, Button
import os

from tas import recorder, playback
from pynput.keyboard import Controller as KeyboardController

OPEN_FROM_MAIN = "__main__" == __name__

class TASRecorderGUI:
    def __init__(self):
        self.WIDTH = 500
        self.HEIGHT = 500
        
        self.profiles = [["profile1", "Profile 1"], ["profile2", "Profile 2"], ["profile3", "Profile 3"]]
        self.currentProfile = 0
        
        self.recordButtonPressed = False
        self.playbackButtonPressed = False

        self.win = Tk()
        self.setup_window()
        self.add_title_label()
        self.add_profile_button()
        self.add_record_button()
        self.add_playback_button()
        self.add_quit_button()

        self.win.mainloop()

    def setup_window(self):
        self.win.geometry(f"{self.WIDTH}x{self.HEIGHT}")
        self.win.resizable(False, False)
        self.win.title("TAS-Recorder GUI")

    def add_title_label(self):
        self.titleLabel = Label(self.win, text="TAS-Recorder", font=("Calibri", 30))
        self.titleLabel.place(x=(self.WIDTH - self.titleLabel.winfo_reqwidth()) / 2, y=0)
        
    def add_profile_button(self):
        self.profileButton = Button(self.win, text=self.profiles[self.currentProfile][1], font=("Calibri", 15), width=10, height=1, command=self.cycle_profile)
        self.profileButton.place(x=100, y=self.HEIGHT-60)
        
        self.currentProfile = -1
        self.cycle_profile()
    
    def cycle_profile(self):
        self.currentProfile = (self.currentProfile + 1) % len(self.profiles)
        profile_string = self.profiles[self.currentProfile][1]
        self.profileButton["text"] = profile_string
        
        profile_file = self.profiles[self.currentProfile][0]
        pathToDir = f"gui/profiles/" if OPEN_FROM_MAIN else f"profiles/"
        pathToFile = pathToDir + (f"{profile_file}.json")
        
        if not os.path.exists(pathToDir):
            os.mkdir(pathToDir)
        
        if not os.path.isfile(pathToFile):
            with open(pathToFile, "w") as f:
                f.write("[]")
        
        self.currentFile = pathToFile
        

    def add_quit_button(self):
        self.quitButton = Button(self.win, text="Quit", font=("Calibri", 15), width=10, height=1, command=self.win.quit)
        self.quitButton.place(x=300, y=self.HEIGHT-60)
        
    def add_record_button(self):
        self.recordButton = Button(self.win, text="Record", font=("Calibri", 15), width=10, height=1, command=self.record_button)
        self.recordButton.place(x=100, y=100)
    
    def add_playback_button(self):
        self.recordButton = Button(self.win, text="Playback", font=("Calibri", 15), width=10, height=1, command=self.playback_button)
        self.recordButton.place(x=300, y=100)
        
    def record_button(self):
        self.recordButtonPressed = not self.recordButtonPressed
        
        if (self.recordButtonPressed): # start record logic
            self.minimize_window()
            
            recorder.record(self.currentFile)
            
            while recorder.record.isDoneCalling == False:
                pass
            
            self.open_window()
            
        else: # stop record logic
            pass
    
    def playback_button(self):
        self.playbackButtonPressed = not self.playbackButtonPressed
        
        if (self.playbackButtonPressed): # start playback logic
            self.minimize_window()
            
            playback.play(self.currentFile)
        else: # stop playback logic
            pass
    
    def open_window(self):
        self.win.state(newstate='normal')
    
    def minimize_window(self):
        self.win.state(newstate='iconic')
        

if __name__ == '__main__':
    app = TASRecorderGUI()

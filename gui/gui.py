from tkinter import Tk, Label, Button
from tas import recorder, playback

class TASRecorderGUI:
    def __init__(self):
        self.WIDTH = 500
        self.HEIGHT = 500
        
        self.profiles = [["profile1", "Profile 1"], ["profile2", "Profile 2"], ["profile3", "Profile 3"]]
        self.currentProfile = 0

        self.win = Tk()
        self.setup_window()
        self.add_title_label()
        self.add_profile_button()
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
        button_width = 10 * 10  # Assuming each character is 10 pixels wide and the width is set to 10 characters
        total_button_width = 2 * button_width
        spacing = (self.WIDTH - total_button_width) / 3

        self.profileButton = Button(self.win, text=self.profiles[self.currentProfile][1], font=("Calibri", 15), width=10, height=1, command=self.cycle_profile)
        self.profileButton.place(x=spacing, y=self.HEIGHT-60)
    
    def cycle_profile(self):
        self.currentProfile = (self.currentProfile + 1) % len(self.profiles)
        self.profileButton["text"] = self.profiles[self.currentProfile][1]

    def add_quit_button(self):
        button_width = 10 * 10
        total_button_width = 2 * button_width
        spacing = (self.WIDTH - total_button_width) / 3

        self.quitButton = Button(self.win, text="Quit", font=("Calibri", 15), width=10, height=1, command=self.win.quit)
        self.quitButton.place(x=2 * spacing + button_width, y=self.HEIGHT-60)

if __name__ == '__main__':
    app = TASRecorderGUI()

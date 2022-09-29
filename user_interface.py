import wx
import ctypes

user32 = ctypes.windll.user32
screenSize = int(user32.GetSystemMetrics(0)*.95), int(user32.GetSystemMetrics(1)*.95)
buttonSize = int(screenSize[0]*.1), int(screenSize[0]*.05)
horizontalSpacer, verticalSpacer = int(screenSize[0]*.1) + 5, int(screenSize[0]*.05) + 5

green_color = (57, 255, 20)
red_color = (255, 87, 51)

class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='Control Systems', size=screenSize)
        panel = wx.Panel(self)  # creates the panel

        horizontalBox = wx.BoxSizer(wx.HORIZONTAL)

        # Open All Valves
        self.open_all = wx.Button(panel, label="Open All Valves", size=buttonSize, pos = (5,5))
        # self.open_all.Bind(wx.EVT_BUTTON, self.open_valves)
        horizontalBox.Add(self.open_all, 0, wx.ALL)

        #  Solenoids Valve
        self.solenoids = wx.Button(panel, label='Solenoids Off', size=buttonSize, pos= (horizontalSpacer,5))  # button element
        self.solenoids.SetBackgroundColour(red_color)
        # self.solenoids.Bind(wx.EVT_BUTTON, self.solenoids_press)  # ties the event to the button
        horizontalBox.Add(self.solenoids, 0,  wx.ALL|wx.EXPAND, 20)



        #  PID
        self.pid_button = wx.Button(panel, label='PID Off', size=buttonSize, pos= (horizontalSpacer*2,5))  # button element
        self.pid_button.SetBackgroundColour(red_color)
        # self.pid_button.Bind(wx.EVT_BUTTON, self.pid_button_press)  # ties the event to the button
        horizontalBox.Add(self.pid_button)

        #  Calibrate PID
        self.pid_calibrate = wx.Button(panel, label='Calibrate PID', size=buttonSize)  # button element
        # self.pid_calibrate.Bind(wx.EVT_BUTTON, self.pid_calibrate_press)  # ties the event to the button
        horizontalBox.Add(self.pid_calibrate)

        self.Show()  # creates the app window

if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame()
    app.MainLoop()
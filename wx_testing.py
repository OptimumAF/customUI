import wx
import ctypes

user32 = ctypes.windll.user32
screensize = int(user32.GetSystemMetrics(0)*.95), int(user32.GetSystemMetrics(1)*.95)
print(screensize)
buttonsize = screensize[0]*.1, screensize[0]*.05

green_color = (57, 255, 20)
red_color = (255, 87, 51)

class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='Hello World', size=screensize)
        panel = wx.Panel(self)  # creates the panel

        valve_sizer = wx.BoxSizer(wx.VERTICAL)
        solenoid_sizer = wx.BoxSizer(wx.VERTICAL)

        # self.text_ctrl = wx.TextCtrl(panel, pos=(5, 5))  # text element
        # valve_sizer.Add(self.text_ctrl, 0, wx.ALL | wx.EXPAND, 5)  # matches the width of the window

        # Open All Valves
        self.open_all = wx.Button(panel, label = "Open All Valves", size = buttonsize)
        self.open_all.Bind(wx.EVT_BUTTON, self.open_valves)
        valve_sizer.Add(self.open_all, 0, wx.ALL | wx.ALIGN_LEFT, 5)

        #  Press Valve
        self.press_valve = wx.Button(panel, label='Press Closed', size=buttonsize)  # button element
        self.press_valve.SetBackgroundColour(red_color)
        self.press_valve.Bind(wx.EVT_BUTTON, self.press_valve_press)  # ties the event to the button
        valve_sizer.Add(self.press_valve, 0, wx.ALL | wx.ALIGN_LEFT, 5)  # matches the width of the window

        #  Kerosene Main Valve
        self.kero_main = wx.Button(panel, label='Kero Main Closed', size=buttonsize)  # button element
        self.kero_main.SetBackgroundColour(red_color)
        self.kero_main.Bind(wx.EVT_BUTTON, self.kero_main_press)  # ties the event to the button
        valve_sizer.Add(self.kero_main, 0, wx.ALL | wx.ALIGN_LEFT, 5)  # matches the width of the window

        #  Kerosene Vent Valve
        self.kero_vent = wx.Button(panel, label='Kero Vent Closed', size=buttonsize)  # button element
        self.kero_vent.SetBackgroundColour(red_color)
        self.kero_vent.Bind(wx.EVT_BUTTON, self.kero_vent_press)  # ties the event to the button
        valve_sizer.Add(self.kero_vent, 0, wx.ALL | wx.ALIGN_LEFT, 5)  # matches the width of the window

        #  LOX Main Valve
        self.lox_main = wx.Button(panel, label='LOX Vent Closed', size=buttonsize)  # button element
        self.lox_main.SetBackgroundColour(red_color)
        self.lox_main.Bind(wx.EVT_BUTTON, self.lox_main_press)  # ties the event to the button
        valve_sizer.Add(self.lox_main, 0, wx.ALL | wx.ALIGN_LEFT, 5)  # matches the width of the window

        #  LOX Vent Valve
        self.lox_vent = wx.Button(panel, label='Kero Vent Closed', size=buttonsize)  # button element
        self.lox_vent.SetBackgroundColour(red_color)
        self.lox_vent.Bind(wx.EVT_BUTTON, self.lox_vent_press)  # ties the event to the button
        valve_sizer.Add(self.lox_vent, 0, wx.ALL | wx.ALIGN_LEFT, 5)  # matches the width of the window

        # Close All Valves
        self.close_all = wx.Button(panel, label="Close All Valves", size=buttonsize)
        self.close_all.Bind(wx.EVT_BUTTON, self.close_valves)
        valve_sizer.Add(self.close_all, 0, wx.ALL | wx.ALIGN_LEFT, 5)

        panel.SetSizer(valve_sizer)  # matches the width of the window

        #  Solenoids Valve
        self.solenoids = wx.Button(panel, label='Solenoids Off', size=buttonsize)  # button element
        self.solenoids.SetBackgroundColour(red_color)
        self.solenoids.Bind(wx.EVT_BUTTON, self.solenoids_press)  # ties the event to the button
        solenoid_sizer.Add(self.solenoids, 2525, wx.ALL | wx.ALIGN_LEFT, 100)  # matches the width of the window

        self.Show()  # creates the app window

    def open_valves(self, event):  # adds functionality to the button
        self.press_valve.SetBackgroundColour(green_color)
        self.press_valve.SetLabel("Press Open")
        self.kero_main.SetBackgroundColour(green_color)
        self.kero_main.SetLabel("Kero Main Open")
        self.kero_vent.SetBackgroundColour(green_color)
        self.kero_vent.SetLabel("Kero Vent Open")
        self.lox_main.SetBackgroundColour(green_color)
        self.lox_main.SetLabel("LOX Main Open")
        self.lox_vent.SetBackgroundColour(green_color)
        self.lox_vent.SetLabel("LOX Vent Open")

    def press_valve_press(self, event):  # adds functionality to the button
        color = self.press_valve.GetBackgroundColour()
        if color == red_color:
            print("red color")
            self.press_valve.SetBackgroundColour(green_color)
            self.press_valve.SetLabel("Press Open")
        if color == green_color:
            print("green color")
            self.press_valve.SetBackgroundColour(red_color)
            self.press_valve.SetLabel("Press Closed")

    def kero_main_press(self, event):  # adds functionality to the button
        color = self.kero_main.GetBackgroundColour()
        if color == red_color:
            self.kero_main.SetBackgroundColour(green_color)
            self.kero_main.SetLabel("Kero Main Open")
        if color == green_color:
            self.kero_main.SetBackgroundColour(red_color)
            self.kero_main.SetLabel("Kero Main Closed")

    def kero_vent_press(self, event):  # adds functionality to the button
        color = self.kero_vent.GetBackgroundColour()
        if color == red_color:
            self.kero_vent.SetBackgroundColour(green_color)
            self.kero_vent.SetLabel("Kero Vent Open")
        if color == green_color:
            self.kero_vent.SetBackgroundColour(red_color)
            self.kero_vent.SetLabel("Kero Vent Closed")

    def lox_main_press(self, event):  # adds functionality to the button
        color = self.lox_main.GetBackgroundColour()
        if color == red_color:
            self.lox_main.SetBackgroundColour(green_color)
            self.lox_main.SetLabel("LOX Main Open")
        if color == green_color:
            self.lox_main.SetBackgroundColour(red_color)
            self.lox_main.SetLabel("LOX Main Closed")

    def lox_vent_press(self, event):  # adds functionality to the button
        color = self.lox_vent.GetBackgroundColour()
        if color == red_color:
            self.lox_vent.SetBackgroundColour(green_color)
            self.lox_vent.SetLabel("LOX Vent Open")
        if color == green_color:
            self.lox_vent.SetBackgroundColour(red_color)
            self.lox_vent.SetLabel("LOX Vent Closed")

    def close_valves(self, event):  # adds functionality to the button
        self.press_valve.SetBackgroundColour(red_color)
        self.press_valve.SetLabel("Press Closed")
        self.kero_main.SetBackgroundColour(red_color)
        self.kero_main.SetLabel("Kero Main Closed")
        self.kero_vent.SetBackgroundColour(red_color)
        self.kero_vent.SetLabel("Kero Vent Closed")
        self.lox_main.SetBackgroundColour(red_color)
        self.lox_main.SetLabel("LOX Main Closed")
        self.lox_vent.SetBackgroundColour(red_color)
        self.lox_vent.SetLabel("LOX Vent Closed")

    def solenoids_press(self, event):  # adds functionality to the button
        color = self.solenoids.GetBackgroundColour()
        if color == red_color:
            self.solenoids.SetBackgroundColour(green_color)
            self.solenoids.SetLabel("Solenoids On")
        if color == green_color:
            self.solenoids.SetBackgroundColour(red_color)
            self.solenoids.SetLabel("Solenoids Off")


if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame()
    app.MainLoop()


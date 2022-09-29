import wx
import ctypes

user32 = ctypes.windll.user32
screensize = int(user32.GetSystemMetrics(0)*.95), int(user32.GetSystemMetrics(1)*.95)
buttonsize = int(screensize[0]*.1), int(screensize[0]*.05)
horizontalSpacer, verticalSpacer = int(screensize[0]*.1) + 5, int(screensize[0]*.05) + 5



green_color = (57, 255, 20)
red_color = (255, 87, 51)

class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='Control Systems', size=screensize)
        panel = wx.Panel(self)  # creates the panel

        # Open All Valves
        self.open_all = wx.Button(panel, label = "Open All Valves", size = buttonsize, pos=(5,5))
        self.open_all.Bind(wx.EVT_BUTTON, self.open_valves)

        #  Solenoids Valve
        self.solenoids = wx.Button(panel, label='Solenoids Off', size=buttonsize, pos=(horizontalSpacer, 5))  # button element
        self.solenoids.SetBackgroundColour(red_color)
        self.solenoids.Bind(wx.EVT_BUTTON, self.solenoids_press)  # ties the event to the button

        #  PID
        self.pid_button = wx.Button(panel, label='PID Off', size=buttonsize, pos=(horizontalSpacer*2, 5))  # button element
        self.pid_button.SetBackgroundColour(red_color)
        self.pid_button.Bind(wx.EVT_BUTTON, self.pid_button_press)  # ties the event to the button

        #  Calibrate PID
        self.pid_calibrate = wx.Button(panel, label='Calibrate PID', size=buttonsize, pos=(horizontalSpacer*3, 5))  # button element
        self.pid_calibrate.Bind(wx.EVT_BUTTON, self.pid_calibrate_press)  # ties the event to the button

        #  Press Valve
        self.press_valve = wx.Button(panel, label='Press Closed', size=buttonsize, pos=(5, verticalSpacer))  # button element
        self.press_valve.SetBackgroundColour(red_color)
        self.press_valve.Bind(wx.EVT_BUTTON, self.press_valve_press)  # ties the event to the button

        # Kero PID values
        self.kero_prop = wx.TextCtrl(panel, size=buttonsize, pos=(horizontalSpacer, verticalSpacer))
        self.kero_int = wx.TextCtrl(panel, size=buttonsize, pos=(horizontalSpacer*2, verticalSpacer))
        self.kero_der = wx.TextCtrl(panel, size=buttonsize, pos=(horizontalSpacer*3, verticalSpacer))

        #  Kero PID
        self.kero_pid = wx.Button(panel, label='Kero PID', size=(buttonsize[0]*3+10,buttonsize[1]), pos=(horizontalSpacer, verticalSpacer*2))  # button element
        self.kero_pid.Bind(wx.EVT_BUTTON, self.kero_pid_press)  # ties the event to the button

        # LOX PID values
        self.lox_prop = wx.TextCtrl(panel, size=buttonsize, pos=(horizontalSpacer, verticalSpacer*3))
        self.lox_int = wx.TextCtrl(panel, size=buttonsize, pos=(horizontalSpacer * 2, verticalSpacer*3))
        self.lox_der = wx.TextCtrl(panel, size=buttonsize, pos=(horizontalSpacer * 3, verticalSpacer*3))

        #  LOX PID
        self.lox_pid = wx.Button(panel, label='LOX PID', size=(buttonsize[0] * 3 + 10, buttonsize[1]),
                                  pos=(horizontalSpacer, verticalSpacer * 4))  # button element
        self.lox_pid.Bind(wx.EVT_BUTTON, self.lox_pid_press)  # ties the event to the button


        #  Kerosene Main Valve
        self.kero_main = wx.Button(panel, label='Kero Main Closed', size=buttonsize, pos=(5, verticalSpacer*2))  # button element
        self.kero_main.SetBackgroundColour(red_color)
        self.kero_main.Bind(wx.EVT_BUTTON, self.kero_main_press)  # ties the event to the button

        #  Kerosene Vent Valve
        self.kero_vent = wx.Button(panel, label='Kero Vent Closed', size=buttonsize, pos=(5, verticalSpacer*3))  # button element
        self.kero_vent.SetBackgroundColour(red_color)
        self.kero_vent.Bind(wx.EVT_BUTTON, self.kero_vent_press)  # ties the event to the button

        #  LOX Main Valve
        self.lox_main = wx.Button(panel, label='LOX Main Closed', size=buttonsize, pos=(5, verticalSpacer*4))  # button element
        self.lox_main.SetBackgroundColour(red_color)
        self.lox_main.Bind(wx.EVT_BUTTON, self.lox_main_press)  # ties the event to the button

        #  LOX Vent Valve
        self.lox_vent = wx.Button(panel, label='LOX Vent Closed', size=buttonsize, pos=(5, verticalSpacer*5))  # button element
        self.lox_vent.SetBackgroundColour(red_color)
        self.lox_vent.Bind(wx.EVT_BUTTON, self.lox_vent_press)  # ties the event to the button

        # Close All Valves
        self.close_all = wx.Button(panel, label="Close All Valves", size=buttonsize, pos=(5, verticalSpacer*6))
        self.close_all.Bind(wx.EVT_BUTTON, self.close_valves)

        #  Sensor Log
        self.sensor_log = wx.Button(panel, label='Sensor Log Disabled', size=buttonsize,
                                  pos=(horizontalSpacer, verticalSpacer * 5))  # button element
        self.sensor_log.SetBackgroundColour(red_color)
        self.sensor_log.Bind(wx.EVT_BUTTON, self.sensor_log_press)  # ties the event to the button

        # calibrate sensor
        self.calibrate_sensor = wx.Button(panel, label="Calibrate Sensor", size=buttonsize, pos=(horizontalSpacer*2, verticalSpacer * 5))
        self.calibrate_sensor.Bind(wx.EVT_BUTTON, self.calibrate_sensor_press)


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

    def pid_button_press(self, event):  # adds functionality to the button
        color = self.pid_button.GetBackgroundColour()
        if color == red_color:
            self.pid_button.SetBackgroundColour(green_color)
            self.pid_button.SetLabel("PID On")
        if color == green_color:
            self.pid_button.SetBackgroundColour(red_color)
            self.pid_button.SetLabel("PID Off")

    def pid_calibrate_press(self, event):  # adds functionality to the button
        pass

    def kero_pid_press(self, event):  # adds functionality to the button
        p, i, d = int(self.kero_prop.GetValue()), int(self.kero_int.GetValue()), int(self.kero_der.GetValue())
        print(p,i,d)
        self.kero_prop.SetValue(""), self.kero_int.SetValue(""), self.kero_der.SetValue("")


    def lox_pid_press(self, event):  # adds functionality to the button
        p,i,d = int(self.lox_prop.GetValue()), int(self.lox_int.GetValue()), int(self.lox_der.GetValue())
        print(p,i,d)
        self.lox_prop.SetValue(""), self.lox_int.SetValue(""), self.lox_der.SetValue("")


    def sensor_log_press(self, event):  # adds functionality to the button
        color = self.sensor_log.GetBackgroundColour()
        if color == red_color:
            print("red color")
            self.sensor_log.SetBackgroundColour(green_color)
            self.sensor_log.SetLabel("Sensor Log Enabled")
        if color == green_color:
            print("green color")
            self.sensor_log.SetBackgroundColour(red_color)
            self.sensor_log.SetLabel("Sensor Log Disabled")

    def calibrate_sensor_press(self, event):  # adds functionality to the button
        pass



if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame()
    app.MainLoop()


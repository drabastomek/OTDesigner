import tkinter as tk
import tkinter.ttk as ttk

# class Winding(object):
#     def __init__(self):
#         self.name = None
#         self.listOfParams = ['name', 'turns', 'layers', 'awg']
#         self.widgets = []

#     def add_winding(self, frame, row):
#         label = tk.Entry(frame, width=10,
#             justify='center')
#         label.grid(column=0, row=row)

#         for i, param in enumerate(self.listOfParams[1:]):
#             entry = tk.Entry(frame, width=10, 
#                 justify='right')
#             entry.grid(column=i+1, row=row)

#             self.widgets.append(entry)

#     def add_named_winding(self, frame, name, row):
#         self.name = name

#         label = tk.Label(frame, text=name,
#             width=10)
#         label.grid(column=0, row=row)

#         for i, param in enumerate(self.listOfParams[1:]):
#             entry = tk.Entry(frame, width=10, 
#                 justify='right')
#             entry.grid(column=i+1, row=row)

#             self.widgets.append(entry)

#     def get_values(self):
#         vals = []

#         for widget in self.widgets:
#             print(widget)


class View(tk.Toplevel):
    def __init__(self, master):
        tk.Toplevel.__init__(self, master)
        self.protocol('WM_DELETE_WINDOW', self.master.destroy)

        self.bobbinKeys = ['width', 'height', 'depth', 'lip']

        self.view_Bobbin = {            
            'width': None, 
            'height': None, 
            'depth': None, 
            'lip': None,
            'units': None
        }
        self.view_Windings = []

        self.grid()

        # add bobbin input
        self.bobbinFrame = tk.LabelFrame(self, 
            text='Bobbin')
        self.add_BobbinInput(self.bobbinFrame)
        self.bobbinFrame.grid(column=0, row=0)
        
        # add bobbin dimensions image
        self.bobbinImageCanvas = tk.Canvas(self, 
            height=250, width=250)
        # >>> add the image here!!! <<<
        self.bobbinImageCanvas.grid(column=1, row=0)

        # add windings data
        self.windingsFrame = tk.LabelFrame(self,
            text='Winding parameters')
        self.add_WindingsHeader(self.windingsFrame)
        self.windingsFrame.grid(column=0, row=1, columnspan=2)

        self.windings_button = tk.Button(self,
            text=u"Add winding")
        self.windings_button.grid(column=0,row=10, columnspan=4)

    def set_BobbinInput(self, key, value):
        self.view_Bobbin[key].delete(0,'end')
        self.view_Bobbin[key].insert('end', str(value))  

    def add_BobbinInput(self, frame):
        for i, key in enumerate(self.bobbinKeys):
            label = tk.Label(frame, text=key)
            label.grid(column=0, row=i, sticky='ew')

            self.view_Bobbin[key] = \
                tk.Entry(frame, width=11, 
                justify='right')
            self.view_Bobbin[key].grid(column=1, row=i)

        # units
        label = tk.Label(frame, text='units:')
        label.grid(column=0, row=5)

        self.view_Bobbin['units'] = \
            ttk.Combobox(frame, width=8, 
            values=['in.','mm.'],
            state='readonly')
        self.view_Bobbin['units'].grid(column=1, row=5)
        self.view_Bobbin['units'].set('in.')

        self.checkButton = tk.Button(self, text='Check',
            width=8)
        self.checkButton.grid(column=0, row=11, columnspan=4)

    def add_WindingsHeader(self, frame):

        winding_name = tk.Label(frame, text='Name', 
            fg='white', bg='grey', width=10)
        winding_name.grid(column=0, row=0)

        winding_turns = tk.Label(frame, text='Turns', 
            fg='white', bg='grey', width=10)
        winding_turns.grid(column=1, row=0)

        winding_layers = tk.Label(frame, text='Layers', 
            fg='white', bg='grey', width=10)
        winding_layers.grid(column=2, row=0)

        winding_size = tk.Label(frame, text='Size (AWG)', 
            fg='white', bg='grey', width=10)
        winding_size.grid(column=3, row=0)

    def add_Winding(self, winding, row):
        view_winding = {}
        for i, key in enumerate(winding.windingParameters):
            view_winding[key] = \
                tk.Entry(self.windingsFrame, width=10, 
                justify='right')
            view_winding[key].grid(column=i, row=row)

        self.view_Windings.append(view_winding)
        
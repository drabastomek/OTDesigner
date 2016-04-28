import tkinter as tk
import tkinter.ttk as ttk

class Winding(object):
    def __init__(self):
        self.name = None
        self.listOfParams = ['Name', 'Turns', 'Layers', 'AWG']
        self.widgets = []

    def add_winding(self, frame, row):
        # variable = tk.StringVar()
        label = tk.Entry(frame, width=10,
            # textvariable=variable,
            justify='center')
        label.grid(column=0, row=row)

        for i, param in enumerate(self.listOfParams[1:]):
            # variable = tk.IntVar()
            entry = tk.Entry(frame, width=10, 
                # textvariable=variable, 
                justify='right')
            entry.grid(column=i+1, row=row)

            self.widgets.append(entry)

    def add_named_winding(self, frame, name, row):
        self.name = name

        label = tk.Label(frame, text=name,
            width=10)
        label.grid(column=0, row=row)

        for i, param in enumerate(self.listOfParams[1:]):
            # variable = tk.IntVar()
            entry = tk.Entry(frame, width=10, 
                # textvariable=variable, 
                justify='right')
            entry.grid(column=i+1, row=row)

            # self.widgets.append((variable, entry))
            self.widgets.append(entry)

    def get_values(self):
        vals = []

        for widget in self.widgets:
            print(widget)


class View(tk.Toplevel):
    def __init__(self, master):
        tk.Toplevel.__init__(self, master)
        self.protocol('WM_DELETE_WINDOW', self.master.destroy)

        self.windings = []

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
        self.add_WindingsInput(self.windingsFrame)
        self.windingsFrame.grid(column=0, row=1, columnspan=2)

        self.windings_button = tk.Button(self.windingsFrame,
            text=u"Click me!"
            , command=self.add_Winding
            )
        self.windings_button.grid(column=0,row=4, columnspan=4)

        
    def add_BobbinInput(self, frame):
        # width
        bobbin_width_label = tk.Label(frame, text='Width:')
        bobbin_width_label.grid(column=0, row=1, sticky='ew')

        bobbin_width_inputVar = tk.IntVar()
        bobbin_width_input = tk.Entry(frame, width=11, 
            textvariable=bobbin_width_inputVar, 
            justify='right')
        bobbin_width_input.grid(column=1, row=1)

        # height
        bobbin_height_label = tk.Label(frame, text='Height:')
        bobbin_height_label.grid(column=0, row=2)

        bobbin_height_inputVar = tk.IntVar()
        bobbin_height_input = tk.Entry(frame, width=11, 
            textvariable=bobbin_height_inputVar, 
            justify='right')
        bobbin_height_input.grid(column=1, row=2)

        # depth
        bobbin_depth_label = tk.Label(frame, text='Depth:')
        bobbin_depth_label.grid(column=0, row=3)

        bobbin_depth_inputVar = tk.IntVar()
        bobbin_depth_input = tk.Entry(frame, width=11, 
            textvariable=bobbin_depth_inputVar, 
            justify='right')
        bobbin_depth_input.grid(column=1, row=3)

        # lip
        bobbin_lip_label = tk.Label(frame, text='Lip:')
        bobbin_lip_label.grid(column=0, row=4)

        bobbin_lip_inputVar = tk.IntVar()
        bobbin_lip_input = tk.Entry(frame, width=11, 
            textvariable=bobbin_lip_inputVar, 
            justify='right')
        bobbin_lip_input.grid(column=1, row=4)

        # units
        bobbin_unit_label = tk.Label(frame, text='Units:')
        bobbin_unit_label.grid(column=0, row=5)

        bobbin_unit_inputVar = tk.IntVar()
        bobbin_unit_input = ttk.Combobox(frame, width=8, 
            textvariable=bobbin_unit_inputVar, 
            values=['in.','mm.'],
            state='readonly')
        bobbin_unit_input.grid(column=1, row=5)

        bobbin_unit_input.set('in.')

    def add_WindingsInput(self, frame):

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

        p = Winding()
        p.add_named_winding(frame, 'p', 1)
        self.windings.append(p)

        s = Winding()
        s.add_named_winding(frame, 's', 2)
        self.windings.append(s)

    def add_Winding(self):
        n = Winding()
        n.add_winding(self.windingsFrame, len(self.windings) + 1)
        self.windings.append(n)

        
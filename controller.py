import model
import view

class Controller:
    def __init__(self, root):
        self.model = model.Model()
        self.view = view.View(root)

        self.view.checkButton.config(command=self.check)

        self.add_BobbinControl()
        
    def check(self):
        self.model.getBobbinValues()

    def add_BobbinControl(self):
        for key in self.view.bobbinKeys:
            self.model.model_bobbin[key] \
                .addCallback(self.valueChanged)

            self.view.view_Bobbin[key].bind(
                '<FocusOut>', 
                lambda event, k=key:
                    self.update_Bobbin(event, k)    
            )

            self.view.view_Bobbin[key].bind(
                '<Return>',  
                lambda event, k=key:
                    self.update_Bobbin(event, k)    
            )

            self.valueChanged(key, 
                self.model.model_bobbin[key].get())

        # units
        self.view.view_Bobbin['units'].bind(
            '<<ComboboxSelected>>', 
            lambda event, k='units':
                    self.update_Bobbin(event, k)   
        )

        self.valueChanged('units', 
            self.model.model_bobbin['units'].get())

    def update_Bobbin(self, even, key):
        self.model.setBobbinValue(key, 
            self.view.view_Bobbin[key].get())

    def valueChanged(self, key, value):
        self.view.set_BobbinInput(key, value)

    def add_Winding(self):
        n = Winding()
        n.add_winding(self.windingsFrame, len(self.windings) + 1)
        self.windings.append(n)
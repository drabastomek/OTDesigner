import model
import view

class Controller:
    def __init__(self, root):
        self.model = model.Model()
        self.view = view.View(root)

        # self.view.checkButton.config(command=self.check)

        self.view.windings_button.config(
            command=self.add_Winding)

        self.add_BobbinControl()
        
    def check(self):
        self.model.getBobbinValues()

    def add_BobbinControl(self):
        for key in self.view.bobbinKeys:
            self.model.model_Bobbin[key] \
                .addCallback(self.valueChanged_Bobbin)

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

            self.valueChanged_Bobbin(key, 
                self.model.model_Bobbin[key].get())

        # units
        self.view.view_Bobbin['units'].bind(
            '<<ComboboxSelected>>', 
            lambda event, k='units':
                    self.update_Bobbin(event, k)   
        )

        self.valueChanged_Bobbin('units', 
            self.model.model_Bobbin['units'].get())

    def update_Bobbin(self, even, key):
        self.model.setBobbinValue(key, 
            self.view.view_Bobbin[key].get())

    def valueChanged_Bobbin(self, key, value):
        self.view.set_BobbinInput(key, value)

    def add_Winding(self):
        winding, row = self.model.add_Winding()

        self.view.add_Winding(winding, row+1)
        
    def buttonTest(self):
        print('Testing')
    # def add_Winding(self):
    #     n = Winding()
    #     n.add_winding(self.windingsFrame, len(self.windings) + 1)
    #     self.windings.append(n)
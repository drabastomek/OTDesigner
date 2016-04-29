import model
import view

class Controller:
    def __init__(self, root):
        self.model = model.Model()
        self.model.model_bobbin['width'].addCallback(self.valueChanged)

        self.view = view.View(root)

        self.view.checkButton.config(command=self.check)

        self.bobbin_cbs = ['width', 'height', 'depth', 'lip']

        for key in self.bobbin_cbs:
            self.model.model_bobbin[key] \
                .addCallback(self.valueChanged)

            self.view.view_bobbin[key].bind(
                '<FocusOut>', 
                lambda event, k=key:
                    self.update_Bobbin(event, k)    
            )

            self.view.view_bobbin[key].bind(
                '<Return>',  
                lambda event, k=key:
                    self.update_Bobbin(event, k)    
            )

            self.valueChanged(key, 
                self.model.model_bobbin[key].get())

        self.view.view_bobbin['units'].bind(
            '<<ComboboxSelected>>', self.update_BobbinUnits   
        )

        self.valueChanged('units', 
            self.model.model_bobbin['units'].get())
        
    def check(self):
        self.model.getBobbinValues()
        # print('checked')

    def update_Bobbin(self, even, key):
        self.model.setBobbinValue(key, 
            self.view.view_bobbin[key].get())

    def valueChanged(self, key, value):
        self.view.set_bobbinInput(key, value)

    def add_Winding(self):
        n = Winding()
        n.add_winding(self.windingsFrame, len(self.windings) + 1)
        self.windings.append(n)
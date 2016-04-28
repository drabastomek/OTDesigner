import model
import view

class Controller:
    def __init__(self, root):
        self.model = model.Model()
        self.model.model_bobbin['width'].addCallback(self.valueChanged)

        self.view = view.View(root)

        self.view.checkButton.config(command=self.check)

        self.bobbin_cbs = {
            'width': self.update_BobbinWidth,
            'height': self.update_BobbinHeight,
            'depth': self.update_BobbinDepth,
            'lip': self.update_BobbinLip
        }

        for key in self.bobbin_cbs:
            self.model.model_bobbin[key].addCallback(self.valueChanged)

            self.view.view_bobbin[key].bind(
                '<FocusOut>', self.bobbin_cbs[key]    
            )

            self.view.view_bobbin[key].bind(
                '<Return>', self.bobbin_cbs[key]    
            )

            self.valueChanged(key, 
                self.model.model_bobbin[key].get())

        self.view.view_bobbin['units'].bind(
            '<<ComboboxSelected>>', self.update_BobbinUnits   
        )

        self.valueChanged('units', 
            self.model.model_bobbin['units'].get())
        # for key in self.model.model_bobbin:
        #     print(key)

        # ButtonRelease-1
        
    def check(self):
        self.model.getBobbinValues()
        # print('checked')

    def update_BobbinWidth(self, event):
        print(event.widget)
        self.model.setBobbinValue('width', 
            self.view.view_bobbin['width'].get())

    def update_BobbinHeight(self, event):
        self.model.setBobbinValue('height', 
            self.view.view_bobbin['height'].get())

    def update_BobbinDepth(self, event):
        self.model.setBobbinValue('depth', 
            self.view.view_bobbin['depth'].get())

    def update_BobbinLip(self, event):
        self.model.setBobbinValue('lip', 
            self.view.view_bobbin['lip'].get())

    def update_BobbinUnits(self, event):
        self.model.setBobbinValue('units', 
            self.view.view_bobbin['units'].get())

    def valueChanged(self, key, value):
        self.view.set_bobbinInput(key, value)

    # def AddMoney(self):
    #     self.model.addMoney(10)

    # def RemoveMoney(self):
    #     self.model.removeMoney(10)

    # def MoneyChanged(self, money):
    #     # self.view1.SetMoney(money)
    #     pass

    def add_Winding(self):
        n = Winding()
        n.add_winding(self.windingsFrame, len(self.windings) + 1)
        self.windings.append(n)
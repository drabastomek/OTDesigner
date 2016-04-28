import model
import view

class Controller:
    def __init__(self, root):
        self.model = model.Model()
        self.model.bobbin['width'].addCallback(self.valueChanged)
        # self.model.myMoney.addCallback(self.MoneyChanged)
        

        self.view = view.View(root)

        self.view.checkButton.config(command=self.check)

        self.view.bobbin_width_input.bind("<FocusOut>", 
            self.updateBobbinWidth)
        self.view.bobbin_width_input.bind("<Return>", 
            self.updateBobbinWidth)
        # self.view2 = view.ChangerWidget(self.view1)
        # self.view2.addButton.config(command=self.AddMoney)
        # self.view2.removeButton.config(command=self.RemoveMoney)
        # self.MoneyChanged(self.model.myMoney.get())
        self.valueChanged('width', self.model.bobbin['width'].get())

        # for key in self.model.bobbin:
        #     print(key)
        
    def check(self):
        self.model.getBobbinValues()
        # print('checked')

    def updateBobbinWidth(self, event):
        self.model.setBobbinValue('width', self.view.bobbin_width_input.get())

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
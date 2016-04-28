import observable as ob

class Model:
    def __init__(self):
        self.bobbin = {
            'width': ob.Observable('width', 0), 
            'height': ob.Observable('height', 0), 
            'depth': ob.Observable('depth', 0), 
            'lip': ob.Observable('lip', 0),
            'units': ob.Observable('units', 0)
        }

    def setBobbinValue(self, key, value):
        self.bobbin[key].set(value)

    def getBobbinValues(self):
        print(self.bobbin['width'].get())
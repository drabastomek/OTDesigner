import observable as ob

class Model:
    def __init__(self):
        self.model_bobbin = {
            'width': ob.Observable('width', 0), 
            'height': ob.Observable('height', 0), 
            'depth': ob.Observable('depth', 0), 
            'lip': ob.Observable('lip', 0),
            'units': ob.Observable('units', 'in.')
        }

    def setBobbinValue(self, key, value):
        self.model_bobbin[key].set(value)

    def getBobbinValues(self):
        outStr = []

        for key in self.model_bobbin:
            outStr.append('{0}: {1}'.format(key, self.model_bobbin[key].get()))
        # print(self.model_bobbin['width'].get())
        print(', '.join(outStr))
        # print('{0}'.format('width'))
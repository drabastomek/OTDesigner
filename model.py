import observable as ob

class Winding(object):
    def __init__(self):  
        self.windingParameters = [
            'name', 'turns', 'layers', 'awg'
        ]  
        
        self.params = {}
        self.params['name'] = ob.Observable('name', None)

        for w in self.windingParameters[1:]:
            self.params[w] = ob.Observable(w, 0)

class Model:
    def __init__(self):
        self.model_Bobbin = {
            'width': ob.Observable('width', 0), 
            'height': ob.Observable('height', 0), 
            'depth': ob.Observable('depth', 0), 
            'lip': ob.Observable('lip', 0),
            'units': ob.Observable('units', 'in.')
        }

        self.model_Windings = []

    def setBobbinValue(self, key, value):
        self.model_Bobbin[key].set(value)

    def getBobbinValues(self):
        outStr = []

        for key in self.model_Bobbin:
            outStr.append('{0}: {1}'.format(key, self.model_Bobbin[key].get()))
        print(', '.join(outStr))

    def add_Winding(self):
        w = Winding()
        self.model_Windings.append(w)
        return (self.model_Windings[-1], 
            len(self.model_Windings))

    def get_Winding(self, index):
        return self.model_Windings[index]

    def set_WindingValue(self, index, key, value):
        self.model_Windings[index].params[key].set(value)

    def getWindingsValues(self):

        for i, winding in enumerate(self.model_Windings):
            outStr = []

            for key in winding.windingParameters:
                outStr.append('{0}: {1}'.format(key, 
                    winding.params[key].get()))

            print('Winding {0}: '.format(i) + ', '.join(outStr))
import random

class Colour():
    '''
    Base class for generating colours. Classes created from this need to
    implement an __init__ method and a generate_css method. 
    
    The __init__ method needs to define a self.type and self.data param.
    self.type is just the name of the colour type, and the self.data param
    defines how each part of the colour gets generated. It needs to be in a
    format like:
    self.data = {
        'red': {
            'generate': self.generate_function,
            'inputs': {'min': 0, 'max': 10}
        },
        ...
    }

    To generate a colour, it will iterate over each key in the self.data
    dictionary and call its 'generate' function with the 'inputs' as kwargs.

    The generate_css method needs to be able to take this generated data and
    create a css string.
    
    A subclass object represents different ways of generating a colour. These
    objects dont store the generated colours anywhere.
    '''

    def __init__(self):
        raise NotImplementedError()


    def generate_new(self):
        '''
        Go through each key in self.data and call its generate function with
        given inputs.  The output will be a dict with the same keys and
        self.data but the value is the value returned from the generate
        function.

        Assumed the colour has been defined both in self.type and self.data.
        '''

        output = {}
        for param in self.data:
            generate = self.data[param]['generate']
            inputs = self.data[param]['inputs']

            output[param] = generate(**inputs)
        
        return output


    def rand_int(self, min, max) -> int:
        return random.randint(min, max)
    

    def rand_float(self, min, max) -> float:
        return random.uniform(min, max)


    def generate_css(self) -> str:
        raise NotImplementedError()


    def generate_json(self, data=None):
        '''
        Creates a dict representing all the information of a colour. Can
        optionally take in colour data or generate its own data.
        '''

        if data is None:
            data = self.generate_new()
        
        return {
            'type': self.type,
            'data': data,
            'css': self.generate_css(data=data)
        }


class Rgb(Colour):
    def __init__(self):
        self.type = "rgb"
        self.data = {
            'red': {
                'generate': self.rand_int,
                'inputs': {'min': 0, 'max': 255}
            },
            'green': {
                'generate': self.rand_int,
                'inputs': {'min': 0, 'max': 255}
            },
            'blue': {
                'generate': self.rand_int,
                'inputs': {'min': 0, 'max': 255}
            }
        }
    

    def generate_css(self, data=None) -> str:
        if data is None:
            data = self.generate_new()
        
        return f'rgb({data["red"]}, {data["green"]}, {data["blue"]})'


class Hsl(Colour):
    def __init__(self):
        self.type = "hsl"
        self.data = {
            'hue': {
                'generate': self.rand_int,
                'inputs': {'min': 0, 'max': 359}
            },
            'saturation': {
                'generate': self.rand_int,
                'inputs': {'min': 0, 'max': 100}
            },
            'lightness': {
                'generate': self.rand_int,
                'inputs': {'min': 0, 'max': 100}
            }
        }


    def generate_css(self, data=None) -> str:
        if data is None:
            data = self.generate_new()
        
        return f'hsl({data["hue"]}, {data["saturation"]}%, {data["lightness"]}%)'

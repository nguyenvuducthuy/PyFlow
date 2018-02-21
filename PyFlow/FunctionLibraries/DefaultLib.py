from ..Core.FunctionLibrary import *
from ..Core.AGraphCommon import *
import os


class DefaultLib(FunctionLibraryBase):
    '''
    Default library builting stuff, variable types and conversions
    '''
    def __init__(self):
        super(DefaultLib, self).__init__()

    @staticmethod
    @implementNode(returns=None, nodeType=NodeTypes.Callable, meta={'Category': 'DefaultLib', 'Keywords': ['print']})
    ## Python's 'print' function wrapper
    def pyprint(entity=(DataTypes.String, None)):
        '''
        printing a string
        '''
        print(entity)

    @staticmethod
    @implementNode(returns=None, nodeType=NodeTypes.Callable, meta={'Category': 'DefaultLib', 'Keywords': []})
    ## cls cmd call.
    def cls():
        '''cls cmd call.'''
        os.system('cls')

    @staticmethod
    @implementNode(returns=(DataTypes.Bool, False), meta={'Category': 'GenericTypes', 'Keywords': []})
    ## make simple boolean
    def makeBool(b=(DataTypes.Bool, False)):
        '''make simple boolean'''
        return b

    @staticmethod
    @implementNode(returns=(DataTypes.Int, 0), meta={'Category': 'GenericTypes', 'Keywords': []})
    ## make integer
    def makeInt(i=(DataTypes.Int, 0)):
        '''make integer'''
        return i

    @staticmethod
    @implementNode(returns=(DataTypes.Float, 0.0), meta={'Category': 'GenericTypes', 'Keywords': []})
    ## make floating point number
    def makeFloat(f=(DataTypes.Float, 0.0)):
        '''make floating point number'''
        return f

    @staticmethod
    @implementNode(returns=(DataTypes.String, ''), meta={'Category': 'GenericTypes', 'Keywords': []})
    ## make string
    def makeString(s=(DataTypes.String, '')):
        '''make string'''
        return s

    # Conversions
    @staticmethod
    @implementNode(returns=(DataTypes.Int, 0), meta={'Category': 'Conversion', 'Keywords': []})
    def boolToInt(b=(DataTypes.Bool, False)):
        return int(b)

    @staticmethod
    @implementNode(returns=(DataTypes.Bool, False), meta={'Category': 'Conversion', 'Keywords': []})
    def intToBool(i=(DataTypes.Int, 0)):
        return bool(i)

    @staticmethod
    @implementNode(returns=(DataTypes.Int, 0), meta={'Category': 'Conversion', 'Keywords': []})
    def floatToInt(f=(DataTypes.Float, 0.0)):
        return int(f)

    @staticmethod
    @implementNode(returns=(DataTypes.Float, 0.0), meta={'Category': 'Utils', 'Keywords': []})
    ## Returns the CPU time or real time since the start of the process or since the first call of clock()
    def clock():
        '''Returns the CPU time or real time since the start of the process or since the first call of clock().'''
        return time.clock()

    @staticmethod
    @implementNode(returns=(DataTypes.Bool, False), meta={'Category': 'Conversion', 'Keywords': []})
    def intToFloat(i=(DataTypes.Int, 0)):
        return float(i)

    @staticmethod
    @implementNode(returns=(DataTypes.String, ''), meta={'Category': 'Conversion', 'Keywords': []})
    def intToString(i=(DataTypes.Int, 0)):
        return str(i)

    @staticmethod
    @implementNode(returns=(DataTypes.String, ''), meta={'Category': 'Conversion', 'Keywords': []})
    def floatToString(f=(DataTypes.Float, 0.0)):
        return str(f)

    @staticmethod
    @implementNode(returns=(DataTypes.String, ''), meta={'Category': 'Conversion', 'Keywords': []})
    def boolToString(b=(DataTypes.Bool, str(False))):
        return str(b)

    @staticmethod
    @implementNode(returns=(DataTypes.String, ''), meta={'Category': 'Conversion', 'Keywords': []})
    def arrayToString(arr=(DataTypes.Array, [])):
        return str(arr)

    @staticmethod
    @implementNode(returns=(DataTypes.Int, 0), meta={'Category': 'DefaultLib', 'Keywords': []})
    def arrayLen(arr=(DataTypes.Array, [])):
        return len(arr)
#
# Author: jun10000 (https://github.com/jun10000)
#

class RISignal:
    @staticmethod
    def search_name(bits):
        riitems = {
            'PowerOn'      : '1110101010101001001001010010101001000',
            'PowerOff'     : '1110101010101001001001010010100101000',
            'TapeLeft'     : '11101010010100100100101010010100101000',
            'TapeStop'     : '111010100101001001001010101001001001000',
            'TapeRight'    : '11101010010100100100101010100100101000',
            'AlbumDown'    : '111010100101001001001010100100101001000',
            'AlbumUp'      : '11101010010100100100101010010010101000',
            'PlayListDown' : '1110101001010010010010101001001001001000',
            'PlayListUp'   : '111010100101001001001010100100100101000',
        }

        result = 'Unknown'
        for (name, signal) in riitems.items():
            if signal == bits:
                result = name
                break
        return result

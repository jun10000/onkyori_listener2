#
# Author: jun10000 (https://github.com/jun10000)
#

import settings

class RISignal:
    @staticmethod
    def search_name(bits):
        result = 'Unknown'
        for (name, signal) in settings.common['RISignals'].items():
            if signal == bits:
                result = name
                break
        return result

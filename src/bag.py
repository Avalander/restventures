import json

class bag:

    _reward = {}

    def __init__(self):
        pass

    def put(self, item):
        clau = ""
        valor = 0

        for k,v in item.items():
            clau = k
            valor = v

        if k in self._reward.keys():
            self._reward[k] = self._reward.get(k) + valor
        else:
            self._reward.update(item)


    def get_all(self):
        print(self._reward)

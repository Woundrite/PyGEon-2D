#This is a customised dictionary class cus the builtin one sucks...
class Dict():
    def __init__(self):
        self.keys = []
        self.values = []

    def __str__(self):
        self.returnMain = []
        for i in range(len(self.keys)):
            self.returnMain.append([str(self.keys[i]), str(self.values[i])])

        return str(self.returnMain)

    def __len__(self):
        return len(self.keys)

    def __getitem__(self, i):
        print(len(self.keys), i )
        return [self.keys[i], self.values[i]]

    def __setitem__(self, i, val):
        if len(val)==2 and type(val) == tuple:
            if i <= len(keys):
                if type(val) == type(self.keys[0]):
                    self.keys[i], self.values[i] = val
                else:
                    raise Exception("Cannot append {0} to type {1}".format(type(key), type(self.keys[0])))
        elif len(val)==2 and type(val) == list:
            if i <= len(keys):
                if type(val) == type(self.keys[0]):
                    self.keys[i] = val[0]
                    self.values[i] = val[1]
                else:
                    raise Exception("Cannot append {0} to type {1}".format(type(key), type(self.keys[0])))

    def get(self, key):
        for i in range(len(self.keys)):
            if key == self.keys[i]:
                return self.values[i]

    def append(self,key, value):
        self.keys.append(key)
        self.values.append(value)
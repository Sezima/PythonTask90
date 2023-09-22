class VersionManager:
    
    def __init__(self, version=None):
        if not version: version='0.0.1'
        self.__memory = []
        try:
            arr = [*map(int,version.split('.')[:3])] + [0,0,0]
        except:
            raise Exception("Error occured while parsing version!")
        del arr[3:]
        self.__version = arr if any(arr) else [0,0,1]
    
    def release(self):
        return '.'.join(map(str, self.__version))

    def rollback(self):
        if not self.__memory: raise Exception("Cannot rollback!")
        self.__version = self.__memory.pop()
        return self
        
    def __update(self, i):
        self.__memory.append([*self.__version])
        self.__version[i] += 1
        self.__version[i+1:] = [0] * (len(self.__version)-1-i)
        return self
    
    def major(self): return self.__update(0)
    def minor(self): return self.__update(1)
    def patch(self): return self.__update(2)

class LinealSearch:
    def search(self, data, target):
        for i, item in enumerate(data):
            if item == target:
                return i
        return -1
    
    def get_name(self):
        return "Búsqueda Lineal"
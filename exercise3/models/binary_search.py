
class BinarySearch:
    def search(self, data, target):
        low = 0
        high = len(data) - 1
        
        while low <= high:
            mid = (low + high) // 2
            if data[mid] == target:
                return mid
            elif data[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return -1
    
    def get_name(self):
        return "Búsqueda Binaria"
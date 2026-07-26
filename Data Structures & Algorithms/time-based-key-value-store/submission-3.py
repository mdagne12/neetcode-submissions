class TimeMap:

    def __init__(self):
        self.data_map = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.data_map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        # Contains all the (timestamp, value) pairs associated with a key
        values_arr = self.data_map[key] 

        left, right = 0, len(values_arr) - 1
        while left <= right:
            mid = (left + right) // 2

            if timestamp == values_arr[mid][0]:
                return values_arr[mid][1]

            elif timestamp < values_arr[mid][0]:
                right = mid - 1
            else:
                left = mid + 1

        return values_arr[right][1] if right >= 0 else ""
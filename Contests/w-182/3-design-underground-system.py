import collections


class UndergroundSystem:

    def __init__(self):
        self.__check_in = {}
        self.__time = collections.defaultdict(collections.Counter)
        self.__count = collections.defaultdict(collections.Counter)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        if id in self.__check_in:
            return
        self.__check_in[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        in_s, in_t = self.__check_in[id]
        del self.__check_in[id]
        self.__time[in_s][stationName] += (t - in_t)
        self.__time[stationName][in_s] += (t - in_t)
        self.__count[in_s][stationName] += 1
        self.__count[stationName][in_s] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.__time[startStation][endStation] / self.__count[startStation][endStation]


# Your UndergroundSystem object will be instantiated and called as such:
# undergroundSystem = UndergroundSystem()
# undergroundSystem.checkIn(45, "Leyton", 3)
# undergroundSystem.checkIn(32, "Paradise", 8)
# undergroundSystem.checkIn(27, "Leyton", 10)
# undergroundSystem.checkOut(45, "Waterloo", 15)
# undergroundSystem.checkOut(27, "Waterloo", 20)
# undergroundSystem.checkOut(32, "Cambridge", 22)
# undergroundSystem.getAverageTime("Paradise", "Cambridge")
# undergroundSystem.getAverageTime("Leyton", "Waterloo")
# undergroundSystem.checkIn(10, "Leyton", 24)
# undergroundSystem.getAverageTime("Leyton", "Waterloo")
# undergroundSystem.checkOut(10, "Waterloo", 38)
# undergroundSystem.getAverageTime("Leyton", "Waterloo")



# Running Test Case 2

# undergroundSystem = UndergroundSystem()
# instructoin = ["checkIn", "checkIn", "checkOut", "checkIn", "getAverageTime", "getAverageTime", "checkOut", "checkOut",
#                "checkIn", "checkIn", "checkIn", "checkOut", "checkIn", "getAverageTime", "checkOut", "getAverageTime",
#                "checkOut", "checkIn"]
# values = [[653777, "V3BOL9LF", 71], [34036, "EFB2ARPR", 86], [34036, "SEKKQ7KR", 169], [476790, "U54HBTYV", 223],
#           ["EFB2ARPR", "SEKKQ7KR"], ["EFB2ARPR", "SEKKQ7KR"], [476790, "SEKKQ7KR", 226], [653777, "K2618O72", 255],
#           [680009, "U54HBTYV", 342], [691876, "1DTINDTE", 352], [779975, "0QIA9CN3", 374], [691876, "WGN1M5GY", 412],
#           [18036, "ZSBKMUIV", 467], ["V3BOL9LF", "K2618O72"], [779975, "W858PECF", 485], ["U54HBTYV", "SEKKQ7KR"],
#           [18036, "V6QXVVHS", 516], [141921, "9GUC0EYJ", 533]]
#
# for i in range(len(instructoin)):
#     if instructoin[i] == 'checkIn':
#         undergroundSystem.checkIn(values[i][0], values[i][1], values[i][2])
#     elif instructoin[i] == 'checkOut':
#         undergroundSystem.checkOut(values[i][0], values[i][1], values[i][2])
#     else:
#         undergroundSystem.getAverageTime(values[i][0], values[i][1])

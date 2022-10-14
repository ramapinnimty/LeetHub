class UndergroundSystem:

    def __init__(self):
        '''
        1. Maintain a dict to log and update all the trips from S_start to S_end
            --> {(S_start, S_end): [num_trips, total_time]}
        2. Maintain a dict to keep track of users check-in & check-out
            --> {id: (S_start, t)}
        '''
        self.station_trips = {}
        self.user_log      = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        # Add the user check-in info.
        self.user_log[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        # Get the check-in info. of the user
        startStation, startTime = self.user_log[id][0], self.user_log[id][1]
        # Calculate the total trip time
        tripTime = t - startTime
        # Delete the user after check-out
        del self.user_log[id]

        # Add the trip and related info. to the trips
        if (startStation, stationName) in self.station_trips:
            # Update if already exists
            self.station_trips[(startStation, stationName)][0] += 1
            self.station_trips[(startStation, stationName)][1] += tripTime
        else:
            # Add if doesn't exist
            self.station_trips[(startStation, stationName)] = [1, tripTime]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        numTrips, totalTime = self.station_trips[(startStation, endStation)]

        return totalTime / numTrips


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
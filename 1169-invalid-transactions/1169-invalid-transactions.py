class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        invalid_trs = []
        # STEP-1: Create a HashMap {time: {name: set(1 or more cities)}}
        times_dict = {}
        for tr in transactions:
            # Extract and convert
            name, time, amount, city = tr.split(',')
            time, amount = int(time), int(amount)
            # CHECK-1: If time doesn't already exist
            if time not in times_dict:
                times_dict[time] = {name: set([city])}
            else:
                # CHECK-2: If name doesn't already exist
                if name not in times_dict[time]:
                    times_dict[time][name] = set([city])
                else:
                    # If time & name already exist, simply add to the cities set
                    times_dict[time][name].add(city)

        # STEP-2: Evaluate all the transactions by checking `times_dict`
        for tr in transactions:
            name, time, amount, city = tr.split(',')
            time, amount = int(time), int(amount)
            # CONSTRAINT-1: Check if the amount is greater than 1000
            if amount > 1000:
                invalid_trs.append(tr)
                continue # don't check anything further, move onto next tr
            # CONSTRAINT-2: Check if one tr occurs before/after 60 minutes of another tr
            for t in range(time-60, time+60):
                # Move onto the next tr if time not available
                if t not in times_dict:
                    continue
                if name not in times_dict[t]:
                    continue
                if len(times_dict[t][name]) > 1 \
                    or (next(iter(times_dict[t][name])) != city):
                    invalid_trs.append(tr)
                    break

        return invalid_trs
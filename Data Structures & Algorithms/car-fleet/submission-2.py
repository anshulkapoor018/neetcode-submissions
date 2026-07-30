class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Process cars from closest to target to farthest.
        # A car behind can only merge with a fleet ahead of it.
        cars = sorted(zip(position, speed), reverse=True)

        # Stack stores the arrival time of each distinct fleet.
        st = []

        for pos, spd in cars:
            time = (target - pos) / spd
            st.append(time)

            # If the car behind reaches the target sooner than or
            # at the same time as the fleet ahead, it will catch up
            # before reaching the target and merge into that fleet.
            if len(st) >= 2 and st[-1] <= st[-2]:
                st.pop()

        # Each remaining arrival time represents one distinct fleet.
        return len(st)
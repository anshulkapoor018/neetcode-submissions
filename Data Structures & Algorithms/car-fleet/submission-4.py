class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)

        st = []

        for pos, sp in cars:
            time = (target - pos) / sp
            st.append(time)

            if len(st) >= 2 and st[-1] <= st[-2]:
                st.pop()

        return len(st) 
            
        
        
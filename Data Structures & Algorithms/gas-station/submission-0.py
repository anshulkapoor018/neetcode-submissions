class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # each station contributes GAS - outgoing Travel cost

        total = tank = 0
        start = 0
        for i, (fuel, price) in enumerate(zip(gas, cost)):
            delta = fuel - price
            total += delta
            tank += delta
            if tank < 0:
                start = i + 1
                tank = 0
        
        return start if total >= 0 else -1
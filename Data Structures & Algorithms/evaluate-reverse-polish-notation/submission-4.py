class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = set(['+', '-', '*', '/'])
        st = []

        for i in tokens:
            if i in operators and len(st) >= 2:
                a = int(st.pop())
                b = int(st.pop())
                
                if i == "+":
                    st.append(a + b)
                elif i == "-":
                    st.append(b - a)
                elif i == "*":
                    st.append(a * b)
                elif i == "/":
                    st.append(int(b / a))
            else:
                st.append(int(i))
            
        return st[-1]

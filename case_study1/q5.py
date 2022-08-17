class Stringclass:
    def __init__(self):
        self.s=""

    def getString(self):
        self.s=input("enter the string : ")

    def printString(self):
        k=self.s.upper()
        print(k)

st=Stringclass()

st.getString()
st.printString()

def compoundInterest(principle, time, rate):
    print("Principle is : ",principle)
    print("Time is      : ",time)
    print("Rate is      : ",rate)
    A=principle*pow((1+rate/100),time)
    CI=A-principle
    print("compound Interest is : ",CI)
compoundInterest(1200,2,5.4)

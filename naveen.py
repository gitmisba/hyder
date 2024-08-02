class date:
    def __init__(self , a,b,c):
        self.d=a
        self.m=b
        self.y=c

    def day(self):
        print("days=",self.d)

    def month(self):
        print("month=",self.m)

    def year(self):
        print("year=",self.y)

    def monthname(self):
        months=["unknown","january","february","march","april","may","june","july","august","september","october","november","december"]
        print("month name:",months[self.m])

d1=date(5,2,2024)
d1.day()
d1.month()
d1.year()
d1.monthname()

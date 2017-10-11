from day12.druzyna import Druzyna

team1 = Druzyna("Huragan Polaszki", "Małoznany")

print(team1.budzet)
print(team1.transfery)

team1.budzet = 10000
print(team1.budzet)

team1.transfery = "kowalski"
team1.transfery = ["lewy", "ronaldo"]
print(team1.transfery)


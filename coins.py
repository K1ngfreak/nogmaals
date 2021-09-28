# name of student: Noah Zonneveld
# number of student:  99068856
# purpose of program: Munten inwisselen
# function of program:  School opdracht
# structure of program: Python

i = True
amountToPay = float(input('Amount to pay: '))

while i == True:
  toPay = int(amountToPay * 100) # vraagt hoeveel het in totaal kost
  paid = int(float(input('Paid amount: ')) * 100) # vraagt hoeveel er is betaald
  change = paid - toPay # rekent uit hoeveel er terug moet worden gegeven

  if change > 0: # als de value meer dan 0 is ga je geld terug geven
    coinValue = 500 # starting value

    while change > 0 and coinValue > 0: #
      nrCoins = change // coinValue #

      if nrCoins > 0: #
        print('return maximal ', nrCoins, ' coins of ', coinValue, ' cents!' ) #
        nrCoinsReturned = int(input('How many coins of ' + str(coinValue) +  ' cents did you return? ')) #
        change -= nrCoinsReturned * coinValue #

# comment on code below: 
      if coinValue == 500:
        coinValue = 300
      elif coinValue == 300:
        coinValue = 200
      elif coinValue == 200:
        coinValue = 50
      elif coinValue == 50:
        coinValue = 20
      elif coinValue == 20:
        coinValue = 10
      elif coinValue == 10:
        coinValue = 5
      elif coinValue == 5:
        coinValue = 2
      elif coinValue == 2:
        coinValue = 1
      else:
        coinValue = 0

  if change > 0: #
    print('Change not returned: ', str(change) + ' cents')
    i = False
  elif change < 0:
    n = change * 2
    change = change - n
    change = change / 100
    print('nog te betalen: ' + str(change) + ' euro')
    amountToPay = change
    i = True
  else:
    print('done')
    i = False
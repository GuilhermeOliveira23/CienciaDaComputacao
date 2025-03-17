seconds = int(input("Digite uma quantia de segundos:\n "))

def convertSeconds(seconds):

  minutes =  seconds / 60
  hours = seconds / 3600
  days = seconds / 86400

  print(f"Minutos: {minutes:.2f}\nHoras: {hours:.2f}\nDias: {days:.2f}")
  return minutes, hours, days
  

convertSeconds(seconds)

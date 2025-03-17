# conversor de celsius para farenheit e kelvin

tipoTemperatura = input("Escolha a medida de temperatura que deseja converter(Fahrenheit ou Celsius)\n")
temperatura = int(input("Insira o valor da temperatura: \n"))
converterPara = input("Agora insira a medida de temperatura que deseja converter para: (Fahrenheit ou Celsius)\n")

if tipoTemperatura == "Fahrenheit" and converterPara == "Celsius":
    
  temperatura =  (temperatura - 32) * 5/9
  print(f"Temperatura convertida para {converterPara}: {temperatura:.0f}") 
  
elif tipoTemperatura == "Celsius" and converterPara == "Fahrenheit":
  
    temperatura = (temperatura * 9/5) + 32 
    print(f"Temperatura convertida para {converterPara}: {temperatura:.0f}")

else:
   
   print("Não é possível converter para o mesmo tipo de temperatura!!!")
    
   


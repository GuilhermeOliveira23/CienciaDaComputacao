from datetime import datetime
import locale
locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')
dt_input= input("Data:")
dt = datetime.strptime(dt_input,"%d/%m/%Y")
print(f"{dt.day} de {dt.strftime("%B")} de {dt.year}")


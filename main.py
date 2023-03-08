print('Conversor de temperatura')
op = float(
  input(
    "Que tipo de temperatura dejesa usar: (1)Celsius (2)Fahrenheit (3)Kelvin (4)Rankine"
  ))
if op == 1:
  Temp = int(input("Digite a temperatura em Celsius"))
  op2 = float(
    input(
      "para qual temperatura deseja converter? (1)Fahrenheit,(2)Kelvin,(3)Rankine "
    ))
  if op2 == 1:
    c = Temp
    f = (c * 9 / 5) + 32
    print(f"{c}°C é equivalente a {f}°F.")
  elif op2 == 2:
    c = Temp
    k = c + 273
    print(f"{c}°C é equivalente a {k}K.")
  elif op2 == 3:
    c = Temp
    r = (c * 1.8) + 273
    print(f"{c}°C é equivalente a {r}R.")
  else:
    print("Nao ha esta opcao")

elif op == 2:
  Temp = int(input("Digite a temperatura em Fahrenheit"))
  op2 = float(
    input(
      "para qual temperatura deseja converter? (1)Celcius,(2)Kelvin,(3)Rankine "
    ))
  if op2 == 1:
    f = Temp
    c = ((f / 9) / 5) - 32
    print(f"{f}°F é equivalente a {c}°C.")
  elif op2 == 2:
    f = Temp
    k = ((f - 32) * 5 / 9) + 273
    print(f"{f}°F é equivalente a {k}K.")
  elif op2 == 3:
    f = ((Temp / 9) / 5) - 32
    r = (f * 1.8) + 273
    print(f"{Temp}°F é equivalente a {r} R.")
  else:
    print("Nao ha esta opcao")

elif op == 3:
  Temp = int(input("Digite a temperatura em Kelvin"))
  op2 = float(
    input(
      "para qual temperatura deseja converter? (1)Celcius,(2)Fahrenheit,(3)Rankine "
    ))
  if op2 == 1:
    k = Temp
    c = k - 273
    print(f"{k}K é equivalente a {c}°C.")
  elif op2 == 2:
    k = Temp
    f = (k - 273) * 9 / 5 + 32
    print(f"{k} K é equivalente a {f}°F.")
  elif op2 == 3:
    k = Temp - 273
    r = (k * 1.8) + 273
    print(f"{Temp}K é equivalente a {r} R.")
  else:
    print("Nao ha esta opcao")

elif op == 4:
  Temp = int(input("Digite a temperatura em Rankine"))
  op2 = float(
    input(
      "para qual temperatura deseja converter? (1)Celcius,(2)Fahrenheit,(3)Kelvin "
    ))
  if op2 == 1:
    r = Temp
    c = (r / 1.8) - 273.15
    print(f"{r}R é equivalente a {c}°C.")
  elif op2 == 2:
    r = (Temp / 1.8) - 273.15
    f = (r * 9 / 5) + 32
    print(f"{r}R é equivalente a {f}°F.")
  elif op2 == 3:
    r = (Temp / 1.8) - 273.15
    k = r + 273
    print(f"{r}R é equivalente a {k} K.")
  else:
    print("Nao ha esta opcao")

else:
  print("Nao ha essa opcao")

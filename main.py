st = input("Введите строку, которую необходимо зашифровать: ")

prob = {
  "" : 0 #левая граница
}

abc = sorted(set(st))
leng = len(st)
diff = 0
for a in abc:
  prob[a] = diff + st.count(a)/leng
  diff = prob[a]

probCalc = prob.copy()
for s in st:
  print("\n"+s)
  before_index = list(probCalc.keys()).index(s) - 1
  probCalc[""] = probCalc[list(probCalc.keys())[before_index]]
  dlina = probCalc[s] - probCalc[""]

  print("Левая граница: ", probCalc[""])
  for elem in probCalc:
    if elem != "":
      probCalc[elem] = round(dlina * prob[elem] + probCalc[""], 14)
      print(elem, probCalc[elem])
  print()

before_index = list(probCalc.keys()).index(st[-1]) - 1
probCalc[""] = probCalc[list(probCalc.keys())[before_index]]
print("\nОтвет:", round(probCalc[""] + (probCalc[st[-1]] - probCalc[""]) / 2, 14))


target = float(input("\n ======\n РАСШИФРОВКА с помощью вероятности: "))
stopznak = input("\nВведите стоп-символ - знак, после которого необходимо остановиться расшифровывать: ")
prob = {
  "": 0
}
print("\nВводите символы и их вероятность, \nПОСЛЕДНИМ введите тот же стоп-символ с его вероятностью: ")

key = ""
sum = 0
while (key != stopznak):
  key = input("\nСимвол: ")
  prob[key] = float(input("Значение: "))

prob = dict(sorted(prob.items()))
value = 0
for elem in prob:
  prob[elem] += value
  value = prob[elem]

probCalc = prob.copy()

code = [""]
while (code[-1] != stopznak):
  print("Левая граница: ", probCalc[""])
  for elem in probCalc:
    if elem != "":
      print(elem, ":", probCalc[elem])
  
  for elem in probCalc:
    if target <= float(probCalc[elem]):
      print("Символ: ", elem, "\n")
      right_gran = elem
      break
  code.append(right_gran)

  before_index = list(probCalc.keys()).index(right_gran) - 1
  probCalc[""] = probCalc[list(probCalc.keys())[before_index]]
  dlina = probCalc[right_gran] - probCalc[""]

  for elem in probCalc:
      if elem != "":
        probCalc[elem] = round(dlina*prob[elem] + probCalc[""], 14)

print("Расшифрованная последовательность: ","".join(code))
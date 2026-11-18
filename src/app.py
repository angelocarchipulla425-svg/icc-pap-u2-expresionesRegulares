import re


def main():
    runEjemplo1()
    print("-" * 30)
    runEjemplo2()
    print("-" * 30)
    runEjemplo3()


def runEjemplo1():
  patron = r"ab*"
  palabras = ["a", "ab", "abbb", "abab", "b", ""]
  for p in palabras:
    # re.fullmatch verifica que coincida toda la cadena (equivalente a .matches() en Java)
    coincide = bool(re.fullmatch(patron, p))
    print(f"{p} -> {coincide}")


def runEjemplo2():
  regex = r"[TO][0-9]{3}"
  lista = ["T001", "0120", "T01", "X001", "T0001"]
  for codigo in lista:
    coincide = bool(re.fullmatch(regex, codigo))
    print(f"{codigo} => {coincide}")


def runEjemplo3():
  texto = (
      "Sensores: T001 reporta 23.5 C; O001 reporta 12 PERSONAS; T002 reporta -2"
      " C;"
  )
  patron = r"[TO][0-9]{3}"
  # re.finditer busca todas las coincidencias dentro del texto (equivalente a while(matcher.find()))
  for match in re.finditer(patron, texto):
    print(f"Encontrado: {match.group()}, posición: {match.start()}")


if __name__ == "__main__":
    main()
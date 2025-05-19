Dodge_Challenger_Demon_170 = {
    "carro": "Dodge Challenger Demon 170",
    "preço": 1939000,
    "marca": "Dodge",
    "data de lançamento": "22 de dezembro de 2023"
}

Nissan_Skyline = {
    "carro": "Nissan Skyline:",
    "preço": 2980000,
    "marca": "Nissan",
    "data de lançamento": "Janeiro de 1999"
}

Lamborghini_Aventador = {
    "carro": "Lamborghini Aventador:",
    "preço": 8917403,
    "marca": "Lamborghini",
    "data de lançamento": "28 de fevereiro de 2011"
}

lista = [Dodge_Challenger_Demon_170, Nissan_Skyline, Lamborghini_Aventador]
for cachorro in lista:
    for chave, valor in cachorro.items():
        print(f" {chave}: {valor}")
    print("")

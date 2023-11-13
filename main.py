print("Este diccionario dispone de varias palabras de las nuevas generaciones que les pueden servir a ustedes personas mayores a enterder mejor a sus hijos, y darles la mejor y mas feliz infancia.")
print("   ")
print("   ")
meme_dict= {
            "CRINGE": "| Algo excepcionalmente raro o embarazoso |",
            "LOL": "| Una respuesta común a algo gracioso |",
            "CREEPY": "| Algo aterrador, hasta el punto de ser siniestro |",
            }

word= input("Escriba su selección: ")

if word in meme_dict.keys():
    print("   ")
    print("RESPUESTA:")
    print(meme_dict[word])

else:
    print("   ")
    print("Esa palabra no ha sido encontrada, revise si esta bien escrita e intentelo de nuevo.")
    print("Recuerde que la palabra tiene que estar escrita completamente en mayúsculas: Ejemplo: LOL")

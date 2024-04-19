def get_at_content(dna,num): 
    dna = dna.replace ('N','')
    length = len(dna) 
    a_count = dna.count('A') 
    t_count = dna.count('T') 
    at_content = (a_count + t_count) / length 
    return round (at_content,2) # Redondea dos decimales


at_content = get_at_content("ATGACTGGACCA", 2)
# print("ATGACTGGACCA" + ": " + str(at_content))
# print("AT content ATGACTGGACCA  is " + str(get_at_content("ATGACTGGACCA", 4)))
# print(get_at_content("ATGCGCGAATCG", 2)) #paso arg por posicion
# print (get_at_content("aaatatt", 4))

# print (get_at_content(dna="TATGACAGTA",num=2)) # orden no importa siemrpe y cuando se use el nombre de los parametros
# print (get_at_content(num=1,dna="TATGACAGTA")) # argumentos por palabras clave 
# print (get_at_content("ATGACTGGACCA",num=1)) # a rg por posicion y por nombre
# print (get_at_content(dna="agacaga",2)) # argumentos posicionales deben ir primero

# assert get_at_content("ATGC",2) == 0.5 # ok no regresa nada
# assert get_at_content("ATGC",2) == 0.4 # assert manda error 
# falso 
assert get_at_content ("ATCGNNNNNN",2) == 0.5 # error si cuenta Ns las cuenta para el tamaño de secuencia

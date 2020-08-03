def palabra_rep(frase):
    	conteo = 0
	lista = frase.split()
		for index in lista:
			if palabra==lista[index]:
				conteo +=1
				
				if conteo == 2:
					pos_pal = index
					new_list = lista[pos_pal].split()
			else:
			return -1
		return new_list

palabra_rep("estan lloviendo gatos y gatos")

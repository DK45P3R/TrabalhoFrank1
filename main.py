"""Para  obter  os  pontos  relativos  a  este  trabalho,  vocΓͺ  deverΓ‘  criar  um  programa,  utilizando  a 
linguagem  Python, C, ou C++.  Este  programa,  quando  executado,  irΓ‘  determinar  se  uma  string de 
entrada  faz  parte  da  linguagem  πΏ    definida  por  πΏ = {π₯ | π₯ β
 {π,π}β π ππππ π ππ π₯ Γ© π πππ’πππ πππ ππππ πππππ  ππππ  π} segundo o alfabeto  Ξ£={π,π,π}.  
O  programa  que  vocΓͺ  desenvolverΓ‘  irΓ‘  receber  como  entrada um arquivo de texto  (.txt) 
contendo vΓ‘rias strings. A primeira linha do arquivo indica quantas strings estΓ£o no arquivo de texto de 
entrada. As linhas subsequentes contΓ©m uma string por linha."""

def Inicio(frase):
	try:
		for i in range(len(frase)):
			if frase[i] == "a":
				if esperaB(f"{frase[i+1]}{frase[i+2]}"):
					pass
				else:
					return False
		return True	
	except IndexError:
		return False
		
def esperaB(frase):
	if frase == "bb":
		return True
	else:
		return False
  
if __name__ == '__main__':
		arquivos = ["teste.txt", "teste2.txt"]
		for arquivo in arquivos:
			texto = []
			txts = open(arquivo,"r")
			linhas = txts.readlines()
			for item in linhas:
				texto.append(item.replace("\n",""))
			txts.close()
			for item in range(int(texto[0])):
				if Inicio(texto[item+1]):
					print(texto[item+1] + ": Pertence")
				else:
					print(texto[item+1] + ": Nao Pertence")
	  
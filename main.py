"""Para  obter  os  pontos  relativos  a  este  trabalho,  você  deverá  criar  um  programa,  utilizando  a 
linguagem  Python, C, ou C++.  Este  programa,  quando  executado,  irá  determinar  se  uma  string de 
entrada  faz  parte  da  linguagem  𝐿    definida  por  𝐿 = {𝑥 | 𝑥 ∈
 {𝑎,𝑏}∗ 𝑒 𝑐𝑎𝑑𝑎 𝑎 𝑒𝑚 𝑥 é 𝑠𝑒𝑔𝑢𝑖𝑑𝑜 𝑝𝑜𝑟 𝑝𝑒𝑙𝑜 𝑚𝑒𝑛𝑜𝑠 𝑑𝑜𝑖𝑠 𝑏} segundo o alfabeto  Σ={𝑎,𝑏,𝑐}.  
O  programa  que  você  desenvolverá  irá  receber  como  entrada um arquivo de texto  (.txt) 
contendo várias strings. A primeira linha do arquivo indica quantas strings estão no arquivo de texto de 
entrada. As linhas subsequentes contém uma string por linha."""

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
	  
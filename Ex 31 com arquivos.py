#importação de biblioteca
import os

#declaração de variáveis

#inicio
def main():
	loop()
	
def loop():
	contador: int = 10
	while (contador<=150):
		numero = contador * contador
		escreveArq(numero, contador)
		contador += 1

def escreveArq(num,cont):
	arq: str = ''
	dir: str = ''
	file: str = ''
	texto: str = ''
	enc: str = 'utf-8'
	texto = str(num)
	dir = '/tmp/exercicios/'
	arq = 'ex 31.txt'
	os.makedirs(dir, exist_ok=True)
	os.chmod(dir, 0o744)
	if os.path.exists(dir) and os.path.isdir(dir):
		file = dir + arq 
		if (cont == 10):
			tipo = 'w'
		else:
			tipo = 'a'
		with open(file,tipo,encoding=enc) as file:
			file.write(f'{texto}\n')
             
if __name__ == '__main__':
    main()
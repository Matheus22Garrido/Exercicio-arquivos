#importação de bibliotecas
import os
#declaração de variáveis
valor: int = 0 
arq1: str = ''
dir: str = ''
#inicio
def main():
    global valor
    result: int = 0
    contador: int = 0
    valor = int(input("Digite um valor de 1 a 10: "))
    while valor<1 or valor>10:
        print("Valor inválido")
        valor = int(input("Digite um valor de 1 a 10: "))
    while contador <11:
        result = mult(valor,contador)
        grava(contador,result)
        contador +=1

def grava(c,rslt):
    global dir,arq
    dir = '/tmp/exercicios/'
    arq = 'ex34.txt'
    os.makedirs(dir, exist_ok=True)
    os.chmod(dir, 0o744)
    file: str = ''
    tipo: str = ''
    enc: str = ''
    linha: str = ''
    linha = str(rslt) + '\n'
    if (os.path.exists(dir) and os.path.isdir(dir)):
        enc = 'utf-8'
        file = dir + arq
        if c <= 0:
                tipo = 'w'
        else:
            tipo = 'a'
        with open (file, tipo, encoding=enc) as file:
                file.write(linha)
    else:
        print ("Diretório não existe")

def mult(vlr,tab):
    res: int = 0 
    res = vlr * tab
    return res

if __name__ == "__main__":
    main()
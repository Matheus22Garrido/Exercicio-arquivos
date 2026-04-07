#importar bibliotecas
import os

#declaração de variáveis

#inicio
def main():
    leitor()

def verifica(n):
    return n % 5 == 0

def criaEescreve(n,c):
    tipo: str = ''
    file: str = ''
    dir = '/tmp/exercicios/'
    arq = 'leitor multiplos ex38.txt'
    file = dir + arq
    if c == 1:
        tipo = 'w'
        with open(file, tipo) as file:
            file.write(f"{n}"'\n')
    else:
        tipo = 'a'
        with open(file, tipo) as file:
            file.write(f"{n}"'\n')
def leitor():
    c = 0
    tipoL: str = ''
    tipoL = 'r'
    num: int = 0
    origem: str = '/tmp/exercicios/ex 38.txt'
    if os.path.exists(origem) and os.path.isfile(origem):
        with open(origem, tipoL) as leitura:
            for linha in leitura:
                if 'maior' not in linha and 'menor' not in linha and linha.strip():
                    num = int(linha.strip())
                    if verifica(num):
                        c +=1
                        criaEescreve(num,c)

if __name__ == "__main__":
    main()
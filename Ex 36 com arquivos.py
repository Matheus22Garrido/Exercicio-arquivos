#importação de bibliotecas
import os

#inicio
def main():
    entrada()

def entrada():
    contador: int = 1
    fat: int = 0
    soma: int = 0
    termo: float = 0.0
    valor: int = 0
    valor = int(input("Digite um número positivo: "))
    while contador<=valor:
        fat = Ffatorial(contador)
        termo = Fdivisão(1,fat)
        soma += termo
        criaEescreve(termo, soma, contador, valor)
        contador+=1

def Ffatorial(v):
    c: int = 1
    fat: int = 1
    while (c<=v):
        fat*= c
        c+=1
    return fat

def Fdivisão(num, den):
    return num/den

def criaEescreve(termo, soma, cont, v):
    tipo: str = ''
    file: str = ''
    dir = '/tmp/exercicios/'
    arq = 'ex 36.txt'
    os.makedirs(dir, exist_ok=True)
    os.chmod(dir, 0o744)
    if os.path.exists(dir) and os.path.isdir(dir):
        file = dir + arq
        if v == 1:
            tipo = 'w'
            with open(file, tipo) as file:
                file.write("A soma de 1 + 1/1 = 2")
        else:
            if cont == 1:
                tipo = 'w'
                with open(file, tipo) as file:
                    file.write(f"O valor atual é: {termo}\n")
            elif cont>1 and cont<v:
                tipo = 'a'
                with open(file, tipo) as file:
                    file.write(f"O valor atual é: {termo}\n")
            elif cont==v:
                tipo = 'a'
                with open(file, tipo) as file:
                    file.write(f"O valor atual é: {termo}\n")
                    file.write(f"O resultado total é a soma dos termos + 1: {soma+1}")
            cont+=1

if __name__ == "__main__":
    main()
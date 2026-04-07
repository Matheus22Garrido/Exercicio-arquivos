#importação de bibliotecas
import os

#declaração de variáveis
arq: str = ''
dir: str = ''

#inicio
def main():
    entrada()

def entrada():
    maior: int = 0
    menor: int = 0
    contador: int = 0
    valor: int = 0
    print("Digite um número positivo: ")
    while contador<100:
        valor = int(input("Digite o valor: "))
        if (valor<1):
            print("Número inválido, digite outro: ")
            continue
        contador += 1
        if (contador == 1):
            menor = valor
            maior = valor
        else:
            valor,maior,menor = verifica(valor,maior,menor)
        escreveDir(valor,maior,menor,contador)

def verifica(val,mai,men): 
    if (val<men):
        men = val
    elif (val> mai):
        mai = val
    return(val,mai,men)

def escreveDir(v,M,m,c):
    global arq, dir
    file: str = ''
    tipo: str = ''
    enc: str = ''
    linha: str = ''
    dir = '/tmp/exercicios/'
    arq = 'ex 38.txt'
    linha = str(v) + '\n'
    os.makedirs(dir, exist_ok= True)
    os.chmod(dir, 0o744)
    if (os.path.exists(dir) and os.path.isdir(dir)):
        enc = 'utf-8'
        file = dir + arq
        if c==1:
            tipo = "w"
            with open (file, tipo, encoding=enc) as file:
                file.write(linha)
        elif (c>1) and (c<100):
            tipo = "a"
            with open (file, tipo, encoding=enc) as file:
                file.write(linha)
        elif c==100:
            tipo = "a"
            with open (file,tipo,encoding=enc) as file:
                file.write(linha)
                file.write(f"O maior valor entre eles é: '{M}' e o menor é: '{m}'")

if __name__ == "__main__":
    main()

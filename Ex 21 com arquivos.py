#importação de bibliotecas
import os 
#declaração de variáveis
nome: str = ''
nota1: float = 0.0
nota2: float = 0.0
nota3: float = 0.0
nota4: float = 0.0
valor_media: float = 0.0
dir: str = ''
arq: str = ''
#inicio
def main():
    contador: int = 1
    while contador <6:
        entrada()
        contador += 1

def entrada():
    global nome,nota1,nota2,nota3,nota4,valor_media
    nome = str(input("Digite seu nome: "))
    nota1 = float(input("Digite sua primeira nota: "))
    nota2 = float(input("Digite sua segunda nota: "))
    nota3 = float(input("Digite sua terceira nota: "))
    nota4 = float(input("Digite sua quarta nota: "))
    valor_media = med(nota1,nota2,nota3,nota4)
    print (f"A média das suas notas é: {valor_media}")
    cadastro(nome,nota1,nota2,nota3,nota4,valor_media)

def med(n1,n2,n3,n4):
    media: float = 0.0
    media = (n1+n2+n3+n4)/4
    return media

def cadastro(nm,nt1,nt2,nt3,nt4,vlr_med):
    global arq,dir
    linha: str = ''
    dir = '/tmp/exercicios/'
    arq = 'ex21.txt'
    linha = f"{nm};{nt1};{nt2};{nt3};{nt4};{vlr_med}\n"
    escreveArq(dir,arq,linha)

def escreveArq(diretorio,arquivo,conteudo):
    os.makedirs(dir, exist_ok=True)
    os.chmod(dir, 0o744)
    file: str = ''
    tipo: str = ''
    enc: str = ''
    if (os.path.exists(dir) and os.path.isdir(dir)):
        enc = 'utf-8'
        file = diretorio + arquivo
        if os.path.exists(file):
                tipo = 'a'
        else:
            tipo = 'w'
        with open (file, tipo, encoding=enc) as file:
                file.write(conteudo)
    else:
        print ("Diretório não existe")

if __name__ == "__main__":
    main()
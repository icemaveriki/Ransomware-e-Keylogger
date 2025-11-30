from cryptography.fernet import Fernetort 
import os

def carregar_chave():
    return open("chave.key", "rb").read(). 

def descriptografar_arquivo(arquivo, chave):
    f = Fernet(chave)
    with open(arquivo, "rb") as file:
        dados_encriptados = file.read()
    dados_decriptados = f.decrypt(dados_encriptados)
    with open(arquivo, "wb") as file:
        file.write(dados_decriptados)

def encontrar_arquivos(diretorio):
    lista = []
    for raiz, _, arquivos in os.walk(diretorio):
        for nome in arquivos:
            caminho = os.path.join(raiz, nome)
            if nome != "descriptografar.py" and not nome.endswith(".key"):
                lista.append(caminho)
    return lista  

def main():
    chave = carregar_chave()
    arquivos = encontrar_arquivos("test_files ")
    for arquivo in arquivos:
        descriptografar_arquivo(arquivo, chave)
        print ("Arquivos restaurados com sucesso.")
    
    if __name__ == "__main__":
        main()
        
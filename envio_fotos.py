import shutil
import os

def copiar_fotos(diretorio_origem, diretorio_destino):
    # Verificar se o diretório de destino existe
    if not os.path.exists(diretorio_destino):
        os.makedirs(diretorio_destino)
    
    # Listar todos os arquivos no diretório de origem
    arquivos = os.listdir(diretorio_origem)
    
    for arquivo in arquivos:
        # Verificar se o arquivo é uma foto (pode usar outras extensões também)
        if arquivo.endswith((".jpg", ".jpeg", ".png", ".gif", ".bmp")):
            caminho_origem = os.path.join(diretorio_origem, arquivo)
            caminho_destino = os.path.join(diretorio_destino, arquivo)
            shutil.copyfile(caminho_origem, caminho_destino)
            print(f"Foto {arquivo} copiada com sucesso.")

if __name__ == "__main__":
    # Solicitar os caminhos de origem e destino ao usuário
    diretorio_origem = input("Digite o caminho do diretório de origem: ")
    diretorio_destino = input("Digite o caminho do diretório de destino: ")

    # Chamar a função copiar_fotos com os caminhos fornecidos
    copiar_fotos(diretorio_origem, diretorio_destino)

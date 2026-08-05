import os
import shutil

user = os.getlogin()
path = f"C:\\Users\\{user}\\Downloads" 
os.chdir(path)
arquivos = os.listdir(path)
pastas = ['Documentos_e_Textos', 'Imagens', 'Áudio_e_Vídeo', 'Compactados', 'Outros']

# Cria pastas
for pasta in pastas:
    os.mkdir(pasta)

# Organiza os arquivos na pasta downloads
for arquivo in arquivos:
    if arquivo.endswith('.pdf') or arquivo.endswith('.docx') or arquivo.endswith('.txt') or arquivo.endswith('.xlsx'):
        shutil.move(arquivo, path + '\\Documentos_e_Textos')
    elif arquivo.endswith('.jpg') or arquivo.endswith('.png') or arquivo.endswith('.gif') or arquivo.endswith('.jpeg'):
        shutil.move(arquivo, path + '\\Imagens')
    elif arquivo.endswith('.mp3') or arquivo.endswith('.wav') or arquivo.endswith('.mp4') or arquivo.endswith('.mkv') or arquivo.endswith('.avi'):
        shutil.move(arquivo, path + '\\Áudio_e_Vídeo')
    elif arquivo.endswith('.zip') or arquivo.endswith('.rar'):
        shutil.move(arquivo, path + '\\Compactados')
    else:
        shutil.move(arquivo, path + '\\Outros')
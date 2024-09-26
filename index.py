import os
import shutil

def main():

    print("Introduce la ruta que deseas limpiar: ")
    clear_path = input("")
    images_format = ['png','jpg','jpeg']
    documents_format = ['pdf','txt']
    compresed_files = ['rar','zip']
    new_path = ''

    if not os.path.exists(clear_path):
        print("La ruta especificada no existe")
        
    all_files = os.listdir(clear_path)

    for file in all_files:
        current_file_path = os.path.join(clear_path,file)
        
        #Si es una carpeta
        if os.path.isdir(current_file_path):
            new_path = os.path.join(clear_path,'Carpetas')
            if not os.path.isdir(new_path):
                os.mkdir(new_path)
            if not os.listdir(current_file_path) and file not in os.listdir(new_path):
                shutil.move(current_file_path,new_path)
                print("Moviendo Carpeta:",file)
            else:
                print(f"La carpeta {file} ya existe en el directorio")
                
        #Si es un archivo
        else:
            file_body_arr = file.split('.')
            ext = file_body_arr[len(file_body_arr) - 1]
            if ext in images_format:
                new_path = os.path.join(clear_path,'Imagenes')      
            elif ext in documents_format:
                new_path = os.path.join(clear_path,'Documentos')      
                
            elif ext in compresed_files:
                new_path = os.path.join(clear_path,'Archivos Comprimidos')
            else:
                new_path = os.path.join(clear_path,'Otros Archivos')
            if not os.path.isdir(new_path):
                os.mkdir(new_path)
            if file not in os.listdir(new_path):
                shutil.move(current_file_path,new_path)
                print("Moviendo Archivo:",file)
            else:
                print(f"El archivo {file} ya existe en el directorio")
        
if __name__ == "__main__":
    main()
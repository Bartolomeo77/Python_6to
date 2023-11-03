import magic

def detect_file_type(file_path):
    mime = magic.Magic()
    file_type = mime.from_file(file_path)
    return file_type

# Ejemplo de uso: reemplaza "nombre_del_archivo_subido" con el nombre de tu archivo
audio_file_path = "094. Feid, Zion & Lennox - La Pasamos CXBRXN [UTM!X].m4a"

file_type = detect_file_type(audio_file_path)
print(f"El tipo de archivo subido es: {file_type}")


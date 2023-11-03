import librosa
import magic

# Función para calcular el BPM de un archivo de audio
def calculate_bpm(audio_file):
    try:
        # Carga el archivo de audio
        y, sr = librosa.load(audio_file)
        
        # Aplica preprocesamiento y ajusta parámetros
        y = librosa.effects.preemphasis(y)

        # Ajuste del umbral de detección de golpes (beat_threshold)
        beat_threshold = 0.15  # Ajusta este valor según la sensibilidad que desees

        # Ajuste del tamaño de la ventana de análisis (hop_length)
        hop_length = 512  # Ajusta el tamaño de la ventana de análisis según tu necesidad

        # Separación de la voz y la música
        y_harmonic, y_percussive = librosa.effects.hpss(y)

        # Cálculo del tempo (BPM) con los parámetros ajustados
        tempo, _ = librosa.beat.beat_track(y=y_harmonic, sr=sr, hop_length=hop_length)
        
        return tempo
    except Exception as e:
        return None

# Función para detectar el tipo de archivo
def detect_file_type(file_path):
    try:
        mime = magic.Magic()
        file_type = mime.from_file(file_path)
        return file_type
    except Exception as e:
        return "No se pudo detectar el tipo de archivo"

# Ruta del archivo subido (ajústala según tu necesidad)
file_path = "094. Feid, Zion & Lennox - La Pasamos CXBRXN [UTM!X].m4a"

# Detecta el tipo de archivo
file_type = detect_file_type(file_path)
print(f"Tipo de archivo subido: {file_type}")

# Calcula el BPM si el archivo es de audio
if "audio" in file_type.lower():
    bpm = calculate_bpm(file_path)
    if bpm is not None:
        print(f"El BPM de la canción es aproximadamente {bpm} BPM")
    else:
        print("No se pudo calcular el BPM del archivo.")
else:
    print("El archivo no es de audio.")

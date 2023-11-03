from pydub import AudioSegment
import librosa

# Ruta del archivo .m4a
audio_file_path = "094. Feid, Zion & Lennox - La Pasamos CXBRXN [UTM!X].m4a"

# Convertir el archivo .m4a a un formato de audio compatible (por ejemplo, .wav)
converted_audio_file_path = "audio_convertido.wav"

audio = AudioSegment.from_file(audio_file_path, format="m4a")
audio.export(converted_audio_file_path, format="wav")

# Cargar el archivo de audio convertido
y, sr = librosa.load(converted_audio_file_path)

# Aplicar preprocesamiento y ajustar parámetros
y = librosa.effects.preemphasis(y)
beat_threshold = 0.15
hop_length = 512
y_harmonic, y_percussive = librosa.effects.hpss(y)

# Calcular el tempo (BPM) con los parámetros ajustados
tempo, _ = librosa.beat.beat_track(y=y_harmonic, sr=sr, hop_length=hop_length)

# Muestra el resultado
print(f"El BPM de la música en el archivo .m4a es aproximadamente {tempo} BPM")

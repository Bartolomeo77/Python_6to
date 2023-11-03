import librosa
import librosa.display
import numpy as np

# Carga el archivo de audio en formato .wav
audio_file = "094. Feid, Zion & Lennox - La Pasamos CXBRXN [UTM!X].m4a"
y, sr = librosa.load(audio_file)

# Aplica preprocesamiento y ajusta parámetros
# Filtros de preprocesamiento
y = librosa.effects.preemphasis(y)

# Ajuste del umbral de detección de golpes (beat_threshold)
beat_threshold = 0.15  # Ajusta este valor según la sensibilidad que desees

# Ajuste del tamaño de la ventana de análisis (hop_length)
hop_length = 512  # Ajusta el tamaño de la ventana de análisis según tu necesidad

# Separación de la voz y la música
y_harmonic, y_percussive = librosa.effects.hpss(y)

# Cálculo del tempo (BPM) con los parámetros ajustados
tempo, _ = librosa.beat.beat_track(y=y_harmonic, sr=sr, hop_length=hop_length)

# Muestra el resultado
print(f"El BPM de la canción es aproximadamente {tempo} BPM")

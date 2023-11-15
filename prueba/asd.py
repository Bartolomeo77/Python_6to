# Verifica si PyTorch está instalado y muestra la versión
import torch
print("Versión de PyTorch:", torch.__version__)

# Verifica si CUDA está disponible
print("CUDA disponible:", torch.cuda.is_available())

# Muestra el nombre de la GPU si está disponible
if torch.cuda.is_available():
    print("Nombre de la GPU:", torch.cuda.get_device_name())

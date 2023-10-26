import sys

# Verifica si se proporciona una consulta como argumento
if len(sys.argv) > 1:
    consulta = " ".join(sys.argv[1:])
    print(f"La consulta es: {consulta}")
else:
    print("No se proporcionó una consulta como argumento.")

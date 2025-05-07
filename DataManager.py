import os 
import json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, 'documentacion')

@staticmethod
def pasar_json(objetos):
    serializable = {}

    if isinstance(objetos, dict):
        for key, value in objetos.items():
            clave = str(key)
            if hasattr(value, 'to_dict'):
                valor = value.to_dict()
            else:
                valor = value
            serializable[clave] = valor
    else:
        serializable = objetos  # Si no es dict, lo dejamos como está

    return json.dumps(serializable, indent=4)

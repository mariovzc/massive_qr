import os
import json
import logging
import qrcode

sh = logging.StreamHandler()
logging.basicConfig(format='%(asctime)s |%(name)s|%(levelname)s|%(message)s',
                    level=logging.INFO,
                    handlers=[sh])


def main():
    FILE_PATH = os.getenv("DATA_FILE_PATH")
    data = get_json_from_path(FILE_PATH)
    items = data.get("data", [])
    total = len(items)
    counter = 1

    for item in items:
        logging.info(f"Generando qr {counter} de {total}")
        str_data = json.dumps(item)
        generate_qr(str_data, item['placa'])
        counter += 1

def get_json_from_path(file_path):
    with open(file_path) as json_file:
        data = json.load(json_file)
        if data:
            return data
    return {}

def generate_qr(input_data, name):
    logging.info(f"Generando QR para {name}")

    try:
        qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=5)
        qr.add_data(input_data)
        qr.make(fit=True)
        img = qr.make_image(fill='black', back_color='white')
        img.save(f"./output/{name}.png")
        logging.info(f"QR creado con exito para {name}")
    except:
        logging.error(f"No se pudo generar el QR para {name}")

main()
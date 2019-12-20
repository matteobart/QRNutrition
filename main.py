import qrcode
import json

with open('nutritionV1.json') as json_file:
    json_string = json.load(json_file)

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=4,
    border=2,
)
qr.add_data(json_string)
qr.make(fit=True)

img = qr.make_image(fill_color="green", back_color="white")

img.save('abd.png')
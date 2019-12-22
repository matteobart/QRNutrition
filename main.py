import qrcode
import json

with open('nutritionV1.json') as json_file:
    json_string = json.load(json_file)

qr = qrcode.QRCode(
    version=None,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=4,
    border=2,
)
# qr.add_data(json_string)
qr.add_data("json_string")
qr.make(fit=True)

print(qr.version)
img = qr.make_image(fill_color="white", back_color="darkgreen")

img.save('abd.png')
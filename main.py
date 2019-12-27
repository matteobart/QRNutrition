import qrcode
import json
import train
import argparse



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Turn a nutrition label into a qr code')
    parser.add_argument('json_filename', type=str, help='The file to convert into qr')
    parser.add_argument('-s', action='store_true', help='Will strip newlines and tabs from the file')
    args = parser.parse_args()
    
    with open(args.json_filename) as json_file:
        json_string = str(json.load(json_file))
    if args.s: #if the strip flag is set
        json_string = json_string.replace("\n", "").replace("\t", "")
    encoding = train.get_encoding()
    dict = {}
    for encode in encoding:
    	dict[encode[0]] = encode[1]

    encoded_string = ""
    for char in json_string:
    	encoded_string += dict[char]

    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=4,
        border=2,
    )
    qr.add_data(encoded_string)
    qr.make(fit=True)
    print("Encoded QR version", qr.version)
    img = qr.make_image(fill_color="white", back_color="darkgreen")
    img.save('encoded_output.png')

    qr2 = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=4,
        border=2,
    )
    qr2.add_data(json_string)
    qr2.make(fit=True)
    print("Non-encoded QR version", qr2.version)
    img = qr2.make_image(fill_color="white", back_color="darkgreen")
    img.save('output.png')



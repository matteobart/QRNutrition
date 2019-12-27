## What
The purpose of this repo is to try and create a standard for nutrition labels via json and qrcodes. People are often scanning and tracking their dietary intake, why isn't there a standardize way of scanning our food. This repo allows you to check json for their validity and turn them into qrcodes.

## To install 
```
pip3 install qrcode[pil]
pip3 install argparse
```
## To use 
To check to see if a json file is a valid nutrition label  
`python3 check_valid_json.py your.json`  
This will print any errors or warnings that should be fixed  

After it passes the check...  
Turn the json into a qr code  
`python3 main.py your.json`  

This will create two output files, `encoded_output.png` and `output.png` 
`encoded_output.png` will contain an encoded version of the json (based on a huffman of the most common characters for nutrition labels). To decode the integers, put it through the function `decode(str)` found in `train.py`  

`output.png` will be a qrcode that has the characters as is. This is likely to have a greater version (larger qr) then the encoded one. 

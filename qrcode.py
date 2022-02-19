import pyqrcode
import png

qrcode = pyqrcode.create('https://www.nba.com/')
qrcode.png('nba_image.png', scale=8)

qrcode.show()
print('\nQRcode criado com sucesso!')
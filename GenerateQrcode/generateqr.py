from ensurepip import version
import qrcode

my_qr = qrcode.QRcode(
    version = 15,
    box_size = 10
)


import qrcode

link = "https://pianocoffee.ir"

img = qrcode.make(link)
img.save("qrcode.png")

print("QR Code ساخته شد")

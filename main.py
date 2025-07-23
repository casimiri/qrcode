import qrcode

url = "https://www.iaea.org"
img = qrcode.make(url)
img.save("qr_iaea.png")

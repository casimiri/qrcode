import qrcode

url = "https://example.com"
img = qrcode.make(url)
img.save("qr_direct.png")

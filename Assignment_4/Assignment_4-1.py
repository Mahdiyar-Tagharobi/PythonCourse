import qrcode as q

inp = input("Enter your full name to making QRcode for you: ")

res = q.make(inp)
res.save("QRcode1.png")

import qrcode
from PIL import Image

# Web sayfanın URL'si (QR tarandığında buraya yönlensin)
data = "https://kullaniciadi.github.io/noor-network/"  # Kendi URL’n ile değiştir

# QR kod oluştur
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,  # Yüksek hata toleransı
    box_size=10,
    border=4,
)
qr.add_data(data)
qr.make(fit=True)

# QR görseli (siyah kareler, beyaz arka plan)
img_qr = qr.make_image(fill_color="black", back_color="white").convert("RGB")

# Logo ekleme (logo dosyan qr.py ile aynı klasörde olmalı!)
logo = Image.open("network logo.jpg")  # Logo dosyanın adı tam yazılmalı
logo_size = 80  # Logoyu biraz büyüttük
logo = logo.resize((logo_size, logo_size))
pos = ((img_qr.size[0] - logo_size) // 2, (img_qr.size[1] - logo_size) // 2)
img_qr.paste(logo, pos)

# Kaydet (aynı klasöre)
img_qr.save("NOOR NETWORK.png")

print("✅ Logo eklenmiş QR kod oluşturuldu: NOOR NETWORK.png")

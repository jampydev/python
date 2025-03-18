

# Version: 1.0
import qrcode



# Data to be encoded
data = "https://grupo-sistemas.netlify.app/"



# Creating an instance of QRCode
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)



# Adding data to the instance
qr.add_data(data)
qr.make(fit=True)



# Creating an image from the QR Code instance
img = qr.make_image(fill='black', back_color='white')



# Saving the image
img.save("sistemas.png")
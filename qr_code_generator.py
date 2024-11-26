import qrcode
import image 
qr=qrcode.QRCode(
    version= 15, #15 is the version of the qr code
    box_size= 10, #size of the box to display qr code
    border= 5 #it is the white part of image -- border
)

data ="https://github.com/anvesh741"
# As I have given the data as github link, it will redirect to the github link
# if you don't want to redirect and create for normal text that write text in the quotes 

qr.add_data(data)
qr.make(fit=True)
img=qr.make_image(fill="black", back_color="white")
img.save("github.png")



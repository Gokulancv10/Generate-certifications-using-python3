from PIL import Image, ImageDraw, ImageFont
from datetime import date


def generate_certificate():
    """
    Update Information in default certification template
    """    
    name = "NAME"
    today_date = date.today()
    today = today_date.strftime("%B %d, %Y")
    cert_no = "54672ABGD690NH22994YD364N927N"
    cert_url = f"url/{cert_no}"
    
    # image path
    image = Image.open(r"D:\Data\MY CERTIFICATES\UDEMY-edited.jpg")
    image_draw = ImageDraw.Draw(image)
    
    # retrieved location info using ms-paint
    NAME_LOCATION = (761, 413)
    DATE_LOCATION = (691, 610)
    CERT_NO_LOCATION = (239, 954)
    CERT_URL_LOCATION = (245, 973)
    TEXT_COLOR = (0, 137, 209)
    FONT_TYPE = ImageFont.truetype("arial.ttf", 30)
    FONT_TYPE_CERT = ImageFont.truetype("arial.ttf", 15)
    
    image_draw.text(xy=NAME_LOCATION, text=name, font=FONT_TYPE, fill=TEXT_COLOR)
    image_draw.text(xy=DATE_LOCATION, text=today, font=FONT_TYPE, fill=TEXT_COLOR)
    image_draw.text(xy=CERT_NO_LOCATION, text=cert_no, font=FONT_TYPE_CERT, fill=TEXT_COLOR)
    image_draw.text(xy=CERT_URL_LOCATION, text=cert_url, font=FONT_TYPE_CERT, fill=TEXT_COLOR)
    
    image.save(r"D:\Data\MY CERTIFICATES\auto_generated.jpg")
    
    # convert image into pdf file
    img_to_pdf = image.convert("RGB")
    img_to_pdf.save(r"D:\Data\MY CERTIFICATES\auto-generated.pdf")

    print("image edited successfully!")
    
generate_certificate()  
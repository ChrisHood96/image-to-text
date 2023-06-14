# import discord
from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd  = r'C:\Program Files\Tesseract-OCR\tesseract'
cards1 = Image.open('example_images/card.png')
cards2 = Image.open('example_images/card2.jpg')
cards3 = Image.open('example_images/card3.jpg')

# left, top, right, bottom
card1namexy = (50, 50, 235, 110)
card1seriesxy = (50, 305, 235, 370)
card2namexy = (325, 50, 510, 110)
card2seriesxy = (325, 305, 510, 370)
card3namexy = (600, 50, 785, 110)
card3seriesxy = (600, 305, 785, 370)
card4namexy = (875, 50, 1060, 110)
card4seriesxy = (875, 305, 1060, 370)

card_snapshots = [card1namexy, card1seriesxy, card2namexy, card2seriesxy, card3namexy, card3seriesxy, card4namexy, 
                  card4seriesxy]

def get_card_info(base_image: Image):
    cards = []
    for i in range(len(card_snapshots)):
        num = i+2
        if num % 2 == 0:
            im_name = base_image.crop(card_snapshots[i])
            im_series = base_image.crop(card_snapshots[i+1])
            # im_name.show(   )

            ps_name = str(pytesseract.image_to_string(im_name))
            ps_series = str(pytesseract.image_to_string(im_series))
            name = strip_sting(ps_name)
            series = strip_sting(ps_series)

            card_info = f"character: {name.rstrip()} | series: {series.rstrip()}"
            cards.append(card_info)
    return cards


# def format_card_info(base_image: Image, cards: list):
#     width, height = base_image.size
#     message = f":one: {cards[0]} has x many wishlists\n:two: {cards[1]} has x many wishlists\n:three: {cards[2]} has x many wishlists"
#     if width > 1000:
#         message = message + f"\n:four: {cards[3]} has x many wishlists"
#     return message

# need to figure out what it's doing
def strip_sting(string):
    string = string.replace("\n", " ")
    string = string.replace("\x0c", "   ")
    string = string.replace(".", "")
    string = string.replace("\\", "")
    return string

print(get_card_info(cards3))



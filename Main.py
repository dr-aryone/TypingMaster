def capture():
    import pyscreenshot as ImageGrab

    im = ImageGrab.grab(bbox=(50, 260, 1400, 300))  # X1,Y1,X2,Y2 Screenshot Capturing according to Cordinates
    im.save('screenshot.png') # Screenshot saved in this file


def typing():
    from PIL import Image
    import pytesseract
    import keyboard

    text = str(pytesseract.image_to_string(Image.open('screenshot.png'))) # Fetching text from screenshot and passed in text variable
    print(text) # fetched text from screenshot, print on the console
    keyboard.write(text) # automatically softwares types the text

capture()
typing()
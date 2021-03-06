# crypto display
import requests
import time
from picamera import PiCamera
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


# Get eGLD Price
def get_egld_price():
    egld_info = requests.get('https://api.elrond.com/tokens/WEGLD-bd4d79').json()
    egld_price = egld_info["price"]
    return egld_price


# Get MEX Price
def get_mex_price():
    mex_info = requests.get('https://api.elrond.com/tokens/MEX-455c57').json()
    mex_price = mex_info["price"]
    return mex_price


# Get RIDE Price
def get_ride_price():
    ride_info = requests.get('https://api.elrond.com/tokens/RIDE-7d18e9').json()
    ride_price = ride_info["price"]
    return ride_price


# Get ITHEUM Price
def get_itheum_price():
    itheum_info = requests.get('https://api.elrond.com/tokens/ITHEUM-df6f26').json()
    itheum_price = itheum_info["price"]
    return itheum_price


def take_photo(camera):
    camera.capture("/home/pi/Desktop/CryptoTracker/reaction.jpg")


def display_menu():
    print("Type '1' to show eGLD price")
    print("Type '2' to show MEX price")
    print("Type '3' to show RIDE price")
    print("Type '4' to show ITHEUM price")
    print("Type '5' to show last price reaction")
    print()
    print("Type '0' to exit")
    print()


def show_reaction(message):
    image = Image.open("/home/pi/Desktop/CryptoTracker/reaction.jpg")
    image_draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("FreeMono.ttf", 200)
    image_draw.text((70, 70), message, font=font, fill=(255, 0, 0))
    image.show()


def main():
    camera = PiCamera()
    time.sleep(2)
    last_price = ""

    while True:
        display_menu()
        command = input(">>>")

        if command == '0':
            exit()
        elif command == '1':
            price = str(get_egld_price())[:8]
            print("eGLD Value: " + price + "$\n\n")
            last_price = "eGLD = " + price + "$"
            print("Input your face reaction in 2 seconds!\n")
            take_photo(camera)
        elif command == '2':
            price = str(get_mex_price())[:8]
            print("MEX Value: " + price + "$\n\n")
            last_price = "MEX = " + price + "$"
            print("Input your face reaction in 2 seconds!\n")
            take_photo(camera)
        elif command == '3':
            price = str(get_ride_price())[:8]
            print("RIDE Value: " + price + "$\n\n")
            last_price = "RIDE = " + price + "$"
            print("Input your face reaction in 2 seconds!\n")
            take_photo(camera)
        elif command == '4':
            price = str(get_itheum_price())[:8]
            print("ITHEUM Value: " + price + "$\n\n")
            last_price = "ITHEUM = " + price + "$"
            print("Input your face reaction in 2 seconds!\n")
            take_photo(camera)
        elif command == '5':
            show_reaction(last_price)


main()

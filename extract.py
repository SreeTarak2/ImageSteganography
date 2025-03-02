from PIL import Image

def reveal_data(image_path, decryptPassword):
    image_data = Image.open(image_path)
    pixels = image_data.load()
    width, height = image_data.size

    message_bits = ""
    
    for i in range(height):
        for j in range(width):
            pixel = pixels[j, i]
            for channel in range(3):
                message_bits += str(pixel[channel] & 1)

    byte_message = []
    for i in range(0, len(message_bits), 8):
        byte_message.append(int(message_bits[i:i + 8], 2))

    message = bytes(byte_message)

    password_length = int.from_bytes(message[:2], byteorder='big')
    password = message[2:2 + password_length].decode('utf-8')

    if decryptPassword == password:
        data_length = int.from_bytes(message[2 + password_length:4 + password_length], byteorder='big')
        data = message[4 + password_length:4 + password_length + data_length].decode('utf-8')
        return data
    else:
        print("Password is incorrect.")
        return None

if __name__ == "__main__":
    image_path = input('Enter the image path: ')
    password = input('Enter the password: ')
    data = reveal_data(image_path, password)
    print('Extracting data from image...')
    if data:
        print("Hidden data:", data)
    else:
        print("No data found.")

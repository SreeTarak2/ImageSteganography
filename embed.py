from PIL import Image

def text_to_binary(text):
    return ''.join(format(ord(c), '08b') for c in text)

def hide_text_image(image_path, password, data , output_image='stego.png'):
    image_data = Image.open(image_path)
    pixels = image_data.load()
    width, height = image_data.size
    password_binary = text_to_binary(password)
    data_binary = text_to_binary(data)
    password_length_binary = format(len(password), '016b')
    data_length_binary = format(len(data), '016b')
    binary_message = password_length_binary + password_binary + data_length_binary + data_binary
    binary_index = 0

    for i in range(height):
        for j in range(width):
            if binary_index < len(binary_message):
                r, g, b = pixels[j, i]
                r = (r & 0xFE) | int(binary_message[binary_index])
                binary_index += 1
                if binary_index < len(binary_message):
                    g = (g & 0xFE) | int(binary_message[binary_index])
                    binary_index += 1
                if binary_index < len(binary_message):
                    b = (b & 0xFE) | int(binary_message[binary_index])
                    binary_index += 1
                pixels[j, i] = (r, g, b)

            if binary_index >= len(binary_message):
                break

    image_data.save(output_image)
    print("Message hidden in the image.")

if __name__ == '__main__':
    image_path = input('enter the image path: ')
    password = input('enter the password: ')
    data = input('enter the data to hide: ')
    output_image = input('enter the output image name(optional eg: stego.png): ')
    print('Hiding the text message in the image...')
    hide_text_image(image_path, password, data , output_image if output_image else 'stego.png')

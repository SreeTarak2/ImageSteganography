## Image Steganography Project

## Requirements
- Python 3.x
- **Pillow** library (for image processing)

To install the required dependencies, run:

```bash
pip install pillow
```

## How to Use

1. **Prepare your files**:
   - Choose an image in which you want to hide the data.
   - Decide on the password and the data you wish to hide.

2. **Run the script**:
   - Open a terminal or command prompt and navigate to the project directory.
   - Run the script by executing:

   ```bash
   python steganography.py
   ```

3. **Input the required information**:
   - **Image Path**: Enter the path to the image where you want to hide the data.
   - **Password**: Enter a password that will be used to secure the hidden message.
   - **Data to Hide**: Enter the text or data you want to embed within the image.
   - **Output Image**: Specify the output file name (e.g., `stego.jpg`). If left empty, it will default to `stego.png`.

4. **Output**:
   - The script will process the image and save the modified image (with the hidden data) in the specified output file.
   - You can then share the modified image securely.

## Example

```bash
Enter the image path: image.jpg
Enter the password: mysecretpassword
Enter the data to hide: Hello, this is a secret message!
Enter the output image name (optional, e.g., stego.png): stego.jpg
```

The resulting image will have the message hidden in its pixel values and can be retrieved by authorized users who know the password.

## How It Works

1. **Text to Binary**: The password and data are converted to binary.
2. **Embed Data in Image**: The binary message is embedded into the image by modifying the least significant bit (LSB) of the pixel's RGB color channels.
3. **Save Modified Image**: The modified image is saved as the output file.

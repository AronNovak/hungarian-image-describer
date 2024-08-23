# Anthropic Image Describer

This Python program captures images from a webcam, sends them to the Anthropic API for description, and then speaks the description in Hungarian using the `espeak-ng` text-to-speech engine.

## Requirements

- Python 3.6 or higher
- OpenCV (`cv2`)
- `requests` library
- `espeak-ng` text-to-speech engine

## Installation

1. Clone the repository:

```
git clone https://github.com/yourusername/anthropic-image-describer.git
```

2. Install the required Python libraries:

```
pip install opencv-python requests
```

3. Install the `espeak-ng` text-to-speech engine:

- On Ubuntu/Debian:
```
sudo apt install espeak-ng
```

- On macOS (using Homebrew):
```
brew install espeak-ng
```

- On Windows, download the installer from the [official website](https://github.com/espeak-ng/espeak-ng/releases) and follow the installation instructions.

## Usage

Run the program with your Anthropic API key as a command-line argument:

```
python anthropic_image_describer.py YOUR_API_KEY
```

Press Enter to capture an image from the webcam. The program will send the image to the Anthropic API for description, display the description in the console, and speak it in Hungarian using `espeak-ng`.

To exit the program, press `Ctrl+C` in the terminal.

## Customization

- To change the language of the image description, modify the text in the `content` field of the `payload` dictionary in the `describe_image` function.
- To change the language or voice settings for the text-to-speech engine, modify the arguments passed to `espeak-ng` in the `speak_text` function.

## License

This project is open-source and available under the [MIT License](LICENSE).

## Contributing

Feel free to submit issues or pull requests if you have any suggestions or improvements for the program.

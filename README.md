# HEIC-to-JPG-Converter

## Overview

This project is a simple web application that allows users to convert HEIC (High Efficiency Image File Format) images to JPG format. Using Python's Flask framework and the `pyheif` library, this app provides a user-friendly interface for seamless image conversion.

## Features

- Upload HEIC files for conversion.
- Convert HEIC images to JPG format.
- Download converted JPG images directly from the web interface.
- Built with Flask for easy deployment and use.

## How It Works

The core functionality of the app is based on the `convert_to_jpg` function, which reads a HEIC file and converts it into a JPG image. Here’s a brief overview of the function:

```python
def convert_to_jpg(file_path):
    # Read the HEIF file
    heif_file = pyheif.read(file_path)
    image = Image.frombytes(
        heif_file.mode, 
        heif_file.size, 
        heif_file.data,
        "raw",
        heif_file.mode,
        heif_file.stride,
    )
```

This function utilizes the `pyheif` library to read the HEIC file and the `PIL` (Pillow) library to create an image object from the raw data. The resulting image can then be saved in JPG format.

## Getting Started

To run the application locally, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/heic-to-jpg-converter.git
   cd heic-to-jpg-converter
   ```

2. **Install Dependencies**:
   Ensure you have Python installed, then install the required packages:
   ```bash
   pip install Flask pyheif Pillow
   ```

3. **Run the Application**:
   Start the Flask server:
   ```bash
   python app.py
   ```

4. **Access the Web App**:
   Open your web browser and go to `http://127.0.0.1:5000` to use the converter.

## Live Demo

You can also check out a live demo of the application at [heic.com](https://heic.com).

## Contributing

Contributions are welcome! If you have suggestions or improvements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License.


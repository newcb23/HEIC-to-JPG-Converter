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

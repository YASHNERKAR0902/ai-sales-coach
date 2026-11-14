
import os

file_path = "sample_call.mpeg"

print("File exists:", os.path.exists(file_path))

if os.path.exists(file_path):

    print("File size:", os.path.getsize(file_path), "bytes")

    with open(file_path, "rb") as file:
        header = file.read(32)

    print("File header:", header)
    print("Header in hexadecimal:", header.hex())

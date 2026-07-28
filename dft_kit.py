"""
    to do image analysis --> pip install Pillow


"""
import os

from PIL import Image
from PIL.ExifTags import TAGS
import zipfile
import PyPDF2
from datetime import datetime

print("="*60)
print("        DIGITAL EVIDENCE ANALYZER")
print("="*60)

# ask user to enter file path:

filepath = input("\n Enter File Path: ")

if not os.path.exists(filepath):
    print("\n File not found")
    exit()


# ------------
# extract the file extension
# report.pdf

extension = os.path.splitext(filepath)[1].lower()
print(extension)

# ------------ human readable file size
size = os.path.getsize(filepath)

# 1 kb == ?
# 1 mb == ?


if size < 1024:
    filesize = f"{size} Bytes"
elif size < 1024*1024:
    filesize = f"{round(size/1024,2)} KB"
else:
    filesize = f"{round(size/(1024*1024),2)} MB"



print("\n")
print("="*60)
print("BASIC INFORMATION")
print("="*60)

print("FILE NAME: ",os.path.basename(filepath))
print("EXTENSION: ",extension)
print("SIZE: ",filesize)


# ---------------- TIME ANALYSIS -------------------

print("\n")
print("="*60)
print("TIME LINE ANALYSIS:")
print("="*60)

# ------ created , modified , accessed

created = datetime.fromtimestamp(os.path.getctime(filepath)).strftime("%d-%m-%Y %I:%M:%S %p")
print("Created: ",created)
modfied = datetime.fromtimestamp(os.path.getmtime(filepath)).strftime("%d-%m-%Y %I:%M:%S %p")
print("Modified: ",modfied)
accessed = datetime.fromtimestamp(os.path.getatime(filepath)).strftime("%d-%m-%Y %I:%M:%S %p")
print("Accessed: ",accessed)


# ------- hidden file detection ------------

print("\n")
print("=" * 60)
print("Hidden File Check")
print("=" * 60)

filename = os.path.basename(filepath)

if filename.startswith("."):
    print("Hidden File is there")
else:
    print("No Hidden file available")


# ================== suspicious extension detection
print("\n")
print("=" * 60)
print("Suspicious Extension Check")
print("=" * 60)

dangerous = [".exe",".bat",".cmd",",psl",".vbs",".js",".scr"]

if extension in dangerous:
    print("WARNING: Executable File")
elif filename.count(".") > 1:
    print("WARNING: Multiple Extension Detected")
else:
    print("Extension Looks Normal")

# report.doc.pdf  , photo.jpg.png , system.pdf.exe

# --------- signature analysis -----------

print("\n")
print("=" * 60)
print("File Signature Analysis")
print("=" * 60)

with open(filepath,"rb") as f:
    header = f.read(8)

    print(header)

hexsig = header.hex().upper()
print(hexsig)
# MAGIC BYTE: 25 50 44 65
print("Magic Bytes: "," ".join(hexsig[i:i+2] for i in range(0,len(hexsig),2)))

# --------- virus.exe ---> salary.pdf -----------
magic = {
    "25504446":"PDF Document",
    "FFD8FF":"JPEG Image",
    "89504E47":"PNG Image",
    "504B0304":"Zip Archive",
    "4D5A":"Windows Executable"
}

actual = "Unknown"

for sig , name in magic.items():
    if hexsig.startswith(sig):
        actual = name
        break

print("Detected type: ",actual)




# --------------- IMAGE ANALYSIS ----------------


if extension in [".jpg",".jpeg",".png"]:
    print("\n")
    print("=" * 60)
    print("image analysis")
    print("=" * 60)

    image = Image.open(filepath)

    print("Width: ",image.width)
    print("Height: ",image.height)
    print("Format: ",image.format)
    print("Color Mode: ",image.mode)

    print("MetaData")
    print("-"*60)

    exif = image.getexif()  # metadata
    print(exif)

    if exif:

        print("\n Useful Metadata")

        useful = ["Make","Model","DateTime","Software","GPSInfo","Flash","ExposureTime",
                  "FocalLength","LensModel","ISOSpeedRatings"]

        for tag_id , value in exif.items():
            tag = TAGS.get(tag_id,tag_id)
            if tag in useful:
                print(f"{tag}: {value}")

    else:
        print("No Metadata found")


elif extension == ".pdf":
    print("\n")
    print("=" * 60)
    print("PDF ANALYSIS")
    print("=" * 60)

    with open(filepath,"rb") as file:

        reader = PyPDF2.PdfReader(file)

        print("Pages      :",len(reader.pages))
        print("Encrypted  :",reader.is_encrypted)

        print("\n PDF Metadata")
        print("-"*60)

        metadata = reader.metadata

        if metadata:
            for key , value in metadata.items():
                print(key,":",value)
        else:
            print("No Metadata Found")

        creationdate = metadata["/CreationDate"]
        print(creationdate)

        # convert string to time -- strftime(yyyy-mm-dd)


elif extension == ".zip":
    print("\n")
    print("=" * 60)
    print("ZIP ANALYSIS")
    print("=" * 60)

    with zipfile.ZipFile(filepath,"r") as zip_file:

        files = zip_file.infolist()

        print("Total Files: ",len(files))
        print("\n Files Inside Zip: ")

        encrypted = False

        for file in files:
            print(file.filename)

            # if the encrypted flag is set
            if file.flag_bits & 0x1:
                encrypted = True

        print("Password Protected: ",encrypted)

else:

    print("No Analyzer available for this file type")


print("Investigation completed")
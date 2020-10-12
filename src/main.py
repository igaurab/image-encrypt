from enum import Enum
import argparse
import os
import ntpath
from pathlib import Path
from crypto import encrypt
from crypto import decrypt
import imghdr

class Strings(Enum):
    HELP_ENCRYPT = "Image to be encrypted"
    HELP_DECRYPT = "Image to be decrypted"
    HELP_PASSWORD = "Password for encryption and decryption"
    HELP_OUTPUT = "Name of the output file"
    HELP_DIR_ENC = "Encrypt all images in the given directory"
    HELP_DIR_DEC = "Decrypt all images in the given directory"

def path_leaf(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)

def encrypt_image(path,password,output):
    encrypt(path=path, seed=seed,output=output)

def decrypt_image(path,password,output):
    decrypt(path=path, seed=seed,output=output)

parser = argparse.ArgumentParser(description="Encrypt images")
parser.add_argument('-e',  default="e", help=Strings.HELP_ENCRYPT)
parser.add_argument('-d',  default="d", help=Strings.HELP_DECRYPT)
parser.add_argument('-p',  default=None, required=True, help=Strings.HELP_PASSWORD)
parser.add_argument('-o',  default=None, help=Strings.HELP_OUTPUT)
parser.add_argument('-encdir',default=None, help=Strings.HELP_DIR_ENC)
parser.add_argument('-decdir',default=None, help=Strings.HELP_DIR_DEC)
args = parser.parse_args()

seed = sum([ord(c) for c in args.p])

if args.encdir:
    dir_path = os.path.abspath(Path(args.encdir))
    image_files = [os.path.join(dir_path,f) for f in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path,f)) and imghdr.what(os.path.join(dir_path,f)) != None]
    os.mkdir("encrypted-images")
    os.chdir("encrypted-images")
    for image in image_files:
        name = path_leaf(image).split('.')[0]
        output = name + ".png"
        encrypt_image(image,args.p,output=output)
    os.chdir("../")

if args.decdir:
    dir_path = os.path.abspath(Path(args.decdir))
    image_files = [os.path.join(dir_path,f) for f in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path,f)) and imghdr.what(os.path.join(dir_path,f)) != None]
    os.mkdir("decrypted-images")
    os.chdir("decrypted-images")
    for image in image_files:
        name = path_leaf(image).split('.')[0]
        output = "dec-"+name + ".png"
        decrypt_image(image,args.p,output=output)
    os.chdir("../")

if args.e:
    path = os.path.abspath(Path(args.e))
    if(os.path.isfile(path)):
        name = path_leaf(path).split('.')[0]
        output = "enc-"+name + ".png"
        encrypt_image(path=path,password=args.p, output=output)

if args.d:
    path = os.path.abspath(Path(args.d))
    if(os.path.isfile(path)):
        name = path_leaf(path)[4:].split('.')[0]
        output = "dec-"+name + ".png"
        decrypt_image(path=path,password=args.p, output=output)
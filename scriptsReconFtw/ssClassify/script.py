import pytesseract
from PIL import Image
from pathlib import Path
import os, json, re, sys

def processImage(arg1):

    global varDir
    global dirList

    folder_dir = arg1
    folder_path = Path(folder_dir)
    images = [p for p in folder_path.glob('*') if p.suffix in ('.png', '.jpg', '.jpeg', '.img')]
    images.sort()

#   Make Dirs to move images in

    dirList = ['organised', 'organised/other', 'organised/firewall', 'organised/header', 'organised/unclassified', 'organised/unusedService', 'organised/httpBadRequest', 'organised/login', 'organised/defaultPage', 'organised/error', 'organised/methodNotAllowed', 'organised/blocked']

    firewallKeyList = ['cloudfront403', 'forbidden', 'pageNotFound', 'imperva22', 'requestBlocked', 'accessDenied','unauthorized401','forbidden403', 'forbidden403_1','messageForbidden', 'notFound404', 'iis404']
    blockedKeyList = ['cloudflareBlocked']
    loginKeyList = ['login', 'signup', 'signin', 'register', 'signin1','username','password']
    otherKeyList = ['noRouteMatched','ringBalancer', 'statusOK']
    headerKeyList = ['invalidXYHeader']
    unusedServiceKeyList = ['azureFrontDoor','zendesk']
    defaultPageKeyList = ['nortanLifeLock', 'nortanLifeLock2']
    errorKeyList = ['whitelabelError','error', 'error1', 'cloudflareRayId','dnsResolutionError', 'invalidUrl', 'serviceUnavailable503', 'temporarilyServiceUnavalaible','httpBadRequest','badRequest400', 'anErrorHasOccured','serverError500']
    methodNotAllowedKeyList = ['notAllowed405']

    for varDir in dirList:
        if os.path.isdir(varDir):
            pass
        else:    
            os.system(f'mkdir {arg1}/{varDir}')

#----------------------Iterate over every image file-----------------------
    with open('strings.json', 'r') as file:
        data = json.load(file)

        for image in images:

            imageToProcess = Image.open(image)
            text = pytesseract.image_to_string(imageToProcess)

            for key, value in data.items():
                if any(word in text.rstrip() for word in [value]):
                    
                    if key in firewallKeyList:
                        os.system(f'mv {image} {arg1}/organised/firewall')
                        print(f"[x] {image} moved into '{arg1}/organised/firewall'")
                          

                    elif key in headerKeyList:
                        os.system(f'mv {image} {arg1}/organised/header')
                        print(f"[x] {image} moved into 'organised/header'")
                        

                    elif key in unusedServiceKeyList:
                        os.system(f'mv {image} {arg1}/organised/unusedService')
                        print(f"[x] {image} moved into '{arg1}/organised/unusedService'")
                        

                    elif key in otherKeyList:
                        os.system(f'mv {image} {arg1}/organised/other')
                        print(f"[x] {image} moved into '{arg1}/organised/other'")
                        

                    elif key in loginKeyList:
                        os.system(f'mv {image} {arg1}/organised/login')
                        print(f"[x] {image} moved into '{arg1}/organised/login'")
                        
                        
                    elif key in defaultPageKeyList:
                        os.system(f'mv {image} {arg1}/organised/defaultPage')
                        print(f"[x] {image} moved into '{arg1}/organised/defaultPage'")
                        

                    elif key in errorKeyList:
                        os.system(f'mv {image} {arg1}/organised/error')
                        print(f"[x] {image} moved into '{arg1}/organised/error'")
                           

                    elif key in methodNotAllowedKeyList:
                        os.system(f'mv {image} {arg1}/organised/methodNotAllowed')
                        print(f"[x] {image} moved into '{arg1}/organised/methodNotAllowed'")
                        

                    elif key in blockedKeyList:
                        os.system(f'mv {image} {arg1}/organised/blocked')
                        print(f"[x] {image} moved into '{arg1}/organised/blocked'")
                        

                        

                    break
            else:
                print(f'[-] {image} is unclassified')
                
                os.system(f'mv {image} {arg1}/organised/unclassified')
                print(f"[x] {image} moved into '{arg1}/organised/unclassified'")
                
    file.close()


def removeEmptyDir(dirList, arg1):

    for varDir in dirList:
        if not os.listdir(f'{arg1}/{varDir}'):
            os.system(f'rm -rf {arg1}/{varDir}')

def main():

# To check if the directory which is provided was previously organised
#-----------------------------------------------------------------------

    if len(sys.argv)!=2:
        print("Provide directory containing images")
        print("Usage:\npython3 script.py screenshots")
        sys.exit()

    arg1 = sys.argv[1]

# Remove trailing slash (/)
    if arg1.endswith('/'):
        arg1 = arg1[:-1]

    arg1 = f'{arg1}/screenshots'

#-----------------------------------------------------------------------

    if os.path.isdir(f'{arg1}/organised'):
        print(f'[x] \'screenshots\' is already organised')
        sys.exit()
        

    processImage(arg1)
    removeEmptyDir(dirList,arg1)

    print(f'[+] All image files are classified, and stored in `{arg1}/organised`')
    print("[x] 'Classyfing Screeshots' done")

if __name__ == "__main__":
    main()

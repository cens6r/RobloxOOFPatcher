import os, shutil

def main():
    appdata = os.environ.get("LOCALAPPDATA")

    robloxVersions = []

    roblox = appdata+"/Roblox/Versions/"

    for root, dirs, files in os.walk(roblox):
        for file in files:
            robloxVersions.append(os.path.join(root,file))

    sound = robloxVersions[0]+"/Content/sounds"

    os.remove(sound+"/ouch.ogg")

    shutil.copy("./ouch.ogg", sound)

if __name__ == '__main__':
    main()

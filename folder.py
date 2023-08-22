import glob

def get_musicname():
    list_t = []
    files = glob.glob("files/music/*.mp3")
    for file in files:
        file = file.replace("files/music\\", "")
        file = file.replace(".mp3", "")
        #print(file)
        list_t.append(file)
    return list_t


def get_musicfilename():
    list_t = []
    files = glob.glob("files/music/*.mp3")
    for file in files:
        #print(file)
        list_t.append(file)
    return list_t

if __name__ == "__main__":
    print(get_musicname())
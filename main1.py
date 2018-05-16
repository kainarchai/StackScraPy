with open("urls.txt", "r+") as urls:
    lines = urls.readlines()
    for line in lines:
        line = line[:1]+'https://stackshare.io'+line[1:]
        urls.write(line)
import os

def main():
    i = 0
    path = "C:/Users/belos/Desktop/к стихам/новое новое/"
    for filename in os.listdir(path):
        new_name = "img" + str(i) + ".jpg"
        source = path + filename
        new_name = path + new_name
        os.rename(source, new_name)
        i += 1

if __name__ == '__main__':
    main()



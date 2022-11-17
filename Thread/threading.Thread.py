import threading
import time
import requests




def download_image(img_url):
    img_bytes = requests.get(img_url).content
    img_name = img_url.split('/')[3]   #+ '.jpg'   #on ajoute JPG pour mettre à la bonne extension si l'image n'a pas déjà une bonne extension
    with open(img_name, 'wb') as img_file:
        img_file.write(img_bytes)
        print(f"{img_name} was downloaded")

start = time.perf_counter()

if __name__ == '__main__':
    t1 = threading.Thread(target=download_image,args=['https://astra.icu/p2.png'])
    t2 = threading.Thread(target=download_image,args=['https://astra.icu/p3.png'])

    t1.start()
    t2.start()

    t1.join()
    t2.join()

end = time.perf_counter()
print(f"Tasks ended in {round(end - start, 2)} second(s)")
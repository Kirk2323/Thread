import time
import multiprocessing
import requests

def task():
    print(f"Task starts for 1 second")
    time.sleep(1)
    print(f"Task ends")

img_urls = [
    'https://cdn.pixabay.com/photo/2010/12/13/09/51/fireworks-1758_960_720.jpg',
    'https://cdn.pixabay.com/photo/2017/01/28/02/24/japan-2014618_960_720.jpg',
    'https://cdn.pixabay.com/photo/2015/02/24/15/41/wolf-647528_960_720.jpg'
]

def download_image(img_url):
    img_bytes = requests.get(img_url).content
    img_name = img_url.split('/')[3] #+ '.jpg'   #on ajoute JPG pour mettre à la bonne extension
    with open(img_name, 'wb') as img_file:
        img_file.write(img_bytes)
        print(f"{img_name} was downloaded")

if __name__ == '__main__':
    start = time.perf_counter()
    p1 = multiprocessing.Process(target=download_image, args=['https://astra.icu/p1.png'])
    p2 = multiprocessing.Process(target=download_image,args=['https://astra.icu/p2.png'])
    p3 = multiprocessing.Process(target=download_image,args=['https://astra.icu/p3.png'])
    p1.start()
    p2.start()
    p3.start()
    p1.join()
    p2.join()
    p3.join()
    end = time.perf_counter()
    print(f"Tasks ended in {round(end - start, 2)} second(s)")



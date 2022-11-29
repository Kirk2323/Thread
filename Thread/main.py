import threading
import time
import requests
import concurrent.futures
i = int(input("Merci de rentrer le nombre de tests que vous souhaitez : "))

start = time.perf_counter()

img_urls = [
    'https://cdn.pixabay.com/photo/2010/12/13/09/51/fireworks-1758_960_720.jpg',
    'https://cdn.pixabay.com/photo/2014/09/26/05/56/fireworks-461750_960_720.jpg'
]

def download_image(img_url):
    img_bytes = requests.get(img_url).content
    img_name = img_url.split('/')[3] + '.jpg'   #on ajoute JPG pour mettre à la bonne extension
    with open(img_name, 'wb') as img_file:
        img_file.write(img_bytes)
        print(f"{img_name} was downloaded")



def test():
    print("Attend 1 seconde")
    time.sleep(1)
    print("C'est bon !")


for i in range(i):
    t1 = threading.Thread(target=download_image,args=['https://astra.icu/p2.png'])
    t2 = threading.Thread(target=download_image,args=['https://astra.icu/p3.png'])

    t1.start()
    t2.start()

end = time.perf_counter()
print(f"Tasks ended in {round(end - start, 2)} second(s)")
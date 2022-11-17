import time
import concurrent.futures
import requests

img_urls = [
    'https://cdn.pixabay.com/photo/2010/12/13/09/51/fireworks-1758_960_720.jpg',
    'https://cdn.pixabay.com/photo/2017/01/28/02/24/japan-2014618_960_720.jpg',
    'https://cdn.pixabay.com/photo/2015/02/24/15/41/wolf-647528_960_720.jpg'
]

def download_image(img_url):
    img_bytes = requests.get(img_url).content
    img_name = img_url.split('/')[4] + '.jpg'   #on ajoute JPG pour mettre à la bonne extension
    with open(img_name, 'wb') as img_file:
        img_file.write(img_bytes)
        print(f"{img_name} was downloaded")

start = time.perf_counter()

if __name__ == '__main__':
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(download_image, img_urls)

end = time.perf_counter()
print(f"Tasks ended in {round(end - start, 2)} second(s)")
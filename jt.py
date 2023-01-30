import cv2, time, os, glob
from PIL import Image

def video_to_frames(path):
    try:
        videoCapture = cv2.VideoCapture()
        videoCapture.open(path)
        fps = videoCapture.get(cv2.CAP_PROP_FPS)
        frames = videoCapture.get(cv2.CAP_PROP_FRAME_COUNT)
        height = videoCapture.get(cv2.CAP_PROP_FRAME_HEIGHT)
        width = videoCapture.get(cv2.CAP_PROP_FRAME_WIDTH)
        os.system('cls||clear')
        for i in range(int(frames)):
            ret, frame = videoCapture.read()
            cv2.imwrite(f"frames/{i}.png", frame)
            os.system('cls||clear')
            if i > int(frames):
                exit()
    except Exception as e:
        input()
        exit()
s = 'ponpon'
root_dir = f"frames/"
IMAGES_PATH = f"frames/"  # Адрес коллекции изображений
IMAGES_FORMAT = ['.png']  # Формат изображения
IMAGE_SIZE = 268  # Размер каждой маленькой картинки

IMAGE_COLUMN = 15  # Картинка интервал, то есть после слияния в одну картинку получается всего несколько столбцов
IMAGE_SAVE_PATH = f"./out_tex.png"  # Адрес после преобразования изображения
# Получить все имена изображений под адресом коллекции изображений
image_names = [name for name in os.listdir(IMAGES_PATH) for item in IMAGES_FORMAT if
               os.path.splitext(name)[1] == item]
IMAGE_ROW =  15# Интервал картинки, то есть после объединения в одну картинку получается всего несколько строк
IMAGE_ROW_yu = len(image_names) % IMAGE_COLUMN
if IMAGE_ROW_yu == 0:
    IMAGE_ROW = len(image_names) // IMAGE_COLUMN
else:
    IMAGE_ROW = len(image_names) // IMAGE_COLUMN + 1

# Определить функцию сшивания изображений
def image_compose():
    to_image = Image.new('RGB', (IMAGE_COLUMN * IMAGE_SIZE, IMAGE_ROW * IMAGE_SIZE))  # Создать новую картинку
    # Прокрутите, вставьте каждое изображение в соответствующую позицию по порядку
    total_num = 0
    for y in range(1, IMAGE_ROW + 1):
        for x in range(1, IMAGE_COLUMN + 1):
            from_image = Image.open(IMAGES_PATH + image_names[IMAGE_COLUMN * (y - 1) + x - 1]).resize(
                (IMAGE_SIZE, IMAGE_SIZE), Image.ANTIALIAS)
            to_image.paste(from_image, ((x - 1) * IMAGE_SIZE, (y - 1) * IMAGE_SIZE))
            total_num += 1
            if total_num == len(image_names):
                break
    return to_image.save(IMAGE_SAVE_PATH)  # Сохранить новое изображение

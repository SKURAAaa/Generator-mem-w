import cv2

def generate_meme(image_path, text):
    # Wczytaj obrazek
    ref_image = cv2.imread(image_path)

    if ref_image is None:
        print("Błąd: Nie można wczytać obrazka z podanej ścieżki:", image_path)
        return

    # Pobierz wymiary
    height, width = ref_image.shape[:2]

    # Dodaj border
    border_size = 100
    bordered_image = cv2.copyMakeBorder(ref_image, 0, border_size, 0, 0, cv2.BORDER_CONSTANT, value=(0, 0, 0))

    # Dodaj tekst na dolnej krawędzi czarnej przestrzeni
    font = cv2.FONT_HERSHEY_SIMPLEX
    text_size = cv2.getTextSize(text, font, 2, 3)[0]  # Zwiększamy rozmiar tekstu
    text_x = (width - text_size[0]) // 2
    text_y = height + border_size - 20  # Umieść tekst na dolnej krawędzi inaczej mi nie działało dlategggo powiekkszyłem text
    cv2.putText(bordered_image, text, (text_x, text_y), font, 2, (255, 255, 255), 3, cv2.LINE_AA)  # Zmieniamy kolor tekstu na biały

    # Wyświetl obrazek
    cv2.imshow("Meme Generator", bordered_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

#użycie
image_path = r"C:\Users\Kacper\PycharmProjects\LAB5\venv\images\memik.jpg"  # ścieżka do obrazka referencyjnego
text = "memik"
generate_meme(image_path, text)

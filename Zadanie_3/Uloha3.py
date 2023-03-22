import cv2

# Nacitanie obrazka
img = cv2.imread("D:\School\PVSO\Projects\Zadanie_3\obrazok.jpg")

# Prevod na grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Aplikacia binarizacie na obrazok
_, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# Najdenie kontur v binarizovanom obrazku
contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Nakreslenie najdenych kontur na obrazok
cv2.drawContours(img, contours, -1, (255, 0, 0), 3)

# Zobrazenie vysledneho obrazku s konturami
cv2.imshow("Kontury", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

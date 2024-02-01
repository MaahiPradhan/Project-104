import cv2

img = cv2.imread("solar-system.jpg")

cv2.putText(img,
              "Sun",
               (20, 300),
                cv2.FONT_HERSHEY_COMPLEX,
                0.5,
                (255, 255, 255))

cv2.putText(img,
              "Mercury",
               (100, 300),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.5,
                (128, 0, 255))

cv2.putText(img,
              "Venus",
               (200, 300),
                cv2.FONT_HERSHEY_PLAIN,
                0.5,
                (64, 0, 255))

cv2.putText(img,
              "Earth",
               (300, 300),
                cv2.FONT_HERSHEY_DUPLEX,
                0.5,
                (0, 0, 255))

cv2.putText(img,
              "Mars",
               (400, 300),
                cv2.FONT_HERSHEY_TRIPLEX,
                0.5,
                (0, 64, 255))

cv2.putText(img,
              "Jupiter",
               (500, 300),
                cv2.FONT_HERSHEY_COMPLEX_SMALL,
                0.5,
                (255, 0, 128))

cv2.putText(img,
              "Saturn",
               (800, 300),
                cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,
                0.5,
                (0, 191, 255))

cv2.putText(img,
              "Uranus",
               (950, 300),
                cv2.FONT_HERSHEY_SCRIPT_COMPLEX ,
                0.5,
                (0, 255, 255))

cv2.putText(img,
              "Neptune",
               (1100, 300),
                cv2.FONT_HERSHEY_COMPLEX,
                0.5,
                (0, 255, 191))

cv2.imshow("output", img)
cv2.waitKey(0)
cv2.imwrite("Solar_systemwithname.jpg", img)

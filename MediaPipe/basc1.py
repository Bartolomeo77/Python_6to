import cv2
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

with mp_hands.Hands(
    static_image_mode=True,
    max_num_hands=2,
    min_detection_confidence=0.5) as hands:

    image = cv2.imread("palmas.jpg")
    height, width, _ = image.shape

    image = cv2.flip(image, 1)

    
    image_rgb =cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    results = hands.process(image_rgb)

    # HANDEDNESS
    print('Handedness:', results.multi_handedness)
    #print('Handedness:', results.multi_hand_landmarks)

    if results.multi_hand_landmarks is not None:
        # -----------------
        for hand_landmarks in results.multi_hand_landmarks:
            #print(hand_landmarks)
            index=[4,8,12,16,20]
            for (i,points) in enumerate(hand_landmarks.landmark):
                if i in index:
                    x = int(points.x * width)
                    y = int(points.y * height)
                    cv2.circle(image,(x,y),3,(255,0,0),3)













        # -----------------

            #Accediendo a los puntos clave , de acuerdo a su nombre

            #x1 = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].x * width
            #y1 = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].y * height
            #print(x1,y1)

            #cv2.circle(image,(int(x1),int(y1)),3,(255,0,0),3)



        # -----------------
            #Dibujando los puntos y sus conexiones con mediapipe
            #mp_drawing.draw_landmarks(
             #   image,hand_landmarks, mp_hands.HAND_CONNECTIONS,
              #  mp_drawing.DrawingSpec(color=(255,255,0),thickness=4,circle_radius=5),
               # mp_drawing.DrawingSpec(color=(255,0,255),thickness=4)
            #)



    image = cv2.flip(image, 1)
cv2.imshow("Image",image)
cv2.waitKey(0)
cv2.destroyAllWindows()










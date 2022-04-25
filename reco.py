import cv2, sys, numpy, os, time
size = 3
fn_haar = 'haarcascade_frontalface_default.xml'
fn_dir = 'Photos'

def trainer():
    print ('this is trainer')
    (images, lables, id) = ([], [], 0)

    for (subdirs, dirs, files) in os.walk(fn_dir):

        # Loop through each folder named after the subject in the photos
        for subdir in dirs:
            subjectpath = os.path.join(fn_dir, subdir)

            # Loop through each photo in the folder
            for filename in os.listdir(subjectpath):

        # Skip non-image formates
                f_name, f_extension = os.path.splitext(filename)
                if(f_extension.lower() not in
                ['.png','.jpg','.jpeg','.gif','.pgm']):
                    print("Skipping "+filename+", wrong file type")
                    continue
                path = subjectpath + '/' + filename
                lable = id

                # Add to training data
                images.append(cv2.imread(path, 0))
                lables.append(int(lable))
            id += 1


    # Create a Numpy array from the two lists above
    (images, lables) = [numpy.array(lis) for lis in [images, lables]]

    # OpenCV trains a model from the images
    # NOTE FOR OpenCV2: remove '.face'
    model = cv2.face.LBPHFaceRecognizer_create()
    #model = cv2.face.EigenfaceRecognizer_create()
    model.train(images, lables)
    model.save("trained_model.yml")

def face_reco(infirmiere):
    vretour = []
    count_good = 0
    count_too_many = 0
    # Create a list of images and a list of corresponding names
    (images, lables, names, id) = ([], [], {}, 0)

    # Get the folders containing the training data
    for (subdirs, dirs, files) in os.walk(fn_dir):

        # Loop through each folder named after the subject in the photos
        for subdir in dirs:
            names[id] = subdir
            #trainer()
            id += 1



    # Part 2: Use fisherRecognizer on camera stream
    model = cv2.face.LBPHFaceRecognizer_create()
    model.read("trained_model.yml")
    haar_cascade = cv2.CascadeClassifier(fn_haar)
    video_capture = cv2.VideoCapture(0)
    (im_width, im_height) = (112, 92)
    start = time.time()
    while True:
        end = time.time()

        # Loop until the camera is working
        rval = False
        while(not rval):
            # Put the image from the webcam into 'frame'
            (rval, frame) = video_capture.read()
            if(not rval):
                print("Failed to open webcam. Trying again...")

        # Flip the image (optional)
        frame=cv2.flip(frame,1,0)

        # Convert to grayscalel
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Resize to speed up detection (optinal, change size above)
        mini = cv2.resize(gray, (int(gray.shape[1] / size), int(gray.shape[0] / size)))

        # Detect faces and loop through each one
        faces = haar_cascade.detectMultiScale(mini)
        for i in range(len(faces)):
            face_i = faces[i]

            # Coordinates of face after scaling back by `size`
            (x, y, w, h) = [v * size for v in face_i]
            face = gray[y:y + h, x:x + w]
            face_resize = cv2.resize(face, (im_width, im_height))

            # Try to recognize the face
            prediction = model.predict(face_resize)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)

            # [1]
            # Write the name of recognized face
            if len(faces)>=2:
                count_too_many+=1
            else:
                if prediction[1]<80:
                    cv2.putText(frame,'%s - %.0f' % (names[prediction[0]],prediction[1]),(x-10, y-10), cv2.FONT_HERSHEY_PLAIN,1,(0, 255, 0))
                    if names[prediction[0]] == infirmiere:
                       count_good+=1
                else:
                    cv2.putText(frame,'not recognized', (x-10, y-10), cv2.FONT_HERSHEY_PLAIN,1,(0, 0, 255))

        # Show the image and check ...
        #if cv2.waitKey(1) & 0xFF == ord('q'):
        #    break

        if count_good == 10:
            vretour.append(True)
            break
        
        if count_too_many == 10:
            vretour.append(False)
            vretour.append('trop de faces')
            break

        if  end - start > 30:
            vretour.append(False)
            vretour.append('face non reconnnue avant fin timer') 
            break

        # Display the resulting frame
        cv2.imshow('Video', frame)

    # When everything is done, release the capture
    video_capture.release()
    cv2.destroyAllWindows()
    return vretour

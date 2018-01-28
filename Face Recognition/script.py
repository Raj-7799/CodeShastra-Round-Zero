import face_recognition
import os


os.chdir("known/")
list_known_images = os.listdir()
names_list = []
face_encoding = []
for name in list_known_images:
    names_list.append(face_recognition.load_image_file(name))

print(len(list_known_images))

for image in names_list:
    face_encoding.append(face_recognition.face_encodings(image)[0])


print(len(names_list))
os.chdir("..")
unknown_image = face_recognition.load_image_file("unknown/image.jpeg")

unknown_encoding = face_recognition.face_encodings(unknown_image)[0]

results = face_recognition.compare_faces(face_encoding, unknown_encoding)

print(results)
print(list_known_images)
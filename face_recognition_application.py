import face_recognition
import cv2
import os
import re

# Directory paths for images
known_faces_dir = "known_faces"
test_image_path = "test_images/test_image2.jpg"

# Function to encode known faces from the directory
def load_known_faces(known_faces_dir):
    encoding_list = []
    name_list = []
    for filename in os.listdir(known_faces_dir):
        filepath = os.path.join(known_faces_dir, filename)
        if not os.path.isfile(filepath):
            continue
        # Load and encode face
        image = face_recognition.load_image_file(filepath)
        encodings = face_recognition.face_encodings(image)
        if encodings:
            encoding_list.append(encodings[0])
            # Remove numbers and format the name
            name_without_numbers = re.sub(r'\d+', '', filename.split('.')[0])  # Remove digits
            formatted_name = ' '.join(part.capitalize() for part in name_without_numbers.split('_'))
            name_list.append(formatted_name)  # Use formatted name
        else:
            print(f"Warning: No face found in {filename}. Skipping.")
    return encoding_list, name_list

# Load known faces
encoding_list, name_list = load_known_faces(known_faces_dir)

# Load and process the test image
test_image = face_recognition.load_image_file(test_image_path)
image_rgb = cv2.cvtColor(test_image, cv2.COLOR_BGR2RGB)  # Convert to RGB for accurate results
facelocations = face_recognition.face_locations(image_rgb)
face_encodings = face_recognition.face_encodings(image_rgb, facelocations)

# Process each face found in the test image
for faceloc, face_encoding in zip(facelocations, face_encodings):
    top, right, bottom, left = faceloc
    matches = face_recognition.compare_faces(encoding_list, face_encoding)
    name = "Unknown Person"

    # Find the closest match based on distance
    face_distances = face_recognition.face_distance(encoding_list, face_encoding)
    best_match_index = face_distances.argmin() if matches else None

    if best_match_index is not None and matches[best_match_index]:
        name = name_list[best_match_index]

    # Draw rectangle and name on the image
    cv2.rectangle(test_image, (left, top), (right, bottom), (255, 0, 0), 2)
    cv2.putText(test_image, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (255, 0, 0), 2)

# Convert back to BGR for displaying
test_image_bgr = cv2.cvtColor(test_image, cv2.COLOR_RGB2BGR)

# Display the result
cv2.imshow("Face Recognition", test_image_bgr)
cv2.waitKey(0)
cv2.destroyAllWindows()

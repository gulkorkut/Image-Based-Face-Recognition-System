# Image-Based Face Recognition System

## Overview
The Image-Based Face Recognition System is a Python application designed to recognize and label faces in images using state-of-the-art face recognition techniques. This system leverages the `face_recognition` library along with `OpenCV` to accurately detect and identify known faces from a provided dataset.

## Features
- **Face Recognition**: Identify known individuals in images.
- **Dynamic Naming**: Automatically formats names for display, capitalizing the first letters and removing any numeric suffixes.
- **Visual Feedback**: Draws rectangles around detected faces and displays their names in blue.
- **Customizable Dataset**: Easily add new faces by placing images in the designated directory.

## Requirements
To run this project, you need to have the following installed:
- Python 3.x
- OpenCV
- face_recognition
- dlib
- NumPy

## Installation
Follow these steps to set up the project on your local machine:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/Image-Based-Face-Recognition-System.git
   cd Image-Based-Face-Recognition-System


## Usage
1. **Prepare your dataset**:
   - Create a directory named `known_faces` and place images of known individuals in it.
   - Name the images using the format `first_last.jpg` (e.g., `bill_gates.jpg`, `mark_zuckerberg.jpg`).

2. **Test Image**:
   - Place the test image you want to analyze in the `test_images` directory (e.g., `test_image1.jpg`).

3. **Run the application**:
   ```bash
   python face_recognition_application.py
   ```

4. **View Results**:
   - The output will display the test image with rectangles around recognized faces, labeled with their respective names.

## Example

Result of recognizing Elon Musk's face in a test image.

![Elon Musk Recognition Result](result.png)


## Code Structure
- `face_recognition_app.py`: The main script to run the face recognition application.
- `known_faces/`: Directory containing images of known individuals.
- `test_images/`: Directory containing images for testing.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments
- [face_recognition](https://github.com/ageitgey/face_recognition): A powerful library for face detection and recognition.
- [OpenCV](https://opencv.org/): The library used for image processing and displaying results.

## Contact
For any inquiries or feedback, feel free to reach out to me at [serifegulkorkut@gmail.com].


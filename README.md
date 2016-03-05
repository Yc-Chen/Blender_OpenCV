# Blender_OpenCV
A tool combining Blender and OpenCV to create a 3D commemorative coin from an image. 

## Demo
* Input image:
I use Hatsune Miku with a spring onion as an example.

![alt tag](https://cloud.githubusercontent.com/assets/3079912/13548606/48319a6e-e2f4-11e5-9992-9e853d25fd5f.png)

* Intermediate result:
I use the Gaussian filter from the OpenCV library to extract lines. I also flipped the image to make sure it looks the correct way in the model.

![alt tag](https://cloud.githubusercontent.com/assets/3079912/13548607/4c6f9db0-e2f4-11e5-895c-f9f3cc66b823.png)

* Final result:
![alt tag](https://cloud.githubusercontent.com/assets/3079912/13548615/74543bce-e2f4-11e5-8c3c-2a85881b42c6.png)

## How to use it:
### Environment requirements
This tool is built under the environment of OpenCV 2.4.10 and Blender 2.69. OpenCV 2.4.10 has Python2 binding. Blender 2.69 uses Python3.

### Steps
* Put an image in the same folder as the *.py files.
* Open the command and type

```python imgproc.py [sample.png]```

```blender --background -P read_and_proctex.py```

A blender file 'mycoin.blend' will appear in the same folder. Enjoy!

# Exercise 1 - Introduction to Images and Colorspaces
Before getting started on this exercise, please read through the image basics notebook inside of this folder. You should be able to read it from Github if you do not have access to Jupyter on your machine or in VS Code. 

In this exercise, you will be working with creating images from primitive arrays and modifying the image pixels to check your understanding of how both the RGB and HSV colorspaces work. You will then use opencv to do some very basic image conversions and modifications.

Please note that the solution code and a tester file is attached to each of the exercises. This is intentional. I highly recommend that you give each exercise an honest attempt and only reference the solution code if you are really lost and maybe need a few pointers. To run your code against the tester for this exercise, see the instructions at the very end of the exercise.

---

## Getting Started
If you have not gotten all of the exercises and code for this course, then you can do so by either cloning the repo on your local machine or by downloading the entire thing as a zip file. Go to the home Github page for this course, and click on the green dropdown that says 'Code'. When you click on it, it should look something like this:

![githun_clone](https://docs.github.com/assets/images/help/repository/remotes-url.png)

Image Credit: https://docs.github.com/en/github/using-git/getting-changes-from-a-remote-repository 

To clone the repository onto your local machine, copy the url link shown and go to the desired directory where you want to place the code via your terminal. Then type in the following to clone all of the folders and code for this course to your local machine:

```git clone https://github.com/EthanWadsworth/Image_Processing_And_Vision_Basics.git```

The above method requires more advanced knowledge about how to move around in the terminal and also requires that you git installed on your machine. If you feel like you are confused by this, download the zip file instead and move it to the directory you want. 

## 0 - Setting up Our File and Imports
Open up the file ```exercise_1.py```. Make sure that you are using the configured environment you have created. Before we do anything, we need to import the modules that we loaded into our environment in exercise 0. We can do this by putting the following lines in the start of our file:

```import cv2```
```import matplotlib.pyplot as plt```

These 2 lines at the top of our file tell Python that we want to make use of the functions and classes contained in these libraries, and you will see why we need these lines as you go through the exercise.

## 1 - Creating A Canvas Function
Define a function ```create_canvas(width, height)``` that creates an array that represents an RGB image with specified height and width and returns the array. If either of the dimensions are invalid (< 1) then return ```None```. 

## Visualizing the Results
To help you visualize the code you are writing, we can create another function ```visualize_image(img)``` that takes in our image array and uses matplotlib to show us what it looks like. Use this function to test your image conversions to see if they are doing what you expect.
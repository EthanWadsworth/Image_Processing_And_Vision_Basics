# Getting Set Up
Before we can even start programming, we first need to configure our environments to run all of the proper libraries and extensions that are used not just for this course, but in industry as well.

# Python
There are several ways to configure your machine to run the proper Python libraries, and I will explain both down below.

## 1 - Use Anaconda
Anaconda is an amazing package and enviroment manager. You will find that if you choose to install all of your external packages not built in the Python language natively on a single global environment that your environment might get quickly bogged down by dependencies. Anaconda helps prevent this by allowing us to easily create separate environments where we can choose only the external packages that we need for that specific project that we are working on. We can easily switch between environments, and delete them if we feel like we no longer need them. To install Anaconda on your machine, choose the correct link for your OS:
1. Windows: https://docs.anaconda.com/anaconda/install/windows/ 
2. Mac: https://docs.anaconda.com/anaconda/install/mac-os/ 
3. Linux: https://docs.anaconda.com/anaconda/install/linux/

To check to make sure that you installed Anaconda successfully on your machine, type in the following (on Windows, open up the Anaconda prompt, on Mac and Linux, you can type this directly in the terminal):

```conda list```

If you see a list of packages show up, then great! Anaconda has been successfully installed on your machine, and you are ready to procede to environment creation!

### Creating environments in Anaconda (Optional)
You don't have to create separate environments for your projects, however I do recommend it if you plan to frequently use Python for a variety of purposes. 

If you installed Anaconda properly, your install most likely came with both the graphical Anaconda Navigator and also the Anaconda prompt. You can create an environment using either the graphical interface of the command line Anaconda prompt. If you want to know how to create an environment using the graphical interface, feel free to look here. I will only be going through how to create one using the command line interface. 
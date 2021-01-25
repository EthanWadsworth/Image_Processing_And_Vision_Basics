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

---

### Creating environments in Anaconda (Optional)
You don't have to create separate environments for your projects, however I do recommend it if you plan to frequently use Python for a variety of purposes. 

If you installed Anaconda properly, your install most likely came with both the graphical Anaconda Navigator and also the Anaconda prompt. You can create an environment using either the graphical interface of the command line Anaconda prompt. If you want to know how to create an environment using the graphical interface, feel free to look [here](https://docs.anaconda.com/anaconda/navigator/getting-started/#navigator-managing-environments). I will only be going through how to create one using the command line interface. 

To create a new environment, first open up Anaconda Prompt if you are on a Windows machine, or a terminal if you are on a Mac or Linux machine. After doing so, we can create our first Anaconda environment by typing in:

```conda create --name <my_env_name>```

Where you will replace the ```<my_env_name>``` with the name of your environemnt. For this course, I will be using the environment ```ComputerVision```, so wherever you see that being used after this point, know that this is the name of my environment and just replace it with the name of your environment. So for me, I would create my environment by doing:

```conda create --name ComputerVision```

There are many more additional flags we could add to the line above to add additional configurations to our environment on creation. You can find them [here](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html). However, we can add many of those things in after we have created our environment. 

Now that we have created our environment, we can activate and start using it. To activate an Anaconda environment, from the terminal type in:

```conda activate ComputerVision```

Remember to use the name of your environment. If you got no errors, then congratulations! You are now in your Anaconda environment and ready to start adding in the necessary packages that we will need for this course. 

To deactivate an environment (exit out of it) simply type the following from the terminal if you are in your environment:

```conda deactivate```


You can find this section below the other way to creat environments in Python.

---

## Installing the Necessary Packages
Now that we have set up our environments, we are finally ready to install of the packages we will need to complete the exercises. I will demonstrate both ways to get the required packages:

### From Anaconda
First, activate the environment you created earlier. Now type in the following to get opencv installed on your environment:

```conda install opencv```

If conda tells you need to update your conda version, just type in the command they tell you to, follow the instructions, and then after the update finishes retype in the above line. When prompted, type 'y' to confirm the installation. If no errors occur, then you are ready to get started with the exercises.


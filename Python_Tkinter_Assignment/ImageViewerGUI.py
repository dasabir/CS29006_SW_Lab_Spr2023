from my_package.model import ImageCaptioningModel
from my_package.model import ImageClassificationModel
from tkinter import *
from functools import partial
from PIL import ImageTk, Image
from tkinter import filedialog


def fileClick(clicked):
    # Define the function you want to call when the filebrowser button (Open) is clicked.
    # This function should pop-up a dialog for the user to select an input image file.
    # To have a better clarity, please check out the sample video.


def process(clicked, captioner, classifier):
    # This function will produce the required output when 'Process' button is clicked.
    # Note: This should handle the case if the user clicks on the `Process` button without selecting any image file.


if __name__ == '__main__':
    # Complete the main function preferably in this order:
    # Instantiate the root window.
    # Provide a title to the root window.
    # Instantiate the captioner, classifier models.
    # Declare the file browsing button.
    # Declare the drop-down button.
    # Declare the process button.
    # Declare the output label.

# Software Lab 

## Python GUI Assignment (tkinter)

This is a follow up assignment to the Python Datascience assignment which we have already completed. In this assignment we will design a GUI using `tkinter` which would have the following overall functionality:

* The GUI would provide the user to select a file from the computer.
* It will have a dropdown menu to toggle between two output options: `Image Captioning` and `Image Classification`
* If `Image Captioning` is selected then it should show the caption for the selected image file along with the original image file side-by-side.
* For `Image Classification` it should display the classification class instead of the captions.
* We will obtain the captions by taking help from the previous assignment (which you have already done).
* While for classification, we use Image Classification Model (updated in model.py)

Note: Please follow the installation instructions from the previous Python assignment then install tkinter and functools.

## Coding Task:

For this assignment you are expected to modify a single file, which is `ImageViewerGUI.py`.

1. Define the function `fileClick`: This function should pop-up a dialog for the user to select an input image file. Once the image is selected by the user, it should automatically get the corresponding outputs from the captioner (call the captioner from here). Once the output is computed it should be shown automatically based on choice the dropdown button is at.
2. Define the function `process`: Should show the corresponding captions or classification classes with the input image side-by-side wrt the choice provided. This function will just show the output, which should have been already computed in the `fileClick` function above. Also, you should handle the case if the user clicks on the `Process` button without selecting any image file.
3. Complete the `main` function and add the required `imports` at the top.

All the details are mentioned as comments in the code file as well.

In order to be super clear on how the final GUI should function like, here is a sample video showing it. We would expect something similar to this, but individual creativity and additional functionalities are most welcome and encouraged!

&nbsp;
<p align="center">
(https://youtu.be/fcHV8_7QJUc)
</p>
<p align="center">
Sample Video Link. </p>
&nbsp;


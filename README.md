# Neural-Network-Color-Predictor
A GUI application that predicts whether black or white colored text is best suited for a randomly generated background color. Built in Python3 using Tkinter and TensorFlow.

## Installation
1. Make sure you have Python installed (version 3 or above).
2. Clone or download the repo.
3. Install the required dependencies:
   - Tkinter
   - TensorFlow
   - Numpy

## Usage
1. Run the `ColorPredictor.py` file using Python.
2. A GUI window will open, displaying two buttons: "black" and "white".
3. Each button represents the color of the text that is predicted to be best suited for the current background color.
4. Click the button that corresponds to the color you believe is best suited for the background.
5. The model will be trained with the current background color and your selection.
6. The background color will change to a new random color.
7. The prediction will be updated based on the new background color.
8. Click the "Auto Train" button to train the model with a user-specified number of random data points.
    - Enter the number of data points you want to use for training (between 1 and 5000) in the prompt.
    - The model will be trained with the specified number of random data points.
9. To exit the application, click the "Exit" button.

## Example
Here's an example of how the Color Predictor GUI looks:

![image](https://github.com/nahianrahman/Neural-Network-Color-Predictor/assets/62978977/3dc5dd0a-ff1c-4b67-badc-af61b86c9543)

## License
This project is licensed under the [MIT License](LICENSE).

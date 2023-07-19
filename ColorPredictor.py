import tkinter as tk
from tkinter.simpledialog import askinteger
from tensorflow import keras
import numpy as np
import random


root = tk.Tk()


class Launch:
    def __init__(self, root):
        # Size and color of window
        root.geometry('300x300')
        root.resizable(False, False)
        root.title("Color Predictor")

        # Generate the initial color
        self.color = self.generate_random_color()

        # Labels and Buttons
        self.black_button = tk.Button(root, text="black", fg="black", font=('Times New Roman',20),
                            bg="#%02x%02x%02x" % self.color, activebackground="#%02x%02x%02x" % self.color, command=self.black_clicked)
        self.black_button.place(relx=0, rely=0, relwidth=0.5, relheight=0.85)

        self.white_button = tk.Button(root, text="white", fg="white", font=('Times New Roman',20),
                                bg="#%02x%02x%02x" % self.color, activebackground="#%02x%02x%02x" % self.color, activeforeground="white", command=self.white_clicked)
        self.white_button.place(relx=0.5, rely=0, relwidth=0.5, relheight=0.85)

        exit_button = tk.Button(root, text='Exit', bg='red', font=('Times New Roman', 12), command=root.quit)
        exit_button.place(relx=0.6, rely=0.87, relwidth=0.3)

        train_button = tk.Button(root, text='Auto Train', bg='green', font=('Times New Roman', 12), command=self.auto_train)
        train_button.place(relx=0.1, rely=0.87, relwidth=0.3)
        
        self.prob = tk.Label(root, text = '50%', height=1, width=3, bg='white', font=('Times New Roman',17))

        # Place label on a random side
        x = random.randint(0, 1)
        if x == 0:
            self.prob.place(in_=self.black_button, relx=0.5, rely=0.75, anchor='center')
        else:
            self.prob.place(in_=self.white_button, relx=0.5, rely=0.75, anchor='center')

        self.model = self.create_model()


    def generate_random_color(self):
        # pick random values for rgb
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        return (r, g, b)
        

    def white_clicked(self):
        # train the model with the current color
        targets = np.array([[0, 1]])
        (r, g, b) = self.color
        inputs = np.array([[r/255, g/255, b/255]])
        self.model.fit(inputs, targets)
        self.change_color()


    def black_clicked(self):
        # train the model with the current color
        targets = np.array([[1, 0]])
        (r, g, b) = self.color
        inputs = np.array([[r/255, g/255, b/255]])
        self.model.fit(inputs, targets)
        self.change_color()


    def change_color(self):
        # change the background color
        self.color = self.generate_random_color()
        self.black_button.config(bg="#%02x%02x%02x" % self.color, activebackground="#%02x%02x%02x" % self.color)
        self.white_button.config(bg="#%02x%02x%02x" % self.color, activebackground="#%02x%02x%02x" % self.color)
        self.predict_color()


    def predict_color(self):
        # predict whether black or white colored text is best suited
        (r, g, b) = self.color
        inputs = np.array([[r/255, g/255, b/255]])
        prediction = self.model.predict(inputs)
        self.prob.config(text=str(round(np.max(prediction)*100))+'%')
        if np.argmax(prediction) == 0:
            self.prob.place(in_=self.black_button, relx=0.5, rely=0.75, anchor='center')
        else:
            self.prob.place(in_=self.white_button, relx=0.5, rely=0.75, anchor='center')


    def auto_train(self):
        # train the model with user specified no. of data sets
        num_data = askinteger('Samples', 'Please enter the numer of data points \nyou want to train the model with (1 to 5000)')
        while num_data < 1 or num_data > 5000:
            num_data = askinteger('Samples', 'Please enter a valid number (0 to 5000)')
        inputs = []
        targets = []
        for i in range(num_data):
            color = self.generate_random_color()
            # white if r+g+b < (255+255+255)/2, else black
            target = [0, 1] if sum(color) < 383 else [1, 0]
            # normalize input values between 0 and 1
            inputs.append([c/255 for c in color])  
            targets.append(target)
        self.model.fit(np.array(inputs), np.array(targets), batch_size=32, epochs=5)
        self.change_color()


    def create_model(self):
        model = keras.Sequential([
                keras.layers.Dense(72, input_dim=3, activation='relu'),
                keras.layers.Dense(2, activation='softmax')
                ])

        model.compile(loss='binary_crossentropy', optimizer='nadam')

        return model


app = Launch(root)

root.mainloop()

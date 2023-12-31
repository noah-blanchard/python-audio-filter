﻿# python-audio-filter
![image](https://github.com/noah-blanchard/python-audio-filter/assets/17174941/ae36879a-a3cd-4b6a-8d46-f6c27c180770)
# Audio Filter Application

This project is a simple yet powerful audio filtering application, aimed at providing an interface for users to apply Lowpass and Highpass filters to their audio files. If you're passionate about music and curious about how you can manipulate it with code, this is a great starting point.

## 🎵 What Does This Application Do?

- **Load Audio**: You can load any `.wav` file to be processed.
- **Choose Filter**: Users can choose between a Lowpass or Highpass filter.
- **Adjust Parameters**: Customize the cutoff frequency and the order of the filter to achieve the desired effect.
- **Save Output**: After processing, the filtered audio can be saved to a new `.wav` file.

## 🛠️ Technologies and Libraries Used

- **Python**: The backbone of our application.
- **PySimpleGUI**: Used for creating the graphical user interface.
- **soundfile**: To read and write sound files.
- **SciPy**: Specifically, the signal processing module for applying the Butterworth filter.
- **NumPy**: For numerical operations on the audio data.

## 🚀 Getting Started

### Prerequisites

- Ensure you have Python 3.x installed. [Download here](https://www.python.org/downloads/)
- Install necessary libraries:
  ```bash
  pip install numpy scipy soundfile PySimpleGUI
  ```

### Running the Application

- Run the script like any pyton scripts:
  ```bash
  python main.py
  ```

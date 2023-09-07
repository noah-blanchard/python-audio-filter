import os
import numpy as np
import PySimpleGUI as sg
import soundfile as sf
from scipy.signal import butter, lfilter

DEFAULT_SAMPLE_RATE = 44100


def butter_filter(audio_data, cutoff, samplerate, order=1, filter_type='lowpass'):
    """Applies a butter filter to the given audio data."""
    nyquist_freq = 0.5 * samplerate
    normalized_cutoff = cutoff / nyquist_freq
    b_coeff, a_coeff = butter(order, normalized_cutoff,
                              btype=filter_type, analog=False)

    if len(audio_data.shape) == 2 and audio_data.shape[1] == 2:
        left_channel = lfilter(b_coeff, a_coeff, audio_data[:, 0])
        right_channel = lfilter(b_coeff, a_coeff, audio_data[:, 1])
        filtered_data = np.column_stack((left_channel, right_channel))
    else:
        filtered_data = lfilter(b_coeff, a_coeff, audio_data)

    return filtered_data


def apply_filter(file_path, output, cutoff, order, filter_type):
    """Reads audio data, applies the specified filter and writes the result to the output."""
    if os.path.exists(file_path):
        data, samplerate = sf.read(file_path)
        filtered_data = butter_filter(
            data, cutoff, samplerate or DEFAULT_SAMPLE_RATE, order, filter_type)
        sf.write(f"{output}.wav", filtered_data, samplerate)


def main():
    layout = [
        [sg.Text('Fichier audio :'), sg.InputText(key='file_path'), sg.FileBrowse(
            button_text='Parcourir', key='file_browse', file_types=(("WAV File", "*.wav")))],
        [sg.Text('Choisissez un filtre :')],
        [sg.Radio('Lowpass', "RADIO1", default=True, key='lowpass'),
         sg.Radio('Highpass', "RADIO1", key='highpass')],
        [sg.Text('Ordre du filtre :'), sg.Slider(range=(6, 30), default_value=6,
                                                 resolution=6, orientation='h', key='order'), sg.Text('dB')],
        [sg.Text('Fréquence de coupure :'), sg.Slider(range=(
            50, 10000), default_value=1000, resolution=1, orientation='h', key='cutoff'), sg.Text('Hz')],
        [sg.Text('Fichier audio filtré :'), sg.InputText(
            key="output_file"), sg.Text(".wav")],
        [sg.Button('Appliquer'), sg.Button('Quitter')],
    ]

    window = sg.Window('Filtre Audio', layout)

    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED or event == 'Quitter':
            break
        if event == 'Appliquer':
            file_path = values['file_path']
            output = values['output_file']
            cutoff = values['cutoff']
            order = values['order'] / 6

            if values['lowpass']:
                apply_filter(file_path, output, cutoff, order, 'lowpass')
            else:
                apply_filter(file_path, output, cutoff, order, 'highpass')

    window.close()


if __name__ == "__main__":
    main()

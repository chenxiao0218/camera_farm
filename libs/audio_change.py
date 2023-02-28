#!usr/bin/env python
# coding=utf-8
import os
# from Tkinter import *
import pyaudio
import wave
import matplotlib.pyplot as plt
import numpy as np


def getpath():
    project_path = os.getcwd().split('camera_farm')[0] + 'camera_farm\\'
    print(project_path)


def read_wave_data(file_path):
    # open a wave file, and return a Wave_read object
    f = wave.open(file_path, "rb")
    # read the wave's format infomation,and return a tuple
    params = f.getparams()
    # get the info
    nchannels, sampwidth, framerate, nframes = params[:4]
    # Reads and returns nframes of audio, as a string of bytes.
    str_data = f.readframes(nframes)
    # close the stream
    f.close()
    # turn the wave's data to array
    wave_data = np.fromstring(str_data, dtype=np.short)
    # for the data is stereo,and format is LRLRLR...
    # shape the array to n*2(-1 means fit the y coordinate)
    wave_data.shape = -1, 2
    # transpose the data
    wave_data = wave_data.T
    print(wave_data)
    # calculate the time bar
    time = np.arange(0, nframes) * (1.0 / framerate)
    return wave_data, time


def main():
    wave_data, time = read_wave_data(r"D:\python_project\camera_farm\libs\test.wav")
    # draw the wave
    plt.subplot(211)
    plt.plot(time, wave_data[0])
    plt.subplot(212)
    plt.plot(time, wave_data[1], c="g")
    plt.show()


class Audio:
    def __init__(self, camera):
        self.camera = camera

    def record(self, process_id):

        pass


if __name__ == "__main__":
    p = pyaudio.PyAudio()
    info = p.get_host_api_info_by_index(0)
    numdevices = info.get('deviceCount')
    for i in range(0, numdevices):
        if (p.get_device_info_by_host_api_device_index(0, i).get('maxInputChannels')) > 0:
            print("Input Device id ", i, " - ", p.get_device_info_by_host_api_device_index(0, i).get('name'))

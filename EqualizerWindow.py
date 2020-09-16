from PyQt5.QtWidgets import QMainWindow 
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot, QFile, QIODevice
from PyQt5 import QtGui
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QFileDialog
import numpy as np
from matplotlib import pyplot as plt
from scipy.io import wavfile
from scipy import signal as sig
import os, sys
import das
from pathlib import Path

from EqualizerLayout import Ui_Form

class EqualizerWindow(QMainWindow):

    def __init__(self):
        super(EqualizerWindow, self).__init__()
        self.ui=Ui_Form()
        self.ui.setupUi(self)
        self.ui.btn_choose.clicked.connect(self.choose)
        self.ui.btn_save.clicked.connect(self.save)
        self.ui.btn_reset.clicked.connect(self.reset)
        self.ui.btn_filter.clicked.connect(self.filter)
        self.ui.dropdown_presets.activated.connect(self.preset) 
        self.show()

    @pyqtSlot()
    def choose(self):

        filename, filters = QFileDialog.getOpenFileName(self, "Open Template", "c:\\", "Templates (*.wav);;All Files (*.*)")
        self.fs, self.wav = wavfile.read(filename)
        self.wav = self.wav / 2**15
        os.system('play '+ filename)
        
    @pyqtSlot()
    def save(self):
        fileName, _ = QFileDialog.getSaveFileName(self,"QFileDialog.getSaveFileName()","","All Files (*);;Text Files (*.txt)")
        wavfile.write(fileName, self.fs , np.array(self.wav_out*2**15, dtype = 'int16'))
        os.system('play '+ fileName)

    @pyqtSlot()  
    def reset (self):
        self.ui.slider_25.setValue(0)
        self.ui.slider_40.setValue(0)
        self.ui.slider_63.setValue(0)
        self.ui.slider_100.setValue(0)
        self.ui.slider_160.setValue(0)
        self.ui.slider_250.setValue(0)
        self.ui.slider_400.setValue(0)
        self.ui.slider_630.setValue(0)
        self.ui.slider_1k.setValue(0)
        self.ui.slider_1k6.setValue(0)
        self.ui.slider_2k5.setValue(0)
        self.ui.slider_4k.setValue(0)
        self.ui.slider_6k3.setValue(0)
        self.ui.slider_10k.setValue(0)
        self.ui.slider_16k.setValue(0)

    @pyqtSlot()
    def filter(self):
        N = 6
        
        #25Hz
        f1 = 25 / (self.fs/2)
        b1,a1 = sig.iirfilter(5, f1, btype = 'lowpass', ftype = 'butter')
        self.wav1 = sig.lfilter(b1, a1, self.wav)
        gain1 = 10**(self.ui.slider_25.value()/20)

        #40
        f2 = 40 / (self.fs/2)
        
        b2,a2 = sig.iirfilter(2, f2, btype= 'lowpass', ftype = 'butter')
        self.wav2 = sig.lfilter(b2, a2, self.wav)
        gain2 = 10**(self.ui.slider_40.value()/20)

        # f[min,max] = [63,100]
        f3 = 63 / (self.fs/2)
        f4 = 100 / (self.fs/2)
        b3, a3 = sig.iirfilter (3, [f3,f4], btype = 'bandpass', ftype ='butter')   
        self.wav3 = sig.lfilter(b3, a3, self.wav)  # филтрирање
        gain3 = 10**(self.ui.slider_63.value()/20) # засилување

        # f[min,max] = [100,100]
        f5 = 100 / (self.fs/2)
        f6 = 160 / (self.fs/2)
        b4, a4 = sig.iirfilter (3, [f5,f6], btype = 'bandpass', ftype ='butter')   
        self.wav4 = sig.lfilter(b4, a4, self.wav)  # филтрирање
        gain4 = 10**(self.ui.slider_100.value()/20) # засилување


        # f[min,max] = [160,100]
        f7 = 160 / (self.fs/2)
        f8 = 250 / (self.fs/2)
        b5, a5 = sig.iirfilter (4, [f7,f8], btype = 'bandpass', ftype ='butter')   
        self.wav5 = sig.lfilter(b5, a5, self.wav)  # филтрирање
        gain5 = 10**(self.ui.slider_160.value()/20) # засилување

        # f[min,max] = [250,400]
        f9 = 250 / (self.fs/2)
        f10 = 400 / (self.fs/2)
        b6, a6 = sig.iirfilter (4, [f9,f10], btype = 'bandpass', ftype ='butter')   
        self.wav6 = sig.lfilter(b6, a6, self.wav)  # филтрирање
        gain6 = 10**(self.ui.slider_250.value()/20) # засилување

        # f[min,max] = [400,630]
        f11 = 400 / (self.fs/2)
        f12 = 630 / (self.fs/2)
        b7, a7 = sig.iirfilter (5, [f11,f12], btype = 'bandpass', ftype ='butter')   
        self.wav7 = sig.lfilter(b7, a7, self.wav)  # филтрирање
        gain7 = 10**(self.ui.slider_400.value()/20) # засилување

        # f[min,max] = [630,1000]
        f13 = 630 / (self.fs/2)
        f14 = 1000 / (self.fs/2)
        b8, a8 = sig.iirfilter (5, [f13,f14], btype = 'bandpass', ftype ='butter')   
        self.wav8 = sig.lfilter(b8, a8, self.wav)  # филтрирање
        gain8 = 10**(self.ui.slider_630.value()/20) # засилување

        # f[min,max] = [1000,1600]
        f15 = 1000 / (self.fs/2)
        f16 = 1600 / (self.fs/2)
        b9, a9 = sig.iirfilter (N, [f15,f16], btype = 'bandpass', ftype ='butter')   
        self.wav9 = sig.lfilter(b9, a9, self.wav)  # филтрирање
        gain9 = 10**(self.ui.slider_1k.value()/20) # засилување

        # f[min,max] = [1600,2500]
        f17 = 1600 / (self.fs/2)
        f18 = 2500 / (self.fs/2)
        b10, a10 = sig.iirfilter (N, [f17,f18], btype = 'bandpass', ftype ='butter')   
        self.wav10 = sig.lfilter(b10, a10, self.wav)  # филтрирање
        gain10 = 10**(self.ui.slider_1k6.value()/20) # засилување

        # f[min,max] = [2500,4000]
        f19 = 2500 / (self.fs/2)
        f20 = 4000 / (self.fs/2)
        b11, a11 = sig.iirfilter (N, [f19,f20], btype = 'bandpass', ftype ='butter')   
        self.wav11 = sig.lfilter(b11, a11, self.wav)  # филтрирање
        gain11 = 10**(self.ui.slider_2k5.value()/20) # засилување

        # f[min,max] = [4000,6300]
        f21 = 4000 / (self.fs/2)
        f22 = 6300 / (self.fs/2)
        b12, a12 = sig.iirfilter (N, [f21,f22], btype = 'bandpass', ftype ='butter')   
        self.wav12 = sig.lfilter(b12, a12, self.wav)  # филтрирање
        gain12 = 10**(self.ui.slider_4k.value()/20) # засилување

        # f[min,max] = [6300,10000]
        f23 = 6300 / (self.fs/2)
        f24 = 10000 / (self.fs/2)
        b13, a13 = sig.iirfilter (N, [f23,f24], btype = 'bandpass', ftype ='butter')   
        self.wav13 = sig.lfilter(b13, a13, self.wav)  # филтрирање
        gain13 = 10**(self.ui.slider_6k3.value()/20) # засилување

#        # f[min,max] = [10000,16000]
        f25 = 10000 / (self.fs/2)
        f26 = 16000 / (self.fs/2)
        b14, a14 = sig.iirfilter (N, [f25,f26], btype = 'bandpass', ftype ='butter')   
        self.wav14 = sig.lfilter(b14, a14, self.wav)  # филтрирање
        gain14 = 10**(self.ui.slider_10k.value()/20) # засилување
#
        # f[max] = [16K]
        f27 = 16000 / (self.fs/2)
        b9,a9 = sig.iirfilter(N, f27, btype = 'highpass', ftype = 'butter')
        self.wav15 = sig.lfilter(b9, a9, self.wav)
        gain15 = 10**(self.ui.slider_16k.value()/20)

        #linearna kombinacija na site izlezi pomnozeni so zasiluvanjeto
        self.wav_out = self.wav1 *gain1+self.wav2 *gain2+self.wav3 *gain3+self.wav4 *gain4+self.wav5 *gain5+self.wav6 *gain6+self.wav7 *gain7+self.wav8 *gain8+self.wav9 *gain9+ self.wav10* gain10 + self.wav11 * gain11+self.wav12 * gain12 + self.wav13 * gain13 + self.wav14 * gain14 + self.wav15 * gain15
        #normalizacija
        self.wav_out = self.wav_out / np.max(np.abs(self.wav_out))
        

    @pyqtSlot()
    def preset(self):
#        if((self.ui.dropdown_presets.currentIndex() == 0)):
#            self.reset()
        if((self.ui.dropdown_presets.currentIndex() == 0)):
            self.rock()
        if((self.ui.dropdown_presets.currentIndex() == 1)):
            self.jazz()
        if((self.ui.dropdown_presets.currentIndex() == 2)):
            self.blues()
        if((self.ui.dropdown_presets.currentIndex() == 3)):
            self.clasical()
        if((self.ui.dropdown_presets.currentIndex() == 4)):
            self.pop()

    def rock (self):
        self.ui.slider_25.setValue(2);
        self.ui.slider_40.setValue(2);
        self.ui.slider_63.setValue(2);
        self.ui.slider_100.setValue(3);
        self.ui.slider_160.setValue(4);
        self.ui.slider_250.setValue(2);
        self.ui.slider_400.setValue(-3);
        self.ui.slider_630.setValue(-1);
        self.ui.slider_1k.setValue(0);
        self.ui.slider_1k6.setValue(1);
        self.ui.slider_2k5.setValue(2);
        self.ui.slider_4k.setValue(3);
        self.ui.slider_6k3.setValue(5);
        self.ui.slider_10k.setValue(7);
        self.ui.slider_16k.setValue(5);

    def jazz (self):
        self.ui.slider_25.setValue(2);
        self.ui.slider_40.setValue(2);
        self.ui.slider_63.setValue(2);
        self.ui.slider_100.setValue(3);
        self.ui.slider_160.setValue(5);
        self.ui.slider_250.setValue(6);
        self.ui.slider_400.setValue(-2);
        self.ui.slider_630.setValue(0);
        self.ui.slider_1k.setValue(2);
        self.ui.slider_1k6.setValue(2);
        self.ui.slider_2k5.setValue(3);
        self.ui.slider_4k.setValue(4);
        self.ui.slider_6k3.setValue(3);
        self.ui.slider_10k.setValue(3);
        self.ui.slider_16k.setValue(3);

    def blues (self):
        self.ui.slider_25.setValue(2);
        self.ui.slider_40.setValue(2);
        self.ui.slider_63.setValue(2);
        self.ui.slider_100.setValue(3);
        self.ui.slider_160.setValue(3);
        self.ui.slider_250.setValue(3);
        self.ui.slider_400.setValue(-2);
        self.ui.slider_630.setValue(0);
        self.ui.slider_1k.setValue(2);
        self.ui.slider_1k6.setValue(2);
        self.ui.slider_2k5.setValue(1);
        self.ui.slider_4k.setValue(4);
        self.ui.slider_6k3.setValue(8);
        self.ui.slider_10k.setValue(9);
        self.ui.slider_16k.setValue(1);

    def clasical (self):
        self.ui.slider_25.setValue(1);
        self.ui.slider_40.setValue(2);
        self.ui.slider_63.setValue(3);
        self.ui.slider_100.setValue(3);
        self.ui.slider_160.setValue(4);
        self.ui.slider_250.setValue(1);
        self.ui.slider_400.setValue(-1);
        self.ui.slider_630.setValue(0);
        self.ui.slider_1k.setValue(2);
        self.ui.slider_1k6.setValue(2);
        self.ui.slider_2k5.setValue(2);
        self.ui.slider_4k.setValue(4);
        self.ui.slider_6k3.setValue(3);
        self.ui.slider_10k.setValue(8);
        self.ui.slider_16k.setValue(9);

    def pop(self):
        self.ui.slider_25.setValue(1);
        self.ui.slider_40.setValue(2);
        self.ui.slider_63.setValue(3);
        self.ui.slider_100.setValue(3);
        self.ui.slider_160.setValue(4);
        self.ui.slider_250.setValue(-6);
        self.ui.slider_400.setValue(10);
        self.ui.slider_630.setValue(0);
        self.ui.slider_1k.setValue(2);
        self.ui.slider_1k6.setValue(6);
        self.ui.slider_2k5.setValue(-2);
        self.ui.slider_4k.setValue(10);
        self.ui.slider_6k3.setValue(9);
        self.ui.slider_10k.setValue(6);
        self.ui.slider_16k.setValue(4);

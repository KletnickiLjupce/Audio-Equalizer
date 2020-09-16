

#buttons
self.btn_choose.clicked.connect(self.choose)
self.btb_save.clicked.connect(self.save)
self.reset.clicked.connect(self.reset)
self.filter.clicked.connect(self.fitler)
self.dropdown_presets.activated.connect(self.preset)

#functions
def choose(self):
	self.filename = QtGui.QFileDialog.getOpenFileName(self, 'Pick a file:')
	self.fs, self.wav = wavfile.read(self.filename)
	fileNameSplitList = self.filename.split('/') 
	global audioName
	audioName = fileNameSplitList[-1]
	self.text_filename.setText(audioName)


def reset (self):
	self.slider_25.setValue(0);
	self.slider_40.setValue(0);
	self.slider_63.setValue(0);
	self.slider_100.setValue(0);
	self.slider_160.setValue(0);
	self.slider_250.setValue(0);
	self.slider_400.setValue(0);
	self.slider_630.setValue(0);
	self.slider_1k.setValue(0);
	self.slider_1k6.setValue(0);
	self.slider_2k5.setValue(0);
	self.slider_4k.setValue(0);
	self.slider_6k3.setValue(0);
	self.slider_10k.setValue(0);
	self.slider_16k.setValue(0);

def save(save)
	self.savename = QtGui.QFileDialog.getSaveFileName(self, 'Save as:')
	wavfile.write(self.savename, self.fs , np.array(self.wav_out*2**15, dtype = 'int16'))
	np.savetxt("wav.txt", self.wav_out)

def filtriranje(self):
	N = 6

	#25Hz
	f1 = 25 / (self.fs/2)
	b1,a1 = sig.iirfilter(N, f1, btype = 'low', ftype = 'butter')
	self.wav1 = sig.lfilter(b1, a1, self.wav)
	gain1 = 10**(self.slider_25.value()/20)

	#40
	f2 = 40 / (self.fs/2)
	b2,a2 = sig.iirfilter(N, f2, btype= 'low', ftype = 'butter')
	self.wav2 = sig.lfilter(b2, a2, self.wav)
	gain2 = 10**(self.slider_40.value()/20)

	# f[min,max] = [63,100]
	f3 = 63 / (self.fs/2)
	f4 = 100 / (self.fs/2)
	b3, a3 = sig.iirfilter (N, [f3,f4], btype = 'band', ftype ='butter')   
	self.wav3 = sig.lfilter(b3, a3, self.wav)  # филтрирање
	gain3 = 10**(self.slider_63.value()/20) # засилување

	# f[min,max] = [100,100]
	f5 = 100 / (self.fs/2)
	f6 = 160 / (self.fs/2)
	b4, a4 = sig.iirfilter (N, [f5,f6], btype = 'band', ftype ='butter')   
	self.wav4 = sig.lfilter(b4, a4, self.wav)  # филтрирање
	gain4 = 10**(self.slider_100.value()/20) # засилување


	# f[min,max] = [160,100]
	f7 = 160 / (self.fs/2)
	f8 = 250 / (self.fs/2)
	b5, a5 = sig.iirfilter (N, [f7,f8], btype = 'band', ftype ='butter')   
	self.wav5 = sig.lfilter(b5, a5, self.wav)  # филтрирање
	gain5 = 10**(self.slider_160.value()/20) # засилување

	# f[min,max] = [250,400]
	f9 = 250 / (self.fs/2)
	f10 = 400 / (self.fs/2)
	b6, a6 = sig.iirfilter (N, [f9,f10], btype = 'band', ftype ='butter')   
	self.wav6 = sig.lfilter(b6, a6, self.wav)  # филтрирање
	gain6 = 10**(self.slider_250.value()/20) # засилување

	# f[min,max] = [400,630]
	f11 = 400 / (self.fs/2)
	f12 = 630 / (self.fs/2)
	b7, a7 = sig.iirfilter (N, [f11,f12], btype = 'band', ftype ='butter')   
	self.wav7 = sig.lfilter(b7, a7, self.wav)  # филтрирање
	gain7 = 10**(self.slider_400.value()/20) # засилување

	# f[min,max] = [630,1000]
	f13 = 630 / (self.fs/2)
	f14 = 1000 / (self.fs/2)
	b8, a8 = sig.iirfilter (N, [f13,f14], btype = 'band', ftype ='butter')   
	self.wav8 = sig.lfilter(b8, a8, self.wav)  # филтрирање
	gain8 = 10**(self.slider_630.value()/20) # засилување

	# f[min,max] = [1000,1000]
	f15 = 1000 / (self.fs/2)
	f16 = 1000 / (self.fs/2)
	b9, a9 = sig.iirfilter (N, [f15,f16], btype = 'band', ftype ='butter')   
	self.wav9 = sig.lfilter(b9, a9, self.wav)  # филтрирање
	gain9 = 10**(self.slider_1k.value()/20) # засилување

	# f[min,max] = [1000,1600]
	f17 = 1000 / (self.fs/2)
	f18 = 1600 / (self.fs/2)
	b10, a10 = sig.iirfilter (N, [f17,f18], btype = 'band', ftype ='butter')   
	self.wav10 = sig.lfilter(b10, a10, self.wav)  # филтрирање
	gain10 = 10**(self.slider_1k6.value()/20) # засилување

	# f[min,max] = [1600,2500]
	f19 = 1600 / (self.fs/2)
	f20 = 2500 / (self.fs/2)
	b11, a11 = sig.iirfilter (N, [f19,f20], btype = 'band', ftype ='butter')   
	self.wav11 = sig.lfilter(b11, a11, self.wav)  # филтрирање
	gain11 = 10**(self.slider_2k5.value()/20) # засилување

	# f[min,max] = [2500,4000]
	f21 = 2500 / (self.fs/2)
	f22 = 4000 / (self.fs/2)
	b12, a12 = sig.iirfilter (N, [f21,f22], btype = 'band', ftype ='butter')   
	self.wav12 = sig.lfilter(b12, a12, self.wav)  # филтрирање
	gain12 = 10**(self.slider_4k.value()/20) # засилување

	# f[min,max] = [6300,10000]
	f23 = 6300 / (self.fs/2)
	f24 = 10000 / (self.fs/2)
	b13, a13 = sig.iirfilter (N, [f23,f24], btype = 'band', ftype ='butter')   
	self.wav13 = sig.lfilter(b13, a13, self.wav)  # филтрирање
	gain13 = 10**(self.slider_6k3.value()/20) # засилување

	# f[min,max] = [10000,16000]
	f25 = 10000 / (self.fs/2)
	f26 = 16000 / (self.fs/2)
	b14, a14 = sig.iirfilter (N, [f25,f26], btype = 'band', ftype ='butter')   
	self.wav14 = sig.lfilter(b14, a14, self.wav)  # филтрирање
	gain14 = 10**(self.slider_10k.value()/20) # засилување

	# f[max] = [16K]
	f15 = 16000 / (self.fs/2)
	b9,a9 = sig.iirfilter(N, f15, btype = 'high', ftype = 'butter')
	self.wav15 = sig.lfilter(b9, a9, self.wav)
	gain15 = 10**(self.slider_16k.value()/20)


	#linearna kombinacija na site izlezi pomnozeni so zasiluvanjeto
	self.wav_out = self.wav1 * gain1 + self.wav2 * gain2 +self.wav3 * gain3 + self.wav4 * gain4+self.wav5 * gain5 +self.wav6 * gain6 + self.wav7 * gain7 + self.wav8 * gain8+self.wav9 * gain9+self.wav10 * gain10+self.wav11 * gain11+self.wav12 * gain12+self.wav13 * gain13+self.wav14 * gain14+self.wav15 * gain15
	#normalizacija
	self.wav_out = self.wav_out / np.max(np.abs(self.wav_out))


def preset(self)
	if((self.preset_list.currentIndex() == 0)):
		self.reset()
	if((self.preset_list.currentIndex() == 1)):
		self.rock()
	if((self.preset_list.currentIndex() == 2)):
		self.jazz()
	if((self.preset_list.currentIndex() == 3)):
		self.blues()
	if((self.preset_list.currentIndex() == 4)):
		self.clasical()
	if((self.preset_list.currentIndex() == 5)):
		self.pop()

def rock (self):
	self.slider_25.setValue(2);
	self.slider_40.setValue(2);
	self.slider_63.setValue(2);
	self.slider_100.setValue(3);
	self.slider_160.setValue(4);
	self.slider_250.setValue(2);
	self.slider_400.setValue(-3);
	self.slider_630.setValue(-1);
	self.slider_1k.setValue(0);
	self.slider_1k6.setValue(1);
	self.slider_2k5.setValue(2);
	self.slider_4k.setValue(3);
	self.slider_6k3.setValue(5);
	self.slider_10k.setValue(7);
	self.slider_16k.setValue(5);

def jazz (self):
	self.slider_25.setValue(2);
	self.slider_40.setValue(2);
	self.slider_63.setValue(2);
	self.slider_100.setValue(3);
	self.slider_160.setValue(5);
	self.slider_250.setValue(6);
	self.slider_400.setValue(-2);
	self.slider_630.setValue(0);
	self.slider_1k.setValue(2);
	self.slider_1k6.setValue(2);
	self.slider_2k5.setValue(3);
	self.slider_4k.setValue(4);
	self.slider_6k3.setValue(3);
	self.slider_10k.setValue(3);
	self.slider_16k.setValue(3);

def blues (self):
	self.slider_25.setValue(2);
	self.slider_40.setValue(2);
	self.slider_63.setValue(2);
	self.slider_100.setValue(3);
	self.slider_160.setValue(3);
	self.slider_250.setValue(3);
	self.slider_400.setValue(-2);
	self.slider_630.setValue(0);
	self.slider_1k.setValue(2);
	self.slider_1k6.setValue(2);
	self.slider_2k5.setValue(1);
	self.slider_4k.setValue(4);
	self.slider_6k3.setValue(8);
	self.slider_10k.setValue(9);
	self.slider_16k.setValue(1);

def classic (self):
	self.slider_25.setValue(1);
	self.slider_40.setValue(2);
	self.slider_63.setValue(3);
	self.slider_100.setValue(3);
	self.slider_160.setValue(4);
	self.slider_250.setValue(1);
	self.slider_400.setValue(-1);
	self.slider_630.setValue(0);
	self.slider_1k.setValue(2);
	self.slider_1k6.setValue(2);
	self.slider_2k5.setValue(2);
	self.slider_4k.setValue(4);
	self.slider_6k3.setValue(3);
	self.slider_10k.setValue(8);
	self.slider_16k.setValue(9);

def pop(self):
	self.slider_25.setValue(1);
	self.slider_40.setValue(2);
	self.slider_63.setValue(3);
	self.slider_100.setValue(3);
	self.slider_160.setValue(4);
	self.slider_250.setValue(-12);
	self.slider_400.setValue(12);
	self.slider_630.setValue(0);
	self.slider_1k.setValue(2);
	self.slider_1k6.setValue(6);
	self.slider_2k5.setValue(-10;
	self.slider_4k.setValue(10);
	self.slider_6k3.setValue(9);
	self.slider_10k.setValue(6);
	self.slider_16k.setValue(4);




all: mivoz_fft.png mi_voz.png nombre.wav
mivoz_fft.png: fft_de_mi_voz.py
	python fft_de_mi_voz.py
fft_de_mi_voz.py: mi_voz.png
mi_voz.png: nombre.wav
	python grafica_mi_voz.py
nombre.wav: grabar_mi_nombre.x
	./grabar_mi_nombre.x
grabar_mi_nombre.x: grabar_mi_nombre.c
	cc grabar_mi_nombre.c -o grabar_mi_nombre.x

# PlayWords
=============

![PlayWords](https://github.com/Cubillosxy/playwords/blob/master/biblio/Playwords_v.jpg)

```
Program for practice new words spanish/english
```

Playwords is just a code that you can run, this use a GUI on Tkinter also use a dicctionary (file.cfg) to save the words. 

Requirements:
* Python 2.X 
* Tkinter 

### Docker
```
apt-get install x11-xserver-utils
xhost +
docker build -t playwords .
docker run -it -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix  playwords
```

# Questions?

Edwin Cubillos Bohorquez, Colombia : [edwin.cubillos@uptc.edu.co]

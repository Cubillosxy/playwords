# PlayWords

![PlayWords](https://github.com/Cubillosxy/playwords/blob/master/biblio/Playwords_v.jpg)

```
Program for practice new words spanish/english
```

Playwords is a desktop program, it uses a GUI on Tkinter and uses a dicctionary (file.cfg) to save the words. 

Requirements:
* Python 2.X 
* Tkinter 

- load sample dicc (optional)
```
cp biblio/dicc\ 2.cfg dicc.cfg
```

### Docker

linux system

```
apt-get install x11-xserver-utils
xhost +

docker build -t playwords .
docker run -it -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix -v $(pwd):/code playwords

# with docker-compose
docker-compose build
docker-compose up

# exec command in container
docker exec -it playwords_play_1 bash
```

## run without docker
python playenglish.py 

# Questions?

Edwin Cubillos Bohorquez, Colombia : [edwin.cubillos@uptc.edu.co]

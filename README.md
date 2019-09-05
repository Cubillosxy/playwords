# PlayWords

![PlayWords](https://github.com/Cubillosxy/playwords/blob/master/biblio/Playwords_v.jpg)


**Program for practice new words spanish/english**


Playwords is a desktop program, it uses a GUI on Tkinter and uses a dicctionary (file.cfg) to save the words. 

Requirements:
* Python 2.X 
* Tkinter 

##### Load sample dicc (optional)
```
cp biblio/static_config_files/dicc\ 2.cfg biblio/static_config_files/dicc.cfg
```

### Docker

- Linux 

```
apt-get install x11-xserver-utils
xhost +

docker build -t playwords .
docker run -it -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix -v $(pwd):/code -v /home:/home playwords

# with docker-compose
docker-compose build
docker-compose up

# exec command in container
docker exec -it playwords_play_1 bash
docker exec -it playwords_play_1 ipython
```

### Run without docker
`python playenglish.py`

----

<p align="center">This project is licensed under the  <a href='https://opensource.org/licenses/MIT' target="_blank">MIT License</a>.</br>
Copyright &copy; 2016 Edwin Cubillos</p>

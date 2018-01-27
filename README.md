# RemotePy

A remote-desktop sharing application.

![](https://media.giphy.com/media/l0NgRAtb5X8YPL30Y/giphy.gif)

- browser-based, shared over LAN
- cross platform
- control remote-desktop using your mouse and keyboard
- click, double click and right click enabled
- works on touch-screen devices as well!

## Installation

- Clone this repo:
	
	```
	$ git clone https://github.com/nikhilkumarsingh/RemotePy
	```

- Install the requirements:
	
	```
	pip install -r requirements.txt
	```

## Usage

- To run application using the default **Werkzeug server**:
	
	```
	$ python app.py
	```

- To run application using **Gunicorn server**:
	
	```
	$ python wsgi.py
	```

#### A simple CLI has also been provided to tweak different parameters.

- Show help message

	```
	$ python cli.py -h

	usage: cli.py [-h] [-b server] [-p port] [-w workers] [-t threads]

	RemotePy CLI

	optional arguments:
	  -h, --help            show this help message and exit
	  -b server, --server server
	                        IP address of server.
	  -p port, --port port  Port no. of server.
	  -w workers, --workers workers
	                        No. of workers on server.
	  -t threads, --threads threads
	                        No. of threads for server
	
	```

- Run **Gunicorn server** with:
	- IP address **192.168.1.103**, 
	- port no. **8000**, 
	- **2** workers,
	- **5** threads

	```
	$ python cli.py -b 192.168.1.103 -p 8000 -w 2 -t 5
	```

## TODOs

- Improve HTML layout
- Make the multi-threaded server more stable


## References:

- [flask-video-streaming](https://github.com/miguelgrinberg/flask-video-streaming)
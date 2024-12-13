hello-websocket
===============
Webcam over websocket in Python using OpenCV and
`Tornado <http://www.tornadoweb.org>`_.

How it works
------------
A *recorder* process continuously reads images from a webcam.
Upon every capture, it writes the image to a Redis key-value store.

A separate *server* process (running Tornado) handles websocket requests
sent by a *client* (web browser). Upon receiving a request, it retrieves
the latest image from the Redis database and sends it to the client over the
established websocket connection.

.. image:: https://github.com/vmlaker/hello-websocket/blob/master/diagram.png?raw=true

Installation
------------
Install Redis server::

   apt install redis-server

Build the virtual environment with all needed modules::

   make

Usage
-----
make server recorder -j
   
Go to http://localhost:8080 to view the webcam.

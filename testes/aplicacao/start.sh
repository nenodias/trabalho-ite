#!/bin/sh
gunicorn -b 0.0.0.0:8888 wsgi -w5 -ktornado
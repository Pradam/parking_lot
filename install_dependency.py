#!/usr/bin/env bash

sudo aptitude -y install gcc make zlib1g-dev
wget https://www.python.org/ftp/python/3.6.3/Python-3.7.2.tar.xz
tar xJf Python-3.7.2.tar.xz
cd Python-3.7.2
./configure
make
make install
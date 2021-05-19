FROM balenalib/raspberry-pi-debian-python:buster

RUN [ "cross-build-start" ]

# install OS dependencies
RUN sudo apt-get update && sudo apt-get -y install cups-client \
    python3-dev python3-setuptools fonts-freefont-ttf

# install python dependencies
COPY requirements.txt requirements.txt
#RUN rm -rf /usr/lib/python3.7/site-packages/pip
RUN curl -sS https://bootstrap.pypa.io/get-pip.py | sudo python3
RUN python3 -m pip install --trusted-host pypi.python.org -r requirements.txt

# execute the audio player program
COPY print_images.py print_images.py
CMD ["python3", "print_images.py"]

RUN [ "cross-build-end" ]

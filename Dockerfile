# OS
FROM    ubuntu:xenial

# OS packages
RUN     apt-get update
RUN     apt-get upgrade \
            --yes
RUN     apt-get install \
            --yes \
            make \
            python3 \
            python3-numpy \
            python3-scipy \
            python3-sklearn \
            python3-pip \
            python3-setuptools \
            tox \
            virtualenv

# Python packages
ADD     requirements.txt /code/requirements.txt
RUN     virtualenv \
            --python=$(which python3) \
            /code/venv
RUN     /code/venv/bin/pip install \
            --requirement /code/requirements.txt

# The code
ADD     . /code/

# The service
WORKDIR /code
# RUN     make install
CMD     true

# rasberry-pi-open-cv

Small program allowing video manipulation using OpenCV along some popular
image analyzing techniques.

Made for demonstration of Rasberry Pi possibilities.

## Usage

General usage:

```bash
python3 record.py --func $FUN --width $WIDTH --height $HEIGHT
```

For example:

```bash
python3 record.py --func gauss-threshold --width 300 --height 400
```

## Parameters

Provide params using `--param_name`.

`fun` – function that is applied on captured video data. One of:

- `basic-threshold`
- `gauss-threshold`
- `sobel-det` – sobel edge detection
- `laplacian-det` – laplacian edge detection
- `canny-edge-det` – Canny edge detection
- `face-recognition` – face recognition function
- `cartoon`
- `none` – no function is applied on video

## Installation on Raspberry Pi 3B+

Installation instructions taking from plain Raspbian to OpenCV-equipped Raspberry. Tested on Rasberry Pi 3B+.

> **NOTE:** _you can also run the installation script from install.sh which will do the whole thing automatically._

### Preparing the device

#### Expand filesystem

Make the filesystem take up the whole SD card.

```bash
raspi-config --expand-rootfs
```

#### Increase swap size

It will be handy for the installation that demands huge amounts of RAM.

```bash
export SWAPSIZE=2048
```

```bash
# Stop the swap.
sudo dphys-swapfile swapoff
# Make swap bigger (=> 2048MB).
sed -i "/CONF_SWAPSIZE=.*/CONF_SWAPSIZE=$SWAPSIZE/" /etc/dphys-swapfile
# Create and initialize the swapfile.
dphys-swapfile setup
# Start the swap.
sudo dphys-swapfile swapon
```

#### Dependencies

> **Note:** _commands are separated as there are layers of dependencies_

```bash
sudo apt-get update && \
sudo apt-get upgrade && \
sudo apt-get install build-essential cmake pkg-config && \
sudo apt-get install libjpeg-dev libtiff5-dev libjasper-dev libpng12-dev && \
sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev && \
sudo apt-get install libxvidcore-dev libx264-dev && \
sudo apt-get install libgtk2.0-dev libgtk-3-dev && \
sudo apt-get install libatlas-base-dev gfortran && \
sudo apt-get install python3-dev
```

### Installing OpenCV

Save library version as this appears several times later on.

```bash
export VERSION=3.4.3
```

```bash
cd ~
wget -O opencv.zip "https://github.com/Itseez/opencv/archive/$VERSION.zip"
unzip opencv.zip
wget -O opencv_contrib.zip "https://github.com/Itseez/opencv_contrib/archive/$VERSION.zip"
unzip opencv_contrib.zip
```

#### Virtual Python environment

```bash
sudo pip3 install virtualenv virtualenvwrapper
sudo rm -rf ~/.cache/pip
```

```bash
echo "export WORKON_HOME=$HOME/.virtualenvs" >> ~/.profile
echo "source /usr/local/bin/virtualenvwrapper.sh" >> ~/.profile
```

```bash
source ~/.profile
```

```bash
mkvirtualenv cv -p python3
workon cv
```

#### Preparation

```bash
pip3 install numpy
```

```bash
cd ~/opencv-$VERSION
mkdir build
cd build
```

#### Compiling

```bash
cmake \
  -D CMAKE_BUILD_TYPE=RELEASE \
  -D CMAKE_INSTALL_PREFIX=/usr/local \
  -D INSTALL_PYTHON_EXAMPLES=ON \
  -D OPENCV_EXTRA_MODULES_PATH=~/opencv_contrib-$VERSION/modules \
  -D BUILD_EXAMPLES=ON ..
```

Dis gonna b good
```bash
make
```

#### Installing

```bash
sudo make install
sudo ldconfig
```

#### Renaming the library

```bash
ls -l /usr/local/lib/python3.5/site-packages
# cv2.cpython-35m-arm-linux-gnueabihf.so -> cv2.so
# export FILENAME=cv2.cpython-35m-arm-linux-gnueabihf.so
```

```bash
cd /usr/local/lib/python3.5/site-packages/
sudo mv $FILENAME cv2.so
```

```bash
cd ~/.virtualenvs/cv/lib/python3.5/site-packages/
ln -s /usr/local/lib/python3.5/site-packages/cv2.so cv2.so
```

#### Verification

```bash
python3
import cv2
cv2.__version__
```

## Sources

[Installing OpenCV 3.4.3 on Raspberry Pi 3 Model B+](https://www.alatortsev.com/2018/09/05/installing-opencv-3-4-3-on-raspberry-pi-3-b)

[Install guide: Raspberry Pi 3 + Raspbian Jessie + OpenCV 3](https://www.pyimagesearch.com/2016/04/18/install-guide-raspberry-pi-3-raspbian-jessie-opencv-3)

[OpenCV](https://opencv.org)

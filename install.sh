export VERSION=3.4.3
export SWAPSIZE=2048
raspi-config --expand-rootfs
dphys-swapfile swapoff
sed -i "/CONF_SWAPSIZE=.*/CONF_SWAPSIZE=$SWAPSIZE/" /etc/dphys-swapfile
dphys-swapfile setup
dphys-swapfile swapon
apt-get update && \
apt-get upgrade && \
apt-get install -y build-essential cmake pkg-config && \
apt-get install -y libjpeg-dev libtiff5-dev libjasper-dev libpng12-dev && \
apt-get install -y libavcodec-dev libavformat-dev libswscale-dev libv4l-dev && \
apt-get install -y libxvidcore-dev libx264-dev && \
apt-get install -y libgtk2.0-dev libgtk-3-dev && \
apt-get install -y libatlas-base-dev gfortran && \
apt-get install -y python3-dev
wget -O opencv.zip "https://github.com/Itseez/opencv/archive/$VERSION.zip"
unzip opencv.zip
wget -O opencv_contrib.zip "https://github.com/Itseez/opencv_contrib/archive/$VERSION.zip"
unzip opencv_contrib.zip
pip3 install virtualenv virtualenvwrapper
rm -rf ~/.cache/pip
echo "export WORKON_HOME=$HOME/.virtualenvs" >> ~/.profile
echo "source /usr/local/bin/virtualenvwrapper.sh" >> ~/.profile
source ~/.profile
mkvirtualenv cv -p python3
workon cv
pip3 install numpy
cd ~/opencv-$VERSION
mkdir build
cd build
cmake \
  -D CMAKE_BUILD_TYPE=RELEASE \
  -D CMAKE_INSTALL_PREFIX=/usr/local \
  -D INSTALL_PYTHON_EXAMPLES=ON \
  -D OPENCV_EXTRA_MODULES_PATH=~/opencv_contrib-$VERSION/modules \
  -D BUILD_EXAMPLES=ON ..
make
make install
ldconfig
ls -l /usr/local/lib/python3.5/site-packages
export FILENAME="cv2.cpython-35m-arm-linux-gnueabihf.so"
cd /usr/local/lib/python3.5/site-packages
sudo mv $FILENAME cv2.so
cd ~/.virtualenvs/cv/lib/python3.5/site-packages
ln -s /usr/local/lib/python3.5/site-packages/cv2.so cv2.so

# Video capture on Raspberry Pi using OpenCV lib

Small program allowing video capture on Raspberry Pi. App shares few basic video filters like Canny's edge detection,
Gauss threshold function or even Face recognition using Intel haar cascade. 

Code can be used on Raspberry Pi, as well as on normal PC.

## Usage

```
 >> python3 record.py --fun [function_name] --x [x_res_bound] --y [y_res_bound]
 #for example:
 >> python3 record.py --fun gauss-threshold --x 300 -y 400
```

```
  --fun [function_name] => Function that is applied on captured video data, chose from:
                            basic-threshold,
                            gauss-threshold,
                            sobel-det (Sobel edge detection),
                            laplacian-det (Laplacian edge detection),
                            canny-edge-det (Candy edge detection),
                            face-recognition (Face recognition function),
                            cartoon,
                            none (None function is applied on video)
  --x [x_res_bound]     => Width bound. Range 0 to MAX_CAM_RES_X.
  --y [y_res_bound]     => Height bound. Range 0 to MAX_CAM_RES_Y.
```

## Requirements
 - Python 3.X
 - OpenCV library
 - Numpy library
 
##### Note: Instruction for installing OpenvCV library on Raspberry Pi in install_instruction.pdf (Polish language) or at [pyimagesearch.com](https://www.pyimagesearch.com/2016/04/18/install-guide-raspberry-pi-3-raspbian-jessie-opencv-3/)


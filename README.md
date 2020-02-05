# friendly-octo-computing-machine

[Magic Mirror](https://github.com/MichMich/MagicMirror) <br>
[Smart Mirror](https://github.com/HackerShackOfficial/AI-Smart-Mirror)

# Setup Guide

Download the stable version of Node.js: 
https://nodejs.org/en/

Clone the latest MagicMirror code from:
https://github.com/MichMich/MagicMirror

Navigate inside the MagicMirror folder
```shell
cd MagicMirror
```

Install MagicMirror dependencies
```shell
sudo npm install
```
 
Verify it starts
```shell
npm start
```
 
Navigate out of the MagicMirror folder
```shell
cd ..
```
 
Clone this repository (AI Smart Mirror)
```shell
git clone git@github.com:HackerHouseYT/AI-Smart-Mirror.git
```

Copy the folders in `AI-Smart-Mirror/magic_mirror` to `MagicMirror/modules`

Copy the `config.js` file in `AI-Smart-Mirror/magic_mirror` to `MagicMirror/config`
 
## AI
 
Make sure Ruby is installed: https://www.ruby-lang.org/en/documentation/installation/
 
Install Homebrew: http://brew.sh/
 
Navigate to the AI-Smart-Mirror folder
```shell
cd AI-Smart-Mirror
```

Install ffmpeg
```
brew install ffmpeg
```

Use `setup.sh` to create a virtual environment and install dependencies
```shell
sudo ./setup.sh
```

Activate the virual evironment
```shell
source hhsmartmirror/bin/activate
```

Make sure MagicMirror is running, then start the AI
```shell
python bot.py
```

## Setup Facial Recognition

Install openCV with 
```shell
pip install opencv-python
```

Change flags=cv2.cv.CV_HAAR_SCALE_IMAGE in vision.py to:
```shell
flags=cv2.CASCADE_SCALE_IMAGE
```

Start the app
```shell
python bot.py
```

Deactivate the virtual evironment
```shell
deactive
```
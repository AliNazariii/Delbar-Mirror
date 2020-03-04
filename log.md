## Initiating project:
* lsblk
* dd of=<outputfile> if=<inputfile> bs=100MB
* clone
* install dependencies
* chmod MagicMirror
* fix displaying farsi texts in python in smart mirror
* change dates and week days to farsi mode
* connect news part to Alef RSS feed
* switch to a new Smart Mirror. "ah shit here we go again..."
--------------------
## Dependencies phase:
* executing readme.md on AI-Smart-Mirror
* encountered problem at installing pyaudio -> fixed with: sudo apt-get install portaudio19-dev python-pyaudio
* continue executing readme.md on AI-Smart-Mirror
* note: setup.sh on AI-Smart-Mirror doesn't work must execute every command manually
* to install OpenCV don't use brew :|
* use pip3 install opencv-python (in virtual env)
* to cast OpenCV3 to OpenCV4 change cv2.cv.CV_HAAR_SCALE_IMAGE -> cv2.CASCADE_SCALE_IMAGE
--------------------
## MagicMirror:
* Found out how to access log + how to redirect logs to terminal (by adding export ELECTRON_ENABLE_LOGGING=true at the start of run-start.sh found it on: [MagicMirror Wiki]() )
--------------------
## SmartMirror:
* Remove wit APIs
* use if/else to select an action based on speech
* connect news to Magic api
* save voice input
* connect to tosan speech to text api
* match recognized voice with news api
* remove old and redaundant services from smart mirror
* remove natural english language generator and knowledge python files
* completely clean the source codes to add new features

# Notes on required conference video recording

The requirements for the Video are:
- Video Resolution 1280x720 (720p) Landscape
- Video Format mp4 (H.264)
- max size 100MB
- Speaker video embedded in the slides

## Recording using Zoom

General Zoom settings
- Share Screen
  - disable scale to fit shared content to zoom window
  - enable side by side mode to include speaker video
- Video
  - do not check original video
  - do not check HD
- Recording
  - Record video during screen sharing

Settings when switching to shared screen mode
- do not use share computer sound
- do not use optimize screen sharing - the speaker video will be excluded


## Video resolution conversion

The problem is, that the video will be recorded at the maximal screen resolution; when setting the screen to the required resolution 1280x720, zoom records the shared screen in 1280x720, but appends the speaker view in addition on the side resulting in a 1500x720 resultion video.

VLC can be used to resize the video (more or less) to the required resolution

- open VLC
- make sure it is not set to repeat or shuffle!
- Media/convert-save; add required video;
- On the convert screen select mp4 and open settings
- select video codec/resolution
- set Scale to 1 and frame size to 1280 and 720 respectively


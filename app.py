from moviepy.editor import *
from moviepy.video.tools.subtitles import SubtitlesClip
from moviepy.config import change_settings

change_settings({"IMAGEMAGICK_BINARY": r"C:\Program Files\ImageMagick-7.1.1-Q16\magick.exe"})


clip1 = VideoFileClip("gta.mp4").subclip(20, 140).without_audio()
clip2 = VideoFileClip("mrbeast.mp4").subclip(0, 120)

combined = clips_array([ [clip2],[clip1]])
combined.write_videofile("test.mp4")
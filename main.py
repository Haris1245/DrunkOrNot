from moviepy.editor import *
from bing_image_downloader import downloader
import os
from moviepy.config import change_settings
from gtts import gTTS
import random
from elevenlabs.client import ElevenLabs
from elevenlabs import generate, save
change_settings({"IMAGEMAGICK_BINARY": r"C:\Program Files\ImageMagick-7.1.1-Q16\magick.exe"})

def generate_finale():
    tts = gTTS("What did you choose? Write in the comments!", lang="en")
    tts.save("finale.wav")
def generate_numbers():
    # Generate a random number between 0 and 100
    num1 = random.randint(0, 100)
    # Ensure the second number is such that the sum of both is 100
    num2 = 100 - num1
    return num1, num2
    
def text_to_speech(text):
   tts = gTTS(text, lang="en")
   tts.save("audio.wav")
def get_images(one, two):
    image_one = downloader.download(one, limit=1,  output_dir='input_images', adult_filter_off=True)
    image_two = downloader.download(two, limit=1,  output_dir='input_images', adult_filter_off=True)


def create_video(one, two, name):
    num1, num2 = generate_numbers()
    text_to_speech(f"What would you rather {one} or {two}")
    generate_finale()
    finale = "finale.wav"
    audio = "audio.wav"
    tick = "tick.wav"
    image_path = "background.png"
    image_clip = ImageClip(image_path)

    get_images(one, two)

    # Define the directory paths
    input_images_dir = "C:\\Users\\haris\\Desktop\\YouTubeAutomater\\input_images"
    one_images_dir = os.path.join(input_images_dir, one)
    two_images_dir = os.path.join(input_images_dir, two)

    # Check if the directories exist
    if not os.path.exists(one_images_dir) or not os.path.exists(two_images_dir):
        print("Error: One or both input image directories do not exist.")
        return

    # Get the image files
    images_one = os.listdir(one_images_dir)
    images_two = os.listdir(two_images_dir)

    # Check if images exist
    if not images_one or not images_two:
        print("Error: No images found in one or both input image directories.")
        return

    # Choose the first image from each directory
    image_one = os.path.join(one_images_dir, images_one[0])
    image_two = os.path.join(two_images_dir, images_two[0])

    # Load the images as clips
    img1_clip = ImageClip(image_one)
    img2_clip = ImageClip(image_two)
    img1_clip = img1_clip.set_position(((1920/2 - 1080/2) - 85 , 250))
    img1_clip = img1_clip.resize(width=500)
    image_duration = 17
    image_start_time = 1
    img1_clip= img1_clip.set_duration(image_duration)
    img1_clip = img1_clip.fx(vfx.fadein, 1).fx(vfx.fadeout, 1)
    img2_clip = img2_clip.set_position(((1920/2 - 1080/2) - 85 , 1300))
    img2_clip = img2_clip.resize(width=500)
    img2_clip= img2_clip.set_duration(image_duration)
    img2_clip = img2_clip.fx(vfx.fadein, 1).fx(vfx.fadeout, 1)
    text1_clip = TextClip(one, font ="Arial-Bold", fontsize = 70, color ="white").set_position(((1920/2 - 1080/2) - 85 , 100)).set_duration(image_duration).fx(vfx.fadein, 1).fx(vfx.fadeout, 1)
    text2_clip = TextClip(two, font ="Arial-Bold", fontsize = 70, color ="white").set_position(((1920/2 - 1080/2) - 85 , 1100)).set_duration(image_duration).fx(vfx.fadein, 1).fx(vfx.fadeout, 1)
    num1_clip = (TextClip(f"{num1}%", font="Impact", fontsize=80, color="green" if num1 >= num2 else "red", stroke_color="black", stroke_width=5)
             .set_position(((1920 / 2 - 1080 / 2 + 140), 150))
             .set_duration(image_duration)
             .fx(vfx.fadein, 1)
             .fx(vfx.fadeout, 1))

    num2_clip = (TextClip(f"{num2}%", font="Impact", fontsize=80, color="green" if num2 > num1 else "red", stroke_color="black", stroke_width=5)
                .set_position(((1920 / 2 - 1080 / 2 + 140), 1200))
                .set_duration(image_duration)
                .fx(vfx.fadein, 1)
                .fx(vfx.fadeout, 1))

    duration = 17 

    
    audio1_clip = AudioFileClip(audio)
    audio2_clip = AudioFileClip(tick).subclip(0, 3.5)
    audio3_clip = AudioFileClip(finale)

    # Resize te background image to fit the screen (1080x1920)
    image_clip_resized = image_clip.resize(width=1080)

    # Set the duration of the background image in the video
    image_clip_resized = image_clip_resized.set_duration(duration)

    # Set the size of the video
    final_clip = CompositeVideoClip([image_clip_resized,img1_clip.set_start(image_start_time),img2_clip.set_start(image_start_time), text1_clip.set_start(image_start_time), text2_clip.set_start(image_start_time), num1_clip.set_start(7.5), num2_clip.set_start(7.5) ], size=(1080, 1920))
    final_clip.audio = CompositeAudioClip([audio1_clip, audio2_clip.set_start(4), audio3_clip.set_start(8)])
    video = final_clip.subclip(0,13.5)
    video.write_videofile(f"{name}.mp4", fps=24)



one = input("First param: ")
two = input("Second param: ")

create_video(one, two, one + two)


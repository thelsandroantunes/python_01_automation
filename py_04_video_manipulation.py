from moviepy.editor import *

# ========== Crop and Concatenate Videos Start ========== #
clip_1 = VideoFileClip("videos/video_in/ikki_de_fenix.mp4").subclip(4, 10)
clip_2 = VideoFileClip("videos/video_in/ikki_de_fenix.mp4").subclip(24, 30)
clips = [clip_1, clip_2]
final_clip1 = concatenate_videoclips(clips)
final_clip1.write_videofile("videos/video_out/cdz_ikki.mp4")
# ========== Crop and Concatenate Videos End ========== #
# ========== Videos Colors Start ========== #
clip_1 = (VideoFileClip("videos/video_in/ikki_vs_shaka.mp4").subclip(8,
                                                                     15).fx(vfx.colorx, 1.2).fx(vfx.lum_contrast, 0, 30, 100))
clip_2 = (VideoFileClip(
    "videos/video_in/ikki_vs_shaka.mp4").subclip(28, 35).fx(vfx.invert_colors))
clips = [clip_1, clip_2]
final_clip2 = concatenate_videoclips(clips)
final_clip2.write_videofile("videos/video_out/cdz_shaka_ikki.mp4")

# ========== Videos Colors End ========== #
# ========== Videos Audio Start ========== #
clip = VideoFileClip("videos/video_in/ikki_shun.mp4")
clip = clip.subclip(10, 50)
audioclip = AudioFileClip(
    "audio/Dragon Ball Z - Cha-la Head Cha-la.mp3").subclip(10, 50)
final_clip3 = clip.set_audio(audioclip)
final_clip3.write_videofile("videos/video_out/cdz_shun_ikki.mp4")
# ========== Videos Audio End ========== #

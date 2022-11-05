from moviepy.editor import VideoFileClip

clip = VideoFileClip('countdown.mp4')

clip.write_gif('video2gif.gif',fps=10)
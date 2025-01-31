@REM 24 is the FPS

ffmpeg -r 24 -i new_photo_%01d.jpg -vcodec mpeg4 -y movie.mp4
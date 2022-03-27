# update title_ file first, then run this file

# N
yt-dlp --playlist-start 245 -f 140 -o '%(playlist)s/%(playlist_index)03d - %(title)s - %(id)s.%(ext)s' "PLslx0ZK4M9zfRUTXxZfbOgnTp4MuLcTjf"
# H
yt-dlp --playlist-start  83 -f 140 -o '%(playlist)s/%(playlist_index)03d - %(title)s - %(id)s.%(ext)s' "PLslx0ZK4M9zfBC2mVqC6vK5_s0UhbMki7"
# S
yt-dlp --playlist-start  22 -f 140 -o '%(playlist)s/%(playlist_index)03d - %(title)s - %(id)s.%(ext)s' "PLslx0ZK4M9zcXeulFkhF9plJg21wqYno-"

python3 rename.py

sha256sum */* > sha256sum
# update title_ files before running this script

# N
yt-dlp --playlist-start 255 -f 140 -o '%(playlist)s/%(playlist_index)03d - %(title)s - %(id)s.%(ext)s' "PLslx0ZK4M9zfRUTXxZfbOgnTp4MuLcTjf"
# H
yt-dlp --playlist-start  92 -f 140 -o '%(playlist)s/%(playlist_index)03d - %(title)s - %(id)s.%(ext)s' "PLslx0ZK4M9zertJb1q9I4vL3Z8IMtIw4D"
# S
yt-dlp --playlist-start  35 -f 140 -o '%(playlist)s/%(playlist_index)03d - %(title)s - %(id)s.%(ext)s' "PLslx0ZK4M9ze0MqtIiTguDfmP0eOvdj2i"

python3 rename.py

sha256sum */* > sha256sum

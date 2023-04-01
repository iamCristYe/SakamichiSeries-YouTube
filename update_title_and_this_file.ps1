# N
yt-dlp --playlist-start 276 -f 140 -o '%(playlist)s/%(playlist_index)03d - %(title)s - %(id)s.%(ext)s' "PLslx0ZK4M9zfRUTXxZfbOgnTp4MuLcTjf"
# H
yt-dlp --playlist-start 100 -f 140 -o '%(playlist)s/%(playlist_index)03d - %(title)s - %(id)s.%(ext)s' "PLslx0ZK4M9zertJb1q9I4vL3Z8IMtIw4D"
# S
yt-dlp --playlist-start  42 -f 140 -o '%(playlist)s/%(playlist_index)03d - %(title)s - %(id)s.%(ext)s' "PLslx0ZK4M9ze0MqtIiTguDfmP0eOvdj2i"

bash -c "python3 rename.py"

bash -c "sha256sum */* > sha256sum"

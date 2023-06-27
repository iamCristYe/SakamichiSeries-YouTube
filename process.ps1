bash -c "python3 rename.py reverse"

# N
$N_count = (Get-ChildItem "乃木坂46全曲 All Songs from Nogizaka46" | Measure-Object).count
yt-dlp --playlist-start $N_count -f 140 -o '%(playlist)s/%(playlist_index)03d - %(title)s - %(id)s.%(ext)s' "PLslx0ZK4M9ze0MqtIiTguDfmP0eOvdj2i"
# H
$H_count = (Get-ChildItem "日向坂46全曲 All Songs from Hinatazaka46" | Measure-Object).count
yt-dlp --playlist-start $H_count -f 140 -o '%(playlist)s/%(playlist_index)03d - %(title)s - %(id)s.%(ext)s' "PLslx0ZK4M9zertJb1q9I4vL3Z8IMtIw4D"
# S
$S_count = (Get-ChildItem "櫻坂46全曲 All Songs from Sakurazaka46" | Measure-Object).count
yt-dlp --playlist-start $S_count -f 140 -o '%(playlist)s/%(playlist_index)03d - %(title)s - %(id)s.%(ext)s' "PLslx0ZK4M9zd7QFaTHsOJP9SOFnK6tJrs"

bash -c "python3 rename.py rename"

bash -c "sha256sum */* > sha256sum"

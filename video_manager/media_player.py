class Player:
    def __init__(self, name="", source="", duration=0, muted=False, autoplay=True, volume=1.0, time=0.0, quality=360):
            self.name = name
            self.source = source
            self.duration = duration
            self.muted = muted
            self.autoplay = autoplay
            self.volume = volume
            self.time = time
            self.quality = quality
            self.playing = False

    def play(self,source):
        if source == self.source:
            self.playing = True
            print(f"Playing video: {self.name}")

    def pause(self):
        self.playing = False
        print(f"Pausing video: {self.name}")

    allowed_qualities = [144, 280, 380, 720, 1080]
    def change_quality(self,new_quality):
        if new_quality in self.allowed_qualities :
            self.quality = new_quality
            print(f"Changed video quality to {new_quality}")
        else:
            print(f"Invalid quality. Allowed qualities are: {', '.join(map(str, self.allowed_qualities))}")


    def mute_video(self):
        self.muted = not self.muted
        if self.muted:
            print(f"Video muted")
        else:
            print(f"Video unmuted")

    def volume_up(self,add_volume = 0.1):
        self.volume += add_volume
        print(f"Volume increased to {self.volume}")

    def volume_down(self,add_volume = 0.1):
        self.volume -= add_volume
        print(f"Volume decreased to {self.volume}")

     
video_player = Player(name="Sample Video", source="sample.mp4", duration=120)
video_player.play("sample.mp4")
video_player.pause()
video_player.change_quality(720)
video_player.change_quality(500)
video_player.mute_video()
video_player.mute_video()
video_player.volume_up(4.2)
video_player.volume_down(2.1)
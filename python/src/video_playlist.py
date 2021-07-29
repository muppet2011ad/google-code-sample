"""A video playlist class."""


class Playlist:
    """A class used to represent a Playlist."""
    def __init__(self, playlist_name):
        self._name = playlist_name
        self._videos = []

    @property
    def name(self) -> str:
        return self._name

    @property
    def name_nocase(self) -> str:
        return self._name.lower()

    @property
    def videos(self):
        return self._videos

    def add_video(self, video):
        """Adds a video to the playlist. Returns true if successful, false if video already in playlist
        
        Args:
            video: The video object to be added
        """
        if video in self.videos:
            return False
        else:
            self._videos.append(video)
            return True

    def remove_video(self, video):
        """Removes a video from the playlist. Returns true if successful, false if video not in playlist
        
        Args:
            video: The video object to be removed
        """
        if video in self.videos:
            self._videos.remove(video)
            return True
        else:
            return False

    def clear(self):
        """Removes all videos from a playlist"""
        self._videos = []
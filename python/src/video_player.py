"""A video player class."""

from .video_library import VideoLibrary
import random


class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()
        self.playing = None
        self.paused = True

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def prettify_video(self, video):
        """Returns a string representing video. Format is title (id) [#tags]
        
        Args:
            video: the video object to be prettified."""
        output = "{0} ({1}) [".format(video.title, video.video_id)
        first = True
        for tag in video.tags:
            if first:
                first = False
            else:
                output = output + " "
            output = output + tag
        return output + "]"

    def show_all_videos(self):
        """Returns all videos."""

        print("Here's a list of all available videos:")
        videos = self._video_library.get_all_videos()
        videos.sort(key=lambda x: x.title)
        for video in videos:
            print(self.prettify_video(video))
            

    def play_video(self, video_id):
        """Plays the respective video.

        Args:
            video_id: The video_id to be played.
        """
        videos = self._video_library.get_all_videos()
        new_vid = next((vid for vid in videos if vid.video_id == video_id), None)
        if new_vid:
            self.play_me(new_vid)
        else:
            print("Cannot play video: Video does not exist")

    def play_me(self, video):
        """Plays a video object
        
        Args:
            video: The video object to be played"""
        if self.playing:
                print("Stopping video: {0}".format(self.playing.title))
        print("Playing video: {0}".format(video.title))
        self.paused = False
        self.playing = video

    def stop_video(self):
        """Stops the current video."""

        if not self.playing:
            print("Cannot stop video: No video is currently playing")
        else:
            print("Stopping video: {0}".format(self.playing.title))
            self.playing = None

    def play_random_video(self):
        """Plays a random video from the video library."""

        videos = self._video_library.get_all_videos()
        self.play_me(random.choice(videos))

    def pause_video(self):
        """Pauses the current video."""

        if self.playing:
            if self.paused:
                print("Video already paused: {0}".format(self.playing.title))
            else:
                print("Pausing video: {0}".format(self.playing.title))
                self.paused = True
        else:
            print("Cannot pause video: No video is currently playing")

    def continue_video(self):
        """Resumes playing the current video."""

        if self.playing:
            if self.paused:
                print("Continuing video: {0}".format(self.playing.title))
                self.paused = False
            else:
                print("Cannot continue video: Video is not paused")
        else:
            print("Cannot continue video: No video is currently playing")

    def show_playing(self):
        """Displays video currently playing."""

        if self.playing:
            print("Currently playing: {0}".format(self.prettify_video(self.playing)), end="")
            if self.paused:
                print(" - PAUSED")
            else:
                print()
        else:
            print("No video is currently playing")

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("create_playlist needs implementation")

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        print("add_to_playlist needs implementation")

    def show_all_playlists(self):
        """Display all playlists."""

        print("show_all_playlists needs implementation")

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("show_playlist needs implementation")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        print("remove_from_playlist needs implementation")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("clears_playlist needs implementation")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("deletes_playlist needs implementation")

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        print("search_videos needs implementation")

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        print("search_videos_tag needs implementation")

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")

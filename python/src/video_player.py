"""A video player class."""

from .video_library import VideoLibrary
from .video_playlist import Playlist
import random


class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()
        self.playing = None
        self.paused = True
        self.playlists = []

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
        output = output + "]"
        if video.flagged:
            output = output + " - FLAGGED (reason: {0})".format(video.flagged_reason)
        return output

    def find_video(self, video_id):
        """Finds video in the library from a video id. Returns None if no such video is found.
        
        Args:
            video_id: The id of the video to find"""
        return next((vid for vid in self._video_library.get_all_videos() if vid.video_id == video_id), None)

    def find_playlist(self, playlist_name):
        """Finds playlist based on its name. Returns None if no such playlist is found
        
        Args:
            playlist_name: The name of the playlist to find (case insensitive)"""
        playlist_name_lower = playlist_name.lower()
        return next((playlist for playlist in self.playlists if playlist.name_nocase == playlist_name_lower), None)

    def show_all_videos(self):
        """Returns all videos."""

        print("Here's a list of all available videos:")
        videos = self._video_library.get_all_videos()
        videos.sort(key=lambda x: x.title)
        for video in videos:
            print("\t {0}".format(self.prettify_video(video)))
            

    def play_video(self, video_id):
        """Plays the respective video.

        Args:
            video_id: The video_id to be played.
        """
        new_vid = self.find_video(video_id)
        if new_vid:
            self.play_me(new_vid)
        else:
            print("Cannot play video: Video does not exist")

    def play_me(self, video):
        """Plays a video object
        
        Args:
            video: The video object to be played"""
        if not video.flagged:
            if self.playing:
                print("Stopping video: {0}".format(self.playing.title))
            print("Playing video: {0}".format(video.title))
            self.paused = False
            self.playing = video
        else:
            print("Cannot play video: Video is currently flagged (reason: {0})".format(video.flagged_reason))

    def stop_video(self):
        """Stops the current video."""

        if not self.playing:
            print("Cannot stop video: No video is currently playing")
        else:
            print("Stopping video: {0}".format(self.playing.title))
            self.playing = None

    def play_random_video(self):
        """Plays a random video from the video library."""

        videos = list(filter(lambda v: not v.flagged, self._video_library.get_all_videos()))
        if videos:
            self.play_me(random.choice(videos))
        else:
            print("No videos available")

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
        conflicting_playlist = self.find_playlist(playlist_name)
        if conflicting_playlist:
            print("Cannot create playlist: A playlist with the same name already exists")
        else:
            self.playlists.append(Playlist(playlist_name))
            print("Successfully created new playlist: {0}".format(playlist_name))

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        playlist = self.find_playlist(playlist_name)
        if playlist:
            video = self.find_video(video_id)
            if video:
                if not video.flagged:
                    success = playlist.add_video(video)
                    if success:
                        print("Added video to {0}: {1}".format(playlist_name, video.title))
                    else:
                        print("Cannot add video to {0}: Video already added".format(playlist_name))
                else:
                    print("Cannot add video to {0}: Video is currently flagged (reason: {1})".format(playlist_name, video.flagged_reason))
            else:
                print("Cannot add video to {0}: Video does not exist".format(playlist_name))
        else:
            print("Cannot add video to {0}: Playlist does not exist".format(playlist_name))

    def show_all_playlists(self):
        """Display all playlists."""

        if self.playlists:
            print("Showing all playlists:")
            playlists_sorted = sorted(self.playlists, key=lambda p: p.name_nocase)
            for playlist in playlists_sorted:
                print("\t {0}".format(playlist.name))
        else:
            print("No playlists exist yet")

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        playlist = self.find_playlist(playlist_name)
        if playlist:
            print("Showing playlist: {0}".format(playlist_name))
            if playlist.videos:
                for video in playlist.videos:
                    print("\t{0}".format(self.prettify_video(video)))
            else:
                print("\tNo videos here yet")
        else:
            print("Cannot show playlist {0}: Playlist does not exist".format(playlist_name))

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        playlist = self.find_playlist(playlist_name)
        if playlist:
            video = self.find_video(video_id)
            if video:
                success = playlist.remove_video(video)
                if success:
                    print("Removed video from {0}: {1}".format(playlist_name, video.title))
                else:
                    print("Cannot remove video from {0}: Video is not in playlist".format(playlist_name))
            else:
                print("Cannot remove video from {0}: Video does not exist".format(playlist_name))
        else:
            print("Cannot remove video from {0}: Playlist does not exist".format(playlist_name))

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        playlist = self.find_playlist(playlist_name)
        if playlist:
            playlist.clear()
            print("Successfully removed all videos from {0}".format(playlist_name))
        else:
            print("Cannot clear playlist {0}: Playlist does not exist".format(playlist_name))

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        playlist = self.find_playlist(playlist_name)
        if playlist:
            self.playlists.remove(playlist)
            print("Deleted playlist: {0}".format(playlist_name))
        else:
            print("Cannot delete playlist {0}: Playlist does not exist".format(playlist_name))

    def search_results(self, search_term, results):
        """Displays search results and offers to play one of the results
        
        Args:
            search_term: The search term that was used to generate the search
            results: A list of video objects to be displayed"""
        results = list(filter(lambda v: not v.flagged, results))
        print("Here are the results for {0}:".format(search_term))
        x = 0
        while x < len(results):
            print("\t{0}) {1}".format(x+1, self.prettify_video(results[x])))
            x += 1
        print("Would you like to play any of the above? If yes, specify the number of the video.\nIf your answer is not a valid number, we will assume it's a no.")
        raw_selection = input()
        selection = None
        try:
            selection = int(raw_selection)
        except ValueError:
            return
        if selection >= 1 and selection-1 < len(results):
            self.play_me(results[selection-1])

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        term_lower = search_term.lower()
        results = sorted([video for video in self._video_library.get_all_videos() if term_lower in video.title.lower()], key=lambda v: v.title)
        if results:
            self.search_results(search_term, results)
        else:
            print("No search results for {0}".format(search_term))


    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        tag_lower = video_tag.lower()
        results = sorted([video for video in self._video_library.get_all_videos() if tag_lower in map(lambda t: t.lower(), video.tags)], key=lambda v: v.title)
        if results:
            self.search_results(video_tag, results)
        else:
            print("No search results for {0}".format(video_tag))

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        video = self.find_video(video_id)
        if video:
            if not video.flagged:
                video.flag(flag_reason)
                if self.playing == video:
                    self.stop_video()
                print("Successfully flagged video: {0} (reason: {1})".format(video.title, video.flagged_reason))
            else:
                print("Cannot flag video: Video is already flagged")
        else:
            print("Cannot flag video: Video does not exist")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        video = self.find_video(video_id)
        if video:
            if video.flagged:
                video.unflag()
                print("Successfully removed flag from video: {0}".format(video.title))
            else:
                print("Cannot remove flag from video: Video is not flagged")
        else:
            print("Cannot remove flag from video: Video does not exist")

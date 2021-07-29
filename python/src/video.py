"""A video class."""

from typing import Sequence


class Video:
    """A class used to represent a Video."""

    def __init__(self, video_title: str, video_id: str, video_tags: Sequence[str]):
        """Video constructor."""
        self._title = video_title
        self._video_id = video_id
        self._flagged = False
        self._flagged_reason = ""

        # Turn the tags into a tuple here so it's unmodifiable,
        # in case the caller changes the 'video_tags' they passed to us
        self._tags = tuple(video_tags)

    @property
    def title(self) -> str:
        """Returns the title of a video."""
        return self._title

    @property
    def video_id(self) -> str:
        """Returns the video id of a video."""
        return self._video_id

    @property
    def tags(self) -> Sequence[str]:
        """Returns the list of tags of a video."""
        return self._tags

    @property
    def flagged(self) -> bool:
        return self._flagged

    @property
    def flagged_reason(self) -> str:
        if self._flagged:
            return self._flagged_reason
        else:
            return ""

    def flag(self, reason):
        """Flags video for given reason. Reason defaults to 'Not supplied' if left blank
        
        Args:
            reason: The reason for flagging the video"""
        self._flagged = True
        if reason:
            self._flagged_reason = reason
        else:
            self._flagged_reason = "Not supplied"

    def unflag(self):
        """Removes the flag from a video"""
        self._flagged = False
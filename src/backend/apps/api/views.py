"""
Views for the media module.
"""

from flask.views import MethodView

# from flask_babel import gettext as _ # for i18n


class Image(MethodView):
    """
    Endpoint that get Images
    """

    def get(self):
        """
        Gets image
        """
        return ""


class Video(MethodView):
    """
    Endpoint that get Videos
    """

    def get(self):
        """
        Gets video
        """
        return ""


class Audio(MethodView):
    """
    Endpoint that get Audios
    """

    def get(self):
        """
        Gets audio
        """
        return ""

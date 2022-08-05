import os


class Manager():
    @staticmethod
    def video_path(number_video):
        videos_path = [{"id": 1, "path": "movie_day.mp4"}, {"id": 2, "path": "movie_night.mp4"}]
        for item in videos_path:
            if item["id"] == number_video:
                return item["path"]
                break
        return ""

    @staticmethod
    def image_path(number_video):
        videos_path = [{"id": 1, "path": "parking_full.jpg"}]
        for item in videos_path:
            if item["id"] == number_video:
                return item["path"]
                break
        return ""

    @staticmethod
    def play_video(number_video):
        return ""

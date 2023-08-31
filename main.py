import argparse
import os
from datetime import datetime
from pathlib import Path
from moviepy.editor import VideoFileClip


def get_args():
    parser = argparse.ArgumentParser(description="今日の作業効率を計算する")
    parser.add_argument('path', type=str, help="動画ファイルがあるディレクトリ")
    parser.add_argument('worktime', type=int, help="今日の作業時間(分)")
    parser.add_argument('-d', '--date', type=str, help="計算対象の作業日を指定する(YYYY-MM-DD)")
    return parser.parse_args()


class VideoCreateEfficiencyCalculator:
    """今日の作業効率を計算する"""

    def __init__(self, path, worktime, date=None):
        self.target_dir = Path(path)
        self.worktime = worktime
        if date:
            self.target_date = datetime.strptime(date, '%Y-%m-%d').date()
        else:
            self.target_date = datetime.today().date()
        self._total_completed_video_duration = None
        self._efficiency = None

    @property
    def total_completed_video_duration(self):
        if self._total_completed_video_duration is None:
            self._total_completed_video_duration = self._calculate_total_duration()
        return self._total_completed_video_duration

    @property
    def efficiency(self):
        if self._efficiency is None:
            self._efficiency = self.total_completed_video_duration / self.worktime
        return self._efficiency

    def _get_duration_in_minutes(self, video_file):
        """動画ファイルの長さを分単位で返す"""
        file_create_date = datetime.fromtimestamp(os.stat(video_file).st_mtime).date()
        if file_create_date == self.target_date:
            duration = VideoFileClip(str(video_file)).duration / 60
            return duration

    def _calculate_total_duration(self):
        """今日の動画完成合計時間を計算する"""
        total_duration = 0
        for file in self.target_dir.glob('**/*'):
            if file.suffix in ['.mp4', '.mov']:
                duration = self._get_duration_in_minutes(file)
                print(f'{file.name} {duration:.0f}分')
                total_duration += duration
        return total_duration

    def print_efficiency(self):
        print(f'\n合計時間: {self.total_completed_video_duration:.0f}分')
        print(f'作業効率: {self.efficiency:.2f}')


if __name__ == '__main__':
    args = get_args()
    video_create = VideoCreateEfficiencyCalculator(args.path, args.worktime, args.date)
    video_create.print_efficiency()

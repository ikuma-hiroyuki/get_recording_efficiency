import argparse
import os
from datetime import datetime
from pathlib import Path

from moviepy.editor import VideoFileClip

parser = argparse.ArgumentParser(description="今日の作業効率を計算する")
parser.add_argument('path', type=str)
parser.add_argument('worktime', type=int)
args = parser.parse_args()

target_dir = Path(args.path).expanduser().resolve()


def get_duration(file_path):
    clip = VideoFileClip(str(file_path))
    return clip.duration / 60


total_duration = 0
for file in target_dir.glob('*'):
    if file.suffix in ['.mp4', '.mov']:
        create_date = datetime.fromtimestamp(os.path.getctime(file)).date()
        if create_date == datetime.today().date():
            duration = get_duration(file)
            print(f'{file.name} {duration:.0f}分')
            total_duration += duration
print(f'\n今日の合計時間: {total_duration:.0f}分')
print(f'今日の作業効率: {total_duration / args.worktime:.2f}')

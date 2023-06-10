# 本日完成した動画ファイルの再生時間を取得し、収録時間との比率を計算する



## 前提条件

ffmpeg のインストールが必要。

```sh
brew install ffmpeg
```



## ヘルプ

```sh
python3 main.py -h
usage: main.py [-h] path worktime

今日の作業効率を計算する

positional arguments:
  path
  worktime

options:
  -h, --help  show this help message and exit
```


# 本日完成した動画ファイルの再生時間を取得し、収録時間との比率(作業効率)を計算する

## 概要
- 指定したディレクトリのサブディレクトリも含めて `mp4` および `mov` ファイルの再生時間を取得し、作業時間との比率(作業効率)を計算する。
- 対象日を指定しない場合は当日作成されたファイルを集計対象にする


## 使用方法
1. 仮想環境に入る
2. `pip install -r requirements.txt` を実行する
3. `python main.py <動画ファイルがあるディレクトリ> <今日の作業時間(分)> (対象日 [YYYY-MM-DD])` を実行する
4. 作業効率が表示される
5. 同ディレクトリに `video_create_efficiency.xlsx` が作成され、開かれる


## 前提条件

Macはffmpeg のインストールが必要。

```sh
brew install ffmpeg
```



## ヘルプ

```sh
usage: main.py [-h] [-d DATE] path worktime

今日の作業効率を計算する

positional arguments:
  path                  動画ファイルがあるディレクトリ
  worktime              今日の作業時間(分)

options:
  -h, --help            show this help message and exit
  -d DATE, --date DATE  計算対象の作業日を指定する(YYYY-MM-DD)
```


# 動かし方

## 事前準備

下記２つのサイトを参考にOpen JTalkとffmpegの準備を行っておく。

* Windowsで音声合成Open JTalk #音声合成 - Qiita:[https://qiita.com/mkgask/items/0bf9c26dc96e7b0b45ac](https://qiita.com/mkgask/items/0bf9c26dc96e7b0b45ac)
* windowsにffmpegをインストールする | ぱーくん plus idea:[https://plus-idea.net/windows-ffmpeg/](https://plus-idea.net/windows-ffmpeg/)

## DiscordBotの権限等
* 権限（招待URLが写っていますが、Botユーザーを削除済みなのでご心配なく！）
![権限](https://github.com/rainbow0210/YomiageBot/blob/main/images/permission.png?raw=true)

* インテンツの設定
![インテンツの設定](https://github.com/rainbow0210/YomiageBot/blob/main/images/intents.png?raw=true)

## Bot本体の動かし方

1. 下のダウンロードからBotのコードをダウンロードする。
  * [Download](https://github.com/rainbow0210/YomiageBot/archive/refs/heads/main.zip)

2. ダウンロードしたファイルを解凍する。

3. 解凍して出てくる「ffmpeg」ファイルの中に事前ダウンロードしておいたffmpegのzipファイルを解凍したら出てくるbinファイルなどを入れておく。

4. 「main.py」の48行目の「your_discord_token」に自分のDiscordBotのトークンを入れる。

5.　展開したファイル上でコマンドプロンプトかPowerShellを開き、「pip install -r requirements.txt」を実行し、Botを動かすのに必要なライブラリのインストールを行う。

6. 展開したファイル上でコマンドプロンプトかPowerShellを開き、「python main.py」を実行すれば起動させることができます。

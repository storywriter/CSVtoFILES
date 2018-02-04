# CSVtoFILES csv1行ごとに1ファイルを生成する

2018年2月4日 Yoshiki Hayama @storywriter

## 使いかた

前提: Python がインストールされていること。（Python 2.7.10 で動作確認）

1. 分割したいcsvファイルを _.csv という名前で用意する（書式　1列目:id, 2列目:本文）
2. 該当csvファイルがあるフォルダに csv_to_files.py を入れる。
3. コマンドラインで、該当フォルダに移動し、 python csv_to_files.py と入力する。
4. プログラムが src.csv を読み込んで分割し、 ファイルを生成する。

メモ: IBM Watson Discovery 用に Twitter のデータを、大量ファイルに分割したい、というニーズにより作成した。Discovery が単純な txt ファイルに対応していないので、すべて HTML ファイルで生成している。


## 備考

個人用途のため、不正文字列などのエラー処理はしていない。


## 参考

IBM Watson Discovery:
https://www.ibm.com/watson/services/discovery/


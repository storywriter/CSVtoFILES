#! /usr/local/bin/python2.7
# coding: utf-8

# csv1行ごとに1ファイルを生成する
# 2016年2月4日


import os
import csv

path = 'temp'

if os.path.isdir( path ):

  pass # フォルダは存在している

else:

  os.mkdir( path )


# csv の読み込み
with open( '_.csv', "rU" ) as csvfile:

  reader = csv.reader( csvfile )

  for row in reader:

    html = '<!doctype html><html>'

    html = html + '<head><title>' + row[ 0 ] + '</title></head>'

    html = html + '<body>' + row[ 1 ] + '</body>'

    html = html + '</html>'

    # ファイルに出力
    output_file = open( path + '/' + row[ 0 ] + '.html', 'w' )
    output_file.write( html )
    output_file.close()


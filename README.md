# what is
よく2chまとめサイト等に「〇〇な壁紙ください！」みたいなページがありますよね。
このスクリプトはそのページにある画像を全てダウンロードするスクリプトです。

# caution
このスクリプトでは、Aタグで囲まれている画像をダウンロードします。
なので、直接imgタグで画像をはってあるページの画像はダウンロードできません。
pythonを少しわかる方ならこのスクリプトを改造して自分仕様にしていただいてかまいません。
ライセンスはNYSLでｗ

# how to use
<pre>
$ git clone git://github.com/alice1017/image-downloader.git
$ cd image-downloader
$ ./downloaader [URL] [画像を置きたいディレクトリ]
</pre>

# change log
<ol>
	<li>ver 1.0.3 - default</li>
	<li>ver 1.0.4 - ログ機能追加。 $HOME/image-downloader.logでいままで自分がダウンロードしたURLの履歴がみれる</li>
</ol>

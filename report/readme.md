## 卒論について
### 提出期限
12月中旬
### 分量
20ページ程度
### 参考
http://www.wakayama-u.ac.jp/~sakama/sotsuron/sotsuron.html
https://www.flo-shot.com/entry/2016/10/14/174541
https://www.meiji.ac.jp/bungaku/ballc/current/papers.html

## タイトル
LABEL DETECTION ON THE POLE

## 構成内容
1. CHAPTER 1 - INTRODUCTION
    1. Background of the Problem
    1. Problem Statement
    1. Objectives
    1. Scope of study
1. CHAPTER 2- LITERATURE REVIEW
    1. Overview
    1. YOLO
1. CHAPTER 3 - METHODOLOGY
    1. Overview
    1. Find label from picture
    1. Image prosessing
    1. Label recognition
    1. Workflow
    1. Jetson xavier
1. CHAPTER 4 – RESULTS
    1. Preliminary Results
    1. Comparation
    1. Expected Results
1. CHAPTER 5- CONCLUSION 
    1. REFERENCES 

## Chapter1 - Introduction
### Background of the Problem
本研究の意義と現状の課題を記述する
#### 例
自動化技術は我々人類にとって大きな課題である。
近年,AI技術の発達によって様々なタスクが解決可能になってきている。
その中でも文字認識は、データ入力から自動運転まで様々な分野での適用が期待されており、文字認識精度を向上させる事は強く望まれる。
現実世界における文字認識の用途は大まかに2種類に分類できる。一つ目は、紙媒体書類の電子化(OCR)である。もう一つは、看板などのおもに人間向けに設計された標識の読み取りである。
一般物体上の文字の認識は形状や向き、周りの物体に左右され、認識精度は依然として実用化には程遠い。本研究の目的は、これらの文字認識精度の向上である。
#### 英訳
Automation technology is a big topic for us.
In recent years, with the development of AI technology, we can solve various tasks.
Especially character recognition is expected to be applied in various fields from data input to automatic driving, it is strongly desired to improve character recognition accuracy.
The applications of character recognition in the real world can roughly be classified into two types.
The first is Optical Character Recognition(OCR).
The other is recognizing signs designed for people, such as billboards.
Recognition of characters on general objects depends on shape, rotation, objects around them, recognition accuracy is still far from practical use.
The purpose of this research is to improve these character recognition accuracy.

### Problem Statement
研究で取り組む課題は何かを説明する。
#### 例
本研究では、一般物体上、特に柱上にある文字を認識することを考える。近年の研究では、おもに深層学習を利用したものが主流であり、本研究でも深層学習を利用して文字認識を行う。
#### 英訳
In this research, we recognize characters on objects, especially on pillars. Recent studies mainly use deep learning, and this research also uses deep learning to do character recognition.

### Objectives
上記を踏まえて研究の目標を簡潔に定義する。
#### 例
深層学習を利用し円柱曲面状にある文字列を認識する。
#### 英訳
Recognize a character string in a cylindrical curved surface shape using deep learning.

### Scope of study
本研究の取り扱う範囲について記述する。
#### 例
本研究では、画像認識に機械学習フレームワークであるdarknetとYOLOというネットワークを利用する。
YOLOは、現在の一般物体検出においてFaster R-CNNと並んで高い精度を示しており、Faster R-CNNより処理速度に優れるのが特徴である。
#### 英訳
In this research, we use darknet machine learning framework　and YOLO algorithm for image recognition.
YOLO shows high accuracy as well as Faster R-CNN in object detection and much faster.

## CHAPTER 2 - LITERATURE REVIEW
関連する過去の論文や資料、文献を要約、批判的分析を述べる。
### Overview
概要を図にして示す。
#### 例
概要を図_xに示す
#### 英訳
The overview for the literature review can be seen in the figure below.

### YOLO
YOLOについて説明する
#### 例
YOLOは2016年に発表されたリアルタイム物体認識アルゴリズムである。
既存の画像認識のアルゴリズムである「DPM」や「R-CNN」は、画像の領域推定と分類が分断されており、それゆえ処理が複雑であり、かつ処理時間も長くなりがちであった。 「YOLO」では、画像認識を回帰問題に落とし込み、「画像の領域推定」と「分類」を同時に行うことを実現した。 「YOLO」のアルゴリズムは１つのCNNで完結するためシンプルであり、また既存の手法と比較して処理が早く、背景の誤検出が少ないなどのメリットを得ることができる。
#### 英訳
YOLO is a real-time object recognition algorithm, which was announced in 2016.
Regarding existing image recognition algorithms such as "DPM" and "R - CNN", region estimation and classification of images are separated, and therefore processing tends to be complicated and processing time tends to be long. In "YOLO", we perform that "image area estimation" and "classification" at the same time. The algorithm of "YOLO" is simple because it is completed with one CNN, and it has merits such as quick processing as compared with the existing method, less background error detection.


### 画像認識に関する論文X
前例を洗ってこれを分析する。

## CHAPTER 3 - METHODOLOGY
提案手法について説明する。
### Overview
概要を図にして示す。
#### 例
概要を図_Xに示す。我々の提案手法ではまず、写真からラベルを抽出し、切り出した画像に対して何らかの画像処理を行い、出力された画像に対して認識を行う。

### Find label from picture
写真からラベルを抽出するプロセスについて説明する
#### 例
文字を認識する前に、写真から認識したい文字列を含むラベル領域を切り出す。こうすることで文字の謝検出の抑制と計算量の軽減に繋がる。
ラベル領域の認識には前途の通りYOLOを利用する。
まず、何も情報が付加されていない写真にラベリングを行う。
ラベリングとは、もともとあるデータに対して、画像内に含まれるクラスやその座標といった付加情報を与える事であり、機械学習はこのアノテーションデータを元に学習をしていく。訓練用のデータには車載カメラから撮影された電柱の写真を用いる。
YOLOのアノテーションデータの構造は単純で、{カテゴリ番号 オブジェクトの中心ｘ座標 オブジェクトの中心ｙ座標 オブジェクトの幅 オブジェクトの高さ}で表現される。
直接ファイルを編集するのは大変なのでラベリングには、ラベリング用の入力支援ツールを使う事で、作業を視覚的に行うことができる。
我々は、大量の写真に手作業でラベリングを行った。


### Image prosessing
切り出したラベルに対して画像処理を行うプロセスについて説明する。
#### 例
従来の画像認識技術は、たいらな平面状の画像に対して認識を想定しており、歪んだ画像をそのまま認識に使うと高い精度を得られない。したがって、切り出されたラベルを平面に展開する必要がある。
曲面状の画像を平面に変形するには以下の変換公式を使う。
XXXX
この公式を図_Xに適用することによって図_Xを得る

### Label recognition
平面に展開された画像に対して認識を行うプロセスについて説明する。
#### 例
平面に展開された画像に対して認識を行う。認識のプロセスを以下に示す。
YOLOを用いてアルファベットa-zA-Zの52クラスの物体検知を行う。
<!--訓練には、手書き文字データセットであるMNISTを訓練データとして識別を行う。-->
訓練には、フォントXにノイズを載せたり変形したりして水増ししたデータを用いる。



### Workflow
研究計画についてガントチャートを用いて説明する。
#### 例
研究計画を以下に示す。

### jetson xavier
xavierを使う事とその理由について説明する。文字数が足りなければ。

## CHAPTER 4 – RESULTS
### Preliminary Results
実験結果について考察する。

### Evaluatoin
画像処理が精度向上にもたらした事を確かめる。

### Expected Results
期待される結果について考察する

## CHAPTER 5- CONCLUSION

### REFERENCES 

## 概要
研究の概要を1ページ程度に短く記す
### 例
提案手法xxを行って電柱のラベル検出を行ったところ精度はOOになった。

電柱に書いてある文字を認識するためには、曲面状にあるが故の歪みを画像処理によってできるだけ取り除く必要がある。
Iとlのような似たような文字をどうするかも問題である。

## 研究の目的
研究を定義する
何が達せられれば研究目的を達成したのかを定義する。
### 例
深層学習を利用して曲面状にある文字を認識する。
## 問題提起
目的を達成する上で直面する課題についての認識を共有する。

## 研究の説明
提案手法の実現方法を示す

### 例
どのようにすれば認識させることができるか?
- ラベル領域の切り出し
- 文字の認識

## 考察
提案手法が妥当である事を実験結果から導出する。

## 結論


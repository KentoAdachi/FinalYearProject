## 卒論について
### 提出期限
12月14日
### 分量
20ページ程度
### 参考

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
    1. Optical character recognition
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
現実世界における文字認識の用途は大まかに2種類に分類できる。一つ目は、紙媒体書類の電子化である。もう一つは、看板などのおもに人間向けに設計された標識の読み取りである。
一般物体上の文字の認識は形状や向き、周りの物体に左右され、認識精度は依然として実用化には程遠い。本研究の目的は、これらの文字認識精度の向上である。
#### 英訳
Automation technology is a big topic for us.
In recent years, with the development of AI technology, we can solve various tasks.
Especially character recognition is expected to be applied in various fields from data input to automatic driving, it is strongly desired to improve character recognition accuracy.
The applications of character recognition in the real world can roughly be classified into two types.
The first is digitization of documents.
The other is recognizing signs designed for people, such as billboards.
Recognition of characters on general objects depends on shape, rotation, objects around them, recognition accuracy is still far from practical use.
The purpose of this research is to improve these character recognition accuracy.

### Problem Statement
研究で取り組む課題は何かを説明する。
#### 例
本研究では、物体上、特に円柱上にある文字を認識することを考える。近年の研究では、おもに深層学習を利用したものが主流であり、本研究でも深層学習を利用して文字認識を行う。
#### 英訳
In this research, we recognize characters on objects, especially on cylinder. Recent studies mainly use deep learning, and this research also uses deep learning to do character recognition.

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

また、機械学習は大きなリソースを必要とする。そのため、GPUやCPUのパワーがあるデスクトップPCで行う事が多いが、本研究では、最終的にリアルタイムの検出を目指すために、Nvidia Jetson Xavierを使用する。

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

### Optical character recognition
文字認識の概略について示す。
#### 例
光学文字認識は、画像上にある文字を認識し、文字データに変換する事である。従来の画像認識は認識対象画像とフォント画像とのビット差分比較を行うテンプレートマッチングによって行われてきた。この方法では、画像の傾きや回転に弱く、スキャナーでスキャンされた画像に対しては高い精度を示すが、写真から文字を認識するには至らなかった。近年の研究によって、機械学習を使う事で従来よりも高い精度を得られる事が示された。そこで、我々は機械学習の一種である深層学習を利用して写真内にある文字列に対しての認識を目指す。
#### 英訳
ここに英訳を記述

### 物体検出
物体検出の概略について示す。
#### 例
物体検出は画像を取り込み、画像の中から定められた物体の位置とカテゴリ(クラス)を検出することである。
下図のように、画像の中からバウンディングボックスと呼ばれる矩形の位置とそのカテゴリを識別します。
図_X
#### 英訳
Clasification + localization = object detection


 

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
中間結果について報告する

### Expected Results
期待される結果について考察する

## CHAPTER 5- CONCLUSION
レポートの結論(提案が可能でありそうだみたいな事?)を示す
### REFERENCES 
参照

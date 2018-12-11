## 卒論について
### 提出期限
12月14日
### 分量
20ページ程度


## タイトル
TEXT DETECTION ON THE POLE

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
深層学習を利用し円柱曲面状にある文字列を認識する精度を上げる。
強力な組み込みGPUであるNvidia Jetsonによってクライアント側でのMachine Learningを行う。

#### 英訳
1. Increase the accuracy of recognizing character strings in a cylindrical curved surface using deep learning.
1. To use powerful built-in GPU Nvidia Jetson Xavier to develop deep learning on the client side.

### Scope of study
本研究の取り扱う範囲について記述する。
#### 例
本研究では、画像認識に機械学習フレームワークであるdarknetとYOLOというネットワークを利用する。
YOLOは、現在の一般物体検出においてFaster R-CNNと並んで高い精度を示しており、Faster R-CNNより処理速度に優れるのが特徴である。

また、機械学習は大きなリソースを必要とする。そのため、GPUやCPUのパワーがあるデスクトップPCで行う事が多いが、本研究では、最終的にリアルタイムの検出を目指すために、Nvidia Jetson Xavierを使用する。

#### 英訳
In this research, we use darknet machine learning framework　and YOLO algorithm for image recognition.
YOLO shows high accuracy as well as Faster R-CNN in object detection and much faster.

Machine learning also requires large resources. Therefore, it is often done with desktop PC with GPU and CPU power,in this research, Nvidia Jetson Xavier is used for real time detection.

<!-- 
①物体領域候補の提案
②検出物体のクラス分類
③領域の調整（回帰）
-->
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
Optical character recognition is to recognize characters on an image and convert them into character data. Conventional image recognition has been performed by template matching for comparing bit differences between recognition target images and font images. This method is weak against the inclination and rotation of the image. It shows high accuracy for the image scanned by the scanner, but recognition of characters from the photograph is far from practical use. Recent studies have shown that using machine learning can achieve higher accuracy than this. Therefore, we aim at recognition of character strings in photos using deep learning which is a type of machine learning.

### 物体検出
物体検出の概略について示す。
#### 例
物体検出は画像を取り込み、画像の中から定められた物体の位置とカテゴリ(クラス)を検出することである。
下図のように、画像の中からバウンディングボックスと呼ばれる矩形の位置とそのカテゴリを識別します。

初学者向けの画像認識の実装例に「手書き文字の認識」があるが、現実の画像においては、物体が1つであるとは限らない。そこで、1枚の画像の中で様々なサイズで写っている複数の物体を上手く切り出すバウンディングボックスを探す。それをクラス分類の問題にする必要がある。

図_X
#### 英訳
Object detection is to capture an image and detect the position and category (class) of the object determined from the image.
As shown in the figure below, we identify the position of the rectangle called the bounding box and its category from the image.

There is "handwritten characters recognition" in the implementation example of image recognition, but in actual images, there is not always only one object. Normaly, we have to find the various sized of bounding boxes in one image. After that, we can Clasify each images.

### YOLO
YOLOについて説明する
#### 例
YOLOは2016年に発表されたリアルタイム物体検出アルゴリズムである。
既存の画像検出のアルゴリズムである「DPM」や「R-CNN」は、画像の領域推定と分類が分断されており、それゆえ処理が複雑であり、かつ処理時間も長くなりがちであった。 「YOLO」では、画像検出を回帰問題に落とし込み、「画像の領域推定」と「分類」を同時に行うことを実現した。 「YOLO」のアルゴリズムは１つのCNNで完結するためシンプルであり、また既存の手法と比較して処理が早く、背景の誤検出が少ないなどのメリットを得ることができる。
#### 英訳
YOLO is a real-time object detection algorithm, which was announced in 2016.
Regarding existing image detection algorithms such as "DPM" and "R - CNN", region estimation and classification of images are separated, and therefore processing tends to be complicated and processing time tends to be long. In "YOLO", we perform that "image area estimation" and "classification" at the same time. The algorithm of "YOLO" is simple because it is completed with one CNN, and it has merits such as quick processing as compared with the existing method, less background error detection.

### R-CNN, Fast R-CNN, Faster R-CNN
Faster　R-CNNについて説明する。
#### 例
R-CNNは画像全体から特徴を抽出するCNNを元に考案された。それはRegion毎の特徴を検出可能であり、人間の行う認識に近い。
R-CNNではまず、入力画像からregion proposalを抽出する。そして、proposed regionに対して認識を行う。
Fast R-CNNはCNN　Detectorの実行回数を減らすためにモデルを改善したものである。
Faster R-CNNはFaster R-CNNでボトルネック出会ったRegion Proposalを改善したものである。

似た特徴を持った小さい領域を統合させていくことで、物体が存在しそうな領域に当たりをつけるSelective Search(選択的検索法)という手法が用いられた。


### SSD
SSDについて説明する。
#### 例


### 画像認識に関する論文X
前例を洗ってこれを分析する。

## CHAPTER 3 - METHODOLOGY
提案手法について説明する。
### Overview
概要を図にして示す。
#### 例
概要を図_Xに示す。我々の提案手法は3つのプロセスに分けられる。写真からラベルを抽出するプロセス、切り出した画像に対して何らかの画像処理を行うプロセス、出力された画像に対して認識を行うプロセスである。
#### 英訳
The overview is shown in Figure below. Our proposed method can be divirded into three processes.
A process of extracting a label from a photograph, a process of image processing on the cut of image, and a process of 
zing the output.


### Find label from picture
写真からラベルを抽出するプロセスについて説明する
#### 例
文字を認識する前に、写真から認識したい文字列を含むラベル領域を切り出す。こうすることで文字の謝検出の抑制と計算量の軽減に繋がる。
ラベル領域の検出には前途の通りYOLOを利用する。
まず、何も情報が付加されていない写真にラベリングを行う。
ラベリングとは、もともとあるデータに対して、画像内に含まれるクラスやその座標といった付加情報を与える事であり、機械学習はこのアノテーションデータを元に学習をしていく。訓練用のデータには車載カメラから撮影された街灯の写真を用いる。
YOLOのアノテーションデータの構造は単純で、{カテゴリ番号 オブジェクトの中心ｘ座標 オブジェクトの中心ｙ座標 オブジェクトの幅 オブジェクトの高さ}で表現される。
直接ファイルを編集するのは大変なのでラベリングには、ラベリング用の入力支援ツールを使う事で、作業を視覚的に行うことができる。
我々は、大量の写真に手作業でラベリングを行った。
#### 英訳
Before recognizing characters, we extract the label region including character strings to be recognized from the photograph. By doing this, it is possible to suppress the detection of metabolism of characters and to reduce the calculation amount.
To detect the label area, use YOLO as before.
First of all, we do labeling on a plain picture.
Labeling is to give additional information such as classes and their coordinates included in images to original data, and machine learning learns based on this annotation data. For training data, we use photographs of streetlight poles shot from in-vehicle camera.
The structure of YOLO's annotation data is simple and is expressed as {height of width object of center y coordinate object of center x coordinate object of category number object}.
Since it is hard to edit the file directly, it is possible to visually perform the work by using the input support tool for labeling for labeling.
We manually labeled a large number of photographs.


### Image prosessing
切り出したラベルに対して画像処理を行うプロセスについて説明する。
#### 例
従来の画像認識技術は、たいらな平面状の画像に対して認識を想定しており、歪んだ画像をそのまま認識に使うと高い精度を得られない。したがって、切り出されたラベルを平面に展開する必要がある。
曲面状の画像を平面に変形するには以下の方法を提案する。
1. まず、YOLOを利用して街灯を検出する
1. 次に、検出した街灯のx方向の大きさを直径と定義する。
1. ポールの形状がわかったので射影を求め平面に展開する
以上によって平面の画像を得る

#### 英訳
Ordinary, image recognition technology is designed for a flatten image. If distorted images are used for recognition, high accuracy can not be obtained. Therefore, it is necessary to transform label to a flat surface.
To transform a curved surface image into a plane, use the following method.
1. First, detect the pole using YOLO
1. Next, the size of the x direction of the detected pole is defined as a diameter.
1. Calculate the projection of a cylinder

### Label recognition
平面に展開された画像に対して認識を行うプロセスについて説明する。
#### 例
平面に展開された画像に対して認識を行う。認識のプロセスを以下に示す。
YOLOを用いてアルファベットa-zA-Zの52クラスの物体検知を行う。
訓練には、フォントXにノイズを載せたり変形したりして水増ししたデータを用いる。
#### 英訳
Recognize characters from flatten image. The recognition process is shown below.
We perform object detection of 52 classes of alphabet a - z A - Z using YOLO.
For training, use padded font data by placing noise on the image or deforming it.

### Data Augmentation
#### 例
深層学習には、大量の訓練用データが必要である。そこで近年の深層学習[要出典]では、もともとあるデータにガウシアンノイズを乗せたり、コントラストを調整したり、明るさを調整したり、平滑化を行ったり、拡大縮小や回転を行ったり、反転したりと行った処理を組み合わせる事で、データを水増しする。
データ拡張を行う事で、少ないデータで高い精度の認識を可能にする。

#### 英訳
A large amount of training data is necessary for deep learning. Therefore, in deep learning in recent years, researchers performed Gaussian noise on original data, adjust contrast, adjust brightness, perform smoothing, expand / shrink / rotate, invert by combining processing to augment the data.
By applying data augmentation, it is possible to recognize with high accuracy with less data.

### Workflow
研究計画についてガントチャートを用いて説明する。
#### 例
研究計画を以下に示す。
1. FYP Proposal {Sept - Dec}
1. Literature Review {Sept, Oct}
1. Explore deep learning {Sept, Oct}
1. Explore object detection {Oct, Nov}
1. Data acquisition {Nov}
1. Design model {Nov, Dec}
1. Coding {Dec, Jan}
1. Result analysis {Feb, Mar}
1. Write Report {Mar, April, May}


### jetson 
xavierを使う事とその理由について説明する。文字数が足りなければ。
#### 例
Jetsonシリーズは、Nvidiaが開発する、ロボットやドローン、セキュリティカメラなど、比較的小型のモバイル機器に搭載できるAIコンピュータボードだ。
最新モデルのXavierは、512コアのVolta Tensor GPUを搭載して理論上従来のTX2の20倍の性能を獲得した。
#### 英訳
The Jetson series is an AI computer board that can be mounted on relatively small mobile devices such as robots, drone, security cameras developed by Nvidia.  The latest model "Jetson Xavier" has the 512 core Volta Tensor GPU and theoretically gained 20 times the performance of the conventional model TX 2.

## CHAPTER 4 – RESULTS
### Preliminary Results
中間結果について報告する
What we have done
#### 例
我々は、トレーニング用データとして、車載カメラから撮られた風景の画像から、手動で街灯とラベル領域をラベリングした。
街灯は、認識精度を分析するために、三種類の形の違う街灯をラベリングした。
ラベリングには、labelimgというソフトを使用した。ラベリングの例を図_Xに示す。
#### 英訳
We manually labeled streetlights and label areas from landscape images taken from the in-vehicle camera as training data.
In order to analyze the recognition accuracy, we labeled three different types of street lamp.
For labeling, we used software named labelimg.
An example of labeling is shown below.

### Expected Results
期待される結果について考察する
#### 例
期待される結果は、ロボットが現実世界で標識や看板を認識できるような精度の文字検出を実現することである。また、今回は円柱上の文字認識に限定したが、将来的には写真から3次元形状を予測して平面に展開する手法についても検討したい。
#### 英訳
The expected result is to realize character detection with high precision so that robots can recognize signs and signs in the real world. This time we limited it to character detection on a cylinder, but in the future we would like to consider a method to predict a three dimensional shape from a photograph and reshape it on a plane.



## CHAPTER 5- CONCLUSION
レポートの結論(提案が可能でありそうだみたいな事?)を示す
#### 例
我々は、深層学習を利用して写真から柱面上にある文字列を認識する手法を提案した。
深層学習には、今まで成し遂げられなかった課題を解決する力があり、今後も様々な分野で応用がされて行くだろう。
#### 英訳
We have proposed a method to recognize character strings on a cylinder surface from photographs using deep learning.
Deep learning has the power to solve the problems that we have not accomplished so far and will continue to be applied in various fields from now on.

### REFERENCES 
YOLO

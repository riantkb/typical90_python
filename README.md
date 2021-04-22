# Typical90 Python

このリポジトリは、riantkb の Python 練習も兼ねた [競プロ典型 90 問](https://atcoder.jp/contests/typical90) の提出コードをまとめたものです。



## A: 001 - Yokan Party（★4）

- [Problem Link](https://atcoder.jp/contests/typical90/tasks/typical90_a)
- [Tweet Link](https://twitter.com/e869120/status/1376665578513989633)

| Submission Language | Source Code | Submission | Verdict | Exec Time |
| :--- | :---: | :---: | :---: | ---: |
| Python (3.8.2) | [a.py](src/a.py) | [link](https://atcoder.jp/contests/typical90/submissions/21933908) | AC | 214 ms |
| PyPy3 (7.3.0) | [a.py](src/a.py) | [link](https://atcoder.jp/contests/typical90/submissions/21933929) | AC | 100 ms |
| Cython (0.29.16) | [a.py](src/a.py) | [link](https://atcoder.jp/contests/typical90/submissions/21933948) | AC | 159 ms |


### Memo
- 特になし
- 1 問目なので無駄に PyPy と Cython でも同じコードを提出してみた。
  - PyPy はやはり雑に速くなる。
  - Cython も、この使い方だと本来の力の 3 割くらいも出せていなさそうだけどちょっと速くなる。
- `bisect` に key として関数を渡せたら面白そうとも思ったけどできなさそうだった。



## B: 002 - Encyclopedia of Parentheses（★3）

- [Problem Link](https://atcoder.jp/contests/typical90/tasks/typical90_b)
- [Tweet Link](https://twitter.com/e869120/status/1377027868518064129)

| Submission Language | Source Code | Submission | Verdict | Exec Time |
| :--- | :---: | :---: | :---: | ---: |
| Python (3.8.2) | [b.py](src/b.py) | [link](https://atcoder.jp/contests/typical90/submissions/21934332) | AC | 99 ms |
| Python (3.8.2) | [b_bitslow.py](src/b_bitslow.py) | [link](https://atcoder.jp/contests/typical90/submissions/21934351) | AC | 122 ms |


### Memo
- あまり御行儀はよくないが、最後まで潜ったタイミングで出力までやってしまうのが楽そう。
- ```py
  lis.append('(')
  rec(rem - 1, lis, dep + 1)
  lis[-1] = ')'
  rec(rem - 1, lis, dep - 1)
  lis.pop()
  ```
  の部分を
  ```py
  rec(rem - 1, lis + ['('], dep + 1)
  rec(rem - 1, lis + [')'], dep - 1)
  ```
  と書くこともできこちらの方がシンプル（そのように変更したのが [b_bitslow.py](src/b_bitslow.py)）だが、毎回リストのコピーが生成されるので若干遅くなる。



## C: 003 - Longest Circular Road（★4）

- [Problem Link](https://atcoder.jp/contests/typical90/tasks/typical90_c)
- [Tweet Link](https://twitter.com/e869120/status/1377391097836544001)

| Submission Language | Source Code | Submission | Verdict | Exec Time |
| :--- | :---: | :---: | :---: | ---: |
| Python (3.8.2) | [c.py](src/c.py) | [link](https://atcoder.jp/contests/typical90/submissions/21934691) | AC | 413 ms |
| PyPy3 (7.3.0) | [c.py](src/c.py) | [link](https://atcoder.jp/contests/typical90/submissions/21934844) | AC | 301 ms |


### Memo
- 木上のある点からの距離を求めるのに BFS を行っているが、ここで queue として `collections.deque` を使っている。
  - `queue.Queue` は存在するが、これはマルチスレッドに対応したキューであるため、シングルスレッドである場合は `collections.deque` を使う方が高速。
    - https://docs.python.org/ja/3/library/queue.html
- `max` や `sort` などの関数は key として関数を渡すことができ、それにより argmax や argsort に相当する処理をすることが可能。



## D: 004 - Cross Sum（★2）

- [Problem Link](https://atcoder.jp/contests/typical90/tasks/typical90_d)
- [Tweet Link](https://twitter.com/e869120/status/1377752658149175299)

| Submission Language | Source Code | Submission | Verdict | Exec Time |
| :--- | :---: | :---: | :---: | ---: |
| Python (3.8.2) | [d.py](src/d.py) | [link](https://atcoder.jp/contests/typical90/submissions/21935444) | AC | 1,975 ms |
| PyPy3 (7.3.0) | [d.py](src/d.py) | [link](https://atcoder.jp/contests/typical90/submissions/21935454) | AC | 833 ms |
| Cython (0.29.16) | [d.py](src/d.py) | [link](https://atcoder.jp/contests/typical90/submissions/21935466) | AC | 1,701 ms |


### Memo
- なんで通るのかよくわからない、少し書き方を変えると TLE したりする。
- `sys.stdin.readline` を使ってみたり Numba + NumPy でも書いてみたりしたが速くはならなかった。
- [気まぐれでこんなコードを書いてみたりもした（なんの意味が？）](src/d_evil.py)



## E: 005 - Restricted Digits（★7）

- [Problem Link](https://atcoder.jp/contests/typical90/tasks/typical90_e)
- [Tweet Link](https://twitter.com/e869120/status/1378115289649348611)

| Submission Language | Source Code | Submission | Verdict | Exec Time | Description |
| :--- | :---: | :---: | :---: | ---: | :---: |
| Python (3.8.2) | [e_simple.py](src/e_simple.py) | [link](https://atcoder.jp/contests/typical90/submissions/21935912) | TLE | > 5,000 ms | |
| PyPy3 (7.3.0) | [e_simple.py](src/e_simple.py) | [link](https://atcoder.jp/contests/typical90/submissions/21935923) | AC | 1,698 ms | |
| Python (3.8.2) | [e_numpy.py](src/e_numpy.py) | [link](https://atcoder.jp/contests/typical90/submissions/21936110) | AC | 1,778 ms | Using NumPy |
| Python (3.8.2) | [e.py](src/e.py) | [link](https://atcoder.jp/contests/typical90/submissions/21935944) | AC | 721 ms | Using Numba, NumPy |


### Memo
- [e_simple.py](src/e_simple.py) だと PyPy では通るが Python だと通らない。
  - simple と言いつつ `mul` 関数内は `B` が長さ 2 倍になっていたり mod を取るタイミングが調整されていたりするが……。
- `mul` 関数内の処理を NumPy でまとめると Python でも通るようになる ([e_numpy.py](src/e_numpy.py))。
- Numba を用いて JIT コンパイルを行うことで、700 ms 程度で通るようになる ([e.py](src/e.py))。
  - AtCoder の環境では、他の言語がコンパイルするタイミングで代わりに一度入力を何も与えない状態で実行してくれるため、型を指定しかつ `cache=True` とすることで、JIT コンパイルの時間を実行時間に含めないようにすることが可能。



## F: 006 - Smallest Subsequence（★5）

- [Problem Link](https://atcoder.jp/contests/typical90/tasks/typical90_f)
- [Tweet Link](https://twitter.com/e869120/status/1378840212449595393)

| Submission Language | Source Code | Submission | Verdict | Exec Time |
| :--- | :---: | :---: | :---: | ---: |
| Python (3.8.2) | [f.py](src/f.py) | [link](https://atcoder.jp/contests/typical90/submissions/21936433) | AC | 79 ms |


### Memo
- 特になし



## G: 007 - CP Classes（★3）

- [Problem Link](https://atcoder.jp/contests/typical90/tasks/typical90_g)
- [Tweet Link](https://twitter.com/e869120/status/1379202843622576130)

| Submission Language | Source Code | Submission | Verdict | Exec Time | Description |
| :--- | :---: | :---: | :---: | ---: | :---: |
| Python (3.8.2) | [g.py](src/g.py) | [link](https://atcoder.jp/contests/typical90/submissions/21947425) | AC | 866 ms | `bisect.bisect` |
| PyPy3 (7.3.0) | [g.py](src/g.py) | [link](https://atcoder.jp/contests/typical90/submissions/21947931) | AC | 647 ms | `bisect.bisect` |
| Python (3.8.2) | [g_2.py](src/g_2.py) | [link](https://atcoder.jp/contests/typical90/submissions/21947593) | AC | 983 ms | ソートしてからしゃくとり法 |
| PyPy3 (7.3.0) | [g_2.py](src/g_2.py) | [link](https://atcoder.jp/contests/typical90/submissions/21947970) | AC | 886 ms | ソートしてからしゃくとり法 |
| Python (3.8.2) | [g_numpy.py](src/g_numpy.py) | [link](https://atcoder.jp/contests/typical90/submissions/21947265) | AC | 1,137 ms | `numpy.searchsorted` |


### Memo
- C++ の `lower_bound` に対応するのが `bisect.bisect_left`、`upper_bound` に対応するのが `bisect.bisect_right`。
  - `bisect.bisect` は `bisect.bisect_right` のエイリアス
- a の両端に番兵を設置すると、`a[i-1]` や `a[i]` が配列外参照にならずに済み条件分岐を省くことができる。
  - 番兵との距離が最短になってしまうと間違った答えを出力してしまうので注意。
- `bisect.bisect` を N 回呼ぶより最初にソートしてしゃくとりをした方が速いかと思ったが、実際には遅くなった ([g_2.py](src/g_2.py))。
- NumPy にも `bisect` と同等の `numpy.searchsorted` という関数があり、こちらはクエリとして `ndarray` を渡すこともできる。
  - 同時に Numba によるコンパイルも行ってみたが、元の NumPy を用いないコードより遅くなった ([g_numpy.py](src/g_numpy.py))。
    - まぁ `ndarray` の中身を for ループで回しているのはあまりよくなさそう。



## H: 008 - AtCounter（★4）

- [Problem Link](https://atcoder.jp/contests/typical90/tasks/typical90_h)
- [Tweet Link](https://twitter.com/e869120/status/1379565222541680644)

| Submission Language | Source Code | Submission | Verdict | Exec Time |
| :--- | :---: | :---: | :---: | ---: |
| Python (3.8.2) | [h.py](src/h.py) | [link](https://atcoder.jp/contests/typical90/submissions/21948343) | AC | 44 ms |


### Memo
- 特になし
- 内包表記はリストだけではなく dict や set なども作ることが出来る。



## I: 009 - Three Point Angle（★6）

- [Problem Link](https://atcoder.jp/contests/typical90/tasks/typical90_i)
- [Tweet Link](https://twitter.com/e869120/status/1379927227739987972)

| Submission Language | Source Code | Submission | Verdict | Exec Time | Description |
| :--- | :---: | :---: | :---: | ---: | :---: |
| Python (3.8.2) | [i.py](src/i.py) | [link](https://atcoder.jp/contests/typical90/submissions/21956211) | AC | 2,286 ms | |
| PyPy3 (7.3.0) | [i.py](src/i.py) | [link](https://atcoder.jp/contests/typical90/submissions/21956735) | AC | 920 ms | |
| Python (3.8.2) | [i_numpy.py](src/i_numpy.py) | [link](https://atcoder.jp/contests/typical90/submissions/21956672) | AC | 1,128 ms | Using Numba, Numpy |


### Memo
- 二次元平面上の距離、角度等を求めたいときは複素数 `complex` を用いると楽なことがある。
- 番兵を置いたりしているところは G 問題と同様
- `cmath.phase` や `numpy.angle` でなす角（atan2 に相当）を求めることができる。
  - これを用いると偏角ソートができるが、計算誤差の関係で非常に大きさの近い 2 つの角度を正確に比較できないことに注意。

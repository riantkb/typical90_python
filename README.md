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

| Submission Language | Source Code | Submission | Verdict | Exec Time | Description |
| :--- | :---: | :---: | :---: | ---: | :---: |
| Python (3.8.2) | [d.py](src/d.py) | [link](https://atcoder.jp/contests/typical90/submissions/21935444) | AC | 1,975 ms | |
| PyPy3 (7.3.0) | [d.py](src/d.py) | [link](https://atcoder.jp/contests/typical90/submissions/21935454) | AC | 833 ms | |
| Cython (0.29.16) | [d.py](src/d.py) | [link](https://atcoder.jp/contests/typical90/submissions/21935466) | AC | 1,701 ms | |
| Python (3.8.2) | [d_aot.py](src/d_aot.py) | [link](https://atcoder.jp/contests/typical90/submissions/23135463) | AC | 1,537 ms | Using Numba AOT |


### Memo
- なんで通るのかよくわからない、少し書き方を変えると TLE したりする。
- `sys.stdin.readline` を使ってみたり Numba + NumPy でも書いてみたりしたが速くはならなかった。
- Numba で AOT コンパイルすると 1,550 ms ほどで通った（[d_aot.py](src/d_aot.py)）。
  - JIT コンパイルでも一応 1,950 ms ほどで通った。差の 400 ms は基本的に numba の読み込み時間と思われる。
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



## J: 010 - Score Sum Queries（★2）

- [Problem Link](https://atcoder.jp/contests/typical90/tasks/typical90_j)
- [Tweet Link](https://twitter.com/e869120/status/1380290146340245505)

| Submission Language | Source Code | Submission | Verdict | Exec Time | Description |
| :--- | :---: | :---: | :---: | ---: | :---: |
| Python (3.8.2) | [j.py](src/j.py) | [link](https://atcoder.jp/contests/typical90/submissions/21972607) | AC | 632 ms | |
| Python (3.8.2) | [j_stdin.py](src/j_stdin.py) | [link](https://atcoder.jp/contests/typical90/submissions/21974272) | AC | 256 ms | Using `sys.stdin.readline` |


### Memo
- `itertools.accumulate` で累積和が計算できる。
  - 適用する関数を指定することで累積積や累積 XOR なども計算可能。
- 入力が多い場合は、`input` の代わりに `sys.stdin.readline` を使用することで高速になることがある。
  - `sys.stdin.readline` の場合、行末の改行も含んだ文字列を返すことに注意。
    - 整数型に変換する際は読み飛ばしてくれるので問題ないが、文字列として処理する際は意図しない挙動になる可能性がある。
  - `s = sys.stdin.readline().strip()` などというように `strip` 関数を用いることで除去できる。



## K: 011 - Gravy Jobs（★6）

- [Problem Link](https://atcoder.jp/contests/typical90/tasks/typical90_k)
- [Tweet Link](https://twitter.com/e869120/status/1380652465834532865)

| Submission Language | Source Code | Submission | Verdict | Exec Time | Description |
| :--- | :---: | :---: | :---: | ---: | :---: |
| Python (3.8.2) | [k_naive.py](src/k_naive.py) | [link](https://atcoder.jp/contests/typical90/submissions/22099338) | TLE | > 2,000 ms | |
| Python (3.8.2) | [k.py](src/k.py) | [link](https://atcoder.jp/contests/typical90/submissions/22099396) | AC | 161 ms | Using NumPy |


### Memo
- 単純な DP だが、普通に書くと TLE する（[k_naive.py](src/k_naive.py)）。
- NumPy を使うと区間代入みたいなことができる（計算量自体は長さ分かかるが、定数倍がかなり軽い）ので、それをするとかなり速くなる（[k.py](src/k.py)）。
- Numba を用いてコンパイル（JIT キャッシュあり）もしてみたが、かなり遅くなった（530 ms ほどになった）。
  - `import numba` で Numba を読み込むのに 400 ms 近くかかるのが原因と思われる。



## L: 012 - Red Painting（★4）

- [Problem Link](https://atcoder.jp/contests/typical90/tasks/typical90_l)
- [Tweet Link](https://twitter.com/e869120/status/1381376542836596737)

| Submission Language | Source Code | Submission | Verdict | Exec Time | Description |
| :--- | :---: | :---: | :---: | ---: | :---: |
| Python (3.8.2) | [l.py](src/l.py) | [link](https://atcoder.jp/contests/typical90/submissions/22099849) | AC | 482 ms |  |
| Python (3.8.2) | [l_jitclass.py](src/l_jitclass.py) | [link](https://atcoder.jp/contests/typical90/submissions/23136535) | AC | 559 ms | Using `numba.jitclass` |
| Python (3.8.2) | [l_aot.py](src/l_aot.py) | [link](https://atcoder.jp/contests/typical90/submissions/23136675) | AC | 179 ms | Using Numba AOT |


### Memo
- Numba では class も JIT コンパイルすることができる（[l_jitclass.py](src/l_jitclass.py)）。
  - `jitclass` のある位置が Numba のバージョンにより異なるので注意（AtCoder のジャッジ (0.48.0) では `numba.jitclass`、手元 (0.53.1) では `numba.experimental.jitclass`）。
  - cache オプションがないためコンパイルの時間も計算時間に含まれてしまい、また Numba の読み込み時間もかかるため今回は普通に書くより遅くなる。
- AOT（事前コンパイル）ならば jitclass でも関係なく使える。Numba の読み込み時間も削れるためかなり高速になる（[l_aot.py](src/l_aot.py)）。
  - https://numba.pydata.org/numba-doc/dev/user/pycc.html



## M: 013 - Passing（★5）

- [Problem Link](https://atcoder.jp/contests/typical90/tasks/typical90_m)
- [Tweet Link](https://twitter.com/e869120/status/1381739128291614720)

| Submission Language | Source Code | Submission | Verdict | Exec Time | Description |
| :--- | :---: | :---: | :---: | ---: | :---: |
| Python (3.8.2) | [m.py](src/m.py) | [link](https://atcoder.jp/contests/typical90/submissions/22132326) | AC | 795 ms |  |
| Python (3.8.2) | [m_scipy.py](src/m_scipy.py) | [link](https://atcoder.jp/contests/typical90/submissions/22131824) | TLE | > 2,000 ms | Using SciPy |


### Memo
- 優先度つきキューは `heapq` のメソッドで実現できる。
  - `queue.PriorityQueue` も存在するが、C 問題で触れた `Queue` と同様にマルチスレッド対応なので `heapq` の方が高速（なはず）。
- SciPy にいくつかのグラフアルゴリズムが実装されており `dijkstra` も存在するが、TLE した（[m_scipy.py](src/m_scipy.py)）。
  - コストの計算に float64 を用いている（変更不可）ことが原因？



## N: 014 - We Used to Sing a Song Together（★3）

- [Problem Link](https://atcoder.jp/contests/typical90/tasks/typical90_n)
- [Tweet Link](https://twitter.com/e869120/status/1382101716066127872)

| Submission Language | Source Code | Submission | Verdict | Exec Time |
| :--- | :---: | :---: | :---: | ---: |
| Python (3.8.2) | [n.py](src/n.py) | [link](https://atcoder.jp/contests/typical90/submissions/22132880) | AC | 117 ms |


### Memo
- 特になし
- 二次元リストを転置するのは `a = [ list(i) for i in zip(*a) ]` でできる。



## O: 015 - Don't be too close（★6）

- [Problem Link](https://atcoder.jp/contests/typical90/tasks/typical90_o)
- [Tweet Link](https://twitter.com/e869120/status/1382478816627478530)

| Submission Language | Source Code | Submission | Verdict | Exec Time |
| :--- | :---: | :---: | :---: | ---: |
| Python (3.8.2) | [o.py](src/o.py) | [link](https://atcoder.jp/contests/typical90/submissions/22524857) | AC | 863 ms |
| Python (3.8.2) | [o_2.py](src/o_2.py) | [link](https://atcoder.jp/contests/typical90/submissions/22524871) | AC | 741 ms |


### Memo
- 階乗テーブルを計算するときも `itertools.accumulate` が使える。
  - 普通に for 文で回すのとほとんど実行時間に変化はなかった……。
- main の内側の for ループを無理矢理内包表記にすると若干速くなる（[o_2.py](src/o_2.py)）。



## P: 016 - Minimum Coins（★3）

- [Problem Link](https://atcoder.jp/contests/typical90/tasks/typical90_p)
- [Tweet Link](https://twitter.com/e869120/status/1382827276673306624)

| Submission Language | Source Code | Submission | Verdict | Exec Time |
| :--- | :---: | :---: | :---: | ---: |
| Python (3.8.2) | [p.py](src/p.py) | [link](https://atcoder.jp/contests/typical90/submissions/22512078) | TLE | > 2,000 ms |
| PyPy3 (7.3.0) | [p.py](src/p.py) | [link](https://atcoder.jp/contests/typical90/submissions/22512082) | AC | 1,247 ms |
| Python (3.8.2) | [p_fast.py](src/p_fast.py) | [link](https://atcoder.jp/contests/typical90/submissions/22512784) | AC | 32 ms |


### Memo
- 以下、 `M = 10000（枚数の上限）, X = max(A, B, C)` とする
- 想定解の `O(M^2)` は当然（？）Python では通らない。
  - PyPy では通る。
- この問題にはより高速な解法が存在するので、そちらで AC することにする。
  - 拡張ユークリッドの互除法を用いることにより、例えば「A 円硬貨, B 円硬貨の 2 種類の硬貨でちょうど N 円を支払うとき、あり得る支払い方のうち B 円硬貨の枚数が最少であるものを求めよ」という問題に高速に答えられる。
  - なので、A 円硬貨の枚数を決め打ちした上で、B 円硬貨、C 円硬貨に対し上の問題を解くことで元の問題の解答が得られる（B > C としておけば、C 円硬貨の枚数が最少であるものが B 円硬貨と C 円硬貨の枚数の合計も最少であることが保証できる）。
  - 拡張ユークリッドの互除法は B, C に対するものを一度だけ行えばよいので、計算量は `O(M + log X)` となる。
  - 提出してみると 32 ms、かなり速い（[p_fast.py](src/p_fast.py)）。



## Q: 017 - Crossing Segments（★7）

- [Problem Link](https://atcoder.jp/contests/typical90/tasks/typical90_q)
- [Tweet Link](https://twitter.com/e869120/status/1383189464650981378)

| Submission Language | Source Code | Submission | Verdict | Exec Time | Description |
| :--- | :---: | :---: | :---: | ---: | :---: |
| Python (3.8.2) | [q.py](src/q.py) | [link](https://atcoder.jp/contests/typical90/submissions/22522427) | TLE | > 2,000 ms | |
| PyPy3 (7.3.0) | [q.py](src/q.py) | [link](https://atcoder.jp/contests/typical90/submissions/22526684) | AC | 1,239 ms | |
| Python (3.8.2) | [q_numba.py](src/q_numba.py) | [link](https://atcoder.jp/contests/typical90/submissions/22523343) | AC | 1,716 ms | Using Numba |
| Python (3.8.2) | [q_jitclass.py](src/q_jitclass.py) | [link](https://atcoder.jp/contests/typical90/submissions/23138005) | AC | 1,800 ms | Using `numba.jitclass` |
| Python (3.8.2) | [q_aot.py](src/q_aot.py) | [link](https://atcoder.jp/contests/typical90/submissions/23138014) | AC | 1,230 ms | Using Numba AOT |


### Memo
- 公式解説と若干異なる解き方をした。
  - L の小さい順（L が等しい場合は R の大きい順）に見ることで、「 `[L+1, R)` に R が入るような要素」が自分より前に見た要素の中で自分と交わるものなので、その個数を求めればよい。
- 普通に書くと Python では TLE する（[q.py](src/q.py)）ため、Numba を用いてコンパイルした。
  - BIT の中身をバラすと 1,700 ms ほど（[q_numba.py](src/q_numba.py)）、そのまま `jitclass` で実行時コンパイルしても 1,800 ms ほどで通った（[q_jitclass.py](src/q_jitclass.py)）。
    - BIT の class の中身がそこまで大きくないのでコンパイルにそこまで時間がかからなかった？
  - AOT（事前コンパイル）ならば jitclass でも関係なく使える。Numba の読み込み時間も削れるため高速になる（[q_aot.py](src/q_aot.py)）。
    - https://numba.pydata.org/numba-doc/dev/user/pycc.html



## R: 018 - Statue of Chokudai（★3）

- [Problem Link](https://atcoder.jp/contests/typical90/tasks/typical90_r)
- [Tweet Link](https://twitter.com/e869120/status/1383913627325853696)

| Submission Language | Source Code | Submission | Verdict | Exec Time |
| :--- | :---: | :---: | :---: | ---: |
| Python (3.8.2) | [r.py](src/r.py) | [link](https://atcoder.jp/contests/typical90/submissions/22546722) | AC | 27 ms |


### Memo
- 特になし
- `math.hypot` は引数の二乗和の平方根を取る関数、べつに自分で計算してもよい。
  - https://docs.python.org/ja/3/library/math.html#math.hypot
- `math.degrees` は引数をラジアンから度数法に変換したものを返す関数、べつに自分で計算してもよい。



## S: 019 - Pick Two（★6）

- [Problem Link](https://atcoder.jp/contests/typical90/tasks/typical90_s)
- [Tweet Link](https://twitter.com/e869120/status/1384276005330690049)

| Submission Language | Source Code | Submission | Verdict | Exec Time | Description |
| :--- | :---: | :---: | :---: | ---: | :---: |
| Python (3.8.2) | [s.py](src/s.py) | [link](https://atcoder.jp/contests/typical90/submissions/22546996) | AC | 713 ms | |
| Python (3.8.2) | [s_numpy.py](src/s_numpy.py) | [link](https://atcoder.jp/contests/typical90/submissions/22546963) | AC | 401 ms | Using NumPy |
| Python (3.8.2) | [s_cache.py](src/s_cache.py) | [link](https://atcoder.jp/contests/typical90/submissions/22547101) | AC | 1,430 ms | メモ化再帰 |
| Python (3.8.2) | [s_cache_2.py](src/s_cache_2.py) | [link](https://atcoder.jp/contests/typical90/submissions/22547107) | AC | 1,089 ms | Using `functools.lru_cache` |


### Memo
- 一見 `400 ** 3` の区間 DP なので、適当にやると TLE しがち
  - よく見ると区間の長さが偶数であるものしか考えなくてよいので定数倍が 1/4 ほどになり、愚直に Python で実装しても余裕を持って通るようになる（[s.py](src/s.py)）。
- DP の遷移が、いくつかの一次元配列を要素ごとに和をとったものの min、というような形になっているので、Numpy で内側のループを消してあげると少し高速になる（[s_numpy.py](src/s_numpy.py)）。
- メモ化再帰でも実装してみる。普通にメモ用の配列を用意して実装すると 1,400 ms ほど（[s_cache.py](src/s_cache.py)）。
  - `functools.lru_cache` を用いると自動でメモ化を行ってくれて、それを用いると 1,100 ms ほどになった（[s_cache_2.py](src/s_cache_2.py)）。
    - 思ったより速い。これは引数はハッシュ関数さえ定義されていればなんでもメモ化できることもありかなり良さそう。



## T: 020 - Log Inequality（★3）

- [Problem Link](https://atcoder.jp/contests/typical90/tasks/typical90_t)
- [Tweet Link](https://twitter.com/e869120/status/1384638694162780166)

| Submission Language | Source Code | Submission | Verdict | Exec Time |
| :--- | :---: | :---: | :---: | ---: |
| Python (3.8.2) | [t.py](src/t.py) | [link](https://atcoder.jp/contests/typical90/submissions/22547123) | AC | 24 ms |


### Memo
- 特になし
- Python はオーバーフローをあまり気にせず計算できたり整数の累乗があったりしてうれしいね。



## U: 021 - Come Back in One Piece（★5）

- [Problem Link](https://atcoder.jp/contests/typical90/tasks/typical90_u)
- [Tweet Link](https://twitter.com/e869120/status/1385001057512693762)

| Submission Language | Source Code | Submission | Verdict | Exec Time | Description |
| :--- | :---: | :---: | :---: | ---: | :---: |
| Python (3.8.2) | [u.py](src/u.py) | [link](https://atcoder.jp/contests/typical90/submissions/22754869) | AC | 452 ms | Using SciPy |


### Memo
- 強連結成分分解をする問題。SciPy に連結成分分解をする関数が存在するのでそれが使える。
  - https://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.csgraph.connected_components.html



## V: 022 - Cubic Cake（★2）

- [Problem Link](https://atcoder.jp/contests/typical90/tasks/typical90_v)
- [Tweet Link](https://twitter.com/e869120/status/1385363292739104775)

| Submission Language | Source Code | Submission | Verdict | Exec Time |
| :--- | :---: | :---: | :---: | ---: |
| Python (3.8.2) | [v.py](src/v.py) | [link](https://atcoder.jp/contests/typical90/submissions/22754939) | AC | 29 ms |
| Python (3.8.2) | [v_reduce.py](src/v_reduce.py) | [link](https://atcoder.jp/contests/typical90/submissions/22754967) | AC | 37 ms |


### Memo
- 特になし
- `math.gcd` は 2 引数に対してのみ定義されているため、3 個以上の数の gcd を取りたい場合は `gcd(gcd(a, b), c)` などとするか、`functools.reduce` を使う必要がある。



## W: 023 - Avoid War（★7）

- [Problem Link](https://atcoder.jp/contests/typical90/tasks/typical90_w)
- [Tweet Link](https://twitter.com/e869120/status/1385725481920520193)

| Submission Language | Source Code | Submission | Verdict | Exec Time | Description |
| :--- | :---: | :---: | :---: | ---: | :---: |
| PyPy3 (7.3.0) | [w.py](src/w.py) | [link](https://atcoder.jp/contests/typical90/submissions/22756124) | AC | 6,068 ms | |
| Python (3.8.2) | [w_numba.py](src/w_numba.py) | [link](https://atcoder.jp/contests/typical90/submissions/22756564) | AC | 7,716 ms | Using Numba AOT |


### Memo
- かなりしんどい
- 左から k マス目からの連続する W+1 個のマスについての valid な置き方を列挙（これの通り数は `2**(W+1)` よりはずいぶん小さくなる）し、キングを 1 つ置く／置かないについての遷移先をあらかじめ求めておく。
  - 適当なことをするとすぐ計算量に `2**W` がかかってきて死ぬ。
- 当然このままだと Python (not PyPy) では通らないが、Numba で JIT コンパイルすると 8,200 ms くらいになるのが伺える。
  - AOT にして Numba の読み込み時間を削減してギリギリ AC（[w_numba.py](src/w_numba.py)）。



## X: 024 - Select +／- One（★2）

- [Problem Link](https://atcoder.jp/contests/typical90/tasks/typical90_x)
- [Tweet Link](https://twitter.com/e869120/status/1386449961072553990)

| Submission Language | Source Code | Submission | Verdict | Exec Time |
| :--- | :---: | :---: | :---: | ---: |
| Python (3.8.2) | [x.py](src/x.py) | [link](https://atcoder.jp/contests/typical90/submissions/23099171) | AC | 27 ms |


### Memo
- 特になし



## Y: 025 - Digit Product Equation（★7）

- [Problem Link](https://atcoder.jp/contests/typical90/tasks/typical90_y)
- [Tweet Link](https://twitter.com/e869120/status/1386814047081746432)

| Submission Language | Source Code | Submission | Verdict | Exec Time |
| :--- | :---: | :---: | :---: | ---: |
| Python (3.8.2) | [y.py](src/y.py) | [link](https://atcoder.jp/contests/typical90/submissions/23100157) | AC | 103 ms |


### Memo
- 解説とは違い `f(x)` を列挙する解法
- `f(x) = 2**a + 3**b + 5**c + 7**d  または  f(x) = 0` という形で表されるので、 `f(x)` は高々 `40 * 30 * 20 * 15` 通りくらい調べればよい（実際にはもっと少ない）。
- `f(x)` の列挙は、 `itertools.product` で複数リストの直積が生成できるのでこれが使える。
  - 実際には四重ループを回して適宜枝刈りした方が速いかもしれない。



## Z: 026 - Independent Set on a Tree（★4）

- [Problem Link](https://atcoder.jp/contests/typical90/tasks/typical90_z)
- [Tweet Link](https://twitter.com/e869120/status/1387175538544975872)

| Submission Language | Source Code | Submission | Verdict | Exec Time |
| :--- | :---: | :---: | :---: | ---: |
| Python (3.8.2) | [z.py](src/z.py) | [link](https://atcoder.jp/contests/typical90/submissions/23117813) | AC | 248 ms |


### Memo
- 特になし
- BFS の部分は C 問題のときとほぼ同じ。



## AA: 027 - Sign Up Requests （★2）

- [Problem Link](https://atcoder.jp/contests/typical90/tasks/typical90_aa)
- [Tweet Link](https://twitter.com/e869120/status/1387538790017769474)

| Submission Language | Source Code | Submission | Verdict | Exec Time |
| :--- | :---: | :---: | :---: | ---: |
| Python (3.8.2) | [aa.py](src/aa.py) | [link](https://atcoder.jp/contests/typical90/submissions/23118777) | AC | 96 ms |


### Memo
- 特になし
- 登場した文字列を set で管理すれば良い
  - dict でもよい



## AB: 028 - Cluttered Paper（★4）

- [Problem Link](https://atcoder.jp/contests/typical90/tasks/typical90_ab)
- [Tweet Link](https://twitter.com/e869120/status/1387901052683386880)

| Submission Language | Source Code | Submission | Verdict | Exec Time | Description |
| :--- | :---: | :---: | :---: | ---: | :---: |
| Python (3.8.2) | [ab.py](src/ab.py) | [link](https://atcoder.jp/contests/typical90/submissions/23119287) | AC | 507 ms | |
| Python (3.8.2) | [ab_counter.py](src/ab_counter.py) | [link](https://atcoder.jp/contests/typical90/submissions/23119737) | AC | 616 ms | Using `collections.Counter` |


### Memo
- 特になし
- 配列内の各要素の出現回数などは `collections.Counter` でも取得できる（[ab_counter.py](src/ab_counter.py)）。
  - 出力時に dict への添字アクセスをするので少し遅くなる。



## AC: 029 - Long Bricks（★5）

- [Problem Link](https://atcoder.jp/contests/typical90/tasks/typical90_ac)
- [Tweet Link](https://twitter.com/e869120/status/1388262816101007363)

| Submission Language | Source Code | Submission | Verdict | Exec Time | Description |
| :--- | :---: | :---: | :---: | ---: | :---: |
| Python (3.8.2) | [ac.py](src/ac.py) | [link](https://atcoder.jp/contests/typical90/submissions/23120242) | TLE | > 4,000 ms | |
| PyPy3 (7.3.0) | [ac.py](src/ac.py) | [link](https://atcoder.jp/contests/typical90/submissions/23120230) | AC | 1,058 ms | |
| Python (3.8.2) | [ac_numba.py](src/ac_numba.py) | [link](https://atcoder.jp/contests/typical90/submissions/23125259) | AC | 2,255 ms | Using Numba |
| Python (3.8.2) | [ac_aot.py](src/ac_aot.py) | [link](https://atcoder.jp/contests/typical90/submissions/23125429) | AC | 1,871 ms | Using Numba AOT |


### Memo
- 遅延セグメント木は以下のプロジェクトのコードを使用させていただきました。
  - https://github.com/not522/ac-library-python
  - 普通にかなり速く、PyPy で 1,000 ms ほどで通る（[ac.py](src/ac.py)）。
- コードを少し変更して Numba でコンパイルすると 2,200 ms ほどで通り（[ac_numba.py](src/ac_numba.py)）、AOT にすると 1,900 ms になった（[ac_aot.py](src/ac_aot.py)）。
- Numba でコンパイルできるようにするために、以下の変更を行った。
  - Python の List より NumPy の ndarray の方が相性が良く速いのでそちらに変更。
    - この辺は最近のアップデートで変わった？ 少なくとも AtCoder の Numba のバージョン (0.48.0) ではそう。
  - isinstance が Numba では使えないため、初期値配列 (ndarray) のみを受け取れるように変更
- `TYPE_FUNC` に関しては、手元 (0.53.1) では
  ```
  TYPE_FUNC = numba.types.FunctionType(numba.types.int64(numba.types.int64, numba.types.int64))
  ```
  と定義すればよかったが、AtCoder 上のバージョンでは `numba.types.FunctionType` が存在せず、代わりのものが見つからなかったため実際に与える関数の型を `numba.typeof` で取得することで解決した。
- [この行](src/ac_numba.py#L246) で `cache=True` としているが、実際にはグローバル関数 `f` を参照しているためキャッシュできないという警告が出される。引数で `f` を与えるようにしてあげれば良いが、AtCoder 上では動かなかった。



## AD: 030 - K Factors（★5）

- [Problem Link](https://atcoder.jp/contests/typical90/tasks/typical90_ad)
- [Tweet Link](https://twitter.com/e869120/status/1388987881977389059)

| Submission Language | Source Code | Submission | Verdict | Exec Time | Description |
| :--- | :---: | :---: | :---: | ---: | :---: |
| PyPy3 (7.3.0) | [ad.py](src/ad.py) | [link](https://atcoder.jp/contests/typical90/submissions/23155703) | AC | 567 ms | |
| Python (3.8.2) | [ad_numba.py](src/ad_numba.py) | [link](https://atcoder.jp/contests/typical90/submissions/23155654) | AC | 962 ms | Using Numba |


### Memo
- 普通に書くと PyPy では 600 ms 程度で通るが Python では TLE する（最大ケースが手元で 4.5 sec 程度だった）（[ad.py](src/ad.py)）。
  - 長さ `N` の 0 埋めされた配列 `a` を宣言する際、
    ```
    a = [0 for _ in range(N)]
    ```
    とする他に
    ```
    a = [0] * N
    ```
    と書くこともでき、下の書き方が高速になる。今回のように N が非常に大きい時は速度の差が顕著となる。
    - 整数や実数のようなプリミティブ型であればこの書き方をしてよいが、そうでない場合は同じオブジェクトを参照しているため想定した挙動にはならないことに注意。
      - 例えば、二次元配列を下の書き方で宣言すると同じリストの参照が N 個生まれることになる。
- NumPy のスライスによる範囲加算を用いることで高速化でき、Numba も用いることで 960 ms ほどで通った（[ad_numba.py](src/ad_numba.py)）。



## AE: 031 - VS AtCoder（★6）

- [Problem Link](https://atcoder.jp/contests/typical90/tasks/typical90_ae)
- [Tweet Link](https://twitter.com/e869120/status/1389349360866009090)

| Submission Language | Source Code | Submission | Verdict | Exec Time | Description |
| :--- | :---: | :---: | :---: | ---: | :---: |
| PyPy3 (7.3.0) | [ae.py](src/ae.py) | [link](https://atcoder.jp/contests/typical90/submissions/23941220) | AC | 671 ms | |
| Python (3.8.2) | [ae_numba.py](src/ae_numba.py) | [link](https://atcoder.jp/contests/typical90/submissions/23940893) | AC | 622 ms | Using Numba |


### Memo
- 普通に grundy 数のテーブルを埋めていくと PyPy では通るが Python だと TLE する（手元で 5 sec ほど）（[ae.py](src/ae.py)）。
- Numba で高速化すると通るようになる（[ae_numba.py](src/ae_numba.py)）。
  - AOT にすると 200 ms ほどになった。



## AF: 032 - AtCoder Ekiden（★3）

- [Problem Link](https://atcoder.jp/contests/typical90/tasks/typical90_af)
- [Tweet Link](https://twitter.com/e869120/status/1389711962213261316)

| Submission Language | Source Code | Submission | Verdict | Exec Time |
| :--- | :---: | :---: | :---: | ---: |
| Python (3.8.2) | [af.py](src/af.py) | [link](https://atcoder.jp/contests/typical90/submissions/23941679) | AC | 67 ms |


### Memo
- 想定解は順列全探索だが、bitDP で通した。



## AG: 033 - Not Too Bright（★2）

- [Problem Link](https://atcoder.jp/contests/typical90/tasks/typical90_ag)
- [Tweet Link](https://twitter.com/e869120/status/1390074137192767489)

| Submission Language | Source Code | Submission | Verdict | Exec Time |
| :--- | :---: | :---: | :---: | ---: |
| Python (3.8.2) | [ag.py](src/ag.py) | [link](https://atcoder.jp/contests/typical90/submissions/23941854) | AC | 25 ms |


### Memo
- 特になし



## AH: 034 - There are few types of elements（★4）

- [Problem Link](https://atcoder.jp/contests/typical90/tasks/typical90_ah)
- [Tweet Link](https://twitter.com/e869120/status/1390436977808351234)

| Submission Language | Source Code | Submission | Verdict | Exec Time |
| :--- | :---: | :---: | :---: | ---: |
| Python (3.8.2) | [ah.py](src/ah.py) | [link](https://atcoder.jp/contests/typical90/submissions/23942068) | AC | 143 ms |


### Memo
- 特になし



## AI: 035 - Preserve Connectivity（★7）

- [Problem Link](https://atcoder.jp/contests/typical90/tasks/typical90_ai)
- [Tweet Link](https://twitter.com/e869120/status/1390798852299448322)

| Submission Language | Source Code | Submission | Verdict | Exec Time | Description |
| :--- | :---: | :---: | :---: | ---: | :---: |
| Python (3.8.2) | [ai.py](src/ai.py) | [link](https://atcoder.jp/contests/typical90/submissions/23943439) | TLE | > 2,000 ms | |
| PyPy3 (7.3.0) | [ai.py](src/ai.py) | [link](https://atcoder.jp/contests/typical90/submissions/23945713) | AC | 1,325 ms | |
| Python (3.8.2) | [ai_numba.py](src/ai_numba.py) | [link](https://atcoder.jp/contests/typical90/submissions/23945622) | AC | 349 ms | Using Numba AOT |


### Memo
- 普通にやると PyPy だと通るが Python だと TLE する（[ai.py](src/ai.py)）。
- Numba で高速化して AOT すると通るが、以下の理由からかなりしんどい（[ai_numba.py](src/ai_numba.py)）。
  - 動的配列を引数に渡せないのでグラフを隣接リストで渡せない
    - Typed List を使えばできるはずだが、AtCoder の Numba は少しバージョンが古いので速度が少し不安？
  - deque が使えないのと関数内再帰関数がほとんど使えないので LCA 初期化時に DFS も BFS もしづらい
    - List の append/pop で DFS ができる



## AJ: 036 - Max Manhattan Distance（★5）

- [Problem Link](https://atcoder.jp/contests/typical90/tasks/typical90_aj)
- [Tweet Link](https://twitter.com/e869120/status/1391523624897499136)

| Submission Language | Source Code | Submission | Verdict | Exec Time |
| :--- | :---: | :---: | :---: | ---: |
| Python (3.8.2) | [aj.py](src/aj.py) | [link](https://atcoder.jp/contests/typical90/submissions/23946525) | AC | 335 ms |


### Memo
- `|x| = max(x, -x)` であることを踏まえると、
  ```
  |x - X| + |y - Y| = max((x - X) + (y - Y), (x - X) - (y - Y), -(x - X) + (y - Y), -(x - X) - (y - Y))
                    = max((x + y) - (X + Y), (x - y) - (X - Y), (-x + y) - (-X + Y), (-x - y) - (-X - Y))
  ```
  となるので、
  ```
  max_{(x, y)}(|x - X| + |y - Y|) = max( max_{(x, y)}(x + y) - (X + Y),
                                         max_{(x, y)}(x - y) - (X - Y),
                                         max_{(x, y)}(-x + y) - (-X + Y),
                                         max_{(x, y)}(-x - y) - (-X - Y) )
  ```
  となり、結局 `x + y, x - y, -x + y, -x - y` それぞれの最大値だけ持っておけば任意の位置からのマンハッタン距離の最大値が得られることがわかる。



## AK: 037 - Don't Leave the Spice（★5）

- [Problem Link](https://atcoder.jp/contests/typical90/tasks/typical90_ak)
- [Tweet Link](https://twitter.com/e869120/status/1391886390091075586)

| Submission Language | Source Code | Submission | Verdict | Exec Time |
| :--- | :---: | :---: | :---: | ---: |
| Python (3.8.2) | [ak.py](src/ak.py) | [link](https://atcoder.jp/contests/typical90/submissions/23947600) | AC | 1,369 ms |
| PyPy3 (7.3.0) | [ak.py](src/ak.py) | [link](https://atcoder.jp/contests/typical90/submissions/23947638) | AC | 114 ms |


### Memo
- 最初スライド最小値解法を実装したが Python で通る気がしなかったので別解を実装した（スライド最小値は PyPy で 550 ms ほどであった）。
- まず、作る料理の集合を決めたとき、その中で L でも R でもない中途半端な量の香辛料を使う料理は高々一つ、としてもちょうど W g にできるかどうかに変化はない
  - 全て L 側に寄せた上で、余った分を貪欲に埋めていけば中途半端なものは高々一つになる
- また、高々一つである中途半端な量の香辛料を使う料理について、それを、作る料理の集合のうち R - L が最大であるもの、としても問題ない
  - R - L でソートした上で貪欲に余った香辛料を埋めていき、どこか途中で中途半端になった場合はその中途半端な香辛料を末尾の料理に丸々移すことで実現できる
- よって、R - L でソートした上で、L のみ、R のみの遷移で DP をしていき、各料理に対して「現時点の DP テーブル + この料理に香辛料を中途半端に使う、を行ってちょうど W g になるときの価値の最大値」を毎回計算すると、それらの最大値が答えとなる。



## AL: 038 - Large LCM（★3）

- [Problem Link](https://atcoder.jp/contests/typical90/tasks/typical90_al)
- [Tweet Link](https://twitter.com/e869120/status/1392248540882116610)

| Submission Language | Source Code | Submission | Verdict | Exec Time |
| :--- | :---: | :---: | :---: | ---: |
| Python (3.8.2) | [al.py](src/al.py) | [link](https://atcoder.jp/contests/typical90/submissions/23993615) | AC | 27 ms |


### Memo
- 特になし
- Python の場合はオーバーフローなど何も気にせずに lcm を求めても問題ない。



## AM: 039 - Tree Distance（★5）

- [Problem Link](https://atcoder.jp/contests/typical90/tasks/typical90_am)
- [Tweet Link](https://twitter.com/e869120/status/1392612322410057729)

| Submission Language | Source Code | Submission | Verdict | Exec Time |
| :--- | :---: | :---: | :---: | ---: |
| Python (3.8.2) | [am.py](src/am.py) | [link](https://atcoder.jp/contests/typical90/submissions/23994024) | AC | 220 ms |


### Memo
- 特になし



## AN: 040 - Get More Money（★7）

- [Problem Link](https://atcoder.jp/contests/typical90/tasks/typical90_an)
- [Tweet Link](https://twitter.com/e869120/status/1392974101061378049)

| Submission Language | Source Code | Submission | Verdict | Exec Time | Description |
| :--- | :---: | :---: | :---: | ---: | :---: |
| Python (3.8.2) | [an_scipy.py](src/an_scipy.py) | [link](https://atcoder.jp/contests/typical90/submissions/23995356) | AC | 549 ms | Using SciPy |
| Python (3.8.2) | [an_dinic.py](src/an_dinic.py) | [link](https://atcoder.jp/contests/typical90/submissions/23995467) | AC | 49 ms | |


### Memo
- SciPy に maximum_flow を求める関数が存在するため、それを貼ると通せる。
  - Edmonds–Karp 法で実装されているため、計算量は `O(V E^2)`。今回の問題だと辺の数が最大で 5000 程度になるため少し遅い。
    - https://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.csgraph.maximum_flow.html
- Dinic 法は計算量が `O(V^2 E)` である上に、実用上はかなり速いため、かなり高速に通る。
  - Dinic 法の実装は以下のプロジェクトのコードを使用させていただきました。
    - https://github.com/not522/ac-library-python



## AO: 041 - Piles in AtCoder Farm（★7）

- [Problem Link](https://atcoder.jp/contests/typical90/tasks/typical90_ao)
- [Tweet Link](https://twitter.com/e869120/status/1393336369540341760)

| Submission Language | Source Code | Submission | Verdict | Exec Time |
| :--- | :---: | :---: | :---: | ---: |
| Python (3.8.2) | [ao.py](src/ao.py) | [link](https://atcoder.jp/contests/typical90/submissions/24014484) | AC | 520 ms |


### Memo
- 特になし
- SciPy にも凸包を計算する関数が存在したが、実数を受け取る形式になっていたので今回の問題に適用可能かは不明（未検証）。
  - https://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.ConvexHull.html



## AP: 042 - Multiple of 9（★4）

- [Problem Link](https://atcoder.jp/contests/typical90/tasks/typical90_ap)
- [Tweet Link](https://twitter.com/e869120/status/1394062245181595653)

| Submission Language | Source Code | Submission | Verdict | Exec Time |
| :--- | :---: | :---: | :---: | ---: |
| Python (3.8.2) | [ap.py](src/ap.py) | [link](https://atcoder.jp/contests/typical90/submissions/24015063) | AC | 59 ms |


### Memo
- 特になし
- Python は配列外参照は IndexError を返すが、スライスの場合は共通部分だけ返すため、配列の長さより大きい値を入れてもエラーにはならない。

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

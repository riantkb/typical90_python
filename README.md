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

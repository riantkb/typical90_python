#include<stdio.h> /*
"""*/

int a[2010][2010];
int main() {
    int h, w;
    scanf("%d%d", &h, &w);
    int rows[2010] = {};
    int cols[2010] = {};
    for (int i = 0; i < h; i++) {
        for (int j = 0; j < w; ++j) {
            scanf("%d", &a[i][j]);
            rows[i] += a[i][j];
            cols[j] += a[i][j];
        }
    }
    for (int i = 0; i < h; i++) {
        for (int j = 0; j < w; ++j) {
            printf("%d%c", rows[i] + cols[j] - a[i][j], j < w - 1 ? ' ' : '\n');
        }
    }
    return 0;
}
/*"""

import sys
import subprocess


if __name__ == "__main__":
    subprocess.run(f'gcc -x c -O2 {__file__} && ./a.out',
                   shell=True,
                   stdin=sys.stdin,
                   stdout=sys.stdout)
#*/

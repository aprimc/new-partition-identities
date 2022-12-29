"""This code goes with Example 5.3 in the paper arXiv:2106.06262."""

def get_row(i, w):
    return [max(0, x) for x in range(i*2 - 1, i*2 - w - 1, -1)]

def all_subfrequencies(c, r):
    for g0 in range(r + 1):
        if c == 1:
            yield [g0]
        else:
            for gs in all_subfrequencies(c - 1, max(0, r - g0)):
                yield [g0] + gs

def all_frequencies(i, *ks):
    rest = []
    for x in reversed(ks):
        rest.append(x)
    if i > w//2:
        for gs in all_subfrequencies(w, k):
            yield gs
    else:
        for gs in all_subfrequencies(i*2-1, sum(ks[-i*2+1:])):
            yield gs + rest[2 * i-1:]

def filter_frequencies(fs, ms1, *ks):
    k = sum(ks)
    ms = []
    for j, f in enumerate(fs):
        if j:
            m = ms1[j - 1]
            m0 = ms[-1]
            if m0 > m:
                m = m0
            m += f
            if m > k:
                return None
            ms.append(m)
        else:
            ms.append(f)
    return ms

def row_fs_value(row, fs):
    s = 0
    for v, f in zip(row, fs):
        s += v * f
    return s

if __name__ == '__main__':
    """One should put by hand N and the 'highest wight'.
    For w=2n+1 for (k0,k1,...,kn) put [k0,0,k1,0,...,0,kn].
    For w=2n for (k0,k1,...,kn)e put [k0,k1,0,...,0,kn]."""
    N = 6
    highest_weight = [0, 0, 1, 0, 0]
    print("highest_weight =", highest_weight)
    w = len(highest_weight)
    k = sum(highest_weight)
    print('k =', k, ' w =', w)
    i = 1
    frequencies = {}
    result = []
    ms0 = []
    for j in range(0, len(highest_weight)):
        ms0.append(sum(highest_weight[-j-1:]))
    all_total_ms0 = [(0, ms0)]





    while True:
        all_total_ms1 = []
        row1 = get_row(i, w)
        all_fs = list(all_frequencies(i, *highest_weight))
        for total0, ms0 in all_total_ms0:
            for fs1 in all_fs:
                ms = filter_frequencies(fs1, ms0, *highest_weight)
                if ms is None:
                    continue
                total1 = row_fs_value(row1, fs1) + total0
                all_total_ms1.append((total1, ms))
        if i == N:
        #if i == w//2:
            break
        i += 1
        all_total_ms0 = all_total_ms1

result = []
for total1, ms1 in all_total_ms1:
    if total1 <= 6:
        result.append(total1)
print(result)
#print(len(all_total_ms1))


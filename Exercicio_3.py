import random

def activityNotification(exp, d):
    def median(cnt, d):
        c = 0
        if d % 2 == 1:
            m_pos = d // 2 + 1
            for i in range(201):
                c += cnt[i]
                if c >= m_pos:
                    return i
        else:
            m1 = d // 2
            m2 = m1 + 1
            f = None
            s = None
            for i in range(201):
                c += cnt[i]
                if f is None and c >= m1:
                    f = i
                if c >= m2:
                    s = i
                    break
            return (f + s) / 2

    notif = 0
    cnt = [0] * 201

    for i in range(d):
        cnt[exp[i]] += 1

    for i in range(d, len(exp)):
        med = median(cnt, d)
        if exp[i] >= 2 * med:
            notif += 1
        cnt[exp[i - d]] -= 1
        cnt[exp[i]] += 1

    return notif

def main():
    n, d = map(int, input().strip().split())
    exp = list(map(int, input().strip().split()))
    res = activityNotification(exp, d)
    print(res)

if __name__ == '__main__':
    main()

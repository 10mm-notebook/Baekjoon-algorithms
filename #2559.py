temp, K = map(int, input().split())
days = list(map(int, input().split()))

window_sum=sum(days[:K])
max_window=window_sum

for i in range(K,temp):
    window_sum=window_sum-days[i-K]+days[i]
    max_window=max(max_window,window_sum)

print(max_window)

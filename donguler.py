s = [1, 3, 5, 7, 9]
for k in s:
    continue  # döngülerde continue denilince alt satıra geçmez döngü devam eder
    print(k)
for i in range(5):
    continue
    print(s[i])

for i in range(len(s)):  # len komutu length yani uzunluk anlamına gelir ve listenin kaç elemanı varsa onu söyle
    continue
    print(s[i])

# while döngüsü ile
index = 0
while index < len(s):  # index değerimiz sona gelince dur
    print("break varsa tek sefer çalışacam")
    break  # döngü sonlanacak
    print(s[index])
    index = index + 1

# do while ile (aradaki farka bakarız)

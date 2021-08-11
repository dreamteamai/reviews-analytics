data = []
count = 0 
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:
			print(len(data))
print('檔案讀取完了, 總共有', len(data), '筆資料')


# 算留言平均長度
sum_len = 0
for message in data:
	sum_len = sum_len + len(message)
avaerage_len = sum_len / len(data)
print('留言平均長度為', avaerage_len)	

# 找出長度<100的留言 
new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('一共有', len(new), '筆留言長度<100')
print(new[1])

# 清單快寫法  (運算 變數 清單 篩選條件)
good = [d for d in data if 'good' in d]
print('一共有', len(good), '筆留言提到good')



# 文字計數
wc = {}  # word_count
for d in data:
	words = d.split()
	for word in words:
		if word in wc:
			wc[word] += 1
		else:
			wc[word] = 1 # 新增key

for word in wc:
	if wc[word] > 1000000:
		print(word, wc[word])

print(len(wc))
print(wc['Allen'])

while True:
	word = input('請問你想查什麼字:')
	if word == 'q':
		print('感謝使用本查詢功能')
		break
	if word in wc:
		print(word, '出現過的次數為:', wc[word])
	else:
		print('這個字沒有出現過')





import time
def ticktock(*args):
	t = int(time.time() * 10) % 12
	uni = u'\\U0001f55' + hex(t)[2:]
	emoji = bytes(uni, 'raw_unicode_escape').decode('raw_unicode_escape')
	print(emoji, '', *args, end='\r')

def crabby(*args, done=None):
	t = abs(6-(int(time.time() * 10) % 12))
	emoji = '🦀'
	if done is not None:
		n = int(done*20)
		out = '📍' + n*' ' + emoji + ' '*(20-n) + '🏁'
	else:
		out = t*' ' + emoji + ' '*(6 - t)
	print(out, '', *args, end='\r')




if __name__ == '__main__':
	n = 40
	for i in range(n):
		ticktock(i+1,'/',n)
		time.sleep(0.1)

	for i in range(n):
		crabby(i+1,'/',n)
		time.sleep(0.1)

	for i in range(n):
		crabby(i/n, done=i/n)
		time.sleep(0.1)
	print(' '*80, end='\r')
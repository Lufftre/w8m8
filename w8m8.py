import time

def iterate(iterable, *args, out='', **kwargs):
	l = len(iterable)
	time_start = time.time()
	last_tid_kvar = 0
	for i,x in enumerate(iterable):
		procent_per_sek = (i/l)/(time.time() - time_start)
		tid_kvar = (1-(i/l))/procent_per_sek if procent_per_sek > 0 else 0
		smooth_tid_kvar = 1+(tid_kvar + last_tid_kvar)
		tid_text = time.strftime("%H:%M:%S", time.gmtime(smooth_tid_kvar))

		progressbar(i/l, out.format(x, i=i), tid_text, *args, **kwargs)
		yield x

	progressbar(1, out.format(x), *args, **kwargs)
	print()

def progressbar(progress, *args, start='[', end=']', marker='', fill='█', bg=' ',
	length=20, verbose=True, clear=True):

	left = int(length * progress)
	right = length - left

	out = start + fill*left + marker + bg*right + end

	if verbose:
		out += ' {:.2f}%'.format(progress*100)

	if clear:
		out = '\033[K' + out

	print(out, *args, end='\r')


def crabby(*args, **kwargs):
	progressbar(*args, start='🐚', end='🏁 ', marker='🦀', fill=' ', **kwargs)



def loader(*args, start='[', end=' ]', marker='🦀', bg=' ',
	length=16, progress=None, bounce=True, verbose=True):

	if bounce:
		i = abs(length - int(time.time() * 10) % (2*length))
	else:
		i = int(time.time() * 10) % length

	out = start + i*bg + marker + (length-i)*bg + end

	if verbose and progress is not None:
		out += ' {:.2f}%'.format(progress*100)

	print(out, *args, end='\r')

def clocky(*args, **kwargs):
	i = int(time.time() * 10) % 12
	emoji = bytes([240, 159, 149, 144 + i]).decode('utf-8')
	hej = 2
	print("hej", hej)
	print("hej", hej)
	print("hej", hej)
	print("hej", hej)
	loader(*args, start='', end=' ', marker=emoji, bg='', **kwargs)



if __name__ == '__main__':
	import random
	n = 497
	for i in iterate(range(n)):
		time.sleep(random.randint(30,40)/1000)
	# for i in range(n):
	# 	clocky(progress=(i+1)/n)
	# 	time.sleep(0.005)
	# print()

	# for i in range(n):
	# 	loader(progress=(i+1)/n)
	# 	time.sleep(0.005)
	# print()

	# for i in range(n):
	# 	progressbar((i+1)/n)
	# 	time.sleep(0.005)
	# print()
	# for i in range(n):
	# 	crabby((i+1)/n)
	# 	time.sleep(0.005)
	# print()


import time

def progressbar(progress, *args, start='[', end=']', marker='', fill='█', bg=' ',
	length=20, verbose=True):

	left = int(length * progress)
	right = length - left

	out = start + fill*left + marker + bg*right + end

	if verbose:
		out += ' {:.2f}%'.format(progress*100)

	print(out, *args, end='\r')


def crabby(*args, **kwargs):
	progressbar(*args, start='🐚', end='🏁 ', marker='🦀', fill=' ', **kwargs)




if __name__ == '__main__':
	n = 497

	for i in range(n):
		clocky(progress=(i+1)/n)
		time.sleep(0.005)
	print()

	for i in range(n):
		loader(progress=(i+1)/n)
		time.sleep(0.005)
	print()

	for i in range(n):
		progressbar((i+1)/n)
		time.sleep(0.005)
	print()
	for i in range(n):
		crabby((i+1)/n)
		time.sleep(0.005)
	print()
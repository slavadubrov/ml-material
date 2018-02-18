import sys

last_key = None
values_sum = 0

for line in sys.stdin:
	key, value = line.strip().split("\t")
	if key != last_key and last_key is not None:
		print(last_key + "\t" + str(values_sum))
		values_sum = 0
	last_key = key
	values_sum += int(value)

if key != last_key and last_key is not None:
	print(last_key + "\t" + str(values_sum)) 
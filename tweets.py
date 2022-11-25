# program to find the max tweets and printing all equal no of tweets

test_cases = int(input("Enter the number of Test Cases: "))
test_count = 0
tweet_names = []

while test_count < test_cases:

	num = int(input("Enter the number of each Test Case:"))
	count = 0
	while count < num:
		name = str(input("Enter the name and tweet id"))
		tweet_names.append(name)
		count += 1

	test_count += 1

uniq_names = [pref_names.split()[0] for pref_names in tweet_names]
times = {}
for i in uniq_names:
    times[i] = times.get(i,0) + 1

repeat = times.values()

for element in set(repeat):
	dupl = ([(key, value) for key, value in sorted(times.items()) if value == element])

	if len(dupl) > 1:
		for (key, value) in dupl:
			print(key, '', value)

	max_value = max(times.values())
	temp_max_result = [(key, value) for key, value in sorted(times.items()) if value == max_value]

	if temp_max_result != dupl:
		for (key, value) in temp_max_result:
			print(key, '', value)












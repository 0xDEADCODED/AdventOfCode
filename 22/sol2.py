import pathlib
import re
import collections

p1 = 0
p2 = 0

def next_secret(secret: int) -> int:
	secret ^= (secret & 0x3FFFF) << 6
	secret ^= secret >> 5
	secret ^= (secret & 0x1FFF) << 11
	return secret

gain_per_sequence = collections.defaultdict(int)

for match_a in re.compile(r"(?m)(?P<initial>[0-9]+)").finditer((pathlib.Path(__file__).parent / "in").read_text()):
	seen = set()
	
	secret_a = int(match_a["initial"])
	price_a = secret_a % 10
	changes = 159999
	
	for _ in range(2000):
		secret_b = next_secret(secret_a)
		price_b = secret_b % 10
		
		changes = (changes // 20) + (price_b - price_a + 9) *8000
		print(changes)
		
		if changes not in seen:
			seen.add(changes)
			gain_per_sequence[changes] += price_b
		
		secret_a, price_a = secret_b, price_b
	
	p1 += secret_b

m = 0
s = []
for k,v in gain_per_sequence.items():
	if v > m:
		m = v
		s = k
print(m,s)
p2 = max(gain_per_sequence.values())

print(p1)
print(p2)

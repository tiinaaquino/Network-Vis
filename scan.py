import argparse as ap
import matplotlib.pyplot as plt
import pyshark

def frequency(file):
	p = pyshark.FileCapture(file, keep_packets = False)
	packets = []
	protocols = {}
	def counter(*args):
		packets.append(args[0])
	p.apply_on_packets(counter, timeout = 100000)
	for p in packets:
		pr = pack.highest_layer
		if pr in protocols:
			protocols[pr] += 1
		else:
			protocols[pr] = 1
	print(protocols)
	return protocols

def visualize(data):
	size = len(data)
	x = list(data.keys())
	y = list(data.values())
	for i in range(size):
		plt.bar(i, y[i], tick_label = x[i])
	plt.xticks(range(size), x)
	plt.title("Results")
	plt.xlabel("Protocols")
	plt.ylabel("Frequency")
	plt.savefig("graph.png")
	plt.show()

def parse_arg():
	parser = ap.ArgumentParser(description = "Program to graph/ visualize")
	parser.add_argument("file", help = ".pcap file")
	return parser.parse_args()

if __name__ == "__main__":
	argp = parse_arg()
	if argp.file.endswith(".pcap"):
		data = frequency(argp.file)
		visualize(data)
	else:
		print("Unable to open pcap file.")
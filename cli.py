import argparse
from app import app
from wsgi import RemotePyServer


def main():
	parser = argparse.ArgumentParser(description = "RemotePy CLI")

	parser.add_argument("-b", "--server", type = str, nargs=1,
						metavar = "server", default = "0.0.0.0",
						help = "IP address of server.")	

	parser.add_argument("-p", "--port", type = int,
						metavar = "port", default = 5000,
						help = "Port no. of server.")

	parser.add_argument("-w", "--workers", type = int,
						metavar = "workers", default = 1,
						help = "No. of workers on server.")

	parser.add_argument("-t", "--threads", type = int,
						metavar = "threads", default = 2,
						help = "No. of threads for server")

	args = parser.parse_args()

	host = args.server
	port = args.port
	workers = args.workers
	threads = args.threads

	server = RemotePyServer()
	server.run(app, host=host, port=port, workers=workers, threads=threads)

if __name__ == "__main__":
	main()
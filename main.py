import os
from sys import argv
from src.bigdata1.get_nycdata import get_nycdata
import json

if __name__ == "__main__":
	 
	YOUR_APP_KEY = os.getenv('APP_KEY')
	if YOUR_APP_KEY.find('{') != -1:
		YOUR_APP_KEY = YOUR_APP_KEY.strip('{}')

	try:
		page_size = int(argv[1])

		try:
			num_pages = int(argv[2])
		except Exception:
			num_pages = -1
		
		data = get_nycdata(YOUR_APP_KEY, page_size, num_pages)

		try:
			output = argv[3]	
			json_file = json.dumps(data, indent = 4)
			with open(output, "w") as fw: 
				fw.write(json_file)
		except Exception:
			print(data)

	except Exception:
		page_size = int(argv[1][(argv[1].find('=') + 1):])

		try:
			num_pages = int(argv[2][(argv[2].find('=') + 1):])
		except Exception:
			num_pages = -1
		
		data = get_nycdata(YOUR_APP_KEY, page_size, num_pages)

		try:
			if argv[2].find('output') != -1:
				output = argv[2][(argv[2].find('=') + 1):]
			if argv[3].find('output') != -1:
				output = argv[3][(argv[3].find('=') + 1):]

			json_file = json.dumps(data, indent = 4)
			with open(output, "w") as fw: 
				fw.write(json_file)
		except Exception:
			print(data)
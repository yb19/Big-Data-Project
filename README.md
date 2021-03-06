# Big-Data-Project
This is the first part of the project for the Big Data Technology course (STA 9760).

## Description:
You can use this container to extract the Open Parking and Camera Violations data from NYC Open Data. You can also specify the number of rows (of data) on each page, the number of pages you want to load, and whether to print out the data to stdout or write the data to the file that you speficy.

## Instructions:
After pulling this container, you can use the following command to run the container:

docker run -e APP_KEY={YOUR_APP_KEY} -t bigdata1:1.0 python main.py --page_size=1000 --num_pages=4 --output=results.json

Or you can also use the following command:

docker run -e APP_KEY=YOUR_APP_KEY -t bigdata1:1.0 python main.py 1000 4 results.json

YOUR_APP_KEY is your APP TOKEN for the NYC Open Data API.

--page_size=your_page_size or your_page_size is the number of rows (of data) on each page. This command line argument is required.

--num_pages=you_num_pages or you_num_pages is the number of pages you want to load. If omitted, the container will continue requesting data until the entirety of the content has been exhausted.

--output=file_name.file_format or file_name.file_format is the file that the container will write the data to. If omiited, the container will simply print data to stdout.

## Warning:
If you want to spycify more than one command line argument (i.e., num_pages, output), you should follow the order of arguments specified above.

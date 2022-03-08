README.txt

Milestone 3 Report

Student Name: Qian He (17337823), Steven Wu (10791134)
Version: Analyst


Step1: how to run the code that creates the index

Unzip analyst.zip and place its three directories under the same location as all the python files.
Run “invert_index.py” to call the main function to run the code that creates the posting (index).  “invert_index.py” will collect all the existing contents inside all the files such as headers, body, etc. 

Next, it will call “index.py” for tokenizing the text, dealing with the stop word and stem similar words of the token list. Then, it will create a dictionary to index the tokens, URLs along with their tf-idf scores. 

Finally, the dictionary will be stored inside “posting.json”.


Step2: how to start the search interface

Run “main.py”. It will open the “posting.json” first, and then it will pop out the website that links to the web GUI interface: “Please visit http://127.0.0.1:2222/”.
Click the website “http://127.0.0.1:2222/”, and then it will lead you to the website where the title is “An Answer Gained”.

The top box will be the place for you to enter the queries. By clicking the “Gain” button on the right side, you will get the results. The below five boxes are the place to show the top 5 results.


Step3: how to perform a simple query

Enter the query inside the top box, and then click the “Gain” button on its right side to get the top 5 results of the websites inside the below boxes.

For example, enter “machine learning” inside the top box, click “Gain”, and then the 5 most related websites for “machine learning” will appear in the below 5 boxes separately.

# Update100
Update100 is a python and bash script used to automate updating your progress during the #100DaysOfCode. I made this during my journey, check it out [here](https://github.com/NeonStar-Dev/100-days-of-code)!

## Dependencies
* Bash Shell
* Python
* Tweepy
* Twitter developer account + an app/project's keys and tokens

## Setting Up
### Downloading
1. Download update100.py and save it within your filesystem
2. Download update100.sh and save it within your filesystem
3. Open both update100.py and update100.sh in your preferred text editor
### update100.py
1. Go to line 4 and enter the file path for the file you are reading in. This would be whatever file you are using to log your daily progress. For example: ```/home/user/code/100-days-of-code/logfile.md``` \
   ![Variable to hold filepath for log file](./resources/images/filePath)
2. Go to lines 66 - 69 and enter your twitter developer app's:
   * Consumer (API) key
   * Consumer secret (API secret) key
   * Access Token
   * Access Secret Token \
    ![Variable to hold keys and tokens](./resources/images/client)
3. **OPTIONAL** Go to line 7 and enter a desired number of characters to read from your log file and place into the body of the tweet. Default: 200. \
   ![Variable to hold desired characters](./resources/images/bodyLimit)
4. **OPTIONAL** Go to line 61 and enter a desired string for the format of your tweet. Default: \
    Day x/100

    [body of tweet]

    #100DaysOfCode \
    ![Variable to hold string to tweet](./resources/images/tweetString)
5. Save and close update100.py

### update100.sh
1. Go to line 4 and enter the file path for the file you are reading in. This would be whatever file you are using to log your daily progress. For example: ```/home/user/code/100-days-of-code/logfile.md``` \
   ![Variable to hold filepath for log file](./resources/images/filePath2)
2. Go to line 7 and enter the file path for update100.py. For example: ```/home/user/code/100-days-of-code/update100.py``` \
   ![Variable to hold filepath for update100.py](./resources/images/filePath3)
3. Save and close update100.sh
## Usage
### update100.py
This python script is used to automatically tweet updates from your #100daysofcode log file. In order for update100.py to properly function, there are some simple formatting requirements within your log file that must be met. The script finds each day through a search for a substring of "# Day". This means that in order for the script to successfully find the correct day, you must title each new update with a heading and have day as the first word. The level of heading does not matter as long as there is a single # and a single whitespace in front of the word "Day" in the line. The script then automatically takes the next line, saves it to a variable and places it within the string to be tweeted. The update line only reads in 200 characters as a default. If there are more than 200 characters in the string, it cuts the string at the last period before 200 characters reached and places an ellipsis instead. This, along with the entire string sent to twitter can be changed. Remember that a tweet can only contain 280 characters though! (See TL;DR below)

Run the script by using the python3 command with the path to where you saved update100.py. Example:

```
python3 [path/to/file]
```

TL;DR: Whatever you are sending to tweet must come directly after the line titling the day. The number of characters read in can be changed by a variable, the default is 200. Example:

```
# Day 15
This is the line that is being sent to twitter
```

### update100.sh
This bash script is completely optional and just adds functionality. The script will use update100.py so long as it is configured correctly above in the setting up section. The additional features here are that it will add, commit, and push your log file to whatever your set repo is. To keep it simple, once you've got your log file updated and are ready to push it, run the script and it will take care of the repo and your tweet. This means all you have to worry about it your time spend learning and quickly jotting your update into the file!

The commit message provided is "DOCS: Add new day", so if you would like something else that can be changed within update100.sh directly at line 10

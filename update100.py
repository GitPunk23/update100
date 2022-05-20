import tweepy

# - - - - - ENTER PATH OF FILE TO READ IN - - - - -
filePath = ''

# - - - - - CHARACTERS TO READ FROM LOG - - - - -
bodyLimit = 200

# Test String
testString = "Hello, if you're reading this that means I've successfully automated my log update process!\n\n#100DaysofCode"

# Promotion String
repoURL = 'https://github.com/NeonStar-Dev/update100'
promotionString = 'This tweet was sent by update100. Checkout the GitHub repo here!\n' + repoURL

# Read in markdown file
try:
    file = open(filePath, "r")
except:
    print('No file found at:  ' + filePath)
    quit()

# Get day and line from log to add to tweet
lines = file.readlines()
lineNumber = 0
latestUpdateLine = 0
i = 0

for line in lines:
    lineNumber += 1
    if '# Day ' in line :
        i += 1
        latestUpdateLine = lineNumber

# Sets the latest update line to the line after the last heading
try:
    updateLine = lines[latestUpdateLine]
except: 
    print('There were no lines detected beneath:  "' + lines[latestUpdateLine -1] + '"')
    quit()
updateString = ''
periodPos = 0
charNumber = 0

# If line is longer than 200 characters, create a substring up to the last period before 200
if len(updateLine) > bodyLimit:

    for char in range(len(updateLine)):
        charNumber += 1
        if char == '.' and charNumber < bodyLimit:
            periodPos = charNumber
        elif char == ' ' and charNumber - periodPos == 1:
            updateString = updateLine[0:charNumber] + ".."
else:
    updateString = updateLine 

# Close the file
file.close()    

# - - - - - ENTER STRING TO POST TO TWITTER - - - - -
tweetString = "Day " + str(i) + "/100" + "\n\n" + updateString + "\n" + "#100DaysofCode"

# Create twitter client
try:
    consumer_key=""
    consumer_secret=""
    access_token=""
    access_token_secret=""

    auth = tweepy.OAuth1UserHandler(
   consumer_key, consumer_secret,
   access_token, access_token_secret
)
    api = tweepy.API(auth)
    print('Authentication successful')
except:
    print('Authentication failed')
    quit()
    

# Tweet status:
try:
    status = api.update_status(tweetString)
    print('This tweet has been successfully posted on twitter:\n' + tweetString)
    tweetID = status.id
    try:
        api.update_status(promotionString,in_reply_to_status_id=tweetID)
        print('With the reply: \n' + promotionString)
    except:
        print('Promotional reply failed to be created and sent to tweet ID "' + tweetID + '"')

except:
    print('Tweet failed to be created and sent')
    exit()

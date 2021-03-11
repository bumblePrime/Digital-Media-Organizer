# Digital-Media-Organizer
This is a simple scrip that creates a sqlite database file of the  media stored in any folder on HDD. To use this scrip you need a list of the files that can easily be obtained using windows built in directory commands. Simply open a command window in the folder where content is stored and run the following command
``` dir /b /s *.mp4 > Content.txt```
In the above command `*.mp4*` is used to filter mp4 files. If you wish to filter any other file format you can do teh same or better yet remove the filter to geta list of all the files in the directory. 

Once you have the txt file run the python script
``` python MediaDB.py```

Once execution is done you will have a sqlite databse file titles **MediaCollection**.
You can use this databse independently or make a telegram bot that searches it for you . I have made a code template for you to make your own telegram bot here https://github.com/bumblePrime/Digital-Media-Bot.
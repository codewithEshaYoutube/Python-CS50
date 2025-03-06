#mars
'''
Section Leader Application
/
Teaching Demo
Developer Esha
Instructions
As part of your application, you are to prepare a short informal video which showcases your teaching. The video should be 5-6 minutes long. We don't want you to spend too long making this video, certainly no longer than an hour. Recall that you are not competing against others. Instead you are demonstrating that you are ready to teach! Here is a sample teach video (for a different problem) to give you inspiration.

Mars Weight prompt
The problem you are to teach in the demo is Mars Weight. Here is the prompt that is given to the student:

An earthling's weight on Mars is 37.8% of their weight on earth. Write a Python program that prompts the user (an earthling) to enter their weight on earth and prints their calculated weight on Mars.

Solution
Here is a sample run of the program:

$ python marsweight.py
Enter a weight on earth: 120
The equivalent weight on Mars: 45.36
And here is a sample solution:

# File: marsweight.py

# we use constants!
MARS_MULTIPLE = 0.378

def main():
    # Technically weight is measured in newtons, but one of your
    # goals is to focus on the python, not the physics!
    earth_weight_str = input('Enter a weight on earth: ')

    # input() returns a value in string form, get the number out
    earth_weight = float(earth_weight_str)

    # More variables is good times when first learning
    mars_weight = earth_weight * MARS_MULTIPLE

    # Note the string concatenation!
    print('The equivalent weight on Mars: ' + str(mars_weight))

if __name__ == '__main__':
    main()
Learning objectives
The learning objectives for the Mars Weight problem are for students to understand:

That each variable has a type
The difference between assigning variables and using variables
How to "cast" between types
You can't teach all of that in 5 minutes. Choose something to focus on. The Mars Weight is your motivation! Motivation is really important, but the point of the problem is not physics.

Your students
In the Code In Place course, you will teach a section live with students. When recording your teaching demo, there will be no live students (obviously), but to the best of your ability, teach as if there were a live audience (though you do not need to interact with this fake audience).

Assume that your students have attended lecture and were introduced to the relevant concepts (constants, variables, input and print, variable types and casting) and have seen a few worked examples. Their understanding is still pretty new!

You can assume that students find variables and variable types difficult, and they find input, print and constants to be easy.

Students have been given the metaphor that a variable is like a teeny box in your computer where you can store stuff. We will have emphasized that every variable has (1) a name, (2) a type, and (3) a value.

Lesson plan
You can use your 5 minutes any way you like. Here is a sample minute-by-minute breakdown you might adopt:

1 min: Give a brief recap of variables and explain the problem. Make it sound fun! While you should imagine that you are teaching a class of students, don't feel the need to address them or ask them questions.
Type up a solution or pseudocode for how your students may want to approach the solution in an IDE/text editor of choice, explaining the steps as you write. If you write up a solution, make sure you show how to test the program (see the sample teach for an example of this).
1 min: Recap and summarize what you went over.
When showing code to students, you can program in your choice of tool/IDE. We recommend our own IDE as our students will use the same browser-based environment. That being said, Sublime, VSCode, PyCharm or wherever you are most comfortable is fine. The comments we have put in place in our solution are there for your benefit. During your teach, feel free to comment or not comment your code as it feels appropriate!

How we will evaluate your video
We are looking for people who know their content knowledge and who are able to communicate and motivate well. We value quality over quantity, so don't feel pressured to rush through everything. Instead, make sure the content you cover is clear and easy to follow.

Logistics
Here are our recommendations for handling the recording logistics.

Recording

You can record your demo lesson using whatever tools you have available: webcam, screen capture, smart phone, etc. One option is to record using Zoom (instructions below).

Don't fuss about production quality! We are more interested in who you are than the quality of your audio :-). However you record, it should be a "single take", and you shouldn't do any post-production.

Length of the video

We ask for a video of 5-6 minutes. Anything longer is too long! Please cut the video at a maximum of 6 minutes, even if it makes for an abrupt ending. Do not feel the need to overproduce your video! We are trying to scale here, I hope you understand :-)

Uploading the video

After completing your recording, save the video file. You will upload your video using the button to the right

Using Zoom to record (optional)

Here are instructions for using Zoom to make your recording. (You do not need to use Zoom; it is just an option)

Open Zoom and press "New Meeting" (or "Host a Meeting").
Make sure that your microphone is unmuted and if possible, that your video is on.
Zoom has a variety of teaching tools you can take advantage of (though none are required). Press the "Share Screen" button and select one of the following:
Choose your IDE window to show writing code
Choose "Whiteboard" to use the built-in whiteboard feature. Feel free to record an actual whiteboard if you have one, or to not use a whiteboard at all!
Choose "iPhone/iPad" to share work on an iPad (having an iPad is not required).
When you're ready to record, bring up the menu and (if you are screen sharing) press "More" then "Record on this computer" (or just "Record" and then "Record on this computer" if you're starting without screen sharing).
Once you're finished, hit the square Stop symbol to stop the recording, and then "End Meeting."
After ending the meeting, Zoom will save the recording and should automatically open up the folder where the file was saved (if not, go to "Documents/Zoom/[insert date of recording + name of Zoom meeting room]").
The saved mp4 file (which should be called zoom_0.mp4 or something similar) is the one you will upload with your section leader application.
For more information troubleshooting, see this support article from Zoom https://support.zoom.us/hc/en-us/articles/201362473-Local-Recording
Preview
No Video Yet
'''
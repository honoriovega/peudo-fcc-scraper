import os
from flask import Flask,request,jsonify
from random import randint,choice
app = Flask(__name__)

'https://fcc-profile-scraper.herokuapp.com/user/'
def generatRandomChallenge():

      return {
         "title": "Target Elements by Class Using jQuery",
         "completed_at":  choice(["Mar","April","May","June"]) + str(randint(1,30)) + str(randint(2016,2018)),
         "updated_at": "",
         "url": "https://www.freecodecamp.comundefined"
      }

@app.route('/')
def login():
    username = request.args.get('user')
    users = {
      'user512' :{
   "name": "Tom Lee",
   "profileImage": "https://avatars2.githubusercontent.com/u/8117421?v=4",
   "location": "Oakland, CA",
   "completedChallenges": [
      {
         "title": "Build a Tribute Page",
         "completed_at": "Apr 02, 2017",
         "updated_at": "",
         "url": "https://www.freecodecamp.com/challenges/Build a Tribute Page"
      },
      {
         "title": "Reverse a String",
         "completed_at": "May 13, 2017",
         "updated_at": "",
         "url": "https://www.freecodecamp.comundefined"
      },
      {
         "title": "Learn how Free Code Camp Works",
         "completed_at": "Jun 26, 2016",
         "updated_at": "Jun 26, 2016",
         "url": "https://www.freecodecamp.com/challenges/Learn how Free Code Camp Works"
      },
      {
         "title": "Configure your Profile",
         "completed_at": "Jun 26, 2016",
         "updated_at": "Mar 12, 2017",
         "url": "https://www.freecodecamp.com/challenges/Configure your Profile"
      },
      {
         "title": "Join a Free Code Camp Group in Your City",
         "completed_at": "Jun 26, 2016",
         "updated_at": "",
         "url": "https://www.freecodecamp.com/challenges/Join a Free Code Camp Group in Your City"
      },
      {
         "title": "Learn What to Do If You Get Stuck",
         "completed_at": "Jun 27, 2016",
         "updated_at": "",
         "url": "https://www.freecodecamp.com/challenges/Learn What to Do If You Get Stuck"
      },
      {
         "title": "Say Hello to HTML Elements",
         "completed_at": "Jun 27, 2016",
         "updated_at": "Feb 12, 2018",
         "url": "https://www.freecodecamp.comundefined"
      },
      {
         "title": "Headline with the h2 Element",
         "completed_at": "Jun 27, 2016",
         "updated_at": "Mar 15, 2018",
         "url": "https://www.freecodecamp.comundefined"
      },
      {
         "title": "Inform with the Paragraph Element",
         "completed_at": "Jun 27, 2016",
         "updated_at": "",
         "url": "https://www.freecodecamp.comundefined"
      },
      {
         "title": "Declare JavaScript Objects as Variables",
         "completed_at": "Aug 02, 2016",
         "updated_at": "",
         "url": "https://www.freecodecamp.comundefined"
      },
      {
         "title": "Construct JavaScript Objects with Functions",
         "completed_at": "Aug 02, 2016",
         "updated_at": "",
         "url": "https://www.freecodecamp.comundefined"
      },
      {
         "title": "Make Instances of Objects with a Constructor Function",
         "completed_at": "Aug 02, 2016",
         "updated_at": "",
         "url": "https://www.freecodecamp.comundefined"
      },
      {
         "title": "Create a GitHub Account and Join our Chat Rooms",
         "completed_at": "Mar 12, 2017",
         "updated_at": "",
         "url": "https://www.freecodecamp.com/challenges/Create a GitHub Account and Join our Chat Rooms"
      },
      {
         "title": "Read Coding News on our Medium Publication",
         "completed_at": "Mar 12, 2017",
         "updated_at": "",
         "url": "https://www.freecodecamp.com/challenges/Read Coding News on our Medium Publication"
      },
      {
         "title": "Delete HTML Elements",
         "completed_at": "Mar 12, 2017",
         "updated_at": "Feb 05, 2018",
         "url": "https://www.freecodecamp.comundefined"
      },
      {
         "title": "Comment out HTML",
         "completed_at": "Mar 12, 2017",
         "updated_at": "Feb 05, 2018",
         "url": "https://www.freecodecamp.comundefined"
      },
      {
         "title": "Uncomment HTML",
         "completed_at": "Mar 19, 2017",
         "updated_at": "",
         "url": "https://www.freecodecamp.comundefined"
      },
      {
         "title": "Fill in the Blank with Placeholder Text",
         "completed_at": "Mar 19, 2017",
         "updated_at": "",
         "url": "https://www.freecodecamp.comundefined"
      },
      {
         "title": "Change the Color of Text",
         "completed_at": "Mar 19, 2017",
         "updated_at": "",
         "url": "https://www.freecodecamp.comundefined"
      },
      {
         "title": "Use CSS Selectors to Style Elements",
         "completed_at": "Mar 19, 2017",
         "updated_at": "",
         "url": "https://www.freecodecamp.comundefined"
      },
      {
         "title": "Use a CSS Class to Style an Element",
         "completed_at": "Mar 19, 2017",
         "updated_at": "",
         "url": "https://www.freecodecamp.comundefined"
      },
      {
         "title": "Style Multiple Elements with a CSS Class",
         "completed_at": "Mar 19, 2017",
         "updated_at": "",
         "url": "https://www.freecodecamp.comundefined"
      },
      {
         "title": "Change the Font Size of an Element",
         "completed_at": "Mar 19, 2017",
         "updated_at": "",
         "url": "https://www.freecodecamp.comundefined"
      },
      {
         "title": "Set the Font Family of an Element",
         "completed_at": "Mar 19, 2017",
         "updated_at": "",
         "url": "https://www.freecodecamp.comundefined"
      },
      {
         "title": "Import a Google Font",
         "completed_at": "Mar 19, 2017",
         "updated_at": "",
         "url": "https://www.freecodecamp.comundefined"
      },
      {
         "title": "Specify How Fonts Should Degrade",
         "completed_at": "Mar 19, 2017",
         "updated_at": "",
         "url": "https://www.freecodecamp.comundefined"
      },
      {
         "title": "Concatenating Strings with Plus Operator",
         "completed_at": "Apr 02, 2017",
         "updated_at": "",
         "url": "https://www.freecodecamp.comundefined"
      },
      {
         "title": "Using Objects for Lookups",
         "completed_at": "Jun 15, 2017",
         "updated_at": "",
         "url": "https://www.freecodecamp.comundefined"
      },
      {
         "title": "Watch Coding Videos on our YouTube Channel",
         "completed_at": "Jun 17, 2017",
         "updated_at": "",
         "url": "https://www.freecodecamp.com/challenges/Watch Coding Videos on our YouTube Channel"
      },
      {
         "title": "Add Images to your Website",
         "completed_at": "Jun 17, 2017",
         "updated_at": "",
         "url": "https://www.freecodecamp.comundefined"
      },
      {
         "title": "Size your Images",
         "completed_at": "Jun 18, 2017",
         "updated_at": "",
         "url": "https://www.freecodecamp.comundefined"
      },
      {
         "title": "Add Borders Around your Elements",
         "completed_at": "Jun 18, 2017",
         "updated_at": "",
         "url": "https://www.freecodecamp.comundefined"
      },
      {
         "title": "Add Rounded Corners with a Border Radius",
         "completed_at": "Jun 18, 2017",
         "updated_at": "",
         "url": "https://www.freecodecamp.comundefined"
      },
      {
         "title": "Make Circular Images with a Border Radius",
         "completed_at": "Jun 18, 2017",
         "updated_at": "",
         "url": "https://www.freecodecamp.comundefined"
      },
      {
         "title": "Link to External Pages with Anchor Elements",
         "completed_at": "Jun 18, 2017",
         "updated_at": "",
         "url": "https://www.freecodecamp.comundefined"
      },
      {
         "title": "Nest an Anchor Element within a Paragraph",
         "completed_at": "Jun 18, 2017",
         "updated_at": "",
         "url": "https://www.freecodecamp.comundefined"
      },
      {
         "title": "Make Dead Links using the Hash Symbol",
         "completed_at": "Jun 18, 2017",
         "updated_at": "",
         "url": "https://www.freecodecamp.comundefined"
      },
      {
         "title": "Turn an Image into a Link",
         "completed_at": "Jun 18, 2017",
         "updated_at": "",
         "url": "https://www.freecodecamp.comundefined"
      },
      {
         "title": "Create a Bulleted Unordered List",
         "completed_at": "Jun 19, 2017",
         "updated_at": "",
         "url": "https://www.freecodecamp.comundefined"
      },
      {
         "title": "Create an Ordered List",
         "completed_at": "Jun 19, 2017",
         "updated_at": "",
         "url": "https://www.freecodecamp.comundefined"
      },
      {
         "title": "Create a Text Field",
         "completed_at": "Jun 19, 2017",
         "updated_at": "",
         "url": "https://www.freecodecamp.comundefined"
      },
      {
         "title": "Add Placeholder Text to a Text Field",
         "completed_at": "Jun 19, 2017",
         "updated_at": "",
         "url": "https://www.freecodecamp.comundefined"
      },
      {
         "title": "Create a Form Element",
         "completed_at": "Jun 19, 2017",
         "updated_at": "",
         "url": "https://www.freecodecamp.comundefined"
      },
      {
         "title": "Add a Submit Button to a Form",
         "completed_at": "Jun 19, 2017",
         "updated_at": "",
         "url": "https://www.freecodecamp.comundefined"
      },
      {
         "title": "Use HTML5 to Require a Field",
         "completed_at": "Jun 19, 2017",
         "updated_at": "",
         "url": "https://www.freecodecamp.comundefined"
      },
      {
         "title": "Create a Set of Radio Buttons",
         "completed_at": "Jun 19, 2017",
         "updated_at": "",
         "url": "https://www.freecodecamp.comundefined"
      },
      {
         "title": "Create a Set of Checkboxes",
         "completed_at": "Jun 19, 2017",
         "updated_at": "",
         "url": "https://www.freecodecamp.comundefined"
      },
      {
         "title": "Check Radio Buttons and Checkboxes by Default",
         "completed_at": "Jun 19, 2017",
         "updated_at": "",
         "url": "https://www.freecodecamp.comundefined"
      },
      {
         "title": "Nest Many Elements within a Single Div Element",
         "completed_at": "Jul 09, 2017",
         "updated_at": "",
         "url": "https://www.freecodecamp.comundefined"
      },
      {
         "title": "Give a Background Color to a Div Element",
         "completed_at": "Nov 12, 2017",
         "updated_at": "",
         "url": "https://www.freecodecamp.comundefined"
      },
      {
         "title": "Set the ID of an Element",
         "completed_at": "Nov 12, 2017",
         "updated_at": "",
         "url": "https://www.freecodecamp.comundefined"
      },
      {
         "title": "Use an ID Attribute to Style an Element",
         "completed_at": "Nov 12, 2017",
         "updated_at": "",
         "url": "https://www.freecodecamp.comundefined"
      },
      {
         "title": "Adjusting the Padding of an Element",
         "completed_at": "Nov 12, 2017",
         "updated_at": "",
         "url": "https://www.freecodecamp.comundefined"
      },
      {
         "title": "Adjust the Margin of an Element",
         "completed_at": "Nov 12, 2017",
         "updated_at": "",
         "url": "https://www.freecodecamp.comundefined"
      },
      {
         "title": "Add a Negative Margin to an Element",
         "completed_at": "Nov 12, 2017",
         "updated_at": "",
         "url": "https://www.freecodecamp.comundefined"
      },
      {
         "title": "Add Different Padding to Each Side of an Element",
         "completed_at": "Nov 12, 2017",
         "updated_at": "",
         "url": "https://www.freecodecamp.comundefined"
      },
      {
         "title": "Become a Supporter",
         "completed_at": "Dec 03, 2017",
         "updated_at": "",
         "url": "https://www.freecodecamp.com/challenges/Become a Supporter"
      },
      {
         "title": "Add Different Margins to Each Side of an Element",
         "completed_at": "Dec 03, 2017",
         "updated_at": "Dec 03, 2017",
         "url": "https://www.freecodecamp.comundefined"
      },
      {
         "title": "Use Clockwise Notation to Specify the Padding of an Element",
         "completed_at": "Dec 03, 2017",
         "updated_at": "",
         "url": "https://www.freecodecamp.comundefined"
      },
      {
         "title": "Use Clockwise Notation to Specify the Margin of an Element",
         "completed_at": "Dec 03, 2017",
         "updated_at": "",
         "url": "https://www.freecodecamp.comundefined"
      },
      {
         "title": "Style the HTML Body Element",
         "completed_at": "Dec 03, 2017",
         "updated_at": "",
         "url": "https://www.freecodecamp.comundefined"
      },
      {
         "title": "Inherit Styles from the Body Element",
         "completed_at": "Dec 03, 2017",
         "updated_at": "",
         "url": "https://www.freecodecamp.comundefined"
      },
      {
         "title": "Prioritize One Style Over Another",
         "completed_at": "Dec 03, 2017",
         "updated_at": "",
         "url": "https://www.freecodecamp.comundefined"
      },
      {
         "title": "Override Styles in Subsequent CSS",
         "completed_at": "Dec 03, 2017",
         "updated_at": "",
         "url": "https://www.freecodecamp.comundefined"
      },
      {
         "title": "Override Class Declarations by Styling ID Attributes",
         "completed_at": "Dec 03, 2017",
         "updated_at": "",
         "url": "https://www.freecodecamp.comundefined"
      },
      {
         "title": "Override Class Declarations with Inline Styles",
         "completed_at": "Dec 03, 2017",
         "updated_at": "",
         "url": "https://www.freecodecamp.comundefined"
      },
      {
         "title": "Override All Other Styles by using Important",
         "completed_at": "Dec 03, 2017",
         "updated_at": "",
         "url": "https://www.freecodecamp.comundefined"
      },
      {
         "title": "Use Hex Code for Specific Colors",
         "completed_at": "Dec 03, 2017",
         "updated_at": "",
         "url": "https://www.freecodecamp.comundefined"
      },
      {
         "title": "Use Hex Code to Mix Colors",
         "completed_at": "Dec 03, 2017",
         "updated_at": "",
         "url": "https://www.freecodecamp.comundefined"
      },
      {
         "title": "Use Abbreviated Hex Code",
         "completed_at": "Dec 28, 2017",
         "updated_at": "",
         "url": "https://www.freecodecamp.comundefined"
      },
      {
         "title": "Use RGB values to Color Elements",
         "completed_at": "Dec 28, 2017",
         "updated_at": "",
         "url": "https://www.freecodecamp.comundefined"
      },
      {
         "title": "Use RGB to Mix Colors",
         "completed_at": "Dec 28, 2017",
         "updated_at": "",
         "url": "https://www.freecodecamp.comundefined"
      },
      {
         "title": "Use Responsive Design with Bootstrap Fluid Containers",
         "completed_at": "Dec 31, 2017",
         "updated_at": "Dec 31, 2017",
         "url": "https://www.freecodecamp.comundefined"
      },
      {
         "title": "Make Images Mobile Responsive",
         "completed_at": "Dec 31, 2017",
         "updated_at": "",
         "url": "https://www.freecodecamp.comundefined"
      },
      {
         "title": "Center Text with Bootstrap",
         "completed_at": "Dec 31, 2017",
         "updated_at": "",
         "url": "https://www.freecodecamp.comundefined"
      },
      {
         "title": "Create a Bootstrap Button",
         "completed_at": "Dec 31, 2017",
         "updated_at": "",
         "url": "https://www.freecodecamp.comundefined"
      },
      {
         "title": "Create a Block Element Bootstrap Button",
         "completed_at": "Dec 31, 2017",
         "updated_at": "",
         "url": "https://www.freecodecamp.comundefined"
      },
      {
         "title": "Taste the Bootstrap Button Color Rainbow",
         "completed_at": "Dec 31, 2017",
         "updated_at": "",
         "url": "https://www.freecodecamp.comundefined"
      },
      {
         "title": "Call out Optional Actions with Button Info",
         "completed_at": "Dec 31, 2017",
         "updated_at": "",
         "url": "https://www.freecodecamp.comundefined"
      },
      {
         "title": "Warn your Users of a Dangerous Action",
         "completed_at": "Dec 31, 2017",
         "updated_at": "",
         "url": "https://www.freecodecamp.comundefined"
      },
      {
         "title": "Use the Bootstrap Grid to Put Elements Side By Side",
         "completed_at": "Feb 11, 2018",
         "updated_at": "",
         "url": "https://www.freecodecamp.comundefined"
      },
      {
         "title": "Learn how Script Tags and Document Ready Work",
         "completed_at": "Mar 18, 2018",
         "updated_at": "",
         "url": "https://www.freecodecamp.comundefined"
      },
      {
         "title": "Use Comments to Clarify Code",
         "completed_at": "Mar 27, 2018",
         "updated_at": "Mar 27, 2018",
         "url": "https://www.freecodecamp.comundefined"
      },
      {
         "title": "Target HTML Elements with Selectors Using jQuery",
         "completed_at": "Mar 27, 2018",
         "updated_at": "",
         "url": "https://www.freecodecamp.comundefined"
      },
      {
         "title": "Target Elements by Class Using jQuery",
         "completed_at": "Mar 30, 2018",
         "updated_at": "",
         "url": "https://www.freecodecamp.comundefined"
      }
   ]
}
    }

    if username in users:
        return jsonify(users[username])

    else:
      randomData = {}
      randomData['name'] = choice(['Jason Kirn','Angel Gonzalez','Cullen Marchenko','Angelica Smith','John Doe','Jane Doe','Adam Smith','Eve Gonzalez'])
      randomData['profileImage'] = 'https://images.pexels.com/photos/104827/cat-pet-animal-domestic-104827.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=350'
      randomData["location"] = choice(["Oakland, CA","Salinas, CA","Montgomery, AL"])
      randomData["completedChallenges"] = []

      for i in range( randint(20,80)):
        randomData["completedChallenges"].append(generatRandomChallenge())
      return jsonify(randomData)
app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))import os
from flask import Flask,request,jsonify
from random import randint,choice
app = Flask(__name__)

'https://fcc-profile-scraper.herokuapp.com/user/'
def generatRandomChallenge():

      return {
         "title": "Target Elements by Class Using jQuery",
         "completed_at":  choice(["Mar","April","May","June"]) + str(randint(1,30)) + str(randint(2016,2018)),
         "updated_at": "",
         "url": "https://www.freecodecamp.comundefined"
      }

@app.route('/')
def login():
    username = request.args.get('user')
    users = {
      'user512' :{
   "name": "Tom Lee",
   "profileImage": "https://avatars2.githubusercontent.com/u/8117421?v=4",
   "location": "Oakland, CA",
   "completedChallenges": [
      {
         "title": "Build a Tribute Page",
         "completed_at": "Apr 02, 2017",
         "updated_at": "",
         "url": "https://www.freecodecamp.com/challenges/Build a Tribute Page"
      },
      {
         "title": "Reverse a String",
         "completed_at": "May 13, 2017",
         "updated_at": "",
         "url": "https://www.freecodecamp.comundefined"
      },
      {
         "title": "Learn how Free Code Camp Works",
         "completed_at": "Jun 26, 2016",
         "updated_at": "Jun 26, 2016",
         "url": "https://www.freecodecamp.com/challenges/Learn how Free Code Camp Works"
      },
      {
         "title": "Configure your Profile",
         "completed_at": "Jun 26, 2016",
         "updated_at": "Mar 12, 2017",
         "url": "https://www.freecodecamp.com/challenges/Configure your Profile"
      },
      {
         "title": "Join a Free Code Camp Group in Your City",
         "completed_at": "Jun 26, 2016",
         "updated_at": "",
         "url": "https://www.freecodecamp.com/challenges/Join a Free Code Camp Group in Your City"
      },
      {
         "title": "Learn What to Do If You Get Stuck",
         "completed_at": "Jun 27, 2016",
         "updated_at": "",
         "url": "https://www.freecodecamp.com/challenges/Learn What to Do If You Get Stuck"
      },
      {
         "title": "Say Hello to HTML Elements",
         "completed_at": "Jun 27, 2016",
         "updated_at": "Feb 12, 2018",
         "url": "https://www.freecodecamp.comundefined"
      },
      {
         "title": "Headline with the h2 Element",
         "completed_at": "Jun 27, 2016",
         "updated_at": "Mar 15, 2018",
         "url": "https://www.freecodecamp.comundefined"
      },
      {
         "title": "Inform with the Paragraph Element",
         "completed_at": "Jun 27, 2016",
         "updated_at": "",
         "url": "https://www.freecodecamp.comundefined"
      },
      {
         "title": "Declare JavaScript Objects as Variables",
         "completed_at": "Aug 02, 2016",
         "updated_at": "",
         "url": "https://www.freecodecamp.comundefined"
      },
      {
         "title": "Construct JavaScript Objects with Functions",
         "completed_at": "Aug 02, 2016",
         "updated_at": "",
         "url": "https://www.freecodecamp.comundefined"
      },
      {
         "title": "Make Instances of Objects with a Constructor Function",
         "completed_at": "Aug 02, 2016",
         "updated_at": "",
         "url": "https://www.freecodecamp.comundefined"
      },
      {
         "title": "Create a GitHub Account and Join our Chat Rooms",
         "completed_at": "Mar 12, 2017",
         "updated_at": "",
         "url": "https://www.freecodecamp.com/challenges/Create a GitHub Account and Join our Chat Rooms"
      },
      {
         "title": "Read Coding News on our Medium Publication",
         "completed_at": "Mar 12, 2017",
         "updated_at": "",
         "url": "https://www.freecodecamp.com/challenges/Read Coding News on our Medium Publication"
      },
      {
         "title": "Delete HTML Elements",
         "completed_at": "Mar 12, 2017",
         "updated_at": "Feb 05, 2018",
         "url": "https://www.freecodecamp.comundefined"
      },
      {
         "title": "Comment out HTML",
         "completed_at": "Mar 12, 2017",
         "updated_at": "Feb 05, 2018",
         "url": "https://www.freecodecamp.comundefined"
      },
      {
         "title": "Uncomment HTML",
         "completed_at": "Mar 19, 2017",
         "updated_at": "",
         "url": "https://www.freecodecamp.comundefined"
      },
      {
         "title": "Fill in the Blank with Placeholder Text",
         "completed_at": "Mar 19, 2017",
         "updated_at": "",
         "url": "https://www.freecodecamp.comundefined"
      },
      {
         "title": "Change the Color of Text",
         "completed_at": "Mar 19, 2017",
         "updated_at": "",
         "url": "https://www.freecodecamp.comundefined"
      },
      {
         "title": "Use CSS Selectors to Style Elements",
         "completed_at": "Mar 19, 2017",
         "updated_at": "",
         "url": "https://www.freecodecamp.comundefined"
      },
      {
         "title": "Use a CSS Class to Style an Element",
         "completed_at": "Mar 19, 2017",
         "updated_at": "",
         "url": "https://www.freecodecamp.comundefined"
      },
      {
         "title": "Style Multiple Elements with a CSS Class",
         "completed_at": "Mar 19, 2017",
         "updated_at": "",
         "url": "https://www.freecodecamp.comundefined"
      },
      {
         "title": "Change the Font Size of an Element",
         "completed_at": "Mar 19, 2017",
         "updated_at": "",
         "url": "https://www.freecodecamp.comundefined"
      },
      {
         "title": "Set the Font Family of an Element",
         "completed_at": "Mar 19, 2017",
         "updated_at": "",
         "url": "https://www.freecodecamp.comundefined"
      },
      {
         "title": "Import a Google Font",
         "completed_at": "Mar 19, 2017",
         "updated_at": "",
         "url": "https://www.freecodecamp.comundefined"
      },
      {
         "title": "Specify How Fonts Should Degrade",
         "completed_at": "Mar 19, 2017",
         "updated_at": "",
         "url": "https://www.freecodecamp.comundefined"
      },
      {
         "title": "Concatenating Strings with Plus Operator",
         "completed_at": "Apr 02, 2017",
         "updated_at": "",
         "url": "https://www.freecodecamp.comundefined"
      },
      {
         "title": "Using Objects for Lookups",
         "completed_at": "Jun 15, 2017",
         "updated_at": "",
         "url": "https://www.freecodecamp.comundefined"
      },
      {
         "title": "Watch Coding Videos on our YouTube Channel",
         "completed_at": "Jun 17, 2017",
         "updated_at": "",
         "url": "https://www.freecodecamp.com/challenges/Watch Coding Videos on our YouTube Channel"
      },
      {
         "title": "Add Images to your Website",
         "completed_at": "Jun 17, 2017",
         "updated_at": "",
         "url": "https://www.freecodecamp.comundefined"
      },
      {
         "title": "Size your Images",
         "completed_at": "Jun 18, 2017",
         "updated_at": "",
         "url": "https://www.freecodecamp.comundefined"
      },
      {
         "title": "Add Borders Around your Elements",
         "completed_at": "Jun 18, 2017",
         "updated_at": "",
         "url": "https://www.freecodecamp.comundefined"
      },
      {
         "title": "Add Rounded Corners with a Border Radius",
         "completed_at": "Jun 18, 2017",
         "updated_at": "",
         "url": "https://www.freecodecamp.comundefined"
      },
      {
         "title": "Make Circular Images with a Border Radius",
         "completed_at": "Jun 18, 2017",
         "updated_at": "",
         "url": "https://www.freecodecamp.comundefined"
      },
      {
         "title": "Link to External Pages with Anchor Elements",
         "completed_at": "Jun 18, 2017",
         "updated_at": "",
         "url": "https://www.freecodecamp.comundefined"
      },
      {
         "title": "Nest an Anchor Element within a Paragraph",
         "completed_at": "Jun 18, 2017",
         "updated_at": "",
         "url": "https://www.freecodecamp.comundefined"
      },
      {
         "title": "Make Dead Links using the Hash Symbol",
         "completed_at": "Jun 18, 2017",
         "updated_at": "",
         "url": "https://www.freecodecamp.comundefined"
      },
      {
         "title": "Turn an Image into a Link",
         "completed_at": "Jun 18, 2017",
         "updated_at": "",
         "url": "https://www.freecodecamp.comundefined"
      },
      {
         "title": "Create a Bulleted Unordered List",
         "completed_at": "Jun 19, 2017",
         "updated_at": "",
         "url": "https://www.freecodecamp.comundefined"
      },
      {
         "title": "Create an Ordered List",
         "completed_at": "Jun 19, 2017",
         "updated_at": "",
         "url": "https://www.freecodecamp.comundefined"
      },
      {
         "title": "Create a Text Field",
         "completed_at": "Jun 19, 2017",
         "updated_at": "",
         "url": "https://www.freecodecamp.comundefined"
      },
      {
         "title": "Add Placeholder Text to a Text Field",
         "completed_at": "Jun 19, 2017",
         "updated_at": "",
         "url": "https://www.freecodecamp.comundefined"
      },
      {
         "title": "Create a Form Element",
         "completed_at": "Jun 19, 2017",
         "updated_at": "",
         "url": "https://www.freecodecamp.comundefined"
      },
      {
         "title": "Add a Submit Button to a Form",
         "completed_at": "Jun 19, 2017",
         "updated_at": "",
         "url": "https://www.freecodecamp.comundefined"
      },
      {
         "title": "Use HTML5 to Require a Field",
         "completed_at": "Jun 19, 2017",
         "updated_at": "",
         "url": "https://www.freecodecamp.comundefined"
      },
      {
         "title": "Create a Set of Radio Buttons",
         "completed_at": "Jun 19, 2017",
         "updated_at": "",
         "url": "https://www.freecodecamp.comundefined"
      },
      {
         "title": "Create a Set of Checkboxes",
         "completed_at": "Jun 19, 2017",
         "updated_at": "",
         "url": "https://www.freecodecamp.comundefined"
      },
      {
         "title": "Check Radio Buttons and Checkboxes by Default",
         "completed_at": "Jun 19, 2017",
         "updated_at": "",
         "url": "https://www.freecodecamp.comundefined"
      },
      {
         "title": "Nest Many Elements within a Single Div Element",
         "completed_at": "Jul 09, 2017",
         "updated_at": "",
         "url": "https://www.freecodecamp.comundefined"
      },
      {
         "title": "Give a Background Color to a Div Element",
         "completed_at": "Nov 12, 2017",
         "updated_at": "",
         "url": "https://www.freecodecamp.comundefined"
      },
      {
         "title": "Set the ID of an Element",
         "completed_at": "Nov 12, 2017",
         "updated_at": "",
         "url": "https://www.freecodecamp.comundefined"
      },
      {
         "title": "Use an ID Attribute to Style an Element",
         "completed_at": "Nov 12, 2017",
         "updated_at": "",
         "url": "https://www.freecodecamp.comundefined"
      },
      {
         "title": "Adjusting the Padding of an Element",
         "completed_at": "Nov 12, 2017",
         "updated_at": "",
         "url": "https://www.freecodecamp.comundefined"
      },
      {
         "title": "Adjust the Margin of an Element",
         "completed_at": "Nov 12, 2017",
         "updated_at": "",
         "url": "https://www.freecodecamp.comundefined"
      },
      {
         "title": "Add a Negative Margin to an Element",
         "completed_at": "Nov 12, 2017",
         "updated_at": "",
         "url": "https://www.freecodecamp.comundefined"
      },
      {
         "title": "Add Different Padding to Each Side of an Element",
         "completed_at": "Nov 12, 2017",
         "updated_at": "",
         "url": "https://www.freecodecamp.comundefined"
      },
      {
         "title": "Become a Supporter",
         "completed_at": "Dec 03, 2017",
         "updated_at": "",
         "url": "https://www.freecodecamp.com/challenges/Become a Supporter"
      },
      {
         "title": "Add Different Margins to Each Side of an Element",
         "completed_at": "Dec 03, 2017",
         "updated_at": "Dec 03, 2017",
         "url": "https://www.freecodecamp.comundefined"
      },
      {
         "title": "Use Clockwise Notation to Specify the Padding of an Element",
         "completed_at": "Dec 03, 2017",
         "updated_at": "",
         "url": "https://www.freecodecamp.comundefined"
      },
      {
         "title": "Use Clockwise Notation to Specify the Margin of an Element",
         "completed_at": "Dec 03, 2017",
         "updated_at": "",
         "url": "https://www.freecodecamp.comundefined"
      },
      {
         "title": "Style the HTML Body Element",
         "completed_at": "Dec 03, 2017",
         "updated_at": "",
         "url": "https://www.freecodecamp.comundefined"
      },
      {
         "title": "Inherit Styles from the Body Element",
         "completed_at": "Dec 03, 2017",
         "updated_at": "",
         "url": "https://www.freecodecamp.comundefined"
      },
      {
         "title": "Prioritize One Style Over Another",
         "completed_at": "Dec 03, 2017",
         "updated_at": "",
         "url": "https://www.freecodecamp.comundefined"
      },
      {
         "title": "Override Styles in Subsequent CSS",
         "completed_at": "Dec 03, 2017",
         "updated_at": "",
         "url": "https://www.freecodecamp.comundefined"
      },
      {
         "title": "Override Class Declarations by Styling ID Attributes",
         "completed_at": "Dec 03, 2017",
         "updated_at": "",
         "url": "https://www.freecodecamp.comundefined"
      },
      {
         "title": "Override Class Declarations with Inline Styles",
         "completed_at": "Dec 03, 2017",
         "updated_at": "",
         "url": "https://www.freecodecamp.comundefined"
      },
      {
         "title": "Override All Other Styles by using Important",
         "completed_at": "Dec 03, 2017",
         "updated_at": "",
         "url": "https://www.freecodecamp.comundefined"
      },
      {
         "title": "Use Hex Code for Specific Colors",
         "completed_at": "Dec 03, 2017",
         "updated_at": "",
         "url": "https://www.freecodecamp.comundefined"
      },
      {
         "title": "Use Hex Code to Mix Colors",
         "completed_at": "Dec 03, 2017",
         "updated_at": "",
         "url": "https://www.freecodecamp.comundefined"
      },
      {
         "title": "Use Abbreviated Hex Code",
         "completed_at": "Dec 28, 2017",
         "updated_at": "",
         "url": "https://www.freecodecamp.comundefined"
      },
      {
         "title": "Use RGB values to Color Elements",
         "completed_at": "Dec 28, 2017",
         "updated_at": "",
         "url": "https://www.freecodecamp.comundefined"
      },
      {
         "title": "Use RGB to Mix Colors",
         "completed_at": "Dec 28, 2017",
         "updated_at": "",
         "url": "https://www.freecodecamp.comundefined"
      },
      {
         "title": "Use Responsive Design with Bootstrap Fluid Containers",
         "completed_at": "Dec 31, 2017",
         "updated_at": "Dec 31, 2017",
         "url": "https://www.freecodecamp.comundefined"
      },
      {
         "title": "Make Images Mobile Responsive",
         "completed_at": "Dec 31, 2017",
         "updated_at": "",
         "url": "https://www.freecodecamp.comundefined"
      },
      {
         "title": "Center Text with Bootstrap",
         "completed_at": "Dec 31, 2017",
         "updated_at": "",
         "url": "https://www.freecodecamp.comundefined"
      },
      {
         "title": "Create a Bootstrap Button",
         "completed_at": "Dec 31, 2017",
         "updated_at": "",
         "url": "https://www.freecodecamp.comundefined"
      },
      {
         "title": "Create a Block Element Bootstrap Button",
         "completed_at": "Dec 31, 2017",
         "updated_at": "",
         "url": "https://www.freecodecamp.comundefined"
      },
      {
         "title": "Taste the Bootstrap Button Color Rainbow",
         "completed_at": "Dec 31, 2017",
         "updated_at": "",
         "url": "https://www.freecodecamp.comundefined"
      },
      {
         "title": "Call out Optional Actions with Button Info",
         "completed_at": "Dec 31, 2017",
         "updated_at": "",
         "url": "https://www.freecodecamp.comundefined"
      },
      {
         "title": "Warn your Users of a Dangerous Action",
         "completed_at": "Dec 31, 2017",
         "updated_at": "",
         "url": "https://www.freecodecamp.comundefined"
      },
      {
         "title": "Use the Bootstrap Grid to Put Elements Side By Side",
         "completed_at": "Feb 11, 2018",
         "updated_at": "",
         "url": "https://www.freecodecamp.comundefined"
      },
      {
         "title": "Learn how Script Tags and Document Ready Work",
         "completed_at": "Mar 18, 2018",
         "updated_at": "",
         "url": "https://www.freecodecamp.comundefined"
      },
      {
         "title": "Use Comments to Clarify Code",
         "completed_at": "Mar 27, 2018",
         "updated_at": "Mar 27, 2018",
         "url": "https://www.freecodecamp.comundefined"
      },
      {
         "title": "Target HTML Elements with Selectors Using jQuery",
         "completed_at": "Mar 27, 2018",
         "updated_at": "",
         "url": "https://www.freecodecamp.comundefined"
      },
      {
         "title": "Target Elements by Class Using jQuery",
         "completed_at": "Mar 30, 2018",
         "updated_at": "",
         "url": "https://www.freecodecamp.comundefined"
      }
   ]
}
    }

    if username in users:
        return jsonify(users[username])

    else:
      randomData = {}
      randomData['name'] = choice(['Jason Kirn','Angel Gonzalez','Cullen Marchenko','Angelica Smith','John Doe','Jane Doe','Adam Smith','Eve Gonzalez'])
      randomData['profileImage'] = 'https://images.pexels.com/photos/104827/cat-pet-animal-domestic-104827.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=350'
      randomData["location"] = choice(["Oakland, CA","Salinas, CA","Montgomery, AL"])
      randomData["completedChallenges"] = []

      for i in range( randint(20,80)):
        randomData["completedChallenges"].append(generatRandomChallenge())
      return jsonify(randomData)
app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))

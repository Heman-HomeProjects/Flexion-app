# ** Flexion conversion app **

## App introduction

###### The Flexion app converter converts

###### -- temperatures between kelvin, celsius, fahrenheit, and rankine

###### -- volumes between liters, tablespoons, cubic-inches, cups, cubic-feet, and gallons

## Steps to use the app

###### 1. Enter a numerical value in the "Input Numerical Value"

###### 2. Enter a "Input Unit of Measure " . e.g: celsius, fahrenheit, liter etc.

###### 3. Enter " Target Unit of Measure " e.g: kelvin, rankine, gallon etc.

###### 4. Enter a numeric value to the tenths place in "Student's Unit of Response"

###### 5. Hit the "Submit" button

###### 6. If the Student unit of response matches the result of the source to target conversion result, the "Output" will display "correct" else "incorrect"

###### 7. The " Actual Result " will display the calculated result so the user can see actual calculated result after the conversion

**Important Notes:**

_if the user enters a temperature unit as source input and volume unit as target entry or vice versa, the system will throw an error_ "Invalid Target Unit of Measure"

_If a user enters a non-numeric values in either " Input Numerical Value " or " Student's Unit of Response " box, the system will display an error_ "Invalid input - Not a numeric value!"

## Steps to install/run the app

###### 1. Install python on your system ( run python 3.xx version)

###### 2. git clone the repository: https://github.com/hemanmalik/Flexion_CICD.git

###### 3. Flexion is the dev branch and main is the master branch

###### 4. Once cloned, open the terminal on your system and cd into the "Flexion-app" folder on your system where you cloned your repo and run command **"python flexionapp.py"**

###### 5. If your system has both python 2.xx and 3.xx version installed, you may have to run "python3 flexionapp.py" to specify to run with python version 3

###### 6. Once a user intiate the command, a small app with GUI interface will open up and you can follow steps laid above to use the app.

###### The logo would look like this on your machine dock

![image](https://user-images.githubusercontent.com/8081454/102726008-c333ee00-42e0-11eb-937c-6460249dafc3.png)

###### -- The user interface of the app looks like below

![image](https://user-images.githubusercontent.com/8081454/102697518-eb95ec80-41fb-11eb-93a8-dc9a60fe375a.png)

## Upcoming updates to the app

###### 1. Add a drop down menu so a user dont have to manually type source and target temperature/volume conversion values to avoid spelling mistakes

###### 2. Fix the error output values to define if the non-numeric value is provided in the " Input Numerical Value " or " Student's Unit of Response " box for better user experience

###### 3. Fix indentation of the labels to "Left aligned"

###### 4. Add instructions on how to use the app in the app interface

###### 5. Bind Return/Enter from keyboard to "Submit" button so user dont have to manually click the submit button.

###### 6. Add Organization logo and add colour to the app background

###### 7. Add app title on the top beside the logo

## CI/CD

###### 1. Everytime the code is merged into "main" branch the code is deployed to "flexion-master" s3 bucket on AWS

###### 2. To make updates to the main branch, push the changes to "flexion-dev" branch and then merge to main

###### 3. once the changes in code on your local are made run below commands:

###### -- git add --all or add filename

###### -- git commit -m " message "

###### -- git push origin branch_name ( flexion-dev in this case)

###### -- Create a new pull request to merge to main branch and then merge the request.

###### -- The CI/CD pipeline will kick off using the Travis CI and which will kick off the deploy.sh script and copy the files to s3 bucket.

###### -- The Travis CI link: https://travis-ci.com/dashboard

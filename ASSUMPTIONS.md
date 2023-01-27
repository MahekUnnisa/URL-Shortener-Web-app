# My assumptions about the project
## The statement provided
At NewsBytes, the marketing department often finds themselves using long URLs with UTM tracking.

These URLs often travel in emails, getting copied over sheets and docs, thereby are at risk of getting ruined by formatters. 

Objective is to design and implement a URL hashing system which would allow us to overcome these problems primarily. Things to keep in mind: 

- URL length can’t be restricted. 
- Query parameters can’t be ignored. 
- Click tracking should be there but hashed URLs can be made privacy-aware. 
- May be used in a secure manner as the generated URL might be single (limited) use only. 
- You can choose to make the application with UI or only API.

## Requirements:
Finish the system so that it is ready to execute out of the box.
Remember you are making a complete system, so you are free to implement any way you deem fit.

## Suggestions:

- Add a description about your architecture choice and reasoning behind in readme.md.
- Add steps to deploy/use the application and tests (if added) in setup.md.
- If by the end of completing the assignment, you still feel you couldn’t do all you wanted, add a todo.md.
- Add assumptions.md to let us know what you assumed.

Google is your oyster and open source is your pearl, use them wisely but more importantly acknowledge them.

## Recommendations
- No one beats the age old local development. However, you can use technologies available from AWS such as API Gateway, Lambda Functions DynamoDB, S3 and whatever else you think is necessary, just be careful not to leave the freetier. 
- You can use the Serverless framework at serverless.com to make it easy to build and control your application if you use Lambda Functions for your API.

## Judgement criteria:
We will do a code review and things we will consider are:
- Git : Commits and organization of the changes made - multiple branches are not required, if you feel necessary feel free.
- Code organization : Are the scope of the functions well defined and simple?
- Objectivity : Does the project attack the proposal simply and objectively?
- Maintainability : How difficult is it for another developer to make changes?
- Scalability : How the proposed solution/approach scales up.
## What we would like:
- Performance and code readability, remember that both can and should go together.
- Clean code
- Tests
- Swagger of the application.
- Automated deploy pipeline (if required).
## Result:
Once we finish the code review we will contact you.
## Time duration
It would take at least 4 hours to get it up and running but you have up till 24 hours. The solution should justify the time taken.
## Submission:
Please submit a zip file including the git.

## What I understood

1. I assigned to build a URL hashing system for long and complex URLs which usually lose format when pasted in Emails or anywhere.
2. I understood that I need to build a shortener to shorten the link and make it more manageable.
 - Shorten a link
 - add a custom string so we can organize topic wise
 - add a random string at the end, this is my preference but we can add our own custom string again and change the logic
 - We can have a dashboard where we can manage and see all the links details
 - I also added a click count feature which shows how many times each url is viewed or clicked
 - every link will have a specified expiry date
 - the links which are expired can be viewed with a  different color on the dashboard
 - All this features can be built with a basic UI
 - I will not focus much on the UI and take some internet based source code.
- Each URL is clickable in Dashboard and opens in new tab
 
 Please check TODO.md to see what I wanted to implemented more.
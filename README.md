# Step by Step Guide to Deploying and Using this application on the Web

## Deploying
1. launch an EC2 instance
2. connect to it via git bash
3. use sudo apt update and sudo apt upgrade -y to have it ready to use
4. clone the git repo using: git clone git@github.com:zmusa88/books.git
5. use the cd command to move into the books folder
6. use sudo apt sudo apt install python3-venv -y then python3 -m venv .venv and source .venv/bin/activate to set up your python virtual environment
7. use pip to install Flask
8. go to your instance details and select your security group
9. add a new rule to your inbound rules:
                 - type: custom tcp
                 - port range: 5000
                 - source: anywhere
10. go back to git bash and run python -m book_app
11. the application should be running on 52.59.158.179:5000

## Using
1. to use the application just change what comes after 52.59.158.179:5000 in the search bar of your browser. 
2. home (/) or /books will show you all the books on record
3. /books/title will should you all the titles of the books on record
4. to navigate to a specific book, either use /books/<int:book_id> or /books/title/<string:title> 


image of the application working:
<img width="617" height="269" alt="image" src="https://github.com/user-attachments/assets/f62e70b3-277a-48c4-931f-67f13c174b3b" />

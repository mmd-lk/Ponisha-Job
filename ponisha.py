# hello there! don't forget to leave a star: https://github.com/mmd-lk
import time
try:
    import requests
except ImportError:
    print('Requests.py is not installed! Install it via "pip install requests" in the terminal'
          '\nthe script will automatically close in 5 seconds')
    time.sleep(5)
    raise SystemExit
try:
    from bs4 import BeautifulSoup
except ImportError:
    print('bs4.py is not installed! Install it via "pip install bs4" in the terminal'
          '\nthe script will automatically close in 5 seconds')
    time.sleep(5)
    raise SystemExit


class ponisha():
    
    def __init__(self, username , password):
        self.username = username
        self.password = password
                
    ses = requests.session()
    BasicUrl = 'https://ponisha.ir/login'
    
    def UrlLogin(self):
    
        header_log = {
                'accept': 'application/json, application/json;q=0.8, text/plain;q=0.5, */*;q=0.2'
                }
        req = self.ses.get(self.BasicUrl,headers = header_log)
        soup = BeautifulSoup(req.text, 'html.parser')
        csrf = soup.find("meta", {"name":"csrf-token"})['content']
        data = '{''"username"'':' +'"'+ str(self.username) +'"'+ ',''"password"'':'+'"'+ str(self.password) +'"'+'}'
        hed = {
        'x-csrf-token': str(csrf),
        'accept': 'application/json, application/json;q=0.8, text/plain;q=0.5, */*;q=0.2',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9',
        'content-length': '49',
        'content-type': 'application/json'}
        reqLog = self.ses.post(self.BasicUrl,data=data,headers=hed)
        if reqLog.text == '{"action":"redirect","url":"https:\/\/ponisha.ir\/dashboard"}':
            print("login")
            ProjectData= self.ses.get('https://ponisha.ir/search/projects/my-skills')
            soup = BeautifulSoup(ProjectData.text, 'html.parser')
            soupJob = soup.find("ul", {"class":"list-unstyled projects"}).findAll("li",{"class":"item"})
            Counter = 0
            for i in soupJob:
                Counter += 1
                TitleProject = i.find("div",{"class":"title"}).find("a")['title']
                BudgetProject = i.find("div",{'class':"budget"}).find('span')['amount']
                LinkProject = i.find("a",{'class':'absolute'})['href']
                SkillProject = i.find("div",{'class':"labels"}).findAll('a', {'class':'no-link-inherit'})
                ListSkill = []
                for skill in SkillProject:
                    ListSkill.append(skill['title'])
                Project = f"ID : {Counter}\nTitle : {TitleProject}\nBudget : {BudgetProject}rial\nLink : {LinkProject}\nSkill : {ListSkill}"
                print(Project)
        elif reqLog.status_code == 422 : 
            print('Your password or username is wrong')


def main():
    username = input('Enter your username : ')
    password = input('Enter your password : ')           
    Object = ponisha(username=username,password=password)
    Object.UrlLogin()



if __name__ == "__main__":
    main()
import os
import json
global path1

class directory(object):
    def __init__(self,title):
        global path1
        self.htmlpath="/"
        path1=os.getcwd()
        self.path1=os.getcwd()
        self.title = title
        self.mytitle = title
        self.js=""
        self.url=""
        self.json=None
        self.userid=""
        self.redirect=None
        self.email=""
        self.css=""
        self.menu=""
        self.path=os.getcwd()+"/mespages"
        print(self.get_file_with_path("header.html"))
        header1=self.get_file_with_path("header.html")
        footer1=self.get_file_with_path("footer.html")
        self.header=header1.read()
        self.path=""
        self.footer=footer1.read()
    def set_header_with_path(self,header): 
        header1=self.get_file_with_path(header)
        self.header=header1.read()
    def set_footer_with_path(self,footer):   
        footer1=self.get_file_with_path(footer)
        self.footer=footer1.read()
    def edit_title(self,str):
        self.title = str+ " - "+self.mytitle
    def set_title(self,str):
        self.title = str
    def get_title(self):
        return self.title
    def get_email(self):
        return self.email
    def set_email(self,email):
        self.email=email
    def get_json(self):
        return json.dumps(self.json, ensure_ascii=False).replace("'",'"')
        
    def set_json(self,json):
        self.json=json
    def get_redirect(self):
        return self.redirect
    def set_redirect(self,redirect):
        self.redirect=redirect
    def get_userid(self):
        return str(self.userid)
    def set_userid(self,userid):
        self.userid=userid
    def get_menu(self):
        return self.menu
    def set_menu(self,menu):
        self.menu=menu
    def get_url(self):
        return self.url
    def set_url(self,url):
        self.url=url
    def get_content(self):
        return self.content
    def set_content(self,content):
        self.content=content
    def get_header(self):
        return self.header
    def set_header(self,myheader):
        self.header=myheader   
    def get_footer(self):
        return self.footer
    def set_footer(self,myfooter):
        self.footer=myfooter
    def set_filename(self,name):  
        self.filename=name
    def title(self,title):
        self.title = title
    def get_title(self):
        return self.title
    def get_js(self):
        return self.js
    def set_js(self,js):
        self.js=js
    def add_js(self,js):
        self.js+="<script type=\"text/javascript\" src=\""+self.get_htmlpath()+"/"+js+"\"></script>"
    def get_htmlpath(self):
        return self.htmlpath
    def trouver_fichier(self,urlpath,myroutes):
        file=None
        paths=[]
        paths.append(self.path1+urlpath.split("?")[0].replace(".html","")+".html")
        paths.append(self.path1+urlpath.split("?")[0]+"index.html")
        paths.append(path1+urlpath.split("?")[0]+"/index.html")
        paths.append(self.path1+urlpath.split("?")[0].replace(".html",""))
        paths.append(self.path1+str(myroutes.get(urlpath.split("?")[0]))+".html")
        for i in paths:
            try:
                print(i)
                if self.get_file(i) is not None:
                    file=self.get_file(i)
            except:
                print("erreur")
        return file        
    def get_file(self,file):
        
        return open(file,'r')
    def get_file_with_path(self,file):
        
        return open(self.path+"/"+file,'r')
    def add_css(self,css):
        self.css+="<link rel=\"stylesheet\" href=\""+self.get_htmlpath()+"/"+css+"\"/>"
    def get_css(self):
        return self.css
    def set_css(self,css):
        self.css=css
    def get_path(self):
        return self.path
    def get_filename(self):
        return self.filename
    def set_path(self,mypath):
        self.htmlpath=mypath.replace("./","/")
        self.path=self.path1+mypath.replace("./","/")
    def get_filename_path(self,file):
        return self.path+"/"+file
    def get_css_dir_path(self):
        return "./css/" 
    def get_js_dir_path(self):
        return "./js/" 
    def get_image_dir_path(self):
        return "./images/" 
    def path(self,path):
        try:
            self.path = self.path1+path.replace("./","/")
        except Exception as e:
            print(e,"erreur  1111")

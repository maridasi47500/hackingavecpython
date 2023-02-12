# -*- coding: utf-8 -*-
import json
import binascii
import random as rand
import smtplib
import datetime
import sys
import requests
global session
import sqlite3
global copy
global render_pages
global connection
global get_file
global switcher

switcher={
'html':'text/html',
'css':'text/css',
'json':'application/json',
'js':'text/javascript',
'png':"image/png",
'ico':'image/vnd.microsoft.icon'
}


connection = sqlite3.connect("db_burger090ERYYjhTHYYYjj7.db")

# cursor
global crsr
crsr = connection.cursor()

myusers=crsr.execute("PRAGMA table_info([users])")
table_users = myusers.fetchall()
global force_to_unicode
global decode_any_string
def decode_any_string(text):
    try:
        print(text)
        return force_to_unicode(text)
    except UnicodeEncodeError as e:
        print(type(e))
        print('gerer cette erreur')
        return text.encode('utf-8')
    except UnicodeDecodeError as e:
        print(type(e))
        print('gerer cette erreur')
        return text

def force_to_unicode(text):
    "If text is unicode, it is returned as is. If it's str, convert it to Unicode using UTF-8 encoding"
    return text if isinstance(text, unicode) else text.decode('utf-8')
session = requests.Session()
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from os.path import exists
from urlparse import urlparse, parse_qs
import os
global path1
path1=os.getcwd()
sys.path.append(os.path.abspath(os.getcwd()+"/pythonfile"))
from myfunc import *
from pagehtml import *
import codecs
import re

f=open(path1+"/mespages/dump.sql")
for h in f.read().split(";"):
    print(h)
    crsr.execute(h)
    connection.commit()
global Program
global get_file
global get_file_dir
def get_file(file):
    print("get file:")
    print(Program.get_filename_path(file))
    return open(Program.get_filename_path(file),'r')
def get_file_dir(file,dir):
    print("get file:"+dir)
    Program.set_path(dir)
    return open(Program.get_path()+"/"+file,'r')

global mycard
global myparams


from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import SocketServer

import random

# connecting to the database
global infotable
def infotable(tablename):
    crsr.execute("PRAGMA table_info(["+tablename+"])")
    connection.commit()
    matable=crsr.fetchall()
    return matable
def display_collection(sql,sqlargs,templatename,errormessage,tablename,sortby = False,templatesortby = False):
    idprecedent=0
    print(sqlargs)
    print(len(sqlargs))
    print(sql,sqlargs,templatename,errormessage,tablename)
    crsr.execute("PRAGMA table_info(["+tablename+"])")
    connection.commit()
    matable=crsr.fetchall()
    Program.set_path("./mespages")
    h=get_file(templatename+".html")
    template=force_to_unicode(h.read())
    mysql=sql % sqlargs
    print(mysql)
    crsr.execute(mysql)
    connection.commit()
    res=crsr.fetchall()
    myfigure=""
    x=0
    mytemplate=""
    if len(res) > 0:
        print("plusieurs "+tablename)

        for re in res:
            paspremier = False
            mytemplate=force_to_unicode(template)
            for x in range(len(re)):
                print(x)
                print(re[x])
                z=re[x]
                strrep=force_to_unicode("(%s)" % (matable[x][1]))
                print(strrep)
                if type(z) == int or type(z) == float:
                    z=str(z)
                if z is not None:
                    mytemplate=mytemplate.replace(strrep, force_to_unicode(z))
                if matable[x][1] == sortby:
                    if idprecedent != 0:
                        if re[x] != idprecedent:
                            if paspremier:
                                myfigure+="</div>"
                                paspremier = True
                            Program.set_path("./mespages")
                            kk=get_file(templatesortby)
                            kk=kk.read()
                            y=0
                            for y in range(len(re)):
                                mystrrep="(%s)" % (matable[y][1])
                                kk=kk.replace(mystrrep, force_to_unicode(str(re[y])))
                            myfigure += kk
                    idprecedent=re[x]

            myfigure+=mytemplate
            myfigure+="</div>"
        return myfigure
    else:
        return force_to_unicode("<p>"+errormessage+"</p>")
global __words__
__words__ = ""
def render_figure(pathname):
    try:
        global path1
        path1=os.getcwd()
        Program.set_filename(pathname)
        print("render figure")
        print('ok')
        p1=Program.get_path
        p2=Program.get_filename
        print("okdac")
        print(p1())
        print("okokdac")
        print(p2())
        print(p1()+p2())
        print('dac')
        title=Program.get_title
        try:
            print(session.current_user)
            Program.set_path("./mespages")
            h=get_file("mynavsignedin.html")
            Program.set_menu(h.read())
        except:
            h=open("./mespages/mynav.html",'r')
            Program.set_menu(h.read())
        header=Program.get_header
        content=Program.get_content
        footer=Program.get_footer
        layout=Program.get_layout()
        if layout == False:
            print("content")
            try:
                html=decode_any_string(myparams(content()))
            except UnicodeEncodeError as e:
                print(type(e))
                print('gerer cette erreur')
                html=myparams(content()).encode('utf-8')
            except UnicodeDecodeError as e:
                print(type(e))
                print('gerer cette erreur')
                html=myparams(content())
        else:
            html="<!doctype html>"
            html+="<html>"
            html+="<head>"
            html+="<meta charset=\"UTF-8\">"
            html+="<title>"
            print("title")
            html+=title()
            html+="</title>"
            html+="<link rel=\"icon\" href=\"/images/logo.png\">"
            html+="<link rel=\"stylesheet\" href=\"/css/css.css\"/>"
            html+=Program.get_css()
            html+="</head>"
            html+="<body>"
            print("header")
            try:
                html+=decode_any_string(header())
            except UnicodeEncodeError as e:
                print(type(e))
                print('header gerer cette erreur')
                html+=header().encode('utf-8')
            except UnicodeDecodeError as e:
                print(type(e))
                print('gerer cette erreur')
                html+=header()
            html+="<main>"
            print("content")
            try:
                html+=decode_any_string(myparams(content()))
            except UnicodeEncodeError as e:
                print(type(e))
                print('gerer cette erreur')
                html+=myparams(content()).encode('utf-8')
            except UnicodeDecodeError as e:
                print(type(e))
                print('gerer cette erreur')
                html+=myparams(content())
            print("footer")
            print("type footer")

            print(type(force_to_unicode(footer())))

            try:
                html+=decode_any_string(footer())
            except UnicodeEncodeError as e:
                print(type(e))
                print('gerer cette erreur')
                html+=footer().encode('utf-8')
            except UnicodeDecodeError as e:
                print(type(e))
                print('gerer cette erreur')
                html+=footer()
            print("footer ajouté")
            html+="</main>"
            print("type menu")
            print(type(Program.get_menu()))
            try:
                html+=force_to_unicode(Program.get_menu())
            except UnicodeEncodeError as e:
                print(type(e))
                print('gerer cette erreur')
                html+=Program.get_menu().encode('utf-8')
            except UnicodeDecodeError as e:
                print(type(e))
                print('gerer cette erreur')
                html+=Program.get_menu()
            print("meu ajouté")
            html+="<script src=\"/js/jquery.js\"></script>"
            html+="<script src=\"/js/js.js\"></script>"
            html+=Program.get_js()
            html+="</body>"
            html+="</html>"
            #print(html)
            print("fin balise")
        result = re.search('<li class=\"mycat\">(.*?)</li>', html)
        #print(result.group(1))
        __words__ = result.group(1) if result is not None else ''
        print("===words")
        #print(__words__)
        mychemin=p1()+("" if (p1()[-1]=="/" or p2()[0] == "/") else "/")+p2()
        print(mychemin)
        #try:
        #    s1=(html)
        #except Exception as e:
        #    print(e)
        #    s1=(html)
        #    print(type(s1))
        #s1=(html).encode("ascii", "ignore")
        print(type(html))
        if isinstance(html,str):
            s1=html
        else:
            s1=html.encode('utf-8')
        return s1
        #f=codecs.open(mychemin,'w')

        #print(type(s1))
        #f.write(s1)
        #f.close()
        #if (__words__).rstrip() == "Full Menu":
        #print(Program.get_path())
    except Exception as e:
        print(e,'erreru')

# SQL command to create a table in the database
f=codecs.open(path1+"/mespages/dump.sql")
sql_command = f.read()
global myroutes


global splitparams
def splitparams(x):
    return x.split("=")
def myparams(x):
    myvar={
    'monemailici': Program.get_email(),
    'monuseridici': Program.get_userid()
    }
    for y in myvar:
        x=x.replace(y,myvar[y])
    return x

def bootstrapjs(params = None):
    h="""  """
    return h

def bootstrapcss(params = None):
    h="""  """
    return h

def render_pages(params = None):
    home()
    menu()
    signup()
    signin()
    erreur404()
    myaccountinfo()
def copy(params = None):
    os.system("cp "+path1+"/mespages/css/*.css "+path1+"/css")
    os.system("cp "+path1+"/mespages/*.js "+path1+"/js")

Program=directory("Burger King")
#Program.path("./")
class Header:
    global set_my_header
    global set_my_footer

    def set_my_header(headername):
        try:
            Program.set_path("./mespages")
            fff=get_file(headername+".html")
            myheader=fff.read()
            Program.set_header(myheader)
        except IOError:
            Program.set_header("")

    def set_my_footer(headername):
        try:
            Program.set_path("./mespages")
            fff=get_file(headername+".html")
            myfooter=fff.read()
            Program.set_footer(myfooter)
        except IOError:
            Program.set_footer("")

class S(BaseHTTPRequestHandler):
    def _set_headers(self,myheader='text/html'):
        self.send_response(200)
        self.send_header('Content-type', myheader)
        self.end_headers()

    def do_GET(self):
        print("=========new route GET====================")

        try:
            Program=directory("Burger King")
            #Program.path("./")
            Program.set_url(self.path)
            urlpath=self.path
            myurlpath=urlpath.split("?")[0]

            #f = open("index.html", "r")
            query_components = parse_qs(urlparse(urlpath).query)

            try:
                query_components["userid"]=[session.current_user[0]]
            except:
                print("aucun user connecté")
            #print(query_components)
            print(myurlpath)
            crsr.execute("select * from posts")
            connection.commit()
            g=crsr.fetchall()
            if len(g) > 0:
                for h in g:
                    print(h[0],h[1],h[2],h[3])
                    if myurlpath=="/posts/"+str(h[0]):
                        query_components["id"]=[str(h[0])]
                    myroutes["/posts/"+str(h[0])] = showpost
            crsr.execute("select * from scripts")
            connection.commit()
            g=crsr.fetchall()
            if len(g) > 0:
                for h in g:
                    if myurlpath=="/scripts/"+str(h[0]):
                        query_components["id"]=[str(h[0])]
                    myroutes["/scripts/"+str(h[0])] = showscript

            try:
                print(" route_post={")
                print('my path')
                print(myurlpath)
                if myroutes.get(myurlpath) is not None:
                    codehtml=myroutes.get(myurlpath)(query_components)

            except KeyError:
                print("erreur 6")
            #try:
                #x=myroutes.get(urlpath.split("?")[0])
                #if x is not None:
                #    Program.set_url(x)
            #except:
            #    print("pas d'autre route")
            print(urlpath)
            print('my url get')
            #self.data_string = params
            #os.system("echo \""+urlpath+"\"")
            copy()
            #render_pages()
            #myaccountinfo()
            #home()

            print("rendere")

            if myroutes.get(myurlpath) is not None:
                print("code html pour"+urlpath)
                res=myroutes.get(myurlpath)(query_components)
                if isinstance(res,str):
                    print('is code html')
                    codehtml=decode_any_string(force_to_unicode(codehtml))
                elif isinstance(res,object):
                    print("is object")
                    print(res)
                    Program=res
                    if Program.get_current_user() is not None:
                        print("current_user")
                        print(Program.get_current_user())
                        session.current_user=Program.get_current_user()
                    html=render_figure("my file.html")
                    print(html)
                    codehtml=decode_any_string(force_to_unicode(html))
                    print(len(codehtml))
                try:
                    code=(codehtml.decode("utf-8"))
                except UnicodeEncodeError as e:
                    print(type(e))
                    print('gerer cette erreur')
                    code=(codehtml.encode('utf-8'))
                except UnicodeDecodeError as e:
                    print(type(e))
                    print('gerer cette erreur')
                    code=(codehtml)
            if Program.get_mimetype() is not None:
                mytype=Program.get_mimetype()
            else:
                mytype=urlpath.split(".")[-1]
            print(mytype)



            print("Program.get json")
            print(Program.get_json() is None)
            print("mytype")
            print(mytype)
            print(switcher.get(mytype))


            print(myroutes.get(urlpath))
            if switcher.get(mytype) is None:
                mytype="html"
            print("get redirect "+str(Program.get_redirect()))
            if str(Program.get_redirect()) == 'None':
                if mytype != "html":
                    if switcher.get(mytype) is not None:
                        print("trouver fichier")
                        self._set_headers(switcher.get(mytype))
                        self.wfile.write(Program.trouver_fichier(urlpath,myroutes).read())
                elif route_post.get(urlpath) and Program.get_json() != "null":
                    print("return json")
                    x=Program.get_json()
                    Program.set_json(None)

                    self._set_headers(switcher.get("json"))
                    self.wfile.write(x)
                else:
                    print("my html page")
                    print(mytype)


                    self._set_headers(switcher.get(mytype))
                    self.wfile.write(code)
            else:
                print("reirect is not none")
                self.send_response(301)
                myred=Program.get_redirect()
                self.send_header('Location',myred)
                Program.set_redirect(None)
            self.end_headers()

            Program.set_js("")
        except UnboundLocalError as e:
            print("erreur get",e)
            k=get_file_dir("404.html","./erreur")
            self._set_headers(switcher.get("html"))
            self.wfile.write(k.read())
    def do_HEAD(self):
        self._set_headers()
    def do_POST(self):
        print("=========new route POST====================")

        try:
            Program=directory("Burger King")
            Program.set_url(self.path)
            urlpath=Program.get_url()

            query_components = parse_qs(urlparse(urlpath).query)

            try:
                query_components["userid"]=[session.current_user[0]]
            except:
                print("aucun user connecté")
            print "in post method"
            self.data_string = self.rfile.read(int(self.headers['Content-Length']))
            fields = parse_qs(self.data_string)
            myurlpath=urlpath.split("?")[0]
            try:
                print('my path')
                print(myurlpath)
                print(route_post.get(myurlpath))
                if route_post.get(myurlpath) is not None:
                    print("route trouve")
                    print(fields)
                    res=route_post.get(myurlpath)(fields)
                    if isinstance(res,str):
                        codehtml = res
                        print("is code HTML")
                        #print(codehtml)
                    elif isinstance(res,object):
                        print("is object")
                        print(res)
                        Program=res
                        if Program.get_current_user() is not None:
                            print("current_user")
                            print(Program.get_current_user())
                            session.current_user=Program.get_current_user()
                        #.dict2class(res.__dict__)
            except KeyError:
                print("erreur 6")


        #self.data_string = params
            urlpath=self.path
            print("redirect post:")
            print(Program.get_redirect())
            copy()
            #render_pages()
            #myaccountinfo()
            #home()
            mytype=Program.get_mimetype() or self.path.split(".")[-1]
            print(urlpath)
            print("my type")
            print(mytype)
            print("Program.get json")
            print(Program.get_json() is not None)
            print(Program.get_json())
            print(route_post.get(myurlpath))
            print("redirect")
            print(Program.get_redirect())
            print(str(Program.get_redirect()) != 'None')
            if str(Program.get_redirect()) != 'None':
                self.send_response(301)
                myred=Program.get_redirect()
                self.send_header('Location',myred)
                Program.set_redirect(None)


            elif mytype == "json":
                print("return json")
                data=Program.get_json()
                Program.set_json(None)

                self._set_headers(switcher.get("json"))
                self.wfile.write(str(data).replace("'",'"'))
            elif mytype is not None:
                if mytype != "html":
                    if switcher.get(mytype) is not None:


                        if myroutes.get(urlpath) is not None:
                            self._set_headers(switcher.get(mytype))
                            self.wfile.write(codehtml)
            else:
                print(mytype)
                self._set_headers(switcher.get(mytype))
                self.wfile.write(codehtml)
            self.end_headers()
        except UnboundLocalError:
            print("erreur post")
            k=get_file_dir("404.html","./erreur")
            self._set_headers(switcher.get("html"))
            self.wfile.write(k.read())

        return
global newuser
def newuser(params):
    Program.set_path("./mespages")
    Program.set_header(force_to_unicode(get_file("header.html").read()))
    Program.set_footer(force_to_unicode(get_file("footer.html").read()))

    Program.set_content(force_to_unicode(get_file("new_user.html").read()))
    Program.set_mimetype("html")
    Program.add_css("mycss.css")
    Program.add_js("myjs.js")
    return Program
global newscript
def newscript(params):
    Program.set_path("./mespages")
    Program.set_header(force_to_unicode(get_file("header.html").read()))
    Program.set_footer(force_to_unicode(get_file("footer.html").read()))
    Program.set_mimetype("html")

    Program.set_content(force_to_unicode(get_file("new_script.html").read()))
    Program.add_css("mycss.css")
    Program.add_js("myjs.js")
    return Program
global newpost
def newpost(params):
    Program.set_path("./mespages")
    Program.set_header(force_to_unicode(get_file("header.html").read()))
    Program.set_footer(force_to_unicode(get_file("footer.html").read()))
    Program.set_mimetype("html")

    Program.set_content(force_to_unicode(get_file("new_post.html").read()))
    Program.add_css("mycss.css")
    Program.add_js("myjs.js")
    return Program
global signin
def signin(params):
    Program.set_path("./mespages")
    Program.set_header(force_to_unicode(get_file("header.html").read()))
    Program.set_footer(force_to_unicode(get_file("footer.html").read()))
    Program.set_mimetype("html")

    Program.set_content(force_to_unicode(get_file("signin.html").read()))
    Program.add_css("mycss.css")
    Program.add_js("myjs.js")
    return Program
global home
def home(params):
    Program.set_path("./mespages")
    Program.set_header(force_to_unicode(get_file("header.html").read()))
    Program.set_footer(force_to_unicode(get_file("footer.html").read()))
    Program.set_mimetype("html")
    sql="select * from posts"

    cont=get_file("index.html").read()
    sql="select * from posts"
    cont+=display_collection(sql,(),"_post", "aucun post pour le moment","posts")
    sql="select * from scripts"
    cont+=display_collection(sql,(),"_script", "aucun script pour le moment","scripts")
    Program.set_content(force_to_unicode(cont))
    Program.add_css("mycss.css")
    Program.add_js("myjs.js")
    return Program
global showscript
def showscript(params):
    print("SHOW SCRIPT")
    Program.set_path("./mespages")
    #Program.set_header(force_to_unicode(get_file("header.html").read()))
    #Program.set_footer(force_to_unicode(get_file("footer.html").read()))
    Program.set_mimetype("html")
    id=params.get("id")[0]
    sql="select * from scripts where id = ?"
    tablename="scripts"
    crsr.execute(sql,(id))
    connection.commit()
    k=crsr.fetchall()
    if len(k) > 0:
        print(k[0])
        Program.set_content(k[0][2])
    return Program
global showpost
def showpost(params):
    Program.set_path("./mespages")
    #Program.set_header(force_to_unicode(get_file("header.html").read()))
    #Program.set_footer(force_to_unicode(get_file("footer.html").read()))
    Program.set_mimetype("html")
    id=params.get("id")[0]
    sql="select * from posts where id = ?"
    print(sql)
    tablename="posts"
    crsr.execute(sql,(id))
    connection.commit()
    k=crsr.fetchall()
    if len(k) > 0:
        Program.set_content(k[0][2])

    #Program.add_css("mycss.css")
    #Program.add_js("myjs.js")
    return Program
global createpost
def createpost(params):
    Program.set_path("./mespages")
    #Program.set_header(force_to_unicode(get_file("header.html").read()))
    #Program.set_footer(force_to_unicode(get_file("footer.html").read()))
    Program.set_mimetype(None)
    title=params.get("title")[0]
    content=params.get("content")[0]
    sql="insert into posts (title,content, date) values (?,?,?)"

    tablename="posts"
    crsr.execute(sql, (force_to_unicode(title),force_to_unicode(content),force_to_unicode(str(datetime.date.today()))))
    connection.commit()
    Program.set_redirect("/")
    #Program.add_css("mycss.css")
    #Program.add_js("myjs.js")
    return Program
global createscript
def createscript(params):
    Program.set_path("./mespages")
    #Program.set_header(force_to_unicode(get_file("header.html").read()))
    #Program.set_footer(force_to_unicode(get_file("footer.html").read()))
    Program.set_mimetype(None)
    title=params.get("title")[0]
    content=params.get("content")[0]
    sql="insert into scripts (title,content, date) values (?,?,?)"
    paramssql=(force_to_unicode(str(title)),force_to_unicode(str(content)),force_to_unicode(str(datetime.date.today())))
    tablename="scripts"
    crsr.execute(sql,paramssql)
    connection.commit()
    Program.set_redirect("/")
    #Program.add_css("mycss.css")
    #Program.add_js("myjs.js")
    return Program
global signinuser
def signinuser(params):
    Program.set_path("./mespages")
    #Program.set_header(force_to_unicode(get_file("header.html").read()))
    #Program.set_footer(force_to_unicode(get_file("footer.html").read()))
    Program.set_mimetype("html")
    email=params.get("username")[0]
    password=params.get("password")[0]
    sql="select * from users where email = '%s' and password = '%s'" % (email,password)
    tablename="posts"
    crsr.execute(sql)
    connection.commit()
    res=crsr.fetchall()
    if len(res) > 0:
        Program.set_current_user(res[0][0])
        Program.set_redirect("/")
    else:
        Program.set_redirect("/signin")
    #Program.add_css("mycss.css")
    #Program.add_js("myjs.js")
    return Program
global createuser
def createuser(params):
    Program.set_path("./mespages")
    #Program.set_header(force_to_unicode(get_file("header.html").read()))
    #Program.set_footer(force_to_unicode(get_file("footer.html").read()))
    Program.set_mimetype("html")
    email=params.get("username")[0]
    password=params.get("password")[0]
    sql="insert into users (email, password) values ('%s', '%s')" % (email,password)
    tablename="posts"
    crsr.execute(sql)
    connection.commit()
    #Program.set_redirect("/")
    #Program.add_css("mycss.css")
    #Program.add_js("myjs.js")
    return Program
def run(server_class=HTTPServer, handler_class=S, port=8000,host="localhost"):
    server_address = ('', port)
    print("run erver")
    httpd = server_class(server_address, handler_class)
    #print 'http://localhost:8000'
    if len(argv) == 2:
        print 'http://'+host+':'+argv[1]
    else:
        print 'http://'+host+':'+str(port)
    httpd.serve_forever()

if __name__ == "__main__":
    from sys import argv

#rewards()
#offers()
print((__words__).rstrip())

myroutes = {"/": home, "/signin": signin,"/signup": newuser, "/nouveaupost":newpost, "/nouveauscript":newscript

}
global route_post
route_post={"/signinuser":signinuser, "/createuser":createuser, "/createpost":createpost, "/createscript":createscript

}
if len(argv) == 3:
    run(port=int(argv[1]),host=argv[2])
elif len(argv) == 2:
    run(port=int(argv[1]))
else:
    run()

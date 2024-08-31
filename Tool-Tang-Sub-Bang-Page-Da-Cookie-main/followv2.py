# +------------------------------------------------------------ -+
# | Tất Cả Được Share Tại Github Của TAN DA DEN            |
# | Vui Lòng Không Sử Dụng Để Buôn Bán Dưới Bất Kì Hình Thức Nào |
# |                     -- Trân Trọng --                         |
# +--------------------------------------------------------------+

import requests,os,sys,time
from pystyle import Write, Colors,System
from datetime import datetime
try:
    os.remove('list_cookie.txt')
except:
    pass
file1 = open('list_cookie.txt','a+')
list_page = []
#file2 = open('list_page.txt','a+')
# <!--- Colors ---!>
_Black_ = '\033[1;30m'
_Red_ = '\033[1;31m'
_Green_ = '\033[1;32m'
_Yellow_ = '\033[1;33m'
_Blue_ = '\033[1;34m'
_Purple_ = '\033[1;35m'
_Cyan_ = '\033[1;36m'
_White_ = '\033[1;37m'
# <!--- Colors ---!>
def __gach__():
    Write.Print('────────────────────────────────────────────────────────\n', Colors.cyan_to_green, interval=0.00125)
def Banner():
    System.Clear()
    ban = f'''
{_Blue_}    ██╗  ██╗ ██████╗      ██╗██╗   ████████╗
{_White_}    ██║ ██╔╝██╔═══██╗     ██║██║   ╚══██╔══╝
{_Blue_}    █████╔╝ ██║   ██║     ██║██║█████╗██║   
{_White_}    ██╔═██╗ ██║   ██║██   ██║██║╚════╝██║   
{_Blue_}    ██║  ██╗╚██████╔╝╚█████╔╝██║      ██║   
{_White_}    ╚═╝  ╚═╝ ╚═════╝  ╚════╝ ╚═╝      ╚═╝   
{_Cyan_}    [{_Green_}Hello World {_Red_}- {_Green_}こんにちは世界 {_Blue_}- {_Green_}안녕 세계{_Cyan_}]
{_Purple_}─────────────────────────────────────────────────────
{_Cyan_}[ {_White_}🥱 {_Cyan_}] {_Yellow_}Author: {_Red_}TAN DA DEN  {_Red_}( {_Blue_}KsxKoji {_Red_})
{_Cyan_}[ {_White_}🥱 {_Cyan_}] {_White_}Phở Bò: {_Green_}https://www.facebook.com/profile.php?id=100088447571224
{_Cyan_}[ {_White_}🥱 {_Cyan_}] {_Red_}Du Tu Be: {_Cyan_}https://www.youtube.com/
{_Purple_}─────────────────────────────────────────────────────
'''
    for h in ban:
        sys.stdout.write(h)
        sys.stdout.flush()
        time.sleep(0.0025)

def loading(o):
    while o != 0:
        o = o - 1
        print(f'{_Cyan_}[{_Yellow_}/{_Cyan_}] {_Red_}Đang {_Green_}Loading{_Black_}, {_Yellow_}Còn {_Blue_}{o} {_Purple_}Giây {_Cyan_}Nữa      ', end='\r'); time.sleep(1/6)
        print(f'{_Cyan_}[{_Yellow_}-{_Cyan_}] {_Cyan_}Đang {_Red_}Loading{_Black_}, {_Green_}Còn {_Yellow_}{o} {_Blue_}Giây {_Purple_}Nữa      ', end='\r'); time.sleep(1/6)
        print(f'{_Cyan_}[{_Yellow_}\\{_Cyan_}] {_Purple_}Đang {_Cyan_}Loading{_Black_}, {_Red_}Còn {_Green_}{o} {_Yellow_}Giây {_Blue_}Nữa     ', end='\r'); time.sleep(1/6)
        print(f'{_Cyan_}[{_Yellow_}|{_Cyan_}] {_Blue_}Đang {_Purple_}Loading{_Black_}, {_Cyan_}Còn {_Red_}{o} {_Green_}Giây {_Yellow_}Nữa      ', end='\r'); time.sleep(1/6)
class KsxKoji():
    def __init__(self) -> None:
        #self.cookie = cookie
        #self.id_ck = cookie.split('c_user=')[1].split(';')[0]
        self.author = 'TAN DA DEN ( KsxKoji )'
        self.facebook = 'https://facebook.com/100042415576964'
        self.youtube = 'https://www.youtube.com/@WuocsDev'
    def __Get_ThongTin__(self, cookie):
        id_ck = cookie.split('c_user=')[1].split(';')[0]
        a = requests.get('https://mbasic.facebook.com/profile.php?='+id_ck, headers={'cookie': cookie}).text
        #print(f'{_Yellow_} Đang Kiểm Tra Cookie !', end='\r')
        try:
            self.name = a.split('<title>')[1].split('</title>')[0]
            self.fb_dtsg = a.split('<input type="hidden" name="fb_dtsg" value="')[1].split('"')[0]
            self.jazoest = a.split('<input type="hidden" name="jazoest" value="')[1].split('"')[0]
            return True
        except:
            print(f'{_Cyan_}<ERROR:000> {_Red_}Cookie Die, Nhập Cookie Khác !!!')
            __gach__()
            return False
    def __Get_Page__(self, cookie):
        self.dem = 0
        data = {
            'fb_dtsg': self.fb_dtsg,
            'jazoest': self.jazoest,
            'variables': '{"showUpdatedLaunchpointRedesign":true,"useAdminedPagesForActingAccount":false,"useNewPagesYouManage":true}',
            'doc_id': '5300338636681652'
            }
        getidpro5 = requests.post('https://www.facebook.com/api/graphql/', headers = {'cookie': cookie}, data = data).json()['data']['viewer']['actor']['profile_switcher_eligible_profiles']['nodes']
        for uidd in getidpro5:
            self.dem += 1
            uid_page = uidd['profile']['id']
            list_page.append(uid_page)
    def __Follow__(self, cookie, id, taget):
        self.headers = {'accept': '*/*','accept-language': 'vi,vi-VN;q=0.9,en;q=0.8','cache-control': 'max-age=0','content-encoding': 'br','content-type': 'application/x-www-form-urlencoded','cookie': f'{cookie} i_user={id};','origin': 'https://www.facebook.com','referer': 'https://www.facebook.com','sec-ch-prefers-color-scheme': 'light','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'same-origin','sec-fetch-user': '?1','sec-gpc': '1','upgrade-insecure-requests': '1','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'}    
        data = {
            'av': id,
            '__user': id,
            'fb_dtsg': self.fb_dtsg,
            'jazoest': self.jazoest,
            'fb_api_caller_class': 'RelayModern',
            'fb_api_req_friendly_name': 'CometUserFollowMutation',
            'variables': '{"input":{"attribution_id_v2":"ProfileCometTimelineListViewRoot.react,comet.profile.timeline.list,tap_search_bar,1713671419755,394049,190055527696468,,","is_tracking_encrypted":false,"subscribe_location":"PROFILE","subscribee_id":"'+taget+'","tracking":null,"actor_id":"'+id+'","client_mutation_id":"19"},"scale":1}',
            'server_timestamps': 'true',
            'doc_id': '7393793397375006',
        }

        follow = requests.post('https://www.facebook.com/api/graphql/', headers=self.headers, data=data)
        #print(follow.json())
        try:
            check = follow.json()['errors']
            for i in check:
                if i['summary'] == 'Tài khoản của bạn hiện bị hạn chế':
                    return 'block'
        except:
            if 'IS_SUBSCRIBED' in follow.text:
                return True
            else:
                return False
#<!--- VÀO GIAO DIỆN ---!>
def __Main__():
    Banner(); dem_ck = 1
    while True:
        try:
            cookie = input(f'{_Cyan_}[ {_Red_}+ {_Cyan_}] {_Yellow_}Nhập Cookie Account Chứa Pr5 {_Cyan_}[{_Purple_}{dem_ck}{_Cyan_}]{_Yellow_}: {_Green_}')
            if cookie != '' and 'c_user=' in cookie:
                f = KsxKoji()
                fb = f.__Get_ThongTin__(cookie)
                if fb == True:
                    f.__Get_Page__(cookie)
                    __gach__()
                    print(f'{_Cyan_}(*) {_Green_}Name Profile: {_Yellow_}{f.name} {_Red_}| {_Green_}Có {_Yellow_}{f.dem} {_Green_}Page')
                    __gach__()
                    dem_ck += 1
                    save = open('list_cookie.txt','a+').write(cookie+'\n')
            elif cookie == '' and dem_ck >= 1:
                break
            else:
                print(f'{_Red_} Bắt Buộc Nhập Ít Nhất 1 Cookie !!!')
                __gach__()
        except KeyboardInterrupt:
            quit()
    Banner()
    while True:
        taget = input(f'{_Cyan_}[ {_Red_}+ {_Cyan_}] {_Yellow_}Nhập UID Profile Muốn Tăng{_Yellow_}: {_Green_}')
        so_luong = int(input(f'{_Cyan_}[ {_Red_}+ {_Cyan_}] {_Yellow_}Nhập Số Lượng Muốn Tăng{_Yellow_}: {_Green_}'))
        delay = int(input(f'{_Cyan_}[ {_Red_}+ {_Cyan_}] {_Yellow_}Nhập Thời Gian Delay{_Cyan_}({_Purple_}defaul {_Yellow_}>= {_Red_}10{_Cyan_}){_Yellow_}: {_Green_}'))
        if delay < 10:
            print(f'{_Red_} Bắt Buộc Trên 10 Giây Mà 3:)')
            __gach__()
            delay = int(input(f'{_Cyan_}[ {_Red_}+ {_Cyan_}] {_Yellow_}Nhập Thời Gian Delay{_Cyan_}({_Purple_}defaul {_Yellow_}>= {_Red_}10{_Cyan_}){_Yellow_}: {_Green_}'))
        else:
            break
    Banner()
    x = 0; dem = 0; dem_ck = 0
    open_file = open('list_cookie.txt','r').read().split('\n')
    list_page.clear()
    while True:
        try:
            cookie = open_file[dem_ck]
            f.__Get_ThongTin__(cookie)
            f.__Get_Page__(cookie)
            print(f' Setup Page Pr5 Account {f.name}', end='\r')
            while True:
                try:
                    dem += 1
                    id = list_page[x]
                    fl = f.__Follow__(cookie, id, taget)
                    if fl == True:
                        print(f'{_Cyan_}[{_Red_}{dem}{_Cyan_}] {_Purple_}| {_Green_}KsxKoji~ {_Purple_}| {_Cyan_}[{_Yellow_}{id}{_Cyan_}] {_Red_}-> {_Cyan_}Follow {_Red_}-> {_Cyan_}[{_Yellow_}{taget}{_Cyan_}] {_Purple_}| {_Yellow_}Thành Công !')
                        loading(delay)
                    elif fl == 'block':
                        print(f'{_Red_} Các Pro5 Của [{f.name}] Đã Block, Tiến Hành Loại Bỏ Page Pro5 !!!', end='\r')
                        list_page.clear()
                        time.sleep(2)
                        dem_ck += 1
                        x = 0; dem = 0
                        print(' '*100, end='\r')
                        break
                    elif fl == False:
                        print(f'{_Cyan_}[{_Red_}{dem}{_Cyan_}] {_Purple_}| {_Green_}KsxKoji~ {_Purple_}| {_Cyan_}[{_Yellow_}{id}{_Cyan_}] {_Red_}-> {_Cyan_}Follow {_Red_}-> {_Cyan_}[{_Yellow_}{taget}{_Cyan_}] {_Purple_}| {_Red_}Thất Bại !')
                        loading(delay)
                    x += 1
                    if dem >= so_luong:
                        print(f'{_Cyan_} Đã Xong, Out !!                         ')
                        quit()
                except:
                    print(f'{_Green_}Hết Page Trong Profile {_Yellow_}{f.name}{_Green_}, Chuyển Đến Profile Tiếp Theo', end='\r')
                    list_page.clear()
                    time.sleep(2)
                    dem_ck += 1
                    print(' '*100, end='\r')
                    break
        except:
            print(f'{_Cyan_} Hết Cookie Chứa List Pr5, Out !!')
            quit()
try:
    __Main__()
except KeyboardInterrupt:
    quit()

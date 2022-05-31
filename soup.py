from bs4 import BeautifulSoup
import requests

###############################USER AUTH STUFF
cookies = {
    'ASP.NET_SessionId': 'nugwls5ml3ubfl4jlskbxh23',
    'retPath': 'https://northwestern.bluera.com/northwestern/Login/Login.aspx?ReturnUrl=%2fnorthwestern%2frpvf-eng.aspx%3flang%3deng%26redi%3d1%26SelectedIDforPrint%3d0677c83a856bb1494393c73cb959564ba17eb502335e7222a38b25de0c6859eef5f26465225e10261ec097a7b37dab6b%26ReportType%3d2%26regl%3den-US',
    'regl': 'en-US',
    'lang': 'eng',
    'lnid': 'e8b4ba20-b819-4eda-ba88-531fd66056f6',
    '_shibsession_6e6f7274687765737465726e475768747470733a2f2f6e6f7274687765737465726e2e626c756572612e636f6d2f73686962626f6c6574682f64656661756c74': '_0181bb51fde4684a5ae473f332804a10',
    'CookieName': 'FD8031E53DD131752D755DD68BDEA2409737EC4817F04ED3B92C9F6BFE264D9A3A9299CBE30EB056810B4ADB41E4F460981870D4033CD37E18CDE3B23FE8C6D5F522B0ACDCC33DE39503C51E289131BBEDE3A3628E0DC981616283B815509227CDEC758F51AB6439E0795B2421C0DEDFB96FFB69660A3D76598C68DED9C05C00FC631B267C5F15C828CE96C8840331B12B117B1CBCF83FDA722FE7DBE6853A0E',
    'session_token': '8694eb6b24904f7d805310b5d8b7310b',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    # Requests sorts cookies= alphabetically
    # 'Cookie': 'ASP.NET_SessionId=nugwls5ml3ubfl4jlskbxh23; retPath=https://northwestern.bluera.com/northwestern/Login/Login.aspx?ReturnUrl=%2fnorthwestern%2frpvf-eng.aspx%3flang%3deng%26redi%3d1%26SelectedIDforPrint%3d0677c83a856bb1494393c73cb959564ba17eb502335e7222a38b25de0c6859eef5f26465225e10261ec097a7b37dab6b%26ReportType%3d2%26regl%3den-US; regl=en-US; lang=eng; lnid=e8b4ba20-b819-4eda-ba88-531fd66056f6; _shibsession_6e6f7274687765737465726e475768747470733a2f2f6e6f7274687765737465726e2e626c756572612e636f6d2f73686962626f6c6574682f64656661756c74=_0181bb51fde4684a5ae473f332804a10; CookieName=FD8031E53DD131752D755DD68BDEA2409737EC4817F04ED3B92C9F6BFE264D9A3A9299CBE30EB056810B4ADB41E4F460981870D4033CD37E18CDE3B23FE8C6D5F522B0ACDCC33DE39503C51E289131BBEDE3A3628E0DC981616283B815509227CDEC758F51AB6439E0795B2421C0DEDFB96FFB69660A3D76598C68DED9C05C00FC631B267C5F15C828CE96C8840331B12B117B1CBCF83FDA722FE7DBE6853A0E; session_token=8694eb6b24904f7d805310b5d8b7310b',
    'Referer': 'https://fed.it.northwestern.edu/',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'cross-site',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
}

params = {
    'lang': 'eng',
    'redi': '1',
    'SelectedIDforPrint': '0677c83a856bb1494393c73cb959564ba17eb502335e7222a38b25de0c6859eef5f26465225e10261ec097a7b37dab6b',
    'ReportType': '2',
    'regl': 'en-US',
}

###############################USER AUTH STUFF
#brandon winter 2022
voidURL = "https://northwestern.bluera.com/northwestern/rpvf-eng.aspx?lang=eng&redi=1&SelectedIDforPrint=0677c83a856bb1494393c73cb959564ba17eb502335e7222a38b25de0c6859eef5f26465225e10261ec097a7b37dab6b&ReportType=2&regl=en-US"
URL = "https://northwestern.bluera.com/northwestern/rpvf-eng.aspx"
response = requests.get(URL, params=params, cookies=cookies, headers=headers)
soup = BeautifulSoup(response.content, "html.parser")

#dinda fall 2021
retURL = "https://northwestern.bluera.com/northwestern/rpvf-eng.aspx?lang=eng&redi=1&SelectedIDforPrint=9e417f83259b75257669997b4230b82db3803bbc4dd312ec1047ec912fe63fbd1a296b837ab603dbcf3fab9a9961648f&ReportType=2&regl=en-US"
cookies['retPath']=retURL
response = requests.get(URL, params=params, cookies=cookies, headers=headers)
soup2 = BeautifulSoup(response.content, "html.parser")

def get_course_name(soup):
    print(soup.title.text)
    return soup.title.text
get_course_name(soup)
get_course_name(soup2)
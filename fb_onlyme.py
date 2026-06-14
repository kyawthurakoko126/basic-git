import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# --- CONFIGURATION ---
FB_EMAIL = "kyawthurakoko01@gmail.com"  # သင့် Facebook Email ရိုက်ထည့်ပါ
FB_PASSWORD = "Thuzar110457"        # သင့် Facebook Password ရိုက်ထည့်ပါ

def init_driver():
    # Browser Notification တွေကို ပိတ်ဖို့ Options ချိန်ညှိခြင်း
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-notifications")
    # လိုအပ်ပါက Browser မပွင့်ဘဲ နောက်ကွယ်မှာပဲ အလုပ်လုပ်စေချင်ရင် အောက်ကစာသားကို Uncomment ဖွင့်ပါ
    # options.add_argument("--headless") 
    
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    return driver

def login_facebook(driver, email, password):
    driver.get("https://www.facebook.com")
    time.sleep(2)
    
    # Email နဲ့ Password ရိုက်ထည့်ပြီး Login ဝင်ခြင်း
    driver.find_element(By.ID, "email").send_keys(email)
    driver.find_element(By.ID, "pass").send_keys(password)
    driver.find_element(By.NAME, "login").click()
    time.sleep(5) # Login ဝင်အောင် ခေတ္တစောင့်ဆိုင်းခြင်း

def delete_only_me_posts(driver):
    # သင့်ရဲ့ Activity Log (Manage Posts) စာမျက်နှာကို တိုက်ရိုက်သွားခြင်း
    driver.get("https://www.facebook.com/me/manage_posts")
    time.sleep(5)
    
    print("နမူနာလုပ်ဆောင်ချက်- Only Me ပို့စ်များကို ရှာဖွေနေပါပြီ...")
    
    # မှတ်ချက်။ ။ Facebook ရဲ့ HTML Structure (Class Name / ID) တွေဟာ ခဏခဏ ပြောင်းလဲတတ်ပါတယ်။
    # အောက်ပါအဆင့်တွေဟာ ကိုယ်တိုင် 'Inspect' လုပ်ပြီး Element တွေကို တိတိကျကျ ရှာဖွေရမယ့် သဘောတရားဖြစ်ပါတယ်။
    
    try:
        # စာမျက်နှာကို အောက်သို့ Scroll ဆွဲချပြီး Post တွေကို Load လုပ်ခိုင်းခြင်း
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)
        
        # ၁။ Only Me Icon (သော့ခလောက်ပုံစံ) ရှိတဲ့ Post တွေကို Target ထားရှာဖွေရပါမယ်။
        # (Facebook သည် 'Only me' post များအတွက် သီးသန့် aria-label သို့မဟုတ် icon class သုံးတတ်ပါသည်)
        
        # ၂။ ထို Post ဘေးရှိ မီနူး (...) ကို နှိပ်ရပါမယ်။
        # ၃။ 'Move to trash' သို့မဟုတ် 'Delete' ကို နှိပ်ရပါမယ်။
        
        print("လုံခြုံရေးစနစ်အရ လိုအပ်သော Element XPaths များကို လက်ရှိ Facebook Layout အတိုင်း စစ်ဆေးပြင်ဆင်ရန် လိုအပ်ပါသည်။")
        
    except Exception as e:
        print(f"အမှားအယွင်းတစ်ခု ရှိခဲ့ပါတယ်: {e}")

if __name__ == "__main__":
    driver = init_driver()
    try:
        login_facebook(driver, FB_EMAIL, FB_PASSWORD)
        delete_only_me_posts(driver)
    finally:
        # အလုပ်ပြီးရင် Browser ကို ပိတ်လိုက်ခြင်း
        time.sleep(5)
        driver.quit()
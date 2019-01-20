#!/usr/bin/env python
import sys, time, datetime
from random import randint
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def main():
    usage(len(sys.argv))

    # Open browser (Firefox)
    driver = webdriver.Firefox()

    try:
	# Login user
        login(driver)

	# Open file
        with open(sys.argv[3], "r") as f:
            while True:
                hashtag = f.readline()
                if hashtag == '':
                    f.seek(0)
                    time.sleep(1)
                else:
                    like_photo(driver, hashtag)

    except KeyboardInterrupt:
    	print("[+] CTRL+C Pressed... Exiting the program...")
    	sys.exit(0)

# This method displays usage message to the user...
def usage(argc):
    if argc != 4:
        print("Usage: {} <username> <password> <hashtag>\n".format(sys.argv[0]))
        print("Options:")
        print("  username:  your instagram username you want to use to login")
        print("  password:  password of the instagram account")
        print("  hashtag :  a hashtag or a wordlist file containing hashtags to use\n")
        print("Example:")
        print("  {} ___ch1pmunx___ passtheword123 hashtag.txt".format(sys.argv[0]))
        sys.exit(1)

# This method is used to login the user...
def login(driver):
    try:
	# driver = webdriver.Firefox()
	# driver.get("https://www.instagram.com/")
        driver.get("https://www.instagram.com/accounts/login/")

	# Wait for page to load...
        time.sleep(3)

	# Enter username
        username = driver.find_element_by_xpath("//input[@name='username']")
        username.clear()
        username.send_keys(sys.argv[1])

        # Enter password
        password = driver.find_element_by_xpath("//input[@name='password']")
        password.clear()
        password.send_keys(sys.argv[2])
        password.send_keys(Keys.RETURN)

        print("[+] Logged in...")
        time.sleep(3)

    except Exception:
        print("[!] Invalid credentials...")
        sys.exit(1)

# This method clicks on the photo, <3's it, and goes the next photo
def like_photo(driver, hashtag):
    # Navigate to hashtag page
    driver.get("https://www.instagram.com/explore/tags/" + hashtag)

    time.sleep(3)

    # Click the first photo
    first_photo = driver.find_element_by_xpath("/html/body/span/section/main/article/div[1]/div/div/div[1]/div[1]/a")
    driver.execute_script("arguments[0].click();", first_photo)
    time.sleep(1)

    i=0
    while True:
        print("[+] Current photo: {}".format(i))

        if i > randint(144, 188):
            print("[+] {} <3 reached!...".format(i))
            print("[+] Taking a 30 min nap...")
            print("[+] Time stopped: {}".format(datetime.datetime.now()))
            time.sleep(1800)
            break

        # <3 the first photo and go to next...
        try:
            print("  - Trying to <3 the photo...")
            like_photo = driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/article/div[2]/section[1]/span[1]/button")
            like_photo.click()
            time.sleep(1)

            # Go to next photo
            print("  - Next photo...")
            next_photo = driver.find_element_by_xpath("//a[@class='HBoOv coreSpriteRightPaginationArrow']")
            next_photo.click()
            time.sleep(4)

            # Increment `i`
            i+=1
        except Exception:
            print("  - Photo already has <3... Next photo...")
            try:
                next_photo = driver.find_element_by_xpath("//a[@class='HBoOv coreSpriteRightPaginationArrow']")
                next_photo.click()
                time.sleep(2)
                # HERE IS THE BUG
            except:
                print("[!] Locating right arrow!!!!")
                # Go back to the start of the page
		# driver.get("https://www.instagram.com/explore/tags/" + hashtag)
                time.sleep(5)
		# Click the first photo
		# first_photo = driver.find_element_by_xpath("/html/body/span/section/main/article/div[1]/div/div/div[1]/div[1]/a")
		# driver.execute_script("arguments[0].click();", first_photo)
		# time.sleep(1)



if __name__ == "__main__":
	main()

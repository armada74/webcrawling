from selenium import webdriver
import time

if __name__ == "__main__":
        driver = webdriver.Chrome()
        driver.get("https://nid.naver.com/nidlogin.login?url=http%3A%2F%2Fwww.naver.com")

        elem = driver.find_element_by_id("id")
        print(elem)
        elem.send_keys("armada74")
        elem = driver.find_element_by_id("pw")
        elem.send_keys("westwood74")
        elem.submit()

        time.sleep(1)

        elem = driver.find_element_by_id("query")
        elem.send_keys("naver")
        elem.submit()
        # driver.close()
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest

class GoogleSearchTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome() # Google Chrome에 관한 테스트
        self.driver.implicitly_wait(10) # 웹 페이지가 로드될 때까지 10초 대기

    # google chrome에서 검색 테스트
    def test_google_search(self): 
        self.driver.get("http://www.google.com")
        self.assertIn("Google", self.driver.title)
        elem = self.driver.find_element("name", "q") # 검색 input name이 q인것 찾기 (보통 웹 페이지에서는 관례적으로 검색 input 상자의 name이 q이다.)
        elem.send_keys("QA") 
        elem.submit()
        # 검색 결과 페이지가 로드될 때까지 대기 (예: 타이틀에 "QA"가 포함될 때까지 대기)
        WebDriverWait(self.driver, 10).until(
            EC.title_contains("QA")
        )
        self.assertIn("QA", self.driver.title) # selenium이 가져온 웹 페이지 title에 QA 라는 문자열이 포함되어있는지 검사하는 코드

    # 테스트 실행 후 브라우저 종료
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()        # uniittest 프레임워크를 실행하여 정의된 모든 테스트 케이스 실행





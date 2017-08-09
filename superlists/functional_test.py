from selenium import webdriver
import unittest

# (1) unittest.TestCase를 상속받는다
class NewVisitorTest(unittest.TestCase):
    # (2) setUp과 tearDown은 테스트 시작 전/후에 실행된다.
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    # (3) test라고 시작되는 모든 메소드는 테스트 메소드이며 테스트 러너에 의해 실행된다.
    #     가능한 테스트 내용을 알 수 있도록 명칭을 작성하는 것이 좋다.
    def test_can_start_a_list_and_retrieve_it_later(self):
        # 에디스 (Edith)는 멋진 작업 목록 온라인 앱이 나왔다는 소식을 듣고
        # 해당 웹 사이트를 확인하러 간다
        self.browser.get('http://localhost:8000')

        # 웹 페이지 타이틀과 헤더가 'To-Do'를 표시하고 있다
        # (4) self.assertIn, assertTrue, assertEqual 등 다양한 assert함수를 지원한다
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

        #그녀는 바로 작업을 추가하기로 한다

        # "공작 깃털 사기"라고 텍스트 상자에 입력한다
        # (에디스의 취미는 날치 잡이용 그물을 만드는 것이다

        # 엔터키를 치면 페이지가 갱신되고 작업 목록에
        # "1: 공작깃털 사기 아이템이 추가된다

        # 추가 아이템을 입력할 수 있는 여분의 텍스트 상자가 존재한다
        # 다시 "공작깃털을 이용해서 그물 만들기"라고 입력한다 (에디스는 매우 체계적인 사람이다

        # 페이지는 다시 갱신되고, 두 개 아이템이 목록에 보인다
        # 에디스는 사이트가 입력한 목록을 저장하고 있는지 궁금하다
        # 사이트는 그녀를 위한 특정 URL을 생성해준다

        # 이 때 URL에 대한 설명도 함께 제공된다

        # 해당 URL에 접속하면 그녀가 만든 작업 목록이 그대로 있는 것을 확인할 수 있다

        # 만족하고 잠자리에 든다

# (5) 이 구문은 스크립트가 다른 스크립트에 의해 임포트 된 것이 아니라 커맨드라인을 통해 실행 됐다는 것을 확인하는 코드이다.
if __name__ == '__main__':
    # (6) 불필요한 리소스 경고를 제거하기 위한 것
    unittest.main(warnings='ignore')
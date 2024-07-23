import unittest

# 간단한 덧셈 관련 단위 테스트 예제
def add(a, b):
    return a + b

class TestAddFunction(unittest.TestCase):

    def test_add_positive_numbers(self):
        self.assertEqual(add(3, 5), 8)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-3, -5), -5) # 에러발생 시 결과 -> failed로 발생

if __name__ == "__main__":
    unittest.main()

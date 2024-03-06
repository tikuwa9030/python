import unittest
from english_word import answerJudge


class testAnswerJudge(unittest.TestCase):
    
    correct_answer: dict = {
        "Japanese": 3,
        "train": 2,
        "zoo": 4,
        "work": 1,
        "carrer": 3
        }
    
    def test_answerJudge_correctanswer(self):
        """answerJudge関数で正解時のテスト"""
        actual: str = answerJudge(
                            3, ('Japanese', ('英語', 'ドイツ語', '日本語', '中国語')))
        expected: str = "正解！"
        
        self.assertEqual(actual, expected)
        
    def test_answerJudge_not_correctanswer(self):
        """answerJudge関数で不正解時のテスト"""
        actual: str = answerJudge(
                            1, ('Japanese', ('英語', 'ドイツ語', '日本語', '中国語')))
        expected: str = "残念、不正解!"
        
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()

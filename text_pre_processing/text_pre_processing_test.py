import unittest
import pytest
import text_pre_processing as tp

class Test(unittest.TestCase):
    def setup(self):
        return

    def test_init_1(self):
        pp = tp.PreProcessor("This is a simple test", 10, 100)
        exp_text = "This is a simple test"
        text = pp.text
        self.assertEquals(text, exp_text)
    
    def test_init_2(self):
        pp = tp.PreProcessor("This is a simple test", 10, 100)
        exp_max_length_tweet = 10
        max_length_tweet = pp.max_length_tweet
        self.assertEquals(max_length_tweet, exp_max_length_tweet)

    def test_init_3(self):
        pp = tp.PreProcessor("This is a simple test", 10, 100)
        exp_max_length_dictionary = 100
        max_length_dictionary = pp.max_length_dictionary
        self.assertEquals(max_length_dictionary, exp_max_length_dictionary)

    def test_init_4(self):
        with pytest.raises(ValueError):
            pp = tp.PreProcessor("This is a simple test", -1, 100)
    
    def test_init_5(self):
        with pytest.raises(ValueError):
            pp = tp.PreProcessor("This is a simple test", 1, -100)
    
    def test_method_clean_text_1(self):
        pp = tp.PreProcessor("This is a simple test", 10, 100)
        pp.clean_text()
        exp_text = "This is a simple test"
        text = pp.text
        self.assertEquals(text, exp_text)
    
    def test_method_clean_text_2(self):
        pp = tp.PreProcessor("https://stackoverflow.com/questions/23337471/how-to-properly-assert-that-an-exception-gets-raised-in-pytest This is a simple test", 10, 100)
        pp.clean_text()
        exp_text = "This is a simple test"
        text = pp.text
        self.assertEquals(text, exp_text)

    def test_method_clean_text_3(self):
        pp = tp.PreProcessor("This is a https://stackoverflow.com/questions/23337471/how-to-properly-assert-that-an-exception-gets-raised-in-pytest simple test", 10, 100)
        pp.clean_text()
        exp_text = "This is a  simple test"
        text = pp.text
        self.assertEquals(text, exp_text)
    
    def test_method_clean_text_4(self):
        pp = tp.PreProcessor("This is a simple test https://stackoverflow.com/questions/23337471/how-to-properly-assert-that-an-exception-gets-raised-in-pytest ", 10, 100)
        pp.clean_text()
        exp_text = "This is a simple test"
        text = pp.text
        self.assertEquals(text, exp_text)

    def test_method_clean_text_5(self):
        pp = tp.PreProcessor("This is a simple test with some interesting \U0001F600\U0001F64F 其他语言或字符 within it.", 10, 100)
        pp.clean_text()
        exp_text = "This is a simple test with some interesting   within it."
        text = pp.text
        self.assertEquals(text, exp_text)

    def test_method_tokenize_text_1(self):
        pp = tp.PreProcessor("This is a simple test with some interesting \U0001F600\U0001F64F 其他语言或字符 within it. https://stackoverflow.com/questions/23337471/how-to-properly-assert-that-an-exception-gets-raised-in-pytest", 10, 100)
        pp.clean_text()
        pp.tokenize_text()
        exp_tokens = ["This", "is", "a", "simple", "test", "with", "some", "interesting", "within", "it"]
        tokens = pp.tokens
        self.assertEquals(tokens, exp_tokens)

    def test_method_tokenize_text_1(self):
        pp = tp.PreProcessor("This is a simple test with some interesting \U0001F600\U0001F64F 其他语言或字符 within it. https://stackoverflow.com/questions/23337471/how-to-properly-assert-that-an-exception-gets-raised-in-pytest", 10, 100)
        pp.clean_text()
        pp.tokenize_text()
        exp_tokens = ["This", "is", "a", "simple", "test", "with", "some", "interesting", "within", "it"]
        tokens = pp.tokens
        self.assertEquals(tokens, exp_tokens)
    
    def test_replace_token_with_index_1(self):
        pp = tp.PreProcessor("This is a simple test with some interesting \U0001F600\U0001F64F 其他语言或字符 within it. https://stackoverflow.com/questions/23337471/how-to-properly-assert-that-an-exception-gets-raised-in-pytest", 20, 100)
        pp.clean_text()
        pp.tokenize_text()
        pp.replace_token_with_index()
        exp_pad = [-1, 15, 8, -1, -1, 18, 78, -1, -1, 21, 3]
        pad = pp.pad
        self.assertEquals(pad, exp_pad)
    
    def test_replace_token_with_index_2(self):
        pp = tp.PreProcessor("This is a simple test with some interesting \U0001F600\U0001F64F 其他语言或字符 within it. https://stackoverflow.com/questions/23337471/how-to-properly-assert-that-an-exception-gets-raised-in-pytest", 5, 100)
        pp.clean_text()
        pp.tokenize_text()
        pp.replace_token_with_index()
        exp_pad = [-1, 15, 8, -1, -1]
        pad = pp.pad
        self.assertEquals(pad, exp_pad)
    
    def test_pad_sequence_1(self):
        pp = tp.PreProcessor("This is a simple test with some interesting \U0001F600\U0001F64F 其他语言或字符 within it. https://stackoverflow.com/questions/23337471/how-to-properly-assert-that-an-exception-gets-raised-in-pytest", 5, 100)
        pp.clean_text()
        pp.tokenize_text()
        pp.replace_token_with_index()
        pp.pad_sequence()
        exp_pad = [-1, 15, 8, -1, -1]
        pad = pp.pad
        self.assertEquals(pad, exp_pad)
    
    def test_pad_sequence_2(self):
        pp = tp.PreProcessor("This is a simple test with some interesting \U0001F600\U0001F64F 其他语言或字符 within it. https://stackoverflow.com/questions/23337471/how-to-properly-assert-that-an-exception-gets-raised-in-pytest", 20, 100)
        pp.clean_text()
        pp.tokenize_text()
        pp.replace_token_with_index()
        pp.pad_sequence()
        exp_pad = [-1, 15, 8, -1, -1, 18, 78, -1, -1, 21, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        pad = pp.pad
        self.assertEquals(pad, exp_pad)
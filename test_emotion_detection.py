from EmotionDetection.emotion_detection import emotion_detector
import unittest

class EmotionDetectionTest(unittest.TestCase):

    def test_emotion_detector(self):
        test_cases = [
            ('I am glad this happened', 'joy'),
            ('I am really mad about this', 'anger'),
            ('I feel disgusted just hearing about this', 'disgust'),
            ('I am so sad about this', 'sadness'),
            ('I am really afraid that this will happen', 'fear')
        ]
        for tc in test_cases:
            d = emotion_detector(tc[0])
            self.assertEqual(d['dominant_emotion'], tc[1])
        
if __name__ == '__main__':
    unittest.main()

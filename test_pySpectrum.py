#!/usr/local/bin/python
import pySpectrum, unittest 
import wave

test_sound_file = 'test_sound_file.wav'

class testPySpectrum(unittest.TestCase):
    def setUp(self):
        pass
        
    def tearDown(self):
        pass

    def test_converts_imported_audio_file_into_the_desired_format(self):
        """
        The audio file should become ( tupleA, tupleB ), 
        where the tuples are the left and right channels.
        They should be equal in length, and contain integers.
        """
        w = pySpectrum.import_audio(test_sound_file)
        self.assertEqual(len(w),2)
        self.assertIsInstance(w,tuple)
        self.assertEqual(len(w[0]),len(w[1]))
        for i in (0,1):
            self.assertIsInstance(w[i],tuple)
            all(self.assertIsInstance(n,int) for n in w[i])

    def test_can_display_sound_waveform(self):
        pass
        # print("%f" % self.w.readframes(2))
        # self.fail("Finish this test")

if __name__ == "__main__":
    unittest.main()

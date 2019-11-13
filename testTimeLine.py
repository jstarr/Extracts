from vTimeLine import video_time_line
import unittest

class test_v_time_line(unittest.TestCase):
    _start_time = '00:00:01'
    _end_time = '00:00:10'
    _source_file_name = 'Source File.mp4'
    _dest_file_name = 'Destination File.mp4'
    _delta = '00:00:09'

    def create_dut(self):
        dut = video_time_line(fmt='%H:%M:%S',
                        start_time=self._start_time,
                        end_time=self._end_time,
                        source_file_name=self._source_file_name,
                        dest_file_name=self._dest_file_name
                    )
        return dut

    def test_init5Vars(self):
        dut = self.create_dut()
        assert dut.sDelta() == self._delta, 'Delta should be {}'.format(self._delta)
        
    def test_starttime(self):
        dut = self.create_dut()
        st = str(dut.vstart_time())[11:]
        assert st == self._start_time, 'Start time should be {}'.format(self._start_time)

    def test_sourceFileName(self):
        dut = self.create_dut()
        assert dut.vsource_file_name(), 'Source file should be {}'.format(self._source_file_name)

    def test_destFileName(self):
        dut = self.create_dut()
        assert dut.vdest_file_name(), 'Destination file should be {}'.format(self._dest_file_name)

if __name__ == '__main__':
    unittest.main()
    print('Everything works!')

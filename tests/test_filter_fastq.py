import unittest
import filecmp
import os

from filter_fastq import gc_content, gc_content_threshold, output_base_name
from filter_fastq import write_output_passed, write_output_failed


class FilterTest(unittest.TestCase):

    def test_gc_content(self):
        self.assertEqual(gc_content('ATGCATGC'), 50)

    def test_gc_content_threshold_0(self):
        self.assertEqual(gc_content_threshold(None), [0, 100])

    def test_gc_content_threshold_1(self):
        self.assertEqual(gc_content_threshold([15]), [15, 100])

    def test_gc_content_threshold_2(self):
        self.assertEqual(gc_content_threshold([15, 30]), [15, 30])

    def test_output_base_name(self):
        self.assertEqual(output_base_name('my_file_filtered', 'my_file.fastq'),
                         'my_file_filtered')

    def test_output_base_name_none(self):
        self.assertEqual(output_base_name(None, 'my_file.fastq'), 'my_file')

    def test_write_output_passed(self):
        write_output_passed('@ReadName\n', 'ATGCATGCATGC\n', '+\n', 'FFHHJJFFHHJ#\n',
                            'test_output')
        self.assertTrue(filecmp.cmp('test_output__passed.fastq', 'test_file.fastq'))
        os.remove('test_output__passed.fastq')

    def test_write_output_failed(self):
        write_output_failed('@ReadName\n', 'ATGCATGCATGC\n', '+\n', 'FFHHJJFFHHJ#\n',
                            'test_output', True)
        self.assertTrue(filecmp.cmp('test_output__failed.fastq', 'test_file.fastq'))
        os.remove('test_output__failed.fastq')

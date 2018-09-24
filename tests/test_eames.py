import pytest
import pandas as pd

import eames as em


def test_clean_returns_expected_results():
	"""Uses known report for assertion testing"""
	file = "inputs/Analytics All Web Site Data Browser Window Sizes and Device Category 20180621-20180921.xlsx"
	sheet = 'Dataset1'
	cleaned_frame = em.clean_excel_file(file, sheet)
	assert(len(cleaned_frame) == 890)

def test_flatten_frame_returns_arrays():
	data = {'Browser Size': ["1280x960", "1920x950", "380x550"],
			'Device Category': ["desktop", "desktop", "mobile"],
			'Users': [2, 1, 1]}

	frame = pd.DataFrame(data)
	flattened = em.flatten_frame(frame)
	assert(len(flattened.index) == 4)

	
def create_single_output(filename, content):
	"""
	Outputs test content into a filename
	"""
	with open(filename, 'w') as f:
		f.write(content)

def create_multifile_output(filenames, contents):
	"""
	Outputs several text contents into several files
	"""
	for idx, filename in enumerate(filenames):
		with open(filename, 'w') as f:
			f.write(contents[idx])

def compare_results(tokens, expected_tokens):
	for tdx, expected_token in enumerate(expected_tokens):
		assert tokens[tdx] == expected_tokens[tdx]
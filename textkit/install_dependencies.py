import os
import click
import nltk
from textkit.utils import read_tokens, output


@click.command('install_dependencies')
@click.option('--path', 
              help='Separator between token and count in output.',
              show_default=True)

def install_dependencies(path):
    '''
	Install required libraries.
	Note this library will install nltk dependencies into your
	user directory.
    '''
    if path:
    	nltk.data.path.append(path)

    click.echo("Installing nltk packages into your user directories in " +
    	"the following order of existence (first found):\n" + 
    	'\n'.join(nltk.data.path))
    
    extensions = [("taggers", "averaged_perceptron_tagger")]
    
    missing = check_packages_exist(extensions)

    for ext_tuple in missing:
    	nltk.download(ext_tuple[1])	

def check_packages_exist(extensions):
	'''
	Finds missing nltk extensions.
	'''
	paths = nltk.data.path # there are usually quite a few, so we check them all.
	missing = []
	ext_found = False
	for ext_tuple in extensions:
		print("Looking for " + ext_tuple[1])
		for path in paths:
			if os.path.exists(os.path.join(path, ext_tuple[0], ext_tuple[1])):
				ext_found = True
				print("Found " + ext_tuple[1])
				break;
		if not ext_found:
			missing.append(ext_tuple)

	return missing


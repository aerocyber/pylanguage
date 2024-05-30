# Create model file that act as a translation object


def get_python_code():
	return """
import json
import pathlib

TRANSLATION_DIR = str(pathlib.Path.join(pathlib.Path(__file__).parent()), 'translations')

def get_i18n_obj(lang_code: str):
	translation_object = {}
	try:
		f = open(str(pathlib.Path(TRANSLATION_DIR).join(lang_code + '.json'), 'r')
		translation_object = json.load(f)
		f.close()
	except FileNotFoundException:
		raise Exception("Translation not supported.")
	return translation_object
"""

def get_js_code():
	return """
var TRANSLATION_DIR = "../src/";

function get_i18n_obj(lang_code) {
	var jsonHandler = json.decode(TRANSLATION_DIR + lang_code + ".json");
	return jsonHandler;
}

"""

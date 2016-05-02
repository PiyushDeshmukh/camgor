from camgor.camgor import *

"""
Test file for sanity checks over the git url
Checks if the url is in the expected format
IMP : Does not check for the validity of url
"""

def test_accepts_https():
	"""
	sanity check to accept https urls only
	"""
	assert sanityCheck("https://github.com/facebook/react.git") == True

def test_rejects_http():
	"""
	sanity check to reject all https urls
	"""
	assert sanityCheck("http://github.com/facebook/react.git") == False
	assert sanityCheck("ftp://github.com/facebook/react.git") == False

def test_accepts_github_urls_only():
	"""
	sanity check to accept github only urls
	"""
	assert sanityCheck("https://github.com/facebook/react.git") == True
	assert sanityCheck("https://github.com/angular/angular.git") == True

def test_rejects_non_github_urls():
	"""
	sanity check to reject all non-github urls
	"""
	assert sanityCheck("https://google.com/angular/angular.git") == False

def test_accepts_git_urls_only():
	"""
	check whether analyzed url ends with a .git format
	"""
	assert sanityCheck("https://github.com/facebook/react.git") == True
	assert sanityCheck("https://github.com/angular/angular.git") == True
	assert sanityCheck("https://github.com/torvalds/linux.git") == True

def test_rejects_non_git_urls():
	"""
	check whether analyzed url does not end with extension other than .git
	"""
	assert sanityCheck("https://github.com/PiyushDeshmukh/camgor/archive/master.zip") == False

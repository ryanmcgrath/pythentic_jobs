#!/usr/bin/python

"""Pythentic Jobs - A small pure Python wrapper for the Authentic Jobs API (http://www.authenticjobs.com/)"""

import urllib2

from urlparse import urlparse
from urllib2 import HTTPError

__author__ = "Ryan McGrath <ryan@venodesigns.net>"
__version__ = "1.0"

try:
	import simplejson
except ImportError:
	try:
		import json as simplejson
	except ImportError:
		try:
			from django.utils import simplejson
		except:
			raise Exception("pythentic_jobs requires the simplejson library (or Python 2.6) to work. http://www.undefined.org/python/")

class PythenticJobsError(Exception):
	def __init__(self, msg):
		self.msg = msg
	def __str__(self):
		return repr(self.msg)

class pythentic:
	def __init__(self, api_key):
		"""	__init__()

			Instantiates an instance of Pythentic. Takes parameters for authentication and such (see below).

			Parameters:
				api_key: Your API key that authenticates you for requests against Authentic Jobs.
		"""
		self.base_url = "http://www.authenticjobs.com/api/?api_key=%s&format=json" % api_key
	
	def checkResponse(self, resp):
		"""	checkResponse(self, resp)
			
			Takes the returned JSON result from Authentic Jobs and checks it for odd errors, returning the response
			if everything checks out alright. There's only a few we actually have to check against; we dodge the others 
			by virtue of using a library.

			Parameters:
				resp: A JSON object returned from Authentic Jobs.
		"""
		if resp["stat"] == "ok":
			return resp
		elif resp["stat"] == "fail":
			if resp["code"] == 0:
				raise PythenticJobsError("The Authentic Jobs API is currently undergoing maintenance. Try again in a bit!")
			elif resp["code"] == 2:
				raise PythenticJobsError("It would seem that your API key is disabled. Have you been doing something you shouldn't have? ;)")
			else:
				raise PythenticJobsError("There's something wrong with your API key; it can't be recognized. Check it, and try again.")
		else:
			raise PythenticJobsError("Something went terribly wrong. Check all your calls and try again!")
	
	def getCompanies(self):
		"""	getCompanies(self)

			Returns a list of companies that are currently advertising positions.

			Parameters:
				None
		"""
		companies = simplejson.load(urllib2.urlopen(self.base_url + "&method=aj.jobs.getCompanies"))
		return self.checkResponse(companies)
	
	def getLocations(self):
		"""	getLocations(self)

			Returns a list of locations for companies that are currently advertising positions.

			Parameters:
				None
		"""
		locations = simplejson.load(urllib2.urlopen(self.base_url + "&method=aj.jobs.getLocations"))
		return self.checkResponse(locations)
	
	def search(self, **kwargs):
		"""	search(self, **kwargs)

			Returns a list of current positions, filtered by optional parameters. The response is split into multiple pages, if necessary.

			Note: Pass all parameters as string arguments.

			Parameters:
				category: The id of a job category to limit to. See getJobCategories().
				type: The id of a job type to limit to. See getJobTypes().
				sort: Accepted values are: date-posted-desc (the default) and date-posted-asc.
				company: Free-text matching against company names. Suggested values are the ids from getCompanies().
				location: Free-text matching against company location names. Suggested values are the ids from getLocations().
				keywords: Keywords to look for in the title or description of the job posting. Separate multiple keywords with commas. Multiple keywords will be treated as an OR.
				page: The page of listings to return. Defaults to 1.
				perpage: The number of listings per page. The default value is 10. The maximum value is 100.
		"""
		search_url = self.base_url + "&method=aj.jobs.search" + "&".join(["%s=%s" %(key, value) for (key, value) in kwargs.iteritems()])
		results = simplejson.load(urllib2.urlopen(search_url))
		return self.checkResponse(results)
	
	def getJobTypes(self):
		"""	getJobTypes(self)

			Returns a list of available job types.

			Parameters:
				None
		"""
		retlist = simplejson.load(urllib2.urlopen(self.base_url + "&method=aj.types.getList"))
		return self.checkResponse(retlist)
	
	def getJobCategories(self):
		"""	getJobCategories(self)

			Returns a list of current job categories.

			Parameters:
				None
		"""
		retlist = simplejson.load(urllib2.urlopen(self.base_url + "&method=aj.categories.getList"))
		return self.checkResponse(retlist)

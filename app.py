#!/usr/bin/env python
"""
A script to get all documents' info in the repository.
Runs successfully with Python 2.7.12 and cmislib 0.5.1.
"""

from cmislib import CmisClient

cmis_url = 'http://alfrescodemo.com:8080/alfresco/cmisatom'
cmis_uid = 'admin'
cmis_pwd = 'admin'

client = CmisClient(
	cmis_url,
	cmis_uid,
	cmis_pwd
)

repo = client.defaultRepository

print(repo)

results = repo.query("SELECT * FROM cmis:document")

for row in results:
	# Uncomment below to see all property keys and values
	#print row.properties
	print
	# Will give the name of the document:
	print 'Name: {}'.format(row.properties['cmis:name'])
	
	# Shows noderef which can be used with any public Alfresco API
	print 'NodeRef: {}'.format(row.properties['alfcmis:nodeRef'])

	# Shows the user who created the document (creater is also owner)
	print 'Owner: {}'.format(row.properties['cmis:createdBy'])

	# Shows last modified date and last modified by and latest version of document.
	print 'Last Mod Date: {}'.format(row.properties['cmis:lastModificationDate'])
	print 'Last Mod By: {}'.format(row.properties['cmis:lastModifiedBy'])
	print 'Latest Version: {}'.format(row.properties['cmis:versionLabel'])

	# Get the document object so we can get the path and the available ACLs for it.
	doc = repo.getObject(row.properties['cmis:objectId'])

	try:
		print 'Paths: {}'.format(doc.getPaths()[0])
	except IndexError:
		print 'Paths: N/A'
	acl = doc.getACL()
	print 'ACLs: {}'.format(acl.getEntries())
	print
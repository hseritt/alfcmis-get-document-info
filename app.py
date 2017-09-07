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
	print 'Name: {}'.format(row.properties['cmis:name'])
	print 'NodeRef: {}'.format(row.properties['alfcmis:nodeRef'])
	print 'Owner: {}'.format(row.properties['cmis:createdBy'])
	print 'Last Mod Date: {}'.format(row.properties['cmis:lastModificationDate'])
	print 'Last Mod By: {}'.format(row.properties['cmis:lastModifiedBy'])
	print 'Latest Version: {}'.format(row.properties['cmis:versionLabel'])

	doc = repo.getObject(row.properties['cmis:objectId'])
	try:
		print 'Paths: {}'.format(doc.getPaths()[0])
	except IndexError:
		print 'Paths: N/A'
	acl = doc.getACL()
	print 'ACLs: {}'.format(acl.getEntries())
	print
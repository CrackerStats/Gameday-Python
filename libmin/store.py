import pymssql

from . import *
import sys
from ConfigParser import ConfigParser

class Store:
	def __init__(self, **args):
		parser = ConfigParser()
		parser.read('%s/db_aaa.ini' % sys.path[0])

		user = parser.get('db', 'user')
		password = parser.get('db', 'password')
		db = parser.get('db', 'database')

		args = {'user': user, 'password': password, 'database': db}

		if parser.has_option('db', 'host'):
			args['host'] = parser.get('db', 'host')




		try:
			self.db = pymssql.connect(**args)
			self.db.autocommit(True)
			self.cursor = self.db.cursor()

		except (pymssql.Error, pymssql.Warning), e:
			if type(e.args) is tuple and len(e.args) > 1:
				msg = e.args[1]
			else:
				msg = str(e)

			logger.error('Connect Error: %s\n\n' % (msg))



	def save(self):
		#self.db.commit()
		pass

	def finish(self):
		#self.db.commit()
		self.db.close()

	def query(self, query, values = None):
		simplefilter("error", pymssql.Warning)

		try:
			#print query
			#print values

			res = self.cursor.execute(query , values)
			#return self.cursor.fetchall()


		except (pymssql.Error, pymssql.Warning), e:
			if type(e.args) is tuple and len(e.args) > 1:
				msg = e.args[1]
			else:
				msg = str(e)

			logger.error('%s\nQUERY: %s\nVALUES: %s\n\n' % (msg, query, ','.join([str(v) for v in values])))


	def query2(self, query):  #quick hack to start progress
		#simplefilter("error", pymssql.Warning)

		try:
			#print query

			res = self.cursor.execute(query)
			#return self.cursor.fetchall()


		except (pymssql.Error, pymssql.Warning), e:
			if type(e.args) is tuple and len(e.args) > 1:
				msg = e.args[1]
			else:
				msg = str(e)

			logger.error('%s\nQUERY: %s\n\n' % (msg, query))





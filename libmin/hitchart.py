from xml.dom import minidom
from . import *

class HitChart(list):

	def save(self):
		DB = store.Store()

		for hip in self:
			for key in hip.keys():
				if hip[key] == '': hip[key] = None
			sql = 'insert INTO hitchart (%s) VALUES(%s)' % (','.join(hip.keys()), ','.join(["'"+str(v)+"'" for v in hip.values()]))

			sql = sql.replace("'None'","NULL")
			sql = sql.replace("'null'","NULL")


		#sql = 'INSERT INTO pitch (%s) VALUES(%s)' % (','.join(self.values.keys()), ','.join(['%s'] * len(self.values)))
		#sql = 'INSERT INTO pitch (%s) VALUES(%s)' % (','.join(self.values.keys()), ','.join(["'"+str(v)+"'" for v in hip.values()]))

			#print sql
			DB.query2(sql)
		DB.save()

	def __init__(self, gid, game_id):
		super(HitChart, self).__init__()

		year, month, day = gid.split('_')[1:4]
		url = '%syear_%s/month_%s/day_%s/%s/inning/inning_hit.xml' % (CONSTANTS.BASE, year, month, day, gid)

		contents = Fetcher.fetch(url)
		if contents is None:
			return

		doc = minidom.parseString(contents)
		for element in doc.getElementsByTagName('hip'):
			hip = {'game_id': game_id}
			for attr in element.attributes.keys():
				hip[attr] = element.attributes[attr].value
			self.append(hip)
from xml.dom import minidom
from BeautifulSoup import BeautifulSoup
from re import search
from . import *

class Players(list):

	def save(self):
		DB = store.Store()

		#current_game = DB.getgame()
		#print current_game
		#print threads
		#print self.game_id


		for player in self:
			#print player.values()[8]
			for key in player.keys():
				#print key
				if player[key] == '' or player[key] == 'null':
					player[key] = None

			sql = 'insert INTO player (%s) VALUES (%s)' % (','.join(player.keys()), ','.join(["'"+str(v).replace("'", "''")+"'" for v in player.values()]))

		#sql = 'INSERT INTO pitch (%s) VALUES(%s)' % (','.join(self.values.keys()), ','.join(['%s'] * len(self.values)))
		#sql = 'INSERT INTO pitch (%s) VALUES(%s)' % (','.join(self.values.keys()), ','.join(["'"+str(v)+"'" for v in player.values()]))
		##str.replace('"', '\\"').replace("'", "\\'")

			#print current_game

			playerid = str(player.values()[8])
			playertype = str(player.values()[10])

			sql = sql.replace("'None'","NULL")
			sql = sql.replace("'null'","NULL")
			#print sql

			###DB.query2("delete from player where id = '%s' and type ='%s'" % (playerid, playertype))
			DB.query2(sql)

		DB.save()
		DB.finish()

	def __init__(self, gid, game_id):
		super(Players, self).__init__()

		year, month, day = gid.split('_')[1:4]
		url = '%syear_%s/month_%s/day_%s/%s/%ss/' % (CONSTANTS.BASE, year, month, day, gid, self.type.lower())

		contents = Fetcher.fetch(url)
		if contents is None:
			return

		soup = BeautifulSoup(contents)

		for batter_link in soup.findAll('a'):
			if search(r'\d+\.xml', batter_link['href']):
				batter_url = '%s%s' % (url, batter_link['href'])
				doc = minidom.parseString(Fetcher.fetch(batter_url))
				element = doc.getElementsByTagName('Player').item(0)

				player = {}
				for attr in element.attributes.keys():
					player[attr] = element.attributes[attr].value
				self.append(player)
				player["game_id"] = self.game_id  #added


class Pitchers(Players):

	def __init__(self, gid, game_id):
		self.type = 'PITCHER'
		self.game_id = game_id
		super(Pitchers, self).__init__(gid, game_id)

class Batters(Players):

	def __init__(self, gid, game_id):
		self.type = 'BATTER'
		self.game_id = game_id
		super(Batters, self).__init__(gid, game_id)
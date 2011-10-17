import pymssql
from xml.dom import minidom
from BeautifulSoup import BeautifulSoup
from time import mktime, strptime
from . import CONSTANTS, store, Fetcher


class Game:
	FIELDS = ['game_id', 'game_type', 'game_pk', 'home_sport_code', 'home_team_code', 'home_id', 'home_fname', 'home_sname', 'home_wins', \
		'home_loss','home_games_back', 'away_team_code', 'away_id', 'away_fname', 'away_sname', 'away_wins', 'away_loss','away_games_back', 'away_team_runs', 'home_team_runs','status_ind', 'date', 'home_time', 'winning_pitcher', \
		'losing_pitcher', 'save_pitcher','league' ]

	def _parseBox(self, elem):
		for key in elem.attributes.keys():
			if key in Game.FIELDS:
				val = elem.attributes[key].value

				if key == 'date333':
					val = DateFromTicks(mktime(strptime(val, '%B %d, %Y')))
				elif val.isdigit():
					val = int(val)
				else:
					val = str(val)

				setattr(self, key, val)

	def save(self):
		# make sure we have a status, said status is F(inal), and
		# that we have a game_type
		#print self.status_ind
		#print self.game_type
		#self.status_ind = 'F'
		if ((self.status_ind and self.game_type and self.status_ind == 'F')
                    or self.status_ind and self.game_type and self.status_ind == 'FR'):
			DB = store.Store()

#			sql = "REPLACE INTO game (%s) VALUES (%s)" % (','.join(Game.FIELDS), ','.join(["'%s'"] * len(Game.FIELDS)))
			sql = "INSERT INTO game (%s) VALUES (%s)" % (','.join(Game.FIELDS), ','.join(["'"+str(getattr(self, field))+"'" for field in Game.FIELDS] ))

			#sql = sql % (getattr(self, field) for field in Game.FIELDS)
			#print sql % Game.FIELDS
			#print (getattr(self, field) for field in Game.FIELDS)
			#values = ''
			#for field in Game.FIELDS:
			#	if field == 'game_id':
			#		values = "'" + str(getattr(self, field))
			#	else:
			#		values = values + "','" + str(getattr(self, field)).replace(',','')

			sql = sql.replace("'None'","NULL")
			sql = sql.replace("'null'","NULL")
			sql = sql.replace(",''", ", NULL")

			#print getattr(self, 'game_id')
			current_game = getattr(self, 'game_id')
			print 'Working on: ' + current_game

			#values = values + "'"
			#print sql
			#print str(values)

			#sql = sql % (values)
			DB.query2("delete from game where game_id = '%s'" % (getattr(self, 'game_id')) )
			DB.query2("delete from atbat where game_id = '%s'" % (getattr(self, 'game_id')) )
			DB.query2("delete from pitch where game_id = '%s'" % (getattr(self, 'game_id')) )
			DB.query2("delete from hitchart where game_id = '%s'" % (getattr(self, 'game_id')) )
			DB.query2("delete from player where game_id = '%s'" % (getattr(self, 'game_id')) )

			DB.query2(sql)
			DB.query2("update game set processed = getdate() where game_id = '%s'" % (getattr(self, 'game_id')) )
			DB.save()

	def __init__(self, game_id):
		self.game_id = game_id
		self.status_ind = self.game_type = None

		year, month, day = game_id.split('_')[1:4]
		url = '%syear_%s/month_%s/day_%s/%s/' % (CONSTANTS.BASE, year, month, day, game_id)
		soup = BeautifulSoup(Fetcher.fetch(url))

		box_url = '%sboxscore.xml' % url
		contents = Fetcher.fetch(box_url)

		self.home_wins = 'None'
		self.home_loss = 'None'
		self.away_wins = 'None'
		self.away_loss = 'None'
		self.home_id = 'None'
		self.away_id = 'None'
	

		linescore_url = '%slinescore.xml' % url
		linescore_contents = Fetcher.fetch(linescore_url)

		if contents is not None and linescore_contents is not None:
			doc = minidom.parseString(contents)
			line = minidom.parseString(linescore_contents)
		
			if line.getElementsByTagName('game').length == 1:
				game = line.getElementsByTagName('game').item(0)

				try:
					self.game_type = game.attributes['game_type'].value
				except:
					self.game_type = '?'


				try:
					self.status_ind = game.attributes['status_ind'].value
				except:
					self.status_ind = game.attributes['ind'].value




			
			if int(year) >= 2006:
				if line.getElementsByTagName('winning_pitcher').length == 1:
					winning_pitcher = line.getElementsByTagName('winning_pitcher').item(0)
					self.winning_pitcher = winning_pitcher.attributes['id'].value
			else:
				self.winning_pitcher = 'None'

			if int(year) >= 2006:
				if line.getElementsByTagName('losing_pitcher').length == 1:
					losing_pitcher = line.getElementsByTagName('losing_pitcher').item(0)
					self.losing_pitcher = losing_pitcher.attributes['id'].value
			else:
				self.losing_pitcher = 'None'

			if year == '2011':
				if line.getElementsByTagName('save_pitcher').length == 1:
					save_pitcher = line.getElementsByTagName('save_pitcher').item(0)
					self.save_pitcher = save_pitcher.attributes['id'].value
			else:
				self.save_pitcher = 'None'


			if doc.getElementsByTagName('boxscore').length == 1:
				self._parseBox(doc.getElementsByTagName('boxscore').item(0))

			if game.attributes['game_type'].value == 'R':
				if game.attributes['home_games_back'].value == '-' :
					self.home_games_back = 0.0
				else:
					self.home_games_back = game.attributes['home_games_back'].value
			else:
				self.home_games_back = 'None'
				
			if game.attributes['game_type'].value == 'R':
				if game.attributes['away_games_back'].value == '-' : 
					self.away_games_back = 0.0
				else:
					self.away_games_back = game.attributes['away_games_back'].value
			else:
				self.away_games_back = 'None'
		
			self.league = game.attributes['league'].value
			self.away_team_runs = game.attributes['away_team_runs'].value
			self.home_team_runs = game.attributes['home_team_runs'].value
			self.home_time = game.attributes['home_time'].value
			
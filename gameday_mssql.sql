If exists drop table [dbo].[atbat]
CREATE TABLE [dbo].[atbat](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[game_id] [varchar](30) NULL,
	[half] [varchar](10) NULL,
	[inning] [int] NULL,
	[num] [int] NULL,
	[b] [int] NULL,
	[s] [int] NULL,
	[o] [int] NULL,
	[score] [char](1) NULL,
	[batter] [int] NULL,
	[stand] [char](1) NULL,
	[b_height] [varchar](5) NULL,
	[pitcher] [int] NULL,
	[p_throws] [char](1) NULL,
	[des] [varchar](500) NULL,
	[event] [varchar](500) NULL,
	[event2] [varchar](500) NULL,
	[event3] [varchar](500) NULL,
	[event4] [varchar](500) NULL,
	[home_team_runs] [int] NULL,
	[away_team_runs] [int] NULL,
	[start_tfs] [int] NULL,
	[start_tfs_zulu] [varchar](200) NULL,
 CONSTRAINT [PK_atbat] PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX  = OFF, STATISTICS_NORECOMPUTE  = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS  = ON, ALLOW_PAGE_LOCKS  = ON) ON [PRIMARY]
) ON [PRIMARY]

If exists drop table [dbo].[fetch_log]
CREATE TABLE [dbo].[fetch_log](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[game_day] [datetime] NULL,
	[type] [varchar](50) NULL,
	[output] [text] NULL,
	[processed] [datetime] NULL
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]

If exists drop table [dbo].[game]
CREATE TABLE [dbo].[game](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[game_id] [varchar](30) NULL,
	[game_type] [char](1) NULL,
	[game_pk] [int] NULL,
	[home_sport_code] [varchar](10) NULL,
	[home_id] [int] NULL,
	[home_team_code] [varchar](3) NULL,
	[home_fname] [varchar](30) NULL,
	[home_sname] [varchar](30) NULL,
	[home_wins] [int] NULL,
	[home_loss] [int] NULL,
	[home_games_back] [varchar](50) NULL,
	[away_id] [int] NULL,
	[away_team_code] [varchar](3) NULL,
	[away_fname] [varchar](50) NULL,
	[away_sname] [varchar](50) NULL,
	[away_wins] [int] NULL,
	[away_loss] [int] NULL,
	[away_games_back] [varchar](50) NULL,
	[away_team_runs] [int] Not Null,
	[home_team_runs] [int] Not Null,
	[status_ind] [char](1) NULL,
	[date] [datetime] NULL,
	[home_time] [time] NULL,
	[processed] [datetime] NULL,
	[winning_pitcher] [int] NULL,
	[losing_pitcher] [int] NULL,
	[save_pitcher] [int] NULL,
	[league] [varchar] (3) NULL
	
 CONSTRAINT [PK_game] PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX  = OFF, STATISTICS_NORECOMPUTE  = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS  = ON, ALLOW_PAGE_LOCKS  = ON) ON [PRIMARY]
) ON [PRIMARY]


If exists drop table [dbo].[hitchart]
CREATE TABLE [dbo].[hitchart](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[game_id] [varchar](30) NULL,
	[des] [varchar](25) NULL,
	[x] [decimal](7, 3) NULL,
	[y] [decimal](7, 3) NULL,
	[batter] [int] NULL,
	[pitcher] [int] NULL,
	[type] [char](1) NULL,
	[team] [char](1) NULL,
	[inning] [int] NULL
) ON [PRIMARY]

If exists drop table [dbo].[last]
CREATE TABLE [dbo].[last](
	[type] [varchar](5) NULL,
	[year] [int] NULL,
	[month] [int] NULL,
	[day] [int] NULL
) ON [PRIMARY]


If exists drop table [dbo].[pitch]
CREATE TABLE [dbo].[pitch](
	[pid] [int] IDENTITY(1,1) NOT NULL,
	[game_id] [varchar](30) NULL,
	[num] [int] NULL,
	[pitcher] [int] NULL,
	[batter] [int] NULL,
	[b] [int] NULL,
	[s] [int] NULL,
	[des] [varchar](100) NULL,
	[id] [int] NULL,
	[type] [varchar](3) NULL,
	[x] [decimal](7, 3) NULL,
	[y] [decimal](7, 3) NULL,
	[on_1b] [int] NULL,
	[on_2b] [int] NULL,
	[on_3b] [int] NULL,
	[sv_id] [varchar](20) NULL,
	[start_speed] [decimal](7, 3) NULL,
	[end_speed] [decimal](7, 3) NULL,
	[sz_top] [decimal](7, 3) NULL,
	[sz_bot] [decimal](7, 3) NULL,
	[pfx_x] [decimal](7, 3) NULL,
	[pfx_z] [decimal](7, 3) NULL,
	[px] [decimal](7, 3) NULL,
	[pz] [decimal](7, 3) NULL,
	[x0] [decimal](7, 3) NULL,
	[y0] [decimal](7, 3) NULL,
	[z0] [decimal](7, 3) NULL,
	[vx0] [decimal](7, 3) NULL,
	[vy0] [decimal](7, 3) NULL,
	[vz0] [decimal](7, 3) NULL,
	[ax] [decimal](7, 3) NULL,
	[ay] [decimal](7, 3) NULL,
	[az] [decimal](7, 3) NULL,
	[break_y] [decimal](7, 3) NULL,
	[break_angle] [decimal](7, 3) NULL,
	[break_length] [decimal](7, 3) NULL,
	[pitch_type] [char](2) NULL,
	[type_confidence] [float] NULL,
	[spin_dir] [decimal](7, 3) NULL,
	[spin_rate] [decimal](7, 3) NULL,
	[zone] [int] NULL,
 CONSTRAINT [PK_pitch] PRIMARY KEY CLUSTERED 
(
	[pid] ASC
)WITH (PAD_INDEX  = OFF, STATISTICS_NORECOMPUTE  = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS  = ON, ALLOW_PAGE_LOCKS  = ON) ON [PRIMARY]
) ON [PRIMARY]


If exists drop table [dbo].[player]
CREATE TABLE [dbo].[player](
	[game_id] [varchar](50) NULL,
	[team] [varchar](3) NULL,
	[id] [int] NOT NULL,
	[pos] [varchar](3) NULL,
	[type] [varchar](15) NULL,
	[first_name] [varchar](30) NULL,
	[last_name] [varchar](30) NULL,
	[jersey_number] [varchar](2) NULL,
	[height] [varchar](5) NULL,
	[weight] [int] NULL,
	[bats] [varchar](3) NULL,
	[throws] [varchar](3) NULL,
	[dob] [varchar](20) NULL
) ON [PRIMARY]







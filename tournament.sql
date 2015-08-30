
-- Table definitions for the tournament project.

-- Drop previous testing database if they exist
DROP DATABASE IF EXISTS tournament;

-- Create the 'tournament' DB.
CREATE DATABASE tournament;

-- Connect to 'tournament' DB prior to creating tables
\c tournament;

-- Create 'players' table in 'tournament' DB.
CREATE TABLE players ( id SERIAL PRIMARY KEY,
	name TEXT
	);

-- Create 'matches' table in 'tournament' DB.
CREATE TABLE matches ( id SERIAL PRIMARY KEY,
	winner INTEGER REFERENCES players (id),
	loser INTEGER REFERENCES players (id)
	);

-- Create 'results' table in 'tournament' DB.
CREATE TABLE results ( match_results_id SERIAL PRIMARY KEY,
	winner INTEGER REFERENCES players (id),
	loser INTEGER REFERENCES players (id)
	);

-- Create 'standings_view' in 'tournament' DB.
CREATE VIEW standings_view AS
	SELECT players.id AS player_id, players.name,
		(SELECT COUNT(matches.winner)
			FROM matches
			WHERE matches.winner = players.id)
		AS wins,
		(SELECT COUNT(matches.winner)
			FROM matches
			WHERE players.id
			IN (winner, loser))
		AS matches_played
	FROM players
	GROUP BY players.id
	ORDER BY wins DESC;

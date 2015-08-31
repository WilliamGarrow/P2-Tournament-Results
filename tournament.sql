
-- Table definitions for the tournament project.

-- Drops the previous testing database if it exists.
DROP DATABASE IF EXISTS tournament;

-- Create the 'tournament' DB.
CREATE DATABASE tournament;

-- Connects to 'tournament' DB prior to creating tables.
\c tournament;

-- Create 'players' table in 'tournament' DB.
CREATE TABLE players ( id SERIAL PRIMARY KEY,
	name TEXT
	);

-- Create 'matches' table in 'tournament' DB.
-- Assigns a column for the 'winner' and a column for the 'loser'.
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
	--
	SELECT players.id AS player_id, players.name,
		-- Function to return the number and values of the records in the 'matches' table.
		(SELECT COUNT(matches.winner)
			FROM matches
			WHERE matches.winner = players.id)
		-- Using 'AS' allows the 'wins' results to be sorted later.
		AS wins,
		(SELECT COUNT(matches.winner)
			FROM matches
			WHERE players.id
			IN (winner, loser))
		AS matches_played
	FROM players
	-- Group the result with aggregate functions by player.
	-- Sorting performed on the database by wins in descending order.
	GROUP BY players.id
	ORDER BY wins DESC;

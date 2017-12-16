Tournament-Results
=======================================================

Full Stack Web Development

## Overview

In this project, I have written a Python module that uses the PostgreSQL database to keep track of players and matches in a Swiss style game tournament. The tournament pairs up players in each round: players are not eliminated, and each player is paired with another player with the same number of wins, or as close as possible.

## Requirements

[PostgreSQL](http://www.postgresql.org/), [Python](https://www.python.org/), and a clone of [fullstack-nanodegree-vm](https://github.com/udacity/fullstack-nanodegree-vm.git). Staring with the code templates in Git cloned VM /vagrant directory there are two files, tournament.sql, tournament.py, and a unit test file tournament_test.py to check status of the code written.

## Tournament Results Project Setup and Runtime
### Database Setup

The tournament.sql file will drop previous database, if it exists, create a new database named 'tournament' and connect to it.
```
psql -f tournament.sql
```

#### Terminal Results
```
vagrant@vagrant-ubuntu-trusty-32:/vagrant/tournament$ psql -f tournament.sql
DROP DATABASE
CREATE DATABASE
You are now connected to database "tournament" as user "vagrant".
CREATE TABLE
CREATE TABLE
CREATE TABLE
CREATE VIEW
CREATE VIEW
```

### Run Unit Test File
```
python tournament_test.py
```
#### Terminal Results
```
vagrant@vagrant-ubuntu-trusty-32:/vagrant/tournament$ python tournament_test.py
1. Old matches can be deleted.
2. Player records can be deleted.
3. After deleting, countPlayers() returns zero.
4. After registering a player, countPlayers() returns 1.
5. Players can be registered and deleted.
6. Newly registered players appear in the standings with no matches.
7. After a match, players have updated standings.
8. After one match, players with one win are paired.
Success!  All tests pass!
vagrant@vagrant-ubuntu-trusty-32:/vagrant/tournament$
```
If the code written meets meets the use case testing file the prompt **Success!  All tests pass!** will be rendered.

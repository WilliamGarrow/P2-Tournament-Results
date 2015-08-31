#!/usr/bin/env python
#
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2
import contextlib


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


@contextlib.contextmanager
def with_cursor():
    """This function is a decorator that can be used to define a factory
    function for with statement context managers.

    Cursor used to establish database connections, database commit, and
    database close.

    Reference: https://docs.python.org/2/library/contextlib.html
    """
    conn = connect()
    cur = conn.cursor()
    try:
        yield cur
    except:
        raise
    else:
        conn.commit()
    finally:
        cur.close()
        conn.close()


def deleteMatches():
    """Remove all the match records from the database."""
    # Switched to Python decorators using contextmanager 'def with_cursor():'
    with with_cursor() as cursor:
        cursor.execute("DELETE FROM matches;")


def deletePlayers():
    """Remove all the player records from the database."""
    with with_cursor() as cursor:
        cursor.execute("DELETE FROM players;")


def countPlayers():
    """Returns the number of players currently registered."""
    with with_cursor() as cursor:
        cursor.execute("SELECT count(*) FROM players;")
        player_count = cursor.fetchone()[0]
    return player_count


def registerPlayer(name):
    """Adds a player to the tournament database.

    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)

    Args:
      name: the player's full name (need not be unique).
    """
    # Introduces query instead of c.execute as a (query) in order to add arguments 'args'.
    with with_cursor() as cursor:
        query = "INSERT INTO players(name) VALUES(%s);"
        args = (name,)
        cursor.execute(query, args)


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    with with_cursor() as cursor:
        query = "SELECT player_id, name, wins, matches_played \
        FROM standings_view ORDER BY wins DESC;"
        cursor.execute(query)
        match_standings = cursor.fetchall()
    return match_standings


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    with with_cursor() as cursor:
        query = "INSERT INTO matches(winner, loser) VALUES(%s, %s);"
        args = (winner, loser,)
        cursor.execute(query, args)


def swissPairings():
    """Returns a list of pairs of players for the next round of a match.

    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.

    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    with with_cursor() as cursor:
        query = "SELECT a.id, a.name, b.id, b.name \
        FROM player_wins as a JOIN player_wins as b \
        ON a.wins = b.wins WHERE a.id > b.id;"
        cursor.execute(query)
        results = cursor.fetchall()
    return results

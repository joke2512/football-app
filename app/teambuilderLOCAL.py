import mysql.connector
from pulp import *
"""
Local teambuilder version. For testing.
"""
def positionSH():
    """
    Returns position shorthands
    """
    return {
        "goalkeeper": ["GK"], 
        "fullback": ["LB","RB","LWB","RWB"],
        "halfback": ["CB","LCB","RCB","CDM","LDM","RDM","CM","LCM","RCM","LM","RM"],
        "forward": ["CAM","LAM","RAM","LWF","RWF","CF","LCF","RCF"]
    }


def executeQuery(query):
    mydb = mysql.connector.connect(
    host="football-db.cbjwwglbjbqg.eu-central-1.rds.amazonaws.com",
    user="joke2512",
    password="Ju76gw54b8",
    port="3306"
    )
    mycursor = mydb.cursor()
    mycursor.execute(query)
    retval = []
    for row in mycursor:
        retval.append(row)
    mydb.commit()
    mycursor.close()
    mydb.close()
    return retval

def knapsack(budget):
    """
    Looking at it as a knapsack problem
    """
    sys.setrecursionlimit(10**6) 
    data = executeQuery("""
    SELECT id, value, overall, position FROM Football.Players
    """)
    pos = positionSH()
    playerid = []
    point = {}
    cost = {}
    gk = {}
    fb = {}
    hb = {}
    fwd = {}
    # prep data for problem solving
    for row in data:
        playerid.append(row[0])
        point[row[0]] = row[2]
        cost[row[0]] =  row[1]
        if row[3] in pos["goalkeeper"]:
            gk[row[0]] = 1
            fb[row[0]] = 0
            hb[row[0]] = 0
            fwd[row[0]] = 0
        elif row[3] in pos["fullback"]:
            gk[row[0]] = 0
            fb[row[0]] = 1
            hb[row[0]] = 0
            fwd[row[0]] = 0
        elif row[3] in pos["halfback"]:
            gk[row[0]] = 0
            fb[row[0]] = 0
            hb[row[0]] = 1
            fwd[row[0]] = 0 
        elif row[3] in pos["forward"]:
            gk[row[0]] = 0
            fb[row[0]] = 0
            hb[row[0]] = 0
            fwd[row[0]] = 1
        # some players doesn't fit the given categories
        else:
            gk[row[0]] = 0
            fb[row[0]] = 0
            hb[row[0]] = 0
            fwd[row[0]] = 0
    # Create problem
    prob = LpProblem("TeamBuilder",LpMaximize)
    player_vars = LpVariable.dicts("Players",playerid,0,1,LpBinary)

    # objective function
    prob += lpSum([point[i]*player_vars[i] for i in playerid]), "Total Cost"
    # constraints
    prob += lpSum([player_vars[i] for i in playerid]) == 11, "Total 11 Players"
    prob += lpSum([cost[i] * player_vars[i] for i in playerid]) <= budget, "Total Cost"
    prob += lpSum([gk[i] * player_vars[i] for i in playerid]) == 1, "Exactly 1 GK"
    prob += lpSum([fb[i] * player_vars[i] for i in playerid]) == 2, "Exactly 2 FB"
    prob += lpSum([hb[i] * player_vars[i] for i in playerid]) == 3, "Exactly 3 HB"
    prob += lpSum([fwd[i] * player_vars[i] for i in playerid]) == 5, "Exactly 5 FWD"

    # solve
    prob.solve()
    # return list of player ids in the optimal solution
    return [str(variable).split("_")[1] for variable in prob.variables() if variable.varValue > 0.0]

def getTBData(retplayer):
    """
    Get player data from ids
    """
    retval = executeQuery("""
    SELECT name, age, nationality, club, photo, overall, value, position FROM Football.Players
    WHERE ID IN ({}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {})
    """.format(retplayer[0], retplayer[1], retplayer[2], retplayer[3], retplayer[4], retplayer[5], retplayer[6], retplayer[7], retplayer[8], retplayer[9], retplayer[10]))
    return retval

print(knapsack(20000))

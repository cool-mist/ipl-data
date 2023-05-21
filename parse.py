import tabula
import json
import sys
import math

class Match:
    day_n: int
    match_n: int
    day: str
    date: str
    time: str
    home: str
    away: str
    venue: str

def main():
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    print ("Reading from " + input_file)
    dataframes = tabula.read_pdf(input_file, pages = [1, 2])
    matches = []
    teams = ['Sunrisers Hyderabad', 'Gujarat Titans', 'Mumbai Indians', 'Chennai Super Kings',
             'Lucknow Super Giants', 'Delhi Capitals', 'Kolkata Knight Riders', 'Rajasthan Royals',
             'Royal Challengers Bangalore', 'Punjab Kings', 'Qualifier 1 - Team 1 vs Team 2',
             'Eliminator - Team 3 vs Team 4', 'Qualifier 2 - Winner of Eliminator vs Loser of Qualifier 1',
             'TATA IPL 2023 Final - Winner of Qualifier 1 vs. Winner of Qualifier 2']

    for dataframe in dataframes:
        for i in range (2,len(dataframe["MATCH"])):
            x = Match(); 
            x.day_n = dataframe["MATCH"][i]
            x.match_n = dataframe["MATCH.1"][i]
            x.day = dataframe["Unnamed: 0"][i]
            x.date = dataframe["Unnamed: 1"][i]
            x.time = dataframe["Unnamed: 2"][i]
            homeaway = dataframe["Unnamed: 3"][i]
            away = dataframe["Unnamed: 4"][i]
            if away != away:
                for j in teams:
                    if homeaway.startswith(j):
                        x.home = j
                    if homeaway.endswith(j):
                        x.away = j
            else:
                x.home = homeaway
                x.away = away
            x.venue = dataframe["Unnamed: 5"][i]
            teams.append(x.home)
            matches.append(x)

    print ("Writing to " + output_file)
    f = open(output_file, 'w')
    json.dump(matches, f, indent = 4, default = lambda x: x.__dict__)
    f.close()

if __name__ == "__main__":
    main()

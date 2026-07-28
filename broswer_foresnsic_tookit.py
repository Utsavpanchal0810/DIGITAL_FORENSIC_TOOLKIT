"""
    browser foresnic tookit
"""

import os , shutil , sqlite3
from datetime import datetime,timedelta
from urllib.parse import urlparse , parse_qs

print("Browser forensics toolkit")

# chrome history database location
history_path = os.path.expanduser(r"~\AppData\Local\Google\Chrome\User Data\Profile 22\History")

# check whether history file exists
if not os.path.exists(history_path):
    print("History file not found")
    exit()

# copy database because chrome locks the original file
temp_db = "History_Copy.db"
shutil.copy2(history_path,temp_db)

# Connect to copied sqllite database
conn = sqlite3.connect(temp_db)
cur = conn.cursor()

# Fetch browser history records
cur.execute("""
SELECT url , title , visit_count , last_visit_time FROM urls;
""")

rows = cur.fetchall()

# display first 20 history records

print("Top 20 Browsing History records")

for i , row in enumerate(rows[:20],1):

    url , title , visits , ctime = row

    try:

        # Convert Chrome timestamp into readable data & time
        t = (
            datetime(1601,1,1)+timedelta(microseconds=ctime)
        ).strftime("%d-%m-%Y %I:%M:%S %p")
    except:
        t = "Unknown"


    print("-"*60)
    print("Record: ",i)
    print("Title: ",title)
    print("Url: ",url)
    print("Visits: ",visits)
    print("Time: ",t)


# to store information about domain visit and counter
domain_stats = {}
total_visits = 0

# Calculate total visits for each domain
for url , title , visits , ctime in rows:

    if not url:
        continue

    # extract domain name from url
    d = urlparse(url).netloc.replace("www.","")

    if not d:
        continue

    total_visits += visits

    # add visits if domain already exists
    domain_stats[d] = domain_stats.get(d,0) + visits



# sort domains by highest visit count
sorted_domains = sorted(domain_stats.items(),key=lambda x:x[1],reverse=True)


# TOP 10 VISITED DOMAIN
print("="*60)
print("TOP 10 MOST VISITED DOMAINS")

for i , (d,v) in enumerate(sorted_domains[:10],1):
    print(f"{i}. {d} {v} Visits")


print("\n" + "="*60)
print("RECENT GOOGLE SEARCHES")
print("\n" + "="*60)


seen = set()
count = 0

for url, _, _, _ in rows:

    # check weather url is a google search
    if "google.com/search" in url:

        # extract search query parameter
        q = parse_qs(urlparse(url).query).get("q")

        print(q)

        if q and q[0] not in seen:
            seen.add(q[0])
            count+=1
            print(f"{count}.{q[0]}")

        if count==10:
            break

if count==0:
    print("No Google Searchs Found")

print("SUMMARY")
print("Total History Records: ",len(rows))
print("Unique Domains: ",len(domain_stats))
print("Total Website Visits: ",total_visits)

if sorted_domains:
    print("Most Visited Website: ",sorted_domains[0][0])


# close your database connection
conn.close()

# delete temporary database copy
os.remove(temp_db)
print("Investigation completed successfully")




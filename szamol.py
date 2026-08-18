from datetime import datetime, timezone
from time import strftime

def maiNap():
    print(datetime.now(timezone.utc).strftime('%m-%d.%YY'))
maiNap()


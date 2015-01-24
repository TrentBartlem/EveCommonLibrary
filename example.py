from EveCommon.EveCentral import EveCentral
from EveCommon.ZKillboard import ZKillboard
from EveCommon.SDEConnector import SDEConnector

from datetime import datetime, timedelta

end_time = datetime.now()
start_time = end_time - timedelta(days=3)

sde = SDEConnector(db_name='C:\Database\sqlite-latest.sqlite')

zKill = ZKillboard(user_agent='Your USERAGENT', alliance_id=99003214, losses=True, no_attackers=True,
                   start_time=start_time, end_time=end_time, solar_system_id=30000142)
killmails = zKill.get_killmails()

items = []
for killmail in killmails:
    print('Pilot %s lost: %s' % (killmail.victim.characterName, sde.get_type_name_by_type_id(killmail.victim.shipTypeID)))
    for item in killmail.items:
        items.append(item['typeID'])

ec = EveCentral(user_agent='Your USERAGENT', type_id_list=items, system_id=30000142)
prices_list = ec.get_prices_list()

for price in prices_list:
    print ('Price for %s: %s' % (sde.get_type_name_by_type_id(price.item_id), price.sell.percentile))
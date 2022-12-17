from pyzipcode import ZipCodeDatabase

zcdb = ZipCodeDatabase()
in_radius = [z.zip for z in zcdb.get_zipcodes_around_radius('55001', 8)] # ('ZIP', radius in miles)
# radius_utf = [x.encode('UTF-8') for x in in_radius] # unicode list to utf list

print(in_radius)
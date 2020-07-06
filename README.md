# FTL_DjangoApp
FTL_DjangoApp

1. Dummy data present in resources/data.xlsx
2. Loaded the data into sqlite3 DB as a part of pre-processing (not part of django site) 
3. ftl_site contains django app, templates view and models
4. App retrieves data from sqlite3 DB (ftl_db.sqlite3)
5. API endpoint contract as below
   > GET / USERID \
   >  `input = user ID of user` \
   > `output = activity data of user in json`
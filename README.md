## FTL_DjangoApp
1. View data from db as admin : [host]:8000/admin _{{username='admin'}, {password='admin'}}_
2. Loaded the data into sqlite3 DB as a part of pre-processing (not part of django site) 
3. ftl_site contains django ftl_app, templates view and models
4. App retrieves data from sqlite3 DB (ftl_db.sqlite3)
5. API endpoint contract as below
   > POST / USERID \
   >  `input = (multiple) user ID of user` \
   > `output = activity data of user(s) in json`
   
### Features
1. Responsive Mobile UI
2. Support for containerisation in virtual env for linux and windows
3. Download option (available only when API response payload is not too large)

### Usage
1. Configure port, IP and url in `Settings.py`
2. Execute through `run.bat` or `run.sh` depending on OS
3. Test the app using `test.py`
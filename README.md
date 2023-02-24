# deployMerakiDevices
Methods of Deploying Meraki Devices 



## deployMerakiDevices.py
- Reads an excel file (matching headers names as shown in the template) and configures those SNs with information provide in the spreadsheet.
- All devices will get claimed to the provide Org and Network via the following flags. 
    - `-NetworkName`
    - `-OrgName`
    - `-ConfigFile`

```
deployMerakiDevices.py -ConfigFile deployMerakiDevice.xlsx -OrgName "Orgname" -NetworkName "Netname" 
```


## [deployMerakiDevices - Google Sheet](https://docs.google.com/spreadsheets/d/1B3yUDxsuFwzrvn6e2rBmHoKkx5ka7aZN5E1E_VM90OI/edit?usp=sharing)
- Takes information for the google sheet and deployed it 
- Make a Copy, read the read me, deploy

ALL_CURRENCIES = 'https://www.nbrb.by/api/exrates/currencies'
CURRENT_DYMANICS = 'https://www.nbrb.by/API/ExRates/Rates/Dynamics/'
CONNECT = ('SYSTEM/123@//localhost:1521/orcl')

schema_currency = {
    "type": "object",
    "properties": {
        "Cur_ID": {"type": "number"},
        "Cur_ParentID": {"type": "number"},
        "Cur_Code": {"type": "string"},
        "Cur_Abbreviation": {"type": "string"},
        "Cur_Name": {"type": "string"},
        "Cur_Name_Bel": {"type": "string"},
        "Cur_Name_Eng": {"type": "string"},
        "Cur_QuotName": {"type": "string"},
        "Cur_QuotName_Bel": {"type": "string"},
        "Cur_QuotName_Eng": {"type": "string"},
        "Cur_NameMulti": {"type": "string"},
        "Cur_Name_BelMulti": {"type": "string"},
        "Cur_Name_EngMulti":  {"type": "string"},
        "Cur_Scale": {"type": "number"},
        "Cur_Periodicity": {"type": "number"},
        "Cur_DateStart": {"type": "string"},
        "Cur_DateEnd": {"type": "string"},
    },
}

schema_statistics = {
    "type": "object",
    "properties": {
        "Cur_ID": {"type": "number"},
        "Date": {"type": "string"},
        "Cur_OfficialRate": {"type": "number"},
    },
}
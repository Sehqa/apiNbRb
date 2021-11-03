class Currency:
    def __init__(self, kwargs):
        self.cur_id = kwargs.get('Cur_ID')
        self.cur_parent_id = kwargs.get('Cur_ParentID')
        self.cur_code = kwargs.get('Cur_Code')
        self.cur_abbreviation = kwargs.get('Cur_Abbreviation')
        self.cur_name = kwargs.get('Cur_Name')
        self.cur_name_bel = kwargs.get('Cur_Name_Bel')
        self.cur_name_eng = kwargs.get('Cur_Name_Eng')
        self.cur_quot_name = kwargs.get('Cur_QuotName')
        self.cur_quot_name_bel = kwargs.get('Cur_QuotName_Bel')
        self.cur_quot_name_eng = kwargs.get('Cur_QuotName_Eng')
        self.cur_name_multi = kwargs.get('Cur_NameMulti')
        self.cur_scale = kwargs.get('Cur_Scale')
        self.cur_periodicity = kwargs.get('Cur_Periodicity')
        self.cur_date_start = kwargs.get('Cur_DateStart')
        self.cur_date_end = kwargs.get('Cur_DateEnd')
        if (kwargs.get('Cur_NameMulti') == ''):
            self.cur_name_multi = 'emptyvalue'
        else:
            self.cur_name_multi = kwargs.get('Cur_NameMulti')
        if (kwargs.get('Cur_Name_BelMulti') == ''):
            self.cur_name_bel_multi = 'emptyvalue'
        else:
            self.cur_name_bel_multi = kwargs.get('Cur_Name_BelMulti')
        if (kwargs.get('Cur_Name_EngMulti') == ''):
            self.cur_name_eng_multi = 'emptyvalue'
        else:
            self.cur_name_eng_multi = kwargs.get('Cur_Name_EngMulti')

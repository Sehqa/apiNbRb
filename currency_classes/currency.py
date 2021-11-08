class Currency:
    cur_id = ''
    cur_parent_id = ''
    cur_code = ''
    cur_abbreviation = ''
    cur_name = ''
    cur_name_bel = ''
    cur_name_eng = ''
    cur_quot_name = ''
    cur_quot_name_bel = ''
    cur_quot_name_eng = ''
    cur_name_multi = ''
    cur_name_bel_multi = ''
    cur_name_eng_multi = ''
    cur_scale = ''
    cur_periodicity = ''
    cur_date_start = ''
    cur_date_end = ''

    def __init__(self, kwargs):
        kw_dict = kwargs
        update_dict = {}
        list_keys = list(kw_dict.keys())
        iter_for_dict = 0
        for i in list(name for name in Currency.__dict__ if not name.startswith('__')):
            update_dict[i] = kw_dict[list_keys[iter_for_dict]]
            iter_for_dict = iter_for_dict + 1
        for i in update_dict.keys():
            if update_dict[i] == '':
                update_dict[i] = 'emptyvalue'
        self.__dict__.update(update_dict)


